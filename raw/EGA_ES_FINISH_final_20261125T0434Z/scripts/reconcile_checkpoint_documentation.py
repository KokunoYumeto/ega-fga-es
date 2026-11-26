#!/usr/bin/env python3
"""Preserve checkpoint documentation names without repackaging French extracts.

Only records and this reconciliation report are written. This does not merge
records, restore any corpus/input file, compile readers or alter a PDF.
"""
from pathlib import Path
import csv,io,json,hashlib,zipfile,re,collections,shutil
from corpus import RESULT,FR,write_tsv
from audit_iii_alignment import sections

WORK=RESULT.parent
REC=RESULT/'records'
FINAL=['records/III_AUDIT.md','records/III_COMPLETE_COUNTS.json','records/III_COMPLETE_FIDELITY.tsv','records/CAMBIOS_iii.tsv']
FRENCH_FIELDS={'f','f_context','left','right'}

def sha(b):return hashlib.sha256(b).hexdigest()

def main():
 current={p.relative_to(RESULT).as_posix() for p in RESULT.rglob('*') if p.is_file()}
 versions=collections.defaultdict(list);archives={};union=set()
 for i in range(1,5):
  name=f'EGA_ES_FINISH_checkpoint_{i:02d}.zip';p=WORK/'exports'/name
  with zipfile.ZipFile(p) as z:
   archives[name]={n:z.read(n) for n in z.namelist() if not n.endswith('/') and not n.startswith(('tree/','readers/','qa/'))}
  for path,raw in archives[name].items():
   versions[path].append(dict(checkpoint=name,bytes=len(raw),sha256=sha(raw)));union.add(path)
 before_missing=sorted(union-current)
 rows=[];sourcecache={};redaction_totals=collections.Counter();unresolved=[]

 def get_source(ed,part):
  key=(ed,part)
  if key not in sourcecache:
   p=FR/ed/f'BASE/native/ega3/ega3-{part}-fr.tex';s=p.read_text()
   sourcecache[key]=(s,{k:(a,b) for k,a,b in sections(s)},'EGA_ES_FINISH_1_FRANCES/fr/'+ed+f'/BASE/native/ega3/ega3-{part}-fr.tex',sha(p.read_bytes()))
  return sourcecache[key]

 def context(d,parent):
  q=dict(parent)
  for k in ['edition','part','place','id','fstart','fend','fpos']:
   if k in d:q[k]=d[k]
  if 'id' in q:
   ss=q['id'].split(':')
   if len(ss)>=4 and ss[0] in ['current','diplomatic']:q.update(edition=ss[0],part=ss[1],place=ss[2])
  return q

 def redacted(raw,ctx,field,index=None):
  redaction_totals['strings']+=1;redaction_totals['characters']+=len(raw)
  out=dict(redacted=True,sha256=sha(raw.encode()),characters=len(raw),utf8_bytes=len(raw.encode()))
  ed,part,place=ctx.get('edition'),ctx.get('part'),ctx.get('place')
  if not ed or not part:
   out['locator']={'historical_id':ctx.get('id'),'place':place,'status':'source edition/part unavailable'}
   unresolved.append((ctx.get('id'),field,'source unavailable'));return out
  s,units,file,digest=get_source(ed,part)
  loc=dict(source_file=file,source_sha256=digest,place=place)
  if ctx.get('id'):loc['historical_id']=ctx['id']
  if 'fstart' in ctx:loc['historical_context_start']=ctx['fstart'];loc['historical_context_end']=ctx.get('fend')
  out['locator']=loc
  if not raw:loc['status']='empty context marker';return out
  expected=None
  if field=='f' and index is not None and index<len(ctx.get('fpos',[])):expected=ctx['fpos'][index]
  elif field=='f' and 'fstart' in ctx:expected=[ctx['fstart'],ctx.get('fend',ctx['fstart']+len(raw))]
  elif field=='left' and 'fstart' in ctx:expected=[ctx['fstart']-len(raw),ctx['fstart']]
  elif field=='right' and 'fend' in ctx:expected=[ctx['fend'],ctx['fend']+len(raw)]
  if expected and s[expected[0]:expected[1]]==raw:
   positions=[expected[0]];how='exact at historical offsets'
  else:
   a,b=units.get(place,(0,len(s)));positions=[];p=s.find(raw,a,b)
   while p>=0:
    positions.append(p);p=s.find(raw,p+1,b)
   how='exact within named source unit'
   if not positions:
    p=s.find(raw)
    while p>=0:
     positions.append(p);p=s.find(raw,p+1)
    how='exact in source file'
  loc['match_count']=len(positions)
  if positions:
   loc['status']=how
   loc['matches']=[dict(character_start=p,character_end=p+len(raw),first_line=s.count('\n',0,p)+1,last_line=s.count('\n',0,p+len(raw))+1) for p in positions[:25]]
   if len(positions)>25:loc['additional_match_count']=len(positions)-25
  else:
   loc['status']='historical context not verbatim in supplied source; place and original offsets retained'
   if place in units:
    a,b=units[place];loc['unit_first_line']=s.count('\n',0,a)+1;loc['unit_last_line']=s.count('\n',0,b)+1
   unresolved.append((ctx.get('id',str(ed)+':'+str(part)+':'+str(place)),field,'nonverbatim historical context'))
  return out

 def clean(x,parent=None):
  parent=parent or {}
  if isinstance(x,list):return [clean(v,parent) for v in x]
  if not isinstance(x,dict):return x
  ctx=context(x,parent);out={}
  for k,v in x.items():
   if k in FRENCH_FIELDS:
    if isinstance(v,str):out[k]=redacted(v,ctx,k)
    elif isinstance(v,list):out[k]=[redacted(t,ctx,k,i) if isinstance(t,str) else clean(t,ctx) for i,t in enumerate(v)]
    else:out[k]=clean(v,ctx)
   else:out[k]=clean(v,ctx)
  return out

 for p in sorted((WORK/'tmp/III_diagnostics').glob('*.json')):
  path='records/'+p.name;raw=p.read_bytes();data=json.loads(raw);before_count=len(data)
  initial=dict(redaction_totals);n_unresolved=len(unresolved)
  payload=clean(data)
  envelope=dict(status='historical_snapshot_redacted',authoritative=False,final_audit=FINAL[0],superseded_by=FINAL[1:],original_payload_type=type(data).__name__,record_count=before_count,original_snapshot_sha256=sha(raw),checkpoint_versions=versions[path],redaction_policy='French f, f_context and adjacent source-formula contexts are replaced by hashes, lengths and source locators. Spanish e/e_context, IDs, offsets and decisions remain. Short terminology witnesses are retained.',records=payload)
  dest=RESULT/path;dest.write_text(json.dumps(envelope,ensure_ascii=False,indent=2)+'\n')
  nred=redaction_totals['strings']-initial.get('strings',0)
  rows.append([path,';'.join(v['checkpoint'] for v in versions[path]),'restored_redacted','historical; not an active issue queue',';'.join(FINAL),before_count,before_count,sha(raw),sha(dest.read_bytes()),nred,len(unresolved)-n_unresolved,'not merged; diagnostic JSON','Spanish payload and identifiers retained; French source text replaced by locators.'])

 for old,new in [('CAMBIOS_iii_manual.tsv','III_CHANGES_manual.tsv'),('CAMBIOS_iii_math_aligned.tsv','III_CHANGES_math_aligned.tsv')]:
  p=REC/new;dest=REC/old;shutil.copyfile(p,dest);n=sum(1 for _ in csv.DictReader(io.StringIO(p.read_text()),delimiter='\t'))
  rows.append(['records/'+old,';'.join(v['checkpoint'] for v in versions['records/'+old]),'restored_exact_historical_copy','historical alias; consolidated final log controls','records/'+new+';records/CAMBIOS_iii.tsv',n,n,sha(p.read_bytes()),sha(dest.read_bytes()),0,0,'explicitly excluded by merge_records.HISTORICAL_CHANGE_RECORDS','Byte-identical copy of retained historical III_CHANGES log; source corpus not restored.'])

 path='records/CAMBIOS_standard_model.tsv';raw=archives['EGA_ES_FINISH_checkpoint_01.zip'][path]
 old=list(csv.DictReader(io.StringIO(raw.decode()),delimiter='\t'));applied=[]
 for n in ['CAMBIOS_standard_model_applied_01.tsv','CAMBIOS_standard_model_applied_02.tsv']:applied+=list(csv.DictReader((REC/n).open(),delimiter='\t'))
 keys=['file','place','before','after','source'];signature=lambda r:tuple(r[k] for k in keys)
 assert collections.Counter(map(signature,old))==collections.Counter(map(signature,applied))
 assert len(old)==2330 and len(applied)==2330
 (RESULT/path).write_bytes(raw)
 rows.append([path,'EGA_ES_FINISH_checkpoint_01.zip','restored_exact_historical_proposals','historical proposals; applied logs control','records/CAMBIOS_standard_model_applied_01.tsv;records/CAMBIOS_standard_model_applied_02.tsv',len(old),len(old),sha(raw),sha(raw),0,0,'explicitly excluded by merge_records.HISTORICAL_CHANGE_RECORDS','2330 = 2184 + 146; exact row-multiset equality on file/place/before/after/source, preserving duplicates; kind alone changes standard_proposed to standard.'])

 after={p.relative_to(RESULT).as_posix() for p in RESULT.rglob('*') if p.is_file()};remaining=sorted(union-after)
 assert not remaining,remaining
 assert len(rows)==24
 write_tsv(REC/'CHECKPOINT_RECONCILIATION.tsv',['path','present_in_checkpoints','action','status','authoritative_successor','original_records','restored_records','retained_original_sha256','restored_sha256','source_strings_redacted','source_strings_without_verbatim_match','merge_policy','evidence'],sorted(rows))
 summary=dict(checkpoints_checked=[f'EGA_ES_FINISH_checkpoint_{i:02d}.zip' for i in range(1,5)],documentary_paths_in_union=len(union),missing_before=before_missing,restored_paths=len(rows),historical_json=21,historical_tsv=3,historical_json_records=sum(r[5] for r in rows if r[0].endswith('.json')),french_strings_redacted=redaction_totals['strings'],french_characters_replaced=redaction_totals['characters'],nonverbatim_historical_contexts=len(unresolved),nonverbatim_context_locators=unresolved,missing_documentary_paths_after=remaining,corpus_and_reader_paths_excluded_from_restore=True,merge_executed=False)
 (REC/'CHECKPOINT_RECONCILIATION_COUNTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 lines=['# Conciliación documental de checkpoints 01–04','', '**Se conservaron las 24 rutas documentales ausentes: 21 JSON históricos saneados y tres TSV históricos.** La unión de nombres de los cuatro checkpoints no presenta ninguna otra baja documental tras esta conciliación.','', '## Restauraciones','', '- `CAMBIOS_iii_manual.tsv` y `CAMBIOS_iii_math_aligned.tsv` son copias byte a byte de `III_CHANGES_manual.tsv` y `III_CHANGES_math_aligned.tsv`. El registro consolidado autoritativo sigue siendo `CAMBIOS_iii.tsv`.','- Los 21 JSON recuperan sus nombres anteriores. Sus extractos franceses `f`, `f_context` y contextos fuente adyacentes se sustituyen por SHA-256, longitud en caracteres/bytes y localizadores de archivo, unidad, líneas y posiciones cuando hay coincidencia literal. Se conservan español, identificadores, offsets y decisiones. Los términos franceses breves del glosario permanecen como testigos terminológicos.','- `CAMBIOS_standard_model.tsv` se conserva exactamente como en checkpoint01. Sus 2 330 propuestas corresponden íntegramente a las 2 184 filas de `CAMBIOS_standard_model_applied_01.tsv` y 146 de `_02.tsv`. Se verificó igualdad del multiconjunto sobre archivo, lugar, antes, después y fuente; solo cambia `standard_proposed` a `standard`.','', '## Estado y autoridad','', 'Los JSON tienen una envoltura explícita `historical_snapshot_redacted`, con `authoritative: false`, la lista histórica en `records` y enlaces a `III_AUDIT.md`, `III_COMPLETE_COUNTS.json`, `III_COMPLETE_FIDELITY.tsv` y `CAMBIOS_iii.tsv`. Las incidencias antiguas no representan incidencias abiertas del texto final. Los scripts que esperaban una lista desnuda no deben consumir estos archivos como colas activas; el cambio de forma es intencional para señalar su estado histórico.','', 'Los tres TSV históricos quedan expresamente excluidos por `HISTORICAL_CHANGE_RECORDS` en `merge_records.py`. No se ejecutó el merge. Las copias conservan los metadatos originales, incluidas descripciones provisionales; los registros finales y su normalización siguen siendo autoritativos.','', '## Alcance y comprobaciones','', f'- Rutas documentales distintas en la unión: **{len(union)}**.',f'- Registros JSON históricos conservados: **{summary["historical_json_records"]}**.',f'- Cadenas fuente reemplazadas por metadatos: **{redaction_totals["strings"]}**, con **{redaction_totals["characters"]}** caracteres.',f'- Contextos históricos sin coincidencia literal actual: **{len(unresolved)}**; conservan la unidad y los localizadores históricos, sin fabricar una coincidencia.', '- Ningún PDF, lector, fuente, corpus ni README raíz se modificó. No se restauraron archivos de `tree`, `readers` ni `qa` desde los checkpoints.','', 'Las columnas del TSV identifican la procedencia, los hashes, el estado histórico, el sucesor autoritativo y la política de merge de cada ruta. La conservación de nombres no certifica que las antiguas propuestas o diagnósticos sean válidos para el estado final.','']
 (REC/'CHECKPOINT_RECONCILIATION.md').write_text('\n'.join(lines))
 print(json.dumps({k:v for k,v in summary.items() if k not in ['missing_before','nonverbatim_context_locators']},ensure_ascii=False))

if __name__=='__main__':main()

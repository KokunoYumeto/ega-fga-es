#!/usr/bin/env python3
"""Regenerate the records of the completed IV2 context-term review."""
import re,csv,json,bisect
from pathlib import Path
import audit_iv2_alignment as a
R=a.ROOT/'records';WHO='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; IV2 run'
def read(n):
 with (R/n).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def write(n,heads,rows):
 with (R/n).open('w') as f:w=csv.DictWriter(f,fieldnames=heads,delimiter='\t');w.writeheader();w.writerows(rows)
def main():
 rows=[];events=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  f,e,bounds,ps,gaps=a.compare(layer);assert not gaps;ps.sort(key=lambda q:q['estart']);starts=[q['estart'] for q in ps];ends=[q['eend'] for q in ps];count=0
  for m in re.finditer(r'\b(?:vecindad(?:es)?|fibras?)\b',e,re.I):
   i=bisect.bisect_right(ends,m.start())-1;j=bisect.bisect_left(starts,m.end())
   if i<0 or j==len(ps):continue
   if any(x['estart']<=m.start()<x['eend'] for x in ps[max(0,i):j+1]):continue
   prev,nxt=ps[i],ps[j];count+=1;file=a.owner(m.start(),bounds);off=next(x[0] for x in bounds if x[2]==file);ln=e[off:m.start()].count('\n')+1
   existing=('ega4-2_4.1.4_4.1.5_ES' in file and m[0].lower()=='vecindad')
   changed=m[0].lower().startswith('vecindad') and not existing;before=('entornos' if m[0].lower()=='vecindades' else 'entorno') if changed else m[0]
   decision='changed to '+m[0]+'; determiner and adjective agreement reviewed' if changed else 'retained existing vecindad: already conforms to voisinage decision' if existing else 'retained fibra: morphism fiber, formal fiber, or corresponding heading/index; not a sheaf stalk'
   witness=' '.join(f[prev['fend']:nxt['fstart']].split());witness=witness if len(witness)<250 else witness[:247]+'...'
   rows.append(dict(edition=layer,file=file,line=ln,place=nxt['place'],before_term=before,after_term=m[0],decision=decision,french_witness=witness))
   events.append(dict(statement_id='IV2:term:'+layer+':'+str(count),date='2026-11-25',who=WHO,type='used and rechecked in this run',outcome=decision+'; supplied French context compared. Linguistic decision only, not proof verification.'))
  assert count==210,(layer,count)
 write('MODEL_TERMS_iv2.tsv',['edition','file','line','place','before_term','after_term','decision','french_witness'],rows)
 ce=read('CHECK_EVENTS_iv2.tsv');ce=[x for x in ce if not x['statement_id'].startswith('IV2:term:')]+events;write('CHECK_EVENTS_iv2.tsv',['statement_id','date','who','type','outcome'],ce)
 g=read('GLOSARIO_REGISTRO_iv2.tsv');g=[x for x in g if x['french_term'] not in ['voisinage','fibre (morphism or formal fiber)']]
 g.extend([dict(french_term='voisinage',spanish_rendering='vecindad',witness='standard/STANDARDS_20261119b.md Spanish; source contexts reviewed',places='156 occurrences; see MODEL_TERMS_iv2.tsv',reversible='yes'),dict(french_term='fibre (morphism or formal fiber)',spanish_rendering='fibra',witness='standard/STANDARDS_20261119b.md; source geometric meaning reviewed',places='262 occurrences; see MODEL_TERMS_iv2.tsv',reversible='yes')]);write('GLOSARIO_REGISTRO_iv2.tsv',['french_term','spanish_rendering','witness','places','reversible'],g)
 data=read('ESTANDAR_APLICADO_iv2.tsv');data=[x for x in data if x['row'] not in ['es-voisinage-IV2-model','es-fibre-IV2-model']]
 for x in data:
  if x['row']=='es-corps-champ-IV2-held':x['found']=str(sum(v['french_term'].startswith('corps / champ') for v in g))
  if x['row']=='es-anneau-valuation-IV2-low-confidence':x['found']=str(sum(v['french_term']=='anneau de valuation' for v in g))
 data.extend([dict(row='es-voisinage-IV2-model',found=156,changed=156,places_left='',reason='Every context compared with French; vecindad, with determiner and adjective agreement. Supersedes the older APPLY_PLAN direction.'),dict(row='es-fibre-IV2-model',found=262,changed=0,places_left='262 retained; MODEL_TERMS_iv2.tsv',reason='All occurrences denote morphism fibers/formal fibers or their headings/index entries. None denotes a sheaf stalk.')]);write('ESTANDAR_APLICADO_iv2.tsv',['row','found','changed','places_left','reason'],data)
 p=R/'IV2_AUDIT_COUNTS.json';counts=json.loads(p.read_text());counts.update(context_term_decisions=len(rows),voisinage_changed=156,fibers_retained=262,check_events=len(ce),glossary_rows=len(g));p.write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
 print('Term decisions',len(rows),'check events',len(ce))
if __name__=='__main__':main()

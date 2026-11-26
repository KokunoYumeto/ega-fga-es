#!/usr/bin/env python3
"""Finalize EGA I chapter-0 coverage, translation, terminology and reconciliation.
Requires the supplied archive; emits only result-relative/source-archive paths.
No mathematical proof check is performed or claimed.
"""
from pathlib import Path
import re,csv,json,argparse,collections,difflib
from tex_tools import math_spans,retain_translated_text,balanced_end
P=argparse.ArgumentParser();P.add_argument('--source-root',type=Path,required=True);a=P.parse_args();r=Path(__file__).resolve().parents[1]
who='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; chapter-0 run'
keys=['4.4.3','5.1.1','5.2.1','5.3.1','5.4.1','5.5.1','6.0','6.1.1','6.2.1','6.3.1','6.4.1','6.5.1','6.6.1','6.7.1','7.1.1','7.2.1','7.3.1','7.4.1','7.5.1','7.6.1','7.7.1','7.8.1']
names=['ega0_i_4_4_3_8.tex']+['ega0_i_'+'.'.join(k.split('.')[:2]).replace('.','_')+'.tex' for k in keys[1:]]
envpat=re.compile(r'\\begin\{[^}]+\}\[([\d.]+)\]')
markpat=re.compile(r'\\(?:label|oldpage|EGAReaderTarget|tag)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?')
def write(n,h,rows):
 with (r/'records'/n).open('w',encoding='utf-8',newline='') as f:w=csv.writer(f,delimiter='\t');w.writerow(h);w.writerows(rows)
def words(t):
 for s in reversed(math_spans(t)):t=t[:s.start]+' '+t[s.end:]
 t=re.sub(r'(?<!\\)%[^\n]*','',t)
 for m in reversed(list(re.finditer(r'\\(?:label|oldpage|EGAReaderTarget|tag|setcounter|ref|sref)(?:\[[^\]]*\])?\{',t))):
  end=balanced_end(t,m.end()-1)
  if end<len(t) and t[end]=='{':end=balanced_end(t,end)
  t=t[:m.start()]+' '+t[end:]
 t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?',' ',t)
 t=re.sub(r'\\[A-Za-z]+',' ',t)
 return len(re.findall(r'[A-Za-zÀ-ÿ]+(?:[-’\'][A-Za-zÀ-ÿ]+)*',t))
def units(t):
 ms=list(envpat.finditer(t));d={}
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);text=t[m.start():end];h=re.search(r'\\(?:subsection|section)\{',text)
  if h:text=text[:h.start()]
  d[m.group(1)]=(m.start(),text)
 return d
coverage=[];trans=[];events=[];audit=[];summary=[];data={};gloss=[];unit_targets={}
for ed in ['current','diplomatic']:
 src='EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/BASE/native/ega1/ega0-1-fr.tex';fr=(a.source_root/src).read_text();labs={m.group(1):m.start() for m in re.finditer(r'\\label\{([^}]+)\}',fr)}
 ps=list((r/'tree/worktree/es'/ed.upper()/'EGA_I_ch0').glob('ega0_i_*.tex'));ps.sort(key=lambda p:min(labs.get(x,10**9) for x in re.findall(r'\\label\{([^}]+)\}',p.read_text())))
 texts={p:p.read_text() for p in ps};es='\n'.join(texts.values());fi=units(fr);si={};li={}
 for p,t in texts.items():
  for k,(start,u) in units(t).items():assert k not in si;si[k]=(p,start,u);unit_targets[ed,k]=str(p.relative_to(r))
  for l in re.findall(r'\\label\{([^}]+)\}',t):assert l not in li;li[l]=p
  for m in re.finditer(r'\bcuerpos?\b|\bvaloraci[oó]n(?:es)?\b|\bcampos?\b',t):
   term='corps' if m.group().startswith('cuerpo') else 'anneau de valuation' if m.group().startswith('valoraci') else 'champ'
   if term=='champ':continue
   line=t.count('\n',0,m.start())+1;prior=list(envpat.finditer(t[:m.start()]));place='0.'+prior[-1].group(1) if prior else 'heading'
   witness='STANDARDS_20261119b.md, Spanish block; DOUBT_DECISIONS_20261119.tsv: held corps/champ decision; established cuerpo retained' if term=='corps' else 'DOUBT_DECISIONS_20261119.tsv, es anneau de valuation: low-confidence valuación not applied; inherited valoración retained'
   gloss.append([term,m.group(),witness,str(p.relative_to(r))+': '+place+', line '+str(line),'yes'])
 for l,pos in labs.items():
  assert l in li,l
  coverage.append([src,l,ed,str(li[l].relative_to(r)),'translated_and_compared','Exact source anchor; complete numbered-unit inventory, formula sequence and marker sequence checked. No proof verification.'])
 coverage.append([src,'chapter 0 heading',ed,str(ps[0].relative_to(r)),'translated_and_compared','CAPÍTULO 0 / PRELIMINARES; source page-11 marker precedes heading.'])
 assert set(fi)==set(si),(ed,set(fi)-set(si),set(si)-set(fi))
 for k,(start,ft) in fi.items():
  p,sp,st=si[k];fm=math_spans(ft);sm=math_spans(st);same=len(fm)==len(sm) and all(re.sub(r'\s+','',retain_translated_text(x.text,y.text) or x.text)==re.sub(r'\s+','',y.text) for x,y in zip(fm,sm));markers=markpat.findall(ft)==markpat.findall(st)
  assert same,(ed,k,'math')
  audit.append([ed,'0.'+k,str(p.relative_to(r)),len(fm),len(sm),same,'identical in full ordered chapter; unit-local '+str(markers)])
  kind='new translation' if p.name in names else 'inherited translation'
  outcome=('Translated from the supplied '+ed+' French. ' if kind=='new translation' else 'Carried existing Spanish; compared supplied '+ed+' French math and source markers. ')+'Source fidelity only; no mathematical proof verification claimed.'
  events.append([ed.upper()+':0.'+k,'2026-11-25',who,'carried as background without fault found',outcome])
 fm=math_spans(fr);sm=math_spans(es);fullsame=len(fm)==len(sm) and all(re.sub(r'\s+','',retain_translated_text(x.text,y.text) or x.text)==re.sub(r'\s+','',y.text) for x,y in zip(fm,sm));marksame=markpat.findall(fr)==markpat.findall(es);assert fullsame;assert marksame
 summary.append([ed,len(ps),len(fi),len(labs),len(fm),len(markpat.findall(fr)),fullsame,marksame,0])
 for i,(key,name) in enumerate(zip(keys,names)):
  p=r/'tree/worktree/es'/ed.upper()/'EGA_I_ch0'/name;t=p.read_text();ids=[m.group(1) for m in envpat.finditer(t)];first=fi[ids[0]][0]
  if key!='4.4.3':
   candidates=list(re.finditer(r'\\(?:subsection|section)\{',fr[:first]));first=candidates[-1].start()
   if key in ['5.1.1','7.1.1']:first=list(re.finditer(r'\\section\{',fr[:first]))[-1].start()
  end=fi[ids[-1]][0]+len(fi[ids[-1]][1]);line1=fr.count('\n',0,first)+1;line2=fr.count('\n',0,end)+1
  trans.append([str(p.relative_to(r)),src,'lines '+str(line1)+'–'+str(line2)+'; 0.'+ids[0]+'–0.'+ids[-1],words(t)])
 trans.append([str(ps[0].relative_to(r)),src,'lines 1–7; chapter 0 heading',words('CAPÍTULO 0 PRELIMINARES')])
 data[ed]=(fr,fi,texts)
# Every supplied Spanish respell row in chapter 0, identified by JSONL ordinal.
reviews=[]
source_json='EGA_ES_FINISH_4_HECHO/done/RESPELL_CORRECTIONS_20261115.jsonl'
for i,line in enumerate((a.source_root/source_json).read_text().splitlines(),1):
 row=json.loads(line)
 if not row.get('tree','').startswith('es/') or 'EGA_I_ch0/' not in row.get('file',''):continue
 ed=row['tree'].split('/')[1].lower();p=r/'tree/worktree'/row['tree']/row['file'];orig=a.source_root/'EGA_ES_FINISH_2_ESPANOL/worktree'/row['tree']/row['file']
 ot=orig.read_text();offset=sum(len(x)+1 for x in ot.splitlines()[:row['line']-1]);matches=list(envpat.finditer(ot[:offset]));key=matches[-1].group(1) if matches else 'heading';fr,fu,_=data[ed];ft=fu[key][1];unit=units(p.read_text())[key][1]
 assert key in fu
 if 'boldsymbol' in row['as_applied']:
  assert r'\boldsymbol{K}' in ft and r'\boldsymbol{K}' in unit
  reason='The supplied '+ed+' French uses \\boldsymbol{K}. The proposed rollback to \\mathbf{K} conflicts with the later exact-French-TeX instruction and NOTATION_EGA.md §§1,3; source notation retained/restored.'
 elif 'mathfrak' in row['as_applied']:
  assert r'\mathfrak{H}_\lambda' in ft and r'\mathfrak{H}_\lambda' in unit
  reason='The supplied '+ed+' French at 0.3.2.6 uses \\mathfrak{H}_\\lambda and \\varprojlim without an added subscript at this place. The suggested \\mathcal{H} rollback conflicts with the later source-TeX rule; exact source notation retained/restored.'
 else:
  assert row['kind']=='undo_punctuation' and key=='1.6.2'
  assert '  & M_{fg}\n' in ft and '  & M_{fg}\n' in unit
  reason='The supplied French diagram at 0.1.6.2 ends in M_{fg} without the proposed period. Read against the source as requested by the undo_punctuation note; source display punctuation retained.'
 id='RESPELL-'+str(i).zfill(6);reason+=' '+source_json+': row '+str(i)+'; session '+str(row['session'])+'; '+row['tree']+'; entry '+str(row['entry'])+'; original line '+str(row['line'])+'.'
 reviews.append([id,str(p.relative_to(r)),'0.'+key,'does not apply to a translation',reason]);events.append([id,'2026-11-25',who,'used and rechecked in this run','Compared the proposed respell with supplied French and the later notation rule. '+reason])
assert len(reviews)==180,len(reviews)
# Terms from the supplied newest glossary and inherited edition witnesses.
glossary=list(csv.DictReader((a.source_root/'GLOSARIO_es_20261119/GLOSSARY_es.tsv').open(),delimiter='\t'))
terms=['fidèlement plat','de type fini','de présentation finie','quasi-fini','système projectif','cohérent','noethérien','anneau local','corps résiduel']
for term in terms:
 row=next(x for x in glossary if x['french']==term)
 places=[]
 for ed,(fr,fu,ts) in data.items():
  for p,t in ts.items():
   if p.name not in names:continue
   for k,(_,unit) in units(t).items():
    if row['rendering'] in re.sub(r'\s+',' ',unit):places.append(ed.upper()+':0.'+k)
 witness='GLOSARIO_es_20261119/GLOSSARY_es.tsv, '+term+'; supplied decided row; '+(row['level2_research_literature'] or row['level3_wikipedia_on_his_mathematics'] or row['decision_source'])
 gloss.append([term,row['rendering'],witness,'; '.join(places),'yes'])
choices=[
 ('linéairement topologisé','linealmente topologizado','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_IV2/ega4-2_7.4.8_ES.tex:17','0.7.1–0.7.8'),
 ('préadmissible','preadmisible','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex:8521','0.7.1.2'),
 ('préadique','preádico','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex:8520','0.7.1.9'),
 ('topologiquement nilpotent','topológicamente nilpotente','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex:7313','0.7.1.1'),
 ('cochaîne','cocadena','EGA_ES_FINISH_2_ESPANOL/worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-20-es.tex:1836','0.5.4.7'),
 ('cocycle','cociclo','EGA_ES_FINISH_2_ESPANOL/worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-18-es.tex:1015','0.5.4.7–0.5.4.8'),
 ('cobord','coborde','EGA_ES_FINISH_2_ESPANOL/worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-18-es.tex:1024','0.5.4.7'),
 ('produit tensoriel complété','producto tensorial completado','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex:7357','0.7.7'),
 ('séparé complété','separado completado','No direct witness in supplied glossary; literal technical rendering of the supplied French, reversible under the standard rule','0.7.2.10; 0.7.6; 0.7.7'),
 ('séries formelles restreintes','series formales restringidas','No direct witness in supplied glossary; literal technical rendering of the supplied French, reversible under the standard rule','0.7.5'),
 ('anneau complet des fractions','anillo completo de fracciones','No direct witness in supplied glossary; literal technical rendering of the supplied French, reversible under the standard rule','0.7.6')]
for fr,es,w,places in choices:gloss.append([fr,es,w,'CURRENT and DIPLOMATIC: '+places,'yes'])
# Consolidate the existing-text change fragments without losing their exact data.
changes=[]
for name in ['CH0_CHANGES_manual.tsv','CH0_CHANGES_notation.tsv','CH0_CHANGES_punctuation.tsv','CH0_CHANGES_structure.tsv']:
 for row in csv.DictReader((r/'records'/name).open(),delimiter='\t'):changes.append([row[k] for k in ['file','place','before','after','kind','source']])
for row in csv.DictReader((r/'records/DIPLOMATIC_ASSEMBLY_ch0.tsv').open(),delimiter='\t'):
 changes.append([row['file'],'whole unit','absent from supplied DIPLOMATIC tree','Existing Spanish unit assembled; exact diplomatic French differences preserved','assembly',row['source']+'; EGA_ES_FINISH_1_FRANCES/fr/diplomatic/BASE/native/ega1/ega0-1-fr.tex'])
write('MAPA_ch0.tsv',['french_file','place','edition','spanish_file','status','evidence'],coverage)
write('TRADUCCION_ch0.tsv',['file','french_source','range','words'],trans)
write('CAMBIOS_ch0.tsv',['file','place','before','after','kind','source'],changes)
write('GLOSARIO_REGISTRO_ch0.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
write('HECHO_REVISADO_ch0.tsv',['id','file','place','verdict','reason'],reviews)
write('CHECK_EVENTS_ch0.tsv',['statement_id','date','who','type','outcome'],events)
write('CH0_COMPLETE_FIDELITY.tsv',['edition','place','file','french_math_spans','spanish_math_spans','math_equal_with_translated_text_commands','source_markers_check'],audit)
write('CH0_COMPLETE_SUMMARY.tsv',['edition','unit_files','numbered_statements','labels','math_spans','markers','math_equal','markers_equal','missing_units'],summary)
print(json.dumps({'summary':summary,'translation_files':44,'heading_rows':2,'new_words_current':sum(x[3] for x in trans if '/CURRENT/' in x[0]),'new_words_diplomatic':sum(x[3] for x in trans if '/DIPLOMATIC/' in x[0]),'coverage_rows':len(coverage),'changes':len(changes),'respell_rows':len(reviews),'glossary_rows':len(gloss),'events':len(events)},ensure_ascii=False))

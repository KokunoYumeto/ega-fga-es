"""Fourteen individually source-reviewed Obsérvese clauses; no broader pass."""
import re,json
from collections import defaultdict
from iv3_align import units
from iv3_work import DIR
from corpus import RESULT,write_tsv
from tex_tools import math_spans

decisions={
 '10.2.1':('Se observará','On notera',1),
 '10.8.5':('Se observará','On notera',1),
 '10.9.3':('Se observará','On notera',1),
 '10.10.4':('Se observará','On notera',1),
 '11.2.9.4':('Se observará','on notera en outre',1),
 '11.3.6':('Observemos','Notons',1),
 '11.3.15':('Observemos','Notons d’autre part',1),
 '11.7.4':('Se observará','On notera',1),
 '12.2.3':('Se observará','On observera / On notera toutefois',2),
 '12.3.3':('se observa','on remarque en outre',1),
 '12.3.3.1':('Observemos','Notons d’abord',1),
 '13.1.2':('observemos','notons d’autre part',1),
 '13.3.1.1':('Observemos','Notons',1),
}
changes=[];review=[];byfile=defaultdict(list)
for n,(new,witness,expected) in decisions.items():
 q=DIR/'sections'/('ega4-'+n.split('.')[0]+'.tex')
 byfile[q].append((n,new,witness,expected))
for q,rows in byfile.items():
 old=q.read_text();us=units(old);edits=[]
 for n,new,witness,expected in rows:
  s=us[n];ms=list(re.finditer(r'\b[Oo]bsérvese\b',s.text))
  assert len(ms)==expected,(n,len(ms),expected)
  for m in ms:
   a,b=s.start+m.start(),s.start+m.end();edits.append((a,b,new))
   source='EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/ega4-'+n.split('.')[0]+'-fr.tex: '+n+'; '+witness
   changes.append([str(q.relative_to(RESULT)),n,m[0],new,'standard',source])
   review.append([str(q.relative_to(RESULT)),n,witness,m[0],new,
                  'source on: impersonal, same tense' if new.lower().startswith('se ') else 'explicit source author imperative: first person plural'])
 out=old
 for a,b,new in sorted(edits,reverse=True):out=out[:a]+new+out[b:]
 assert [m.text for m in math_spans(old)]==[m.text for m in math_spans(out)]
 q.write_text(out)
assert len(changes)==14
write_tsv(RESULT/'records/CAMBIOS_iv3_register_final_observese.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/IV3_REGISTER_OBSERVESE_FINAL.tsv',['file','place','french_clause','before','after','verdict'],review)
print(json.dumps({'reviewed':14,'changed':14,'source_on_future':8,'source_on_present':1,'source_author_imperative':5,'formulas':'unchanged'}))

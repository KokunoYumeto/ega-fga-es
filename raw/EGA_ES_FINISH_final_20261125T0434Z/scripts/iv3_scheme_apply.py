"""Apply the reviewed lexical distinctions and restore omitted nominal words."""
import json,collections,re
from corpus import RESULT,write_tsv
from iv3_work import apply_edits,DIR
from iv3_manual import patch
from tex_tools import math_spans
rows=json.loads((RESULT/'records/IV3_SCHEME_REVIEW.json').read_text())
original={RESULT/r['file']:(RESULT/r['file']).read_text() for r in rows}
edits=collections.defaultdict(list)
for r in rows:
 if r['status']=='homogeneous exact count':
  typ=r['source_types'][0]
  for m in r['target_matches']:
   word=m['word'];want=word
   if typ=='pre' and 'pre' not in word.lower():want=word.replace('esquema','preesquema').replace('Esquema','Preesquema')
   if typ=='scheme':want=word.replace('preesquema','esquema').replace('Preesquema','Esquema')
   if word!=want:edits[(r['file'],r['source'])].append((m['start'],m['end'],want,r['place']))
  r['verdict']='corrected source scheme/prescheme distinction'
 else:r['verdict']='retained: language order across adjacent formula or joined ultra/pro compound'
for (file,src),ee in edits.items():apply_edits(RESULT/file,ee,src)

custom={
 0:(', al ser localmente de tipo finito sobre ', ', al ser un preesquema localmente de tipo finito sobre '),
 12:(' la unión disjunta de los ',' el preesquema suma de los '),
 14:(r' la \emph{unión disjunta} de los ',r' el preesquema \emph{suma} de los '),
 15:(r' es precisamente la \emph{normalización} de ',r' es precisamente la \emph{normalización} del preesquema '),
 18:(' la unión disjunta de ',' el esquema suma de '),
 21:('existe un esquema $Z$ que es el espectro de un anillo de valoración discreta','existe un espectro de un anillo de valoración discreta $Z$'),
 28:('que en adelante se puede suponer un esquema afín','que en adelante se puede suponer afín'),
 52:('puesto que lo mismo vale para el preesquema reducido','puesto que lo mismo vale para')}
for i,(old,new) in custom.items():
 r=rows[i];patch(r['place'],old,new);r['verdict']='restored source nominal clause without mathematical change';r['before']=old;r['after']=new
for p,t in original.items():assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(p.read_text())],p.name
(RESULT/'records/IV3_SCHEME_REVIEW_FINAL.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
write_tsv(RESULT/'records/IV3_SCHEME_REVIEW_FINAL.tsv',['id','file','source','place','source_types','target_types_before','verdict'],[[r['id'],r['file'],r['source'],r['place'],','.join(r['source_types']),','.join(r['target_types']),r['verdict']] for r in rows])
print('Six exact lexical distinctions and eight source-clause restorations applied; math unchanged')

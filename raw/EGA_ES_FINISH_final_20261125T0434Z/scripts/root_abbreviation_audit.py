"""Audit resp./cf. only where aligned French clauses contain the abbreviation."""
import re,json,collections
import register_review as rr
from corpus import RESULT,FR,write_tsv
from root_scope_pairs import pairs,scoped_units,resolve
rr.PAT=re.compile(r'\b(?:respectivamente|véase|véanse)\b',re.I)
rows=[]
for scope,ed,fp,ft,st,p,offset,fn in pairs():
 fu=scoped_units(ft,fn);su=scoped_units(st,fn)
 for n,f in fu.items():
  if n not in su:continue
  s=su[n]
  for a,b,w,fc,sc in rr.contexts(f.text,s.text):
   abbr='resp.' if w.lower()=='respectivamente' else 'cf.'
   if abbr not in fc:continue
   outp,pos=resolve(st,s.start+a,p,offset)
   rows.append({'scope':scope,'edition':ed,'source':str(fp.relative_to(FR/ed)),'file':str(outp.relative_to(RESULT)),'place':n,'before':w,'after':abbr,'position':pos,'end':pos+(b-a),'fr':fc,'es':sc})
(RESULT/'records/ROOT_ABBREVIATION_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('abbreviation candidates',len(rows),collections.Counter(r['scope'] for r in rows))
for i,r in enumerate(rows):
 if r['edition']=='current':print(i,r['scope'],r['place'],r['before'],'FR',re.sub(r'\s+',' ',r['fr'])[:700],'ES',re.sub(r'\s+',' ',r['es'])[:340])

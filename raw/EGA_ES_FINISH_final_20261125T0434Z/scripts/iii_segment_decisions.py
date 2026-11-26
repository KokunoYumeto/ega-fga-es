#!/usr/bin/env python3
"""Apply explicit source-segment decisions, with matching diplomatic parallels."""
from iii_register_candidates import *
import hashlib
def apply_decisions(O,S={},name='followup'):
 sets={};resolved={};logs=[]
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(ed,part);assert not g;sets[ed,part]=(b,list(segments(ed,part)))
 for (ed,part),(b,ss) in sets.items():
  if ed!='current':continue
  for x in ss:
   k=x['id'].split(':',1)[1]
   if k in O:new=O[k]
   elif k in S:
    new=x['e']
    for a,z in S[k]:
     assert a in new,(k,a,new)
     new=new.replace(a,z)
   else:continue
   resolved[part,x['place'],x['f']]=new
 for (ed,part),(b,ss) in sets.items():
  edits=[]
  for x in ss:
   key=(part,x['place'],x['f'])
   if key not in resolved:continue
   new=resolved[key]
   if new==x['e']:continue
   if any(q[0]<=x['estart'] and x['eend']<=q[1] for q in b):edits.append((x['estart'],x['eend'],new,x['place'],x['e']))
   else:
    for tag,i,j,k,l in difflib.SequenceMatcher(None,x['e'],new,autojunk=False).get_opcodes():
     if tag!='equal':edits.append((x['estart']+i,x['estart']+j,new[k:l],x['place'],x['e'][i:j]))
   logs.append(dict(id=x['id'],edition=ed,part=part,place=x['place'],source_sha256=hashlib.sha256(x['f'].encode()).hexdigest(),before=x['e'],after=new,changed=True,reason=name+'; explicit source comparison; no mathematical proof'))
  if edits:apply_edits(ed,part,edits,b)
  print(name,ed,part,len(edits))
 with (ROOT/'records/III_SEGMENT_DECISIONS.jsonl').open('a') as out:
  for x in logs:out.write(json.dumps(x,ensure_ascii=False)+'\n')
 return logs

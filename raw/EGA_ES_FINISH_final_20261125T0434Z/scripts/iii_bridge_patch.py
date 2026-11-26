#!/usr/bin/env python3
"""Apply manually translated source bridges and their exact diplomatic parallels."""
import json,sys,collections,re,csv,hashlib
from audit_iii_alignment import *
from iii_gap_contexts import bridge
from iii_restore_local_math import translate_math

def masked(t):
 for i,m in reversed(list(enumerate(math_spans(t)))):t=t[:m.start]+f'§{i}§'+t[m.end:]
 return t

def expand(t,fr):
 mm=math_spans(fr);ids=[int(x) for x in re.findall(r'§(\d+)§',t)]
 assert ids==list(range(len(mm))),('formula placeholders',ids,len(mm))
 return re.sub(r'§(\d+)§',lambda m:translate_math(mm[int(m[1])].text),t)

def apply(mapping):
 sets={};resolved={};logs=[]
 for edition,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:sets[edition,part]=bridge(edition,part)
 for key,new in mapping.items():
  ed,part,place,index=key.split(':');all=sets[ed,part][3];x=next(x for x in all if x['id']==key);resolved[(part,place,x['f'])]=expand(new,x['f'])
 for (ed,part),(f,e,b,all) in sets.items():
  edits=[]
  for x in all:
   k=(part,x['place'],x['f'])
   if x['id'] not in mapping and not (ed=='diplomatic' and k in resolved):continue
   new=expand(mapping[x['id']],x['f']) if x['id'] in mapping else resolved[k]
   if not any(q[0]<=x['estart'] and x['eend']<=q[1] for q in b):print('CROSS_INPUT_HELD',x['id']);continue
   edits.append((x['estart'],x['eend'],new,x['place'],x['e']))
   logs.append(dict(edition=ed,part=part,place=x['place'],source_fragment=x['f'],before=x['e'],after=new,kind='source bridge translation; no mathematical proof'))
  if edits:apply_edits(ed,part,edits,b)
  print(ed,part,'applied',len(edits))
 with (ROOT/'records/III_BRIDGE_TRANSLATIONS.jsonl').open('a') as o:
  for x in logs:o.write(json.dumps(x,ensure_ascii=False)+'\n')
 return logs

if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='show':
  part=sys.argv[2];limit=int(sys.argv[3]) if len(sys.argv)>3 else 50;f,e,b,A=bridge('current',part)
  for x in A[:limit]:print('\nID',x['id'],'LEFT',x['left'],'RIGHT',x['right'],'\nFR',masked(x['f']),'\nES',x['e'])
 else:apply(json.load(open(sys.argv[1])))

def apply_units(mapping):
 templates={};logs=[]
 for (part,place),template in mapping.items():
  f=source('current',part).read_text();lo,hi=next((lo,hi) for k,lo,hi in sections(f) if k==place);templates[part,place]=(masked(f[lo:hi]),template)
 for edition,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  if not any(k[0]==part for k in mapping):continue
  f=source(edition,part).read_text();e,b=aggregate(edition,part);fs={k:(lo,hi) for k,lo,hi in sections(f)};es={k:(lo,hi) for k,lo,hi in sections(e)};ed=[]
  for (pr,place),(fm,template) in templates.items():
   if pr!=part:continue
   fa,fb=fs[place];ea,eb=es[place]
   if masked(f[fa:fb])!=fm:print('DIP_UNIT_VARIANT_HELD',edition,part,place);continue
   if not any(q[0]<=ea and eb<=q[1] for q in b):print('CROSS_INPUT_UNIT_HELD',edition,part,place);continue
   new=expand(template,f[fa:fb]);ed.append((ea,eb,new,place,e[ea:eb]));logs.append(dict(edition=edition,part=part,place=place,source_sha256=hashlib.sha256(f[fa:fb].encode()).hexdigest(),before=e[ea:eb],after=new,kind='complete unit source retranslation; no mathematical proof'))
  if ed:apply_edits(edition,part,ed,b)
  print(edition,part,'complete units',len(ed))
 with (ROOT/'records/III_BRIDGE_TRANSLATIONS.jsonl').open('a') as o:
  for x in logs:o.write(json.dumps(x,ensure_ascii=False)+'\n')
 return logs

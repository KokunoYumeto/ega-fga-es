"""Compare scheme/prescheme nouns in source-bounded mathematical intervals."""
import re,json,difflib,collections
from corpus import RESULT,FR
from root_scope_pairs import pairs,scoped_units,resolve
from audit_i_ch1 import mask_notes
from tex_tools import math_spans,math_loose_key
F=re.compile(r'\b(pré)?schéma(s)?\b',re.I);S=re.compile(r'\b(?:sub)?(pre)?esquema(s)?\b',re.I)
R=[];mismatch=[];total=0
for sc,ed,fp,ft,st,p,off,fn in pairs():
 if sc not in ['I','IV4']:continue
 fu=scoped_units(ft,fn);su=scoped_units(st,fn)
 for n,f in fu.items():
  if n not in su or (sc=='I' and n=='prelude'):continue
  s=su[n];ftext=mask_notes(f.text);stext=mask_notes(s.text);ff=math_spans(ftext);ss=math_spans(stext);links=[]
  for bl in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_matching_blocks():links.extend((bl.a+i,bl.b+i) for i in range(bl.size))
  anchors=[(-1,-1)]+links+[(len(ff),len(ss))]
  for (fa,sa),(fb,sb) in zip(anchors,anchors[1:]):
   a=ff[fa].end if fa>=0 else 0;b=ff[fb].start if fb<len(ff) else len(ftext);c=ss[sa].end if sa>=0 else 0;d=ss[sb].start if sb<len(ss) else len(stext);fc=ftext[a:b];ec=stext[c:d]
   fm=list(F.finditer(fc));sm=list(S.finditer(ec));total+=len(fm)
   if not fm and not sm:continue
   if [bool(m[1]) for m in fm]==[bool(m[1]) for m in sm]:continue
   out={'scope':sc,'edition':ed,'source':str(fp.relative_to(FR/ed)),'place':n,'fr':fc,'es':ec,'fr_types':[bool(m[1]) for m in fm],'es_types':[bool(m[1]) for m in sm],'spanish_terms':[]}
   for m in sm:
    q,pos=resolve(st,s.start+c+m.start(),p,off);out['spanish_terms'].append({'file':str(q.relative_to(RESULT)),'position':pos,'end':pos+len(m[0]),'word':m[0]})
   (R if len(fm)==len(sm) else mismatch).append(out)
(RESULT/'records/ROOT_SCHEME_TERMS_REVIEW.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));(RESULT/'records/ROOT_SCHEME_TERMS_COUNT_REVIEW.json').write_text(json.dumps(mismatch,ensure_ascii=False,indent=2))
print('source nominal terms',total,'same-count discrepancies',len(R),'count differences',len(mismatch))
for i,r in enumerate(R):
 if r['edition']=='current':print('SAME',i,r['scope'],r['place'],r['fr_types'],r['es_types'],'FR',re.sub(r'\s+',' ',r['fr'])[:450],'ES',re.sub(r'\s+',' ',r['es'])[:450])
for i,r in enumerate(mismatch):
 if r['edition']=='current':print('COUNT',i,r['scope'],r['place'],r['fr_types'],r['es_types'],'FR',re.sub(r'\s+',' ',r['fr'])[:450],'ES',re.sub(r'\s+',' ',r['es'])[:450])

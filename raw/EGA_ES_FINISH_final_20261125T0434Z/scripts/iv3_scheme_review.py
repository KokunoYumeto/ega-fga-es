"""Compare schéma/préschéma in literal formula-bounded bilingual gaps."""
import re,json,collections
from iv3_align import pairs,units,key
from iv3_core import spans
from audit_i_ch1 import mask_notes
from corpus import RESULT
FP=re.compile(r'\b(?:sous-)?(?:pré)?schémas?\b',re.I)
SP=re.compile(r'\b(?:sub)?(?:pre)?esquemas?\b',re.I)
rows=[];matched=0
for fp,q in pairs():
 ft=fp.read_text();st=q.read_text();fu=units(ft);su=units(st)
 for n,f in fu.items():
  if n not in su or(n=='front' and 'terminal' in fp.name):continue
  s=su[n];ff=spans(mask_notes(f.text));ss=spans(mask_notes(s.text));assert len(ff)==len(ss)
  for i in range(len(ff)+1):
   fa=ff[i-1].end if i else 0;fb=ff[i].start if i<len(ff) else len(f.text)
   sa=ss[i-1].end if i else 0;sb=ss[i].start if i<len(ss) else len(s.text)
   fc=mask_notes(f.text)[fa:fb];sc=mask_notes(s.text)[sa:sb]
   a=list(FP.finditer(fc));b=list(SP.finditer(sc))
   if not a and not b:continue
   at=['pre' if 'pré' in m.group().lower() else 'scheme' for m in a]
   bt=['pre' if 'pre' in m.group().lower() else 'scheme' for m in b]
   if at==bt:matched+=1;continue
   rows.append(dict(id=len(rows),file=str(q.relative_to(RESULT)),source=fp.name,place=n,index=i,
     source_types=at,target_types=bt,french=fc,spanish=sc,
     target_matches=[dict(start=s.start+sa+m.start(),end=s.start+sa+m.end(),word=m.group()) for m in b],
     status='homogeneous exact count' if len(a)==len(b) and len(set(at))==1 else 'manual context'))
(RESULT/'records/IV3_SCHEME_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('matching intervals',matched,'mismatch intervals',len(rows),'classes',dict(collections.Counter(x['status'] for x in rows)))
for r in rows:print(r['id'],r['place'],r['source_types'],r['target_types'],'FR',re.sub(r'\s+',' ',r['french'])[:600],'ES',re.sub(r'\s+',' ',r['spanish'])[:600])

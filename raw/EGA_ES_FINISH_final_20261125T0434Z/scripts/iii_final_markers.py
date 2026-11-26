#!/usr/bin/env python3
"""Add canonical French targets beside retained Spanish aliases; source order QA."""
from audit_iii_alignment import *
PAT=re.compile(r'\\(label|hypertarget)\{([^}]+)\}')
def run():
 out={}
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f=source(ed,part).read_text();e,b=aggregate(ed,part);fm=list(PAT.finditer(f));em=list(PAT.finditer(e));existing={m[2] for m in em};edits=[]
  for m in fm:
   if m[2] in existing:continue
   stem=re.sub(r'[-.]fr$','',m[2]);c=[q for q in em if q[2]==stem]
   assert len(c)==1,('missing target',ed,part,m[2],[x[2] for x in c])
   old=c[0];new=old[0]+'\n\\'+m[1]+'{'+m[2]+'}'+('{}' if m[1]=='hypertarget' else '')
   place=next(k for k,a,z in sections(e) if a<=old.start()<z)
   edits.append((old.start(),old.end(),new,place,old[0]));existing.add(m[2])
  if edits:apply_edits(ed,part,edits,b)
  e,b=aggregate(ed,part);fl=[m[2] for m in fm];el=[m[2] for m in PAT.finditer(e) if m[2] in set(fl)]
  pages=re.compile(r'\\oldpage(?:\[[^]]*\])?\{\d+\}')
  fp=pages.findall(f);ep=pages.findall(e)
  out[ed+'_'+part]=dict(labels_source=len(fl),canonical_targets=len(el),labels_missing=list(set(fl)-set(el)),label_order_exact=fl==el,pages_source=len(fp),pages_spanish=len(ep),page_order_exact=fp==ep)
  if fl!=el:
   print('LABEL_ORDER',ed,part,[(tag,fl[i:j],el[k:l]) for tag,i,j,k,l in difflib.SequenceMatcher(None,fl,el,autojunk=False).get_opcodes() if tag!='equal'])
  if fp!=ep:print('PAGE_ORDER',ed,part,[(tag,fp[i:j],ep[k:l]) for tag,i,j,k,l in difflib.SequenceMatcher(None,fp,ep,autojunk=False).get_opcodes() if tag!='equal'])
 (ROOT/'records/III_MARKER_AUDIT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':run()

#!/usr/bin/env python3
"""Restore source TeX in IV1 ch0 after model comparison of unmatched blocks.
The reviewed one-to-one replacements use the supplied layer, even where a
previous Spanish emendation differs mathematically. No proof claim is made.
"""
from pathlib import Path
import re,csv,difflib,argparse
from tex_tools import math_spans,math_loose_key,retain_translated_text
P=argparse.ArgumentParser();P.add_argument('--source-root',type=Path,required=True);P.add_argument('--apply',action='store_true');a=P.parse_args();r=Path(__file__).resolve().parents[1]
ep=re.compile(r'\\begin\{[^}]+\}\[([\d.]+)\]')
def units(t):
 ms=list(ep.finditer(t));d={}
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);text=t[m.start():end];h=re.search(r'\\(?:section|subsection)\{',text)
  if h:text=text[:h.start()]
  d[m.group(1)]=(m.start(),text)
 return d
changes=[];pending=[]
for ed in ['current','diplomatic']:
 for fp in sorted((a.source_root/'EGA_ES_FINISH_1_FRANCES/fr'/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
  sp=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed.upper())/'ega4'/fp.name.replace('-fr.tex','-es.tex');ft=fp.read_text();st=sp.read_text();fu=units(ft);su=units(st);edits=[]
  for key,(fstart,ftext) in fu.items():
   if key not in su:continue
   sstart,stext=su[key];fs=math_spans(ftext);ss=math_spans(stext);seq=difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in fs],[math_loose_key(x.text) for x in ss],autojunk=False)
   for op,fa,fb,sa,sb in seq.get_opcodes():
    if op=='equal' or (op=='replace' and fb-fa==sb-sa):
     for f,s in zip(fs[fa:fb],ss[sa:sb]):
      new=retain_translated_text(f.text,s.text)
      if new is None:pending.append([ed,fp.name,key,'text commands',f.text,s.text]);continue
      if new==s.text:continue
      punct=''
      if s.kind!='inline' and f.kind=='inline':
       faft=ftext[f.end:];saft=stext[s.end:]
       if faft and faft[0] in '.,;:' and not saft.lstrip().startswith(faft[0]):punct=faft[0]
      edits.append((sstart+s.start,sstart+s.end,new+punct));changes.append([str(sp.relative_to(r)),key,s.text,new+punct,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/IV1/native/ega4/'+fp.name+': '+key+'; model-reviewed source-formula correspondence'])
    else:pending.append([ed,fp.name,key,op,' | '.join(x.text for x in fs[fa:fb]),' | '.join(x.text for x in ss[sa:sb])])
  if a.apply:
   for b,e,z in sorted(edits,reverse=True):st=st[:b]+z+st[e:]
   sp.write_text(st)
with (r/'records/IV1_CH0_MATH_DRY_RUN.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(changes)
if a.apply:
 with (r/'records/IV1_CH0_CHANGES_math.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(changes)
print('planned/applied',len(changes),'pending',len(pending))
for i,x in enumerate(pending):print(i,'\t'.join(x))

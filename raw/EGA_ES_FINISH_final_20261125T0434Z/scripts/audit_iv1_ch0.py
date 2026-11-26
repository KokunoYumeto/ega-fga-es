#!/usr/bin/env python3
"""Audit IV1 chapter-0 formulas against the supplied French; no proof checking."""
from pathlib import Path
import re,csv,difflib,argparse,collections
from tex_tools import math_spans,math_loose_key,retain_translated_text
P=argparse.ArgumentParser();P.add_argument('--source-root',type=Path,required=True);a=P.parse_args();r=Path(__file__).resolve().parents[1]
ep=re.compile(r'\\begin\{[^}]+\}\[([\d.]+)\]')
def units(t):
 ms=list(ep.finditer(t));out={}
 for i,m in enumerate(ms):
  e=ms[i+1].start() if i+1<len(ms) else len(t);text=t[m.start():e];h=re.search(r'\\(?:section|subsection)\{',text)
  if h:text=text[:h.start()]
  out[m.group(1)]=(m.start(),text)
 return out
pending=[];stats=[]
for ed in ['current','diplomatic']:
 for fp in sorted((a.source_root/'EGA_ES_FINISH_1_FRANCES/fr'/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
  sp=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed.upper())/'ega4'/fp.name.replace('-fr.tex','-es.tex');fu=units(fp.read_text());su=units(sp.read_text())
  for key,(fstart,ft) in fu.items():
   if key not in su:pending.append([ed,fp.name,key,'unit missing','','']);continue
   sstart,st=su[key];fs=math_spans(ft);ss=math_spans(st);seq=difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in fs],[math_loose_key(x.text) for x in ss],autojunk=False);paired=0;exact=0
   for op,fa,fb,sa,sb in seq.get_opcodes():
    if op=='equal':
     paired+=fb-fa;exact+=sum(re.sub(r'\s+','',retain_translated_text(f.text,s.text) or f.text)==re.sub(r'\s+','',s.text) for f,s in zip(fs[fa:fb],ss[sa:sb]))
    else:pending.append([ed,fp.name,key,op,' | '.join(x.text for x in fs[fa:fb]),' | '.join(x.text for x in ss[sa:sb])])
   stats.append([ed,fp.name,key,len(fs),len(ss),paired,exact])
  for key in set(su)-set(fu):pending.append([ed,fp.name,key,'extra Spanish numbered unit','',''])
for name,head,rows in [('IV1_CH0_PENDING.tsv',['edition','file','place','kind','french_math','spanish_math'],pending),('IV1_CH0_AUDIT_STATS.tsv',['edition','file','place','french_math','spanish_math','aligned','exact'],stats)]:
 with (r/'records'/name).open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
print('units',len(stats),'math',sum(x[3] for x in stats),'pending',len(pending))
for i,x in enumerate(pending):print(i,'\t'.join(x))

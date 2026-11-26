#!/usr/bin/env python3
"""Align inherited chapter-0 math to supplied French by numbered unit.
This is a transcription audit, not a mathematical proof check.
"""
from pathlib import Path
import re,csv,argparse,difflib,collections
from tex_tools import numbered_units,math_spans,math_loose_key,retain_translated_text
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--apply',action='store_true');a=p.parse_args()
r=Path(__file__).resolve().parents[1];changes=[];pending=[];stats=[]
def units(t):
 us=numbered_units(t)
 for n,u in us.items():
  h=re.search(r'\\(?:subsection|section)\{',u.text)
  if h:u.end=u.start+h.start();u.text=u.text[:h.start()]
 return us
for ed in ['current','diplomatic']:
 rel='EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/BASE/native/ega1/ega0-1-fr.tex';fr=(a.source_root/rel).read_text();fu=units(fr)
 for fp in sorted((r/'tree/worktree/es'/ed.upper()/'EGA_I_ch0').glob('ega0_i_*.tex')):
  text=fp.read_text();edits=[]
  for num,su in units(text).items():
   if tuple(map(int,num.split('.'))) >= (4,4,3):continue
   f=fu[num];fm=math_spans(f.text);sm=math_spans(su.text);seq=difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in fm],[math_loose_key(x.text) for x in sm],autojunk=False);paired=0
   for op,fa,fb,sa,sb in seq.get_opcodes():
    if op=='equal':
     for fi,si in zip(range(fa,fb),range(sa,sb)):
      fs,ss=fm[fi],sm[si];paired+=1
      new=retain_translated_text(fs.text,ss.text)
      if new is None:pending.append([ed,fp.name,num,'text command',fs.text,ss.text]);continue
      if new!=ss.text:
       edits.append((su.start+ss.start,su.start+ss.end,new));changes.append([str(fp.relative_to(r)),num,ss.text,new,'own comparison',rel+': '+num+'; exact source TeX restored'])
    else:pending.append([ed,fp.name,num,op,' | '.join(x.text for x in fm[fa:fb]),' | '.join(x.text for x in sm[sa:sb])])
   stats.append([ed,fp.name,num,len(fm),len(sm),paired])
  if a.apply:
   for b,e,new in sorted(edits,reverse=True):text=text[:b]+new+text[e:]
   fp.write_text(text)
def write(n,h,rs):
 with (r/'records'/n).open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(h);w.writerows(rs)
write('CH0_EXISTING_NOTATION_DRY_RUN.tsv',['file','place','before','after','kind','source'],changes)
write('CH0_EXISTING_NOTATION_PENDING.tsv',['edition','file','place','kind','french_math','spanish_math'],pending)
write('CH0_EXISTING_NOTATION_STATS.tsv',['edition','file','place','french_formulas','spanish_formulas','paired'],stats)
if a.apply:write('CH0_CHANGES_notation.tsv',['file','place','before','after','kind','source'],changes)
print('units',len(stats),'source formulas',sum(x[3] for x in stats),'paired',sum(x[5] for x in stats),'changes',len(changes),'pending',len(pending))
for x in pending:print('\t'.join(x))

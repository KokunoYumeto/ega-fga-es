#!/usr/bin/env python3
"""Restore chapter-0 source anchors and missing chapter heading in both layers."""
from pathlib import Path
import re,csv,argparse
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parents[1];rows=[]
for ed in ['CURRENT','DIPLOMATIC']:
 src='EGA_ES_FINISH_1_FRANCES/fr/'+ed.lower()+'/BASE/native/ega1/ega0-1-fr.tex';fr=(a.source_root/src).read_text();labs={x.removesuffix('-fr'):x for x in re.findall(r'\\label\{([^}]+)\}',fr)}
 for fp in sorted((r/'tree/worktree/es'/ed/'EGA_I_ch0').glob('ega0_i_*.tex')):
  t=fp.read_text();new=t
  for m in reversed(list(re.finditer(r'\\label\{([^}]+)\}',t))):
   old=m.group(1);key=labs.get(old.removesuffix('-fr'))
   if key and key!=old:
    new=new[:m.start(1)]+key+new[m.end(1):];rows.append([str(fp.relative_to(r)),key,m.group(),r'\label{'+key+'}','standard',src+'; NOTATION_EGA.md §6'])
  for m in reversed(list(re.finditer(r'\\(?:ref|sref|eref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]',new))):
   old=m.group(1) or m.group(2);key=labs.get(old.removesuffix('-fr'))
   if key and key!=old:
    k=1 if m.group(1) else 2;new=new[:m.start(k)]+key+new[m.end(k):];rows.append([str(fp.relative_to(r)),key,old,key,'standard',src+'; existing reference target follows restored source label'])
  if fp.name=='ega0_i_1_0_1_3.tex' and 'CAPÍTULO 0' not in new:
   marker=r'\oldpage[0\textsubscript{I}]{11}';assert new.count(marker)==1;new=new.replace(marker+'\n','');pos=new.index('\\section{')
   head='\\clearpage\n'+marker+'\n\\begin{center}\n{\\large CAPÍTULO 0\\par}\n\\vspace{1.5em}\n{\\Large\\bfseries PRELIMINARES\\par}\n\\end{center}\n\n';new=new[:pos]+head+new[pos:];rows.append([str(fp.relative_to(r)),'chapter 0 heading','heading absent; page 11 marker after first subsection',head,'assembly',src+': initial chapter heading and original page marker'])
  fp.write_text(new)
with (r/'records/CH0_CHANGES_structure.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(rows)
print('Structural restorations:',len(rows))

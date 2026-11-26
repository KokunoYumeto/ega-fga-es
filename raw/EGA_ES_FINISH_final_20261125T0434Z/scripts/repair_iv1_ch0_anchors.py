#!/usr/bin/env python3
"""Restore source anchor keys and math mode in IV1 chapter-0 headings."""
from pathlib import Path
import re,csv
from tex_tools import balanced_end
r=Path(__file__).resolve().parents[1];src=r.parent/'source/EGA_ES_FINISH_1_FRANCES/fr';changes=[]
for ed in ['current','diplomatic']:
 for fp in sorted((src/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
  p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed.upper())/'ega4'/fp.name.replace('-fr.tex','-es.tex');fr=fp.read_text();es=p.read_text();labels={x.removesuffix('-fr'):x for x in re.findall(r'\\label\{([^}]+)\}',fr)}
  for m in reversed(list(re.finditer(r'\\label\{([^}]+)\}',es))):
   old=m.group(1);key=old.removesuffix('-es').removesuffix('-fr')
   if key in labels and old!=labels[key]:
    b=m.group();z=r'\label{'+labels[key]+'}';es=es[:m.start()]+z+es[m.end():];changes.append([str(p.relative_to(r)),labels[key],b,z,'standard','NOTATION_EGA.md §6; EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/IV1/native/ega4/'+fp.name])
  for m in reversed(list(re.finditer(r'\\(?:sref|ref|eref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]',es))):
   old=m.group(1) or m.group(2);key=old.removesuffix('-es').removesuffix('-fr')
   if key in labels and old!=labels[key]:
    i=1 if m.group(1) else 2;es=es[:m.start(i)]+labels[key]+es[m.end(i):];changes.append([str(p.relative_to(r)),labels[key],old,labels[key],'standard','NOTATION_EGA.md §6; reference follows source key'])
  if fp.name=='ega0-16-fr.tex':
   b=r'\label{0.16.4.6-es}';z=r'\EGAReaderTarget{canon-ref.0.16.4.6-fr}{0.16.4.6-fr}';assert b in es;es=es.replace(b,z);changes.append([str(p.relative_to(r)),'0.16.4.6',b,z,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/IV1/native/ega4/'+fp.name+': source target command'])
  fh=list(re.finditer(r'\\(?:section|subsection)\{',fr));sh=list(re.finditer(r'\\(?:section|subsection)\{',es));assert len(fh)==len(sh),(fp.name,len(fh),len(sh))
  for fm,sm in reversed(list(zip(fh,sh))):
   fe=balanced_end(fr,fm.end()-1);se=balanced_end(es,sm.end()-1);a=fr[fm.start():fe];b=es[sm.start():se]
   if '$p$' in b and '$p$' not in a:
    z=b.replace('$p$','p');es=es[:sm.start()]+z+es[se:];changes.append([str(p.relative_to(r)),'section heading',b,z,'standard','NOTATION_EGA.md §1; source p in prose heading'])
  if r'\text{et}' in es:
   b=r'\text{et}';z=r'\text{y}';n=es.count(b);es=es.replace(b,z);changes.append([str(p.relative_to(r)),'21.1.4; '+str(n)+' occurrence(s)',b,z,'own comparison','Translate French connective inside formula; permitted text-command translation'])
  p.write_text(es)
with (r/'records/IV1_CH0_CHANGES_anchors.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(changes)
print('anchor/heading/text restorations',len(changes))

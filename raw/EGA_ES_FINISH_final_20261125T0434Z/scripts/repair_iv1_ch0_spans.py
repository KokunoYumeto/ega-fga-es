#!/usr/bin/env python3
"""Apply model-reviewed multi-span/prose correspondences in IV1 chapter 0."""
from pathlib import Path
import re,csv,difflib
from tex_tools import math_spans,math_loose_key,numbered_units
r=Path(__file__).resolve().parents[1];source=r.parent/'source/EGA_ES_FINISH_1_FRANCES/fr';changes=[];texts={}
def edit(ed,n,k,b,z):
 p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed)/'ega4'/('ega0-'+n+'-es.tex');t=texts.get(p,p.read_text());assert t.count(b)==1,(ed,n,k,repr(b),t.count(b));texts[p]=t.replace(b,z);changes.append([str(p.relative_to(r)),k,b,z,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+ed.lower()+'/IV1/native/ega4/ega0-'+n+'-fr.tex: '+k+'; model-reviewed source/prose correspondence'])
# The reviewed displayed lists consist only of source inline formulas and
# punctuation, with Spanish y/para where the source uses et/pour.
allowed={'15.1.9','15.1.15','16.4.3','18.3.1','19.7.1','22.2.5','22.4.3'}
for ed in ['CURRENT','DIPLOMATIC']:
 for n in ['15','16','18','19','22']:
  p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed)/'ega4'/('ega0-'+n+'-es.tex');ft=(source/ed.lower()/'IV1/native/ega4'/('ega0-'+n+'-fr.tex')).read_text();st=p.read_text();fu=numbered_units(ft);su=numbered_units(st)
  for k in allowed.intersection(fu):
   f=fu[k].text;s=su[k].text;fm=math_spans(f);sm=math_spans(s);seq=difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in fm],[math_loose_key(x.text) for x in sm],autojunk=False)
   for op,fa,fb,sa,sb in seq.get_opcodes():
    if op!='replace' or sb-sa!=1 or fb-fa<2 or sm[sa].kind!='display':continue
    b=sm[sa].text;z=f[fm[fa].start:fm[fb-1].end].replace(' et ',' y ').replace('(pour ','(para ');post=f[fm[fb-1].end:];punct=re.match(r'~?[.,;:]',post)
    if punct and not s[sm[sa].end:].lstrip().startswith(punct.group().lstrip('~')):z+=punct.group()
    edit(ed,n,k,b,z)
 # Removing a redundant named object restores the source wording.
 edit(ed,'18','18.3.2',"$E\\oplus_LL'$ deducida de $E$\npor $w$","$E\\oplus_LL'$ deducida de\n$w$")
 edit(ed,'19','19.4.7',"$\\varphi_0$\nel homomorfismo canónico\n$B_0/\\mathfrak K'B_0\\to B_0/\\mathfrak KB_0$","$\\varphi_0:B_0/\\mathfrak K'B_0\\to B_0/\\mathfrak KB_0$ el\nhomomorfismo canónico")
 edit(ed,'20','20.5.11',r'$d(xy)\equiv xdy\pmod{\mathfrak K.\Omega^1_{B/A}}$',r'$d(xy)\equiv xdy$ (mod.~$\mathfrak{K}.\Omega^1_{B/A}$)')
 edit(ed,'21','21.2.1',r'$v(q(z))\equiv z\pmod{\mathfrak K}$',r'$v(q(z))\equiv z$ (mod.~$\mathfrak K$)')
 edit(ed,'21','21.5.3','y sea $\\mathfrak J\\ne0$ un ideal de $C$ contenido en','y sea $\\mathfrak J$ un ideal $\\ne0$ de $C$ contenido en')
 p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed)/'ega4/ega0-21-es.tex';t=texts.get(p,p.read_text())
 for k in ['21.1.6.1','21.4.1','21.5.1']:
  u=numbered_units(t)[k];b=u.text;assert r'n$^\circ$' in b;z=b.replace(r'n$^\circ$',r'n\textsuperscript{o}');edit(ed,'21',k,b,z);t=texts[p]
edit('DIPLOMATIC','17','17.1.8','no divisor de cero forma parte de un sistema de parámetros','no divisor de $0$ forma parte de un sistema de parámetros')
edit('DIPLOMATIC','18','18.2.1',r'$x$ de $f^{-1}(b)$',r'$x\in f^{-1}(b)$')
edit('DIPLOMATIC','21','21.1.4',r'$\alpha,\beta\in A$',r'$\alpha$, $\beta$ en $A$')
p=r/'tree/worktree/es/PORTED_20261109/IV1_DIPLOMATIC/ega4/ega0-21-es.tex';t=texts[p];u=numbered_units(t)['21.8.3'].text
b='uno de los $N_\\alpha$ es nulo';z='uno de los $N_\\alpha$ es $0$';assert b in u;edit('DIPLOMATIC','21','21.8.3',b,z)
b='\\emph{intersección} es nula';z='\\emph{intersección} es $0$';assert b in u;edit('DIPLOMATIC','21','21.8.3',b,z)
for p,t in texts.items():p.write_text(t)
with (r/'records/IV1_CH0_CHANGES_spans.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(changes)
print('Reviewed multi-span/prose changes:',len(changes))

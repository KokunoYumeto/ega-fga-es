#!/usr/bin/env python3
"""Restore supplied IV1 chapter-0 source structure and missing prose."""
from pathlib import Path
import re,csv
r=Path(__file__).resolve().parents[1];changes=[];translation=[];events=[];texts={}
who='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; IV1 chapter-0 run'
def edit(ed,num,place,b,z,kind='own comparison'):
 p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed)/'ega4'/('ega0-'+num+'-es.tex');t=texts.get(p,p.read_text());assert t.count(b)==1,(ed,num,place,repr(b),t.count(b));texts[p]=t.replace(b,z);src='EGA_ES_FINISH_1_FRANCES/fr/'+ed.lower()+'/IV1/native/ega4/ega0-'+num+'-fr.tex'
 changes.append([str(p.relative_to(r)),place,b,z,kind,src+': '+place]);events.append([ed+':0.'+place,'2026-11-25',who,'carried as background without fault found','Compared Spanish to supplied French; restored source structure/text. No mathematical proof verification.'])
for ed in ['CURRENT','DIPLOMATIC']:
 b='\\end{env}\n\n\\oldpage[0\\textsubscript{IV-1}]{62}\n\n\\begin{env}[18.3.6.4]\n\\label{0.18.3.6.4-es}\n';z='\\oldpage[0\\textsubscript{IV-1}]{62}\n\n';edit(ed,'18','18.3.6',b,z)
 b='\\[\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A\'}(B,L)\n  \\tag{18.3.6.4}\n\\]';z='\\begin{equation}\n\\label{0.18.3.6.4-fr}\n\\tag{18.3.6.4}\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A\'}(B,L)\n\\end{equation}'
 if ed=='DIPLOMATIC':b=b.replace('  \\tag{18.3.6.4}\n','')
 prefix='Finalmente, la aplicación $(u,1_B,1_L)_*$ es la aplicación\n';edit(ed,'18','18.3.6.4',prefix+b,prefix+z)
 edit(ed,'19','19.5.6.3',r'\begin{env}[19.5.6.4]'+'\n','')
 b='\\end{enumerate}\n\\end{env}\n\n\\oldpage[0\\textsubscript{IV-1}]{97}\n\n\\begin{lemma}[19.5.6.5]';z='\\end{enumerate}\n\n\\begin{lemma}[19.5.6.5]';edit(ed,'19','19.5.6.3',b,z)
 b='canónica $Q$ en este módulo producto del módulo\n';z='canónica $Q$ en este módulo producto del\n  \\oldpage[0\\textsubscript{IV-1}]{97}\n  módulo\n';edit(ed,'19','19.5.6.3',b,z)
 b='Se pondrá\n\\end{env}\n\n\\begin{env}[21.6.1.2]\n\\label{0.21.6.1.2-es}\n\\[\n';z='Se pondrá\n\\begin{equation}\n\\label{0.21.6.1.2-fr}\n\\tag{21.6.1.2}\n';edit(ed,'21','21.6.1',b,z)
 b='\\cong\\operatorname{Ker}(\\Upsilon_{L/K/k_0}\\to\\Upsilon_{L/K/k})\n\\]';z=b.replace('\\]','\\end{equation}');edit(ed,'21','21.6.1.2',b,z)
 p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed)/'ega4/ega0-21-es.tex';b='\\oldpage[0\\textsubscript{IV-1}]{157}\n';addition='Es claro que las nociones definidas en (21.1.9) no cambian cuando se\nreemplaza $A$ por el subanillo $A[B^p]$ de $B$; en otras palabras, siempre se puede\nsuponer que se tiene $B^p\\subset A\\subset B$.\n\nSi $M$ es una parte $p$-libre de $B$ sobre $A$, es claro que toda parte\nde $M$ es $p$-libre sobre $A$. Además:\n\n';edit(ed,'21','21.1.9',b,b+addition,'assembly');translation.append([str(p.relative_to(r)),'EGA_ES_FINISH_1_FRANCES/fr/'+ed.lower()+'/IV1/native/ega4/ega0-21-fr.tex','21.1.9: two paragraphs after original page marker 157',addition])
b="$\\gr_\\bullet(M)\\otimes(A/\\mathfrak{J}'')$ es inyectiva"
note=r'''\footnote{Precisión editorial: la regularidad de $f_n$ significa la inyectividad de la homotecia. La extensión polinómica es una suma directa de copias del módulo y conserva esta inyectividad. La sobreyectividad no es necesaria: para $A=k[x,y]$, $M=A$ provisto de la filtración $M_0=M$, $M_i=0$ para $i\geq1$, y $(f_1,f_2)=(x,y)$, la multiplicación por $y$ en $k[y]$ es inyectiva y no alcanza $1$.}'''
edit('CURRENT','15','15.1.8',b,b+note,'assembly');translation.append(['tree/worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-15-es.tex','EGA_ES_FINISH_1_FRANCES/fr/current/IV1/native/ega4/ega0-15-fr.tex','15.1.8: source editorial footnote',note])
b='En cambio, $B$ es formalmente suave si y\n  solo si $\\ker(\\rho)=\\ker(\\rho)^2$.';z='En cambio, $B$ solo es formalmente suave si $\\rho$ es \\emph{biyectivo}.';edit('CURRENT','19b','19.10.3',b,z)
for p,t in texts.items():p.write_text(t)
def write(n,h,rows):
 with (r/'records'/n).open('w',encoding='utf-8',newline='') as f:w=csv.writer(f,delimiter='\t');w.writerow(h);w.writerows(rows)
write('IV1_CH0_CHANGES_structure.tsv',['file','place','before','after','kind','source'],changes)
write('IV1_CH0_NEW_PROSE.tsv',['file','french_source','range','text'],translation)
write('IV1_CH0_EVENTS_structure.tsv',['statement_id','date','who','type','outcome'],events)
print('changes',len(changes),'translated passages',len(translation))

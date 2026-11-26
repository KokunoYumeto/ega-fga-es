"""Restore omitted source anchors at the source-corresponding formula or statement."""
import re,csv,collections
from corpus import FR,ES,RESULT,SOURCE,write_tsv,canonical
from audit_i_ch1 import i_units,texts,mask_notes
from tex_tools import math_spans,math_loose_key
changes=[];edits=collections.defaultdict(list)
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);su=i_units(t);have={canonical(m[1]) for m in re.finditer(r'\\label\{([^}]+)\}',t)}
 for fp in sorted((FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex')):
  ft=fp.read_text()
  for n,fu in i_units(ft).items():
   eu=su[n]
   for m in re.finditer(r'\\label\{([^}]+)\}',fu.text):
    if canonical(m[1]) in have:continue
    if m[1]=='I.5.5.5-fr':
     wrong=r'\label{I.5.5.4}';assert wrong in eu.text
     a=eu.start+eu.text.index(wrong);b=a+len(wrong);new=r'\label{I.5.5.5-fr}'
     edits[p].append((a,b,new));changes.append([str(p.relative_to(RESULT)),n,wrong,new,'own comparison',str(fp.relative_to(FR/layer.lower()))+': statement label'])
     continue
    ff=[f for f in math_spans(mask_notes(fu.text)) if f.start>=m.end()]
    assert ff,(n,m[1]);f=ff[0];ss=[s for s in math_spans(mask_notes(eu.text)) if math_loose_key(s.text)==math_loose_key(f.text)]
    assert len(ss)==1,(n,m[1],len(ss));a=eu.start+ss[0].start
    new='\\phantomsection\\label{'+m[1]+'}\n';edits[p].append((a,a,new));changes.append([str(p.relative_to(RESULT)),n,'',new,'own comparison',str(fp.relative_to(FR/layer.lower()))+': source anchor at matching formula'])
for p,ee in edits.items():
 t=p.read_text()
 for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
 p.write_text(t)
p=ES/'worktree/es/PORTED_20261109/IV4/ega4/ega4-16-es/components/00_intro.tex';t=p.read_text()
old=r'\oldpage[IV-4]{5}';assert old in t;t=t.replace(old+'\n','')
new=r'''\clearpage
\thispagestyle{plain}
\oldpage[IV-4]{5}
\phantomsection\label{chapter:IV4-fr}
\begin{center}
{\large CAPÍTULO IV \textit{(fin)}\par}
\vspace{1.5em}
{\Large\bfseries ESTUDIO LOCAL DE LOS ESQUEMAS\\
Y DE LOS MORFISMOS DE ESQUEMAS\par}
\end{center}
'''
t=new+t;p.write_text(t)
changes.append([str(p.relative_to(RESULT)),'chapter:IV4','',new,'own comparison','IV4/native/ega4/ega4-16-fr.tex: initial chapter heading and page marker'])
write_tsv(RESULT/'records/CAMBIOS_root_anchors.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/TRADUCCION_iv4_heading.tsv',['file','french_source','range','words'],[[str(p.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-16-fr.tex','initial chapter heading lines7–12',18]])
print('anchors/headings',len(changes))

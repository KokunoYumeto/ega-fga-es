"""Source-bound repairs and condition-marker spelling in IV3 §13."""
import re
from iv3_manual import patch,source_unit
from iv3_work import DIR,apply_edits
from iv3_align import units
patch('13.1.2',r"$j_0:X_0'\hookrightarrow X_0$",r"$j_0:X'_0\to X_0$")
patch('13.1.3',r'''\[
X=X_0\times_{Y_0}Y,\qquad f=f_0\times 1_Y,
\]''',r'$X=X_0\times_{Y_0}Y$, $f=f_0\times 1_Y$,')
patch('13.2.9',r'''también se satisfacen cuando se sustituye $X'$ por $X''$ y $x$ por $x$''',r'''también se satisfacen para $X''$ y $x$''')
patch('13.3.1.1',r'n$^{\text{o}}$',r'n.º')
patch('13.3.1.1',r'''las imágenes por $p$ de los puntos maximales de $Z$ son los puntos maximales de $Y$''',r'''los puntos maximales de $Z$ tienen por imágenes por $p$ los puntos maximales de $Y$''')
patch('13.3.2',r'equidimen-',r'equidimen%')
# The source uses $a$), $a'$), etc. at these reviewed condition references.
# Align their boundary spelling without treating them as missing algebra.
q=DIR/'sections/ega4-13.tex'
for n in ['13.3.1','13.3.1.1','13.3.2','13.3.3','13.3.8','13.3.9']:
 t=q.read_text();s=units(t)[n];f=source_unit(n)
 fa=0;sa=0
 if n=='13.3.1':
  fa=f.index(r'\begin{proof}');sa=s.text.index(r'\begin{proof}')
 fm=list(re.finditer(r'\$([a-d])(\x27*)\$\)',f[fa:]))
 sm=list(re.finditer(r'\\emph\{[a-d](?:\$\x27+\$)?\)\}|\$[a-d]\x27*\)\$|\$[a-d]\x27*\$\)',s.text[sa:]))
 def label(x):
  return re.sub(r'[^a-d\x27]','',re.sub(r'\\emph','',x))
 assert len(fm)==len(sm) and [label(x.group()) for x in fm]==[label(x.group()) for x in sm],(n,'Condition sequence differs')
 edits=[(s.start+sa+b.start(),s.start+sa+b.end(),a.group(),n) for a,b in zip(fm,sm) if a.group()!=b.group()]
 if edits:apply_edits(q,edits,'ega4-13-fr.tex')
print('Reviewed §13 source clauses complete')


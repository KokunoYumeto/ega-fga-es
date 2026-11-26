"""Complete the reviewed register clauses and contextual glossary corrections."""
import json,re
from iv3_manual import patch,source_unit
from iv3_align import pairs,units
from iv3_work import apply_edits,DIR
from tex_tools import math_spans
from corpus import RESULT

original={q:q.read_text() for fp,q in pairs() if q.name!='ega4-8.tex'}
# All remaining -rnos clauses were compared with the French source. The one
# explicit nous pouvons nous borner (15.7.9) remains in the author register.
for fp,q in pairs():
 if q.name=='ega4-8.tex':continue
 t=q.read_text();ee=[]
 for n,u in units(t).items():
  if n=='front' or (n.startswith('15.7.') != ('terminal' in fp.name) and q.name=='ega4-15.tex'):continue
  for m in re.finditer(r'\b(?:reducirnos|limitarnos|restringirnos)\b',u.text):
   if n in ['15.7.9','9.4.9']:continue
   ee.append((u.start+m.start(),u.start+m.end(),m.group()[:-3],n))
 if ee:apply_edits(q,ee,fp.name)

patch('10.2.7','Basta pues (por','Se puede, pues, (por')
patch('9.4.9','tras restringirnos a un abierto afín','considerando un abierto afín')
patch('9.2.6.1','nos reduce al caso','reduce al caso')
patch('9.7.7','nos permiten suponer','permiten suponer')
patch('11.3.8',r'la inducción sobre $n$ nos reduce inmediatamente al caso',
 r'se reduce inmediatamente por inducción sobre $n$ al caso')
patch('11.3.8','escribimos $g$ en lugar de $g_1$','escribiremos $g$ en lugar de $g_1$')

patch('10.8.8',r'Supongamos que las hipótesis sobre $f$ y $\mathcal F$ son las de \sref{IV.9.9.1}. Entonces la función',
 r'Siendo las hipótesis sobre $f$ y $\mathcal F$ las de \sref{IV.9.9.1}, la función')
patch('11.3.14',r"Si se pone $X'=X\times_Y Y'$, y sean $f':X'\to Y'$ y $g':X'\to X$ las proyecciones. El morfismo $g'$ es integral",
 r"Si se pone $X'=X\times_Y Y'$, y si $f':X'\to Y'$ y $g':X'\to X$ son las proyecciones, $g'$ es entero")
patch('11.3.14','integral y birracional','entero y birracional')
patch('11.3.14','un dominio local íntegro','un anillo local íntegro')
patch('11.3.14','es un dominio íntegro e íntegramente cerrado','es íntegro e íntegramente cerrado')
patch('11.3.14','es un dominio íntegro y es geométricamente','es íntegro y geométricamente')
patch('11.4.1.1',r'Pongamos $A_0=A/\mathfrak J_1$, $M_0=M\otimes_A A_0$ y observemos que',
 r'Poniendo $A_0=A/\mathfrak J_1$, $M_0=M\otimes_A A_0$, observemos que')
patch('11.2.9.5',r'$A_0$ es \emph{reducida}',r'$A_0$ es \emph{reducido}')
patch('11.5.5.1','inyector','inyectivo')
patch('13.1.1','dominios íntegros','anillos íntegros')
patch('14.1.1',r'\emph{no} implica',r'\emph{no implica}')
patch('15.7.4','son reducidos; entonces, por la definición','son reducidos y después, por la definición')
patch('14.4.1.3',r'\sref[$\mathbf{0}_{\mathrm I}$]{0.2.1.8}); esto prueba que',
 r'\sref[$\mathbf{0}_{\mathrm I}$]{0.2.1.8}, que prueban que')
patch('14.4.1.3','es irreducible; reemplazando','es irreducible); reemplazando')
patch('14.4.1.3','Reemplazando finalmente','Reemplazando eventualmente')

# French espaces annelés en anneaux locaux, glossary row 11.
q=DIR/'sections/ega4-10.tex';t=q.read_text();ee=[]
for n,u in units(t).items():
 for m in re.finditer('espacios anillados en anillos locales',u.text):
  assert 'annelés' in source_unit(n),(n,'glossary source')
  ee.append((u.start+m.start(),u.start+m.end(),'espacios localmente anillados',n))
assert len(ee)==4,len(ee)
apply_edits(q,ee,'ega4-10-fr.tex')
for n,old,new in [
 ('11.6.2','anillo local integral unirramificado','anillo local íntegro unirramificado'),
 ('11.7.2','anillos integrales íntegramente cerrados','anillos íntegros íntegramente cerrados'),
 ('11.7.2','es un anillo integral','es un anillo íntegro'),
 ('11.7.4','donde $A$ es integral','donde $A$ es íntegro'),
 ('11.7.4','es un anillo local integral','es un anillo local íntegro'),
 ('11.7.5','anillo local integral completo','anillo local íntegro completo')]:patch(n,old,new)

for q,t in original.items():
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(q.read_text())],(q.name,'prose pass changed math')
print('Source-reviewed register, grammar, and glossary edits applied; formula arrays unchanged')

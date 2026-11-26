"""Restore source wording and formula grouping in reviewed I passages.

Existing editorial notes are retained, including where they discuss a different
reading from the supplied French source layer.
"""
import re,csv
from corpus import RESULT,write_tsv
from audit_i_ch1 import texts,i_units
from tex_tools import balanced_end
LOG=RESULT/'records/CAMBIOS_i_prose_restore.tsv'
H=['file','place','before','after','kind','source']
rows=list(csv.DictReader(LOG.open(),delimiter='\t')) if LOG.exists() else []

def replace(num,old,new,layers=('CURRENT','DIPLOMATIC')):
 for layer in layers:
  p,t=texts(layer);whole=p.read_text();u=i_units(t)[num]
  if new in u.text:continue
  pat=re.escape(old);pat=re.sub(r'(?:\\\s)+',r'\\s+',pat)
  # Literal first, then whitespace-only rebinding for editions with reflowed lines.
  if old in u.text:a=u.text.index(old);b=a+len(old)
  else:
   pat=r'\s+'.join(re.escape(z) for z in old.split());mm=list(re.finditer(pat,u.text))
   if len(mm)!=1:raise ValueError((layer,num,'not unique',old[:100],len(mm)))
   a,b=mm[0].span()
  before=u.text[a:b];whole=whole[:u.start+a]+new+whole[u.start+b:];p.write_text(whole)
  rows.append(dict(zip(H,[str(p.relative_to(RESULT)),num,before,new,'own comparison',f'EGA_ES_FINISH_1_FRANCES/fr/{layer.lower()}/BASE/native/ega1/ega1-{num.split(".")[0]}-fr.tex: {num}; source prose/formula grouping'])))
  write_tsv(LOG,H,[[r[k] for k in H] for r in rows])

replace('1.1.6',r'''Obsérvese que el recíproco de este corolario es falso, como muestra el ejemplo de un dominio entero no noetheriano que posee exactamente un ideal primo distinto de $(0)$ (por ejemplo, un anillo de valoración no discreta de rango $1$).''',r'''Se observará que el recíproco de este corolario es inexacto, como muestra el ejemplo de un anillo íntegro no noetheriano que tiene un solo ideal primo $\neq\{0\}$, por ejemplo un anillo de valoración no discreta de rango 1.''')
replace('1.3.8',r'''Consideremos el homomorfismo canónico
\[
  v\longmapsto\Gamma(v):
  \Hom_{\widetilde{A}}(\widetilde{M},\widetilde{N})
  \longrightarrow
  \Hom_{\Gamma(\widetilde{A})}(\Gamma(\widetilde{M}),\Gamma(\widetilde{N}));
\]''',r'''Consideremos, en efecto, el homomorfismo canónico $v\to\Gamma(v)$ de $\operatorname{Hom}_{\widetilde{A}}(\widetilde{M},\widetilde{N})$ en $\operatorname{Hom}_{\Gamma(\widetilde{A})}
(\Gamma(\widetilde{M}),\Gamma(\widetilde{N}))$;''')
replace('1.3.8','si ponemos','si se pone')
replace('1.6.10',r'''$(\Spec(A),\widetilde{A})$ es un \emph{funtor} de''',r'''$(\operatorname{Spec} A,\widetilde A)$ es un \emph{funtor} en $A$ de''')
replace('1.7.4',r'''$A\longmapsto(\Spec(A),\widetilde{A})$ y $(X,\sh{O}_X)\longmapsto\Gamma(X,\sh{O}_X)$''',r'''$(\operatorname{Spec}(A),\widetilde A)$ en $A$ y $\Gamma(X,\mathscr{O}_X)$ en $(X,\mathscr{O}_X)$''')
replace('3.5.10',r'''puede identificarse con la imagen inversa del subconjunto $X(K)\subseteq Y(K)$ por la aplicación $Y'(K)\to Y(K)$ correspondiente a $g$.''',r'''se identifica con el subconjunto de $Y'(K)$ imagen recíproca por la aplicación $Y'(K)\to Y(K)$ (correspondiente a $g$) del subconjunto $X(K)$ de $Y(K)$.''')
replace('8.2.2',r'''como, para $x\in W$, $\mathfrak a\subset\mathfrak m_x$ equivale a $x\in V(\mathfrak{a})$, y por tanto a $x\in F=W\cap V(\mathfrak{a})$, se tiene efectivamente $\psi(F)=V(\mathfrak{a}C)$''',r'''como $\mathfrak a\subset\mathfrak m_x$ equivale a $x\in V(\mathfrak a)=W\cap F$ para $x\in U$, se tiene efectivamente $\psi(F)=V(\mathfrak a C)$''')
replace('8.2.2','Además, sabemos','Además, se sabe')
replace('8.2.2','sabemos entonces','se sabe entonces')
replace('10.2.2',r'''Podemos decir que los funtores $A\mapsto\Spf(A)$ y $\mathfrak{X}\mapsto\Gamma(\mathfrak{X},\sh{O}_\mathfrak{X})$''',r'''Se puede decir que los funtores $\operatorname{Spf}(A)$ en $A$ y $\Gamma(\mathfrak{X},\mathscr{O}_{\mathfrak{X}})$ en $\mathfrak{X}$''')
replace('10.2.2','pasando al límite inductivo, vemos','pasando al límite inductivo, se ve')
replace('10.2.2',r'''y por \sref[0]{0.3.2.5} tenemos''',r'''y por \sref[0]{0.3.2.5} se tiene''')
replace('10.7.2',r'''$\rho:B\to B\widehat{\otimes}_A C$ y $\sigma:C\to B\widehat{\otimes}_A C$''',r'''$\rho$ y $\sigma$ de $B$ y $C$ en $B\widehat{\otimes}_A C$''')
# Current proof explicitly differs from the diplomatic one. Retain inherited notes.
p,t=texts('CURRENT');u=i_units(t)['5.3.9'];a=u.text.index(r'\begin{proof}');b=u.text.index(r'\end{proof}')+len(r'\end{proof}')
old=u.text[a:b]
notes=[]
for m in re.finditer(r'\\footnote\{',old):notes.append(old[m.start():balanced_end(old,m.end()-1)])
if len(notes)==2:
 editorial=old[len(r'\begin{proof}'):old.index(notes[0])].strip()
 new=r'''\begin{proof}
Para tener una demostración correcta, basta utilizar \sref{I.4.2.4}[a]: para todo $x\in X$, escojamos una vecindad abierta afín $V\subset S$ de su imagen y una vecindad abierta afín $U$ de $x$ en $X$ cuya imagen esté contenida en $V$. Entonces $U\times_SU=U\times_VU$ es una vecindad abierta afín de $\Delta_X(x)$;'''+notes[1]+r'''
teniendo en cuenta \sref{I.5.3.16} (cuya demostración solo utiliza la definición \sref{I.5.3.1.1}), se reduce a demostrar \sref{I.5.3.9} cuando $S=\operatorname{Spec}(B)$ y $X=\operatorname{Spec}(A)$ son esquemas afines; es claro entonces, en virtud de \sref{I.5.3.1.1}, que $\Delta_X$ corresponde al homomorfismo canónico $A\otimes_BA\to A$ que transforma $x\otimes y$ en $xy$; siendo este homomorfismo sobreyectivo, $\Delta_X$ es en este caso una inmersión cerrada \sref{I.4.2.3}, lo que termina la demostración.\footnote{'''+editorial+'}'+notes[0]+r'''
\end{proof}'''
 replace('5.3.9',old,new,('CURRENT',))
replace('5.3.9','Decimos que','Se dice que',('CURRENT',))
print('Recorded changes',len(rows))

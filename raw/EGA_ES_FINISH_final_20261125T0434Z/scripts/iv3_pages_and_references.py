"""Restore the individually inspected source page boundaries and citations."""
import re
from iv3_manual import patch,DIR
from iv3_align import units
from iv3_work import apply_edits
from tex_tools import math_spans

def move(page,unit,anchor,after=False,section=None,back=False):
 k=section or unit.split('.')[0]
 q=DIR/('backmatter-es.tex' if back else f'sections/ega4-{k}.tex')
 source=f'ega4-{k}-fr.tex' if not back and not unit.startswith('15.7.') else 'ega4-15-terminal-fr.tex'
 marker=rf'\oldpage[IV-3]{{{page}}}'
 original=q.read_text();t=original;before_math=[s.text for s in math_spans(t)]
 ee=[(m.start(),m.end(),'',unit) for m in re.finditer(re.escape(marker),t)]
 for a,b,v,n in reversed(ee):t=t[:a]+t[b:]
 u=units(t).get(unit) if not back else None
 lo,hi=(u.start,u.end) if u else (0,len(t))
 pp=list(re.finditer(re.escape(anchor),t[lo:hi]));assert len(pp)==1,(page,unit,anchor,len(pp))
 at=lo+(pp[0].end() if after else pp[0].start())
 if original==t[:at]+'\n'+marker+'\n'+t[at:]:return
 if ee:apply_edits(q,ee,source)
 apply_edits(q,[(at,at,'\n'+marker+'\n',unit)],source)
 assert before_math==[s.text for s in math_spans(q.read_text())],(page,'page crossed formula')

move(97,'10.1.2',' tal que $X_0\\cap U_\\alpha=V_\\alpha$')
move(100,'10.2.7','las cinco aplicaciones restantes',after=True)
move(102,'10.4.2',r'\begin{proposition}[10.4.2]')
move(104,'10.4.11',r'\begin{proof}')
move(105,'10.5.1','finito de sus puntos cerrados')
move(115,'10.10.1','nos limitaremos al marco fijado por Serre')
move(119,'11.1.4',' para los cuales la sucesión')
move(127,'11.2.9.2',r'\begin{lemma}[11.2.9.2]')
move(128,'11.2.9.3','es \\emph{sobreyectivo}. Esto significa')
move(129,'11.2.9.4','un álgebra de polinomios (y, por tanto, noetheriana)')
move(132,'11.2.9.9',r'para $\lambda\leq\mu$')
move(134,'11.3.4',r'utilizando \sref{IV.11.2.9}')
move(145,'11.4.1.1','y, como por hipótesis')
move(146,'11.4.4',r'\begin{proof}')
move(148,'11.4.9','La afirmación relativa al caso en que')
move(162,'11.9.4','en general, que la familia')
move(164,'11.9.10',r'\item Supongamos que $g$')
move(167,'11.9.15',r'\begin{proposition}[11.9.15]')
move(179,'12.1.6','pero, en virtud de~(ii)')
move(181,'12.2.1.3',r'\begin{env}[12.2.1.3]')
move(182,'12.2.2',r'\begin{proof}')
move(207,'14.3.8','cuyos espacios subyacentes son las componentes irreducibles')
move(213,'14.4.6',r'\begin{corollary}[14.4.6]')
move(219,'14.5.8','algebraicamente cerrado. Además')
move(220,'14.5.10','\n'+r'I) \emph{Reducción al caso')
move(223,'14.5.11.1',r'\begin{proof}')
move(225,'15.1.1.6',r'$P=\operatorname{Proj}(B)$')
move(230,'15.4.1','En efecto, por')
move(231,'15.4.3','es equidimensional en el punto')
move(232,'15.5.2.2',r'se tiene $g_1(z_1)=y$')
move(238,'15.6.4',r'se cortan para $2\leqslant i\leqslant n$')
move(72,'9.6.1','suponer que el propio')
move(73,'9.6.1',r"$f_\eta(X_\eta)$ no es una parte localmente cerrada")
move(87,'9.8.7',r'\begin{corollary}[9.8.7]')

q=DIR/'backmatter-es.tex';t=q.read_text();anchor=r'\oldpage[IV-3]{253}';a=t.index(anchor)
apply_edits(q,[(a,a,r'\oldpage[IV-3]{252}'+'\n'+r'\thispagestyle{empty}'+'\n'+r'\null'+'\n\n'+r'\clearpage'+'\n','printed blank page 252')],'ega4-15-terminal-fr.tex')

for n,old,new in [
 ('10.4.11',r'\sref{I.1.8.5}',r'\sref{IV.1.8.5}'),
 ('10.6.1',r'\sref{I.1.3.4}',r'\sref{IV.1.3.4}'),
 ('9.3.2',r'\sref[I]{I.1.5.4}',r'\sref{IV.1.5.4}'),
 ('9.4.9',r'\sref[I]{I.1.8.2}',r'\sref{IV.1.8.2}'),
 ('9.4.9',r'\sref[I]{I.1.1.5}',r'\sref{IV.1.1.5}'),
 ('9.5.6',r'\sref[I]{I.5.4}',r'\sref{IV.1.5.4}')]:patch(n,old,new)

patch('11.2.9.6','(respectivamente, ',r'(resp.\ ',all=True)
patch('11.2.6','\textup{v}',r'\textup{v}')
patch('11.2.8','\textup{i}',r'\textup{i}')
patch('11.2.9.4',r'$\bigoplus_{1\leq j\leq r}B_{i+m_j}\longrightarrow M_i$'+'\nLas hipótesis',
 r'$\bigoplus_{1\leq j\leq r}B_{i+m_j}\longrightarrow M_i$.'+'\nLas hipótesis')
patch('11.2.9.2','bijetivo','biyectivo')
patch('11.4.4',r"Para todo homomorfismo $u:A\to A'$ tal que $M\otimes_A A'$ es un",
 r"Para que un homomorfismo $u:A\to A'$ sea tal que $M\otimes_A A'$ sea un")
patch('14.3.11','por consiguiente, para todo subconjunto','para todo subconjunto')
patch('9.4.7.1',r'\emph{Remarque}~1',r'\emph{Observación}~1')

# End the source proposition before its explanation, retaining all content.
q=DIR/'sections/ega4-15.tex';t=q.read_text();u=units(t)['15.4.1']
a=u.text.index(r'\end{proposition}');b=u.text.index(r'\oldpage[IV-3]{230}')
apply_edits(q,[(u.start+a,u.start+a+len(r'\end{proposition}'),'','15.4.1'),
 (u.start+b,u.start+b,r'\end{proposition}'+'\n\n','15.4.1')],'ega4-15-fr.tex')
print('Source page locations, six incorrect reference targets, and final source clauses restored')

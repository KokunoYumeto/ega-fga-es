"""Read and restored I clauses; French hypotheses and grouping are retained."""
from i_edit_helper import replace
from audit_i_ch1 import texts,i_units
from corpus import FR
from tex_tools import math_spans,balanced_end
import re
replace('1.4.1',r'también al haz $\widetilde{N}$ asociado',r'también al haz asociado')
replace('1.4.3',r'basta demostrar que también es',r'basta demostrar que $\mathscr{G}$ también es')
replace('1.4.3','podemos, restringiéndonos','se puede, restringiéndose')
for num in ['10.1.1','10.6.3']:
 replace(num,r'vecindades de $0$',r'vecindades de 0')
replace('10.3.7',r'vecindades de} $0$',r'vecindades de} 0')
replace('10.7.4',r'''$v^*(\mathscr{L}_\lambda)\mathscr{O}_{\mathfrak{Z}}
\subset\mathscr{M}_\lambda$ para todo $\lambda$.''',r'''$v^*(\mathscr{L}_\lambda)\mathscr{O}_{\mathfrak{Z}}
\subset\mathscr{M}_\lambda$.''')
replace('10.7.4','Si ponemos','Si se pone')
for num in ['10.8.5','10.8.6']:
 replace(num,r'anillo noetheriano $A$',r'anillo noetheriano')
replace('10.15.4',r'$(f_n:X_n\to Y_n)$ de $S_n$-morfismos',r'de $S_n$-morfismos $f_n:X_n\to Y_n$')
# Two grammatical subjects combined into the same printed formula.
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['2.1.4'];old=u.text;new=old.replace('$x$ e $y$','$x,y$')
 if old!=new:replace('2.1.4',old,new,(layer,))
replace('2.1.7',r'''Si $(X,\mathscr{O}_X)$ es un preesquema, el espacio anillado $(U,\mathscr{O}_X|U)$ es un preesquema para toda parte abierta $U$.''',r'''Si $(X,\mathscr{O}_X)$ es un preesquema, para toda parte abierta $U$ de $X$, el espacio anillado $(U,\mathscr{O}_X|U)$ es un preesquema.''')
replace('2.2.6',r'''$\psi(U)$ es abierta (resp. $\psi(F)$ es cerrada) en $Y$.''',r'''$\psi(U)$ es abierta en $Y$ (resp. $\psi(F)$ cerrada en $Y$).''')
replace('2.2.6','Observemos que','Se observará que')
replace('2.2.9',r'''supongamos que $X$ e $Y$ tienen el mismo número finito $n$ de componentes irreducibles $X_i$ e $Y_i$, respectivamente ($(1\leq i\leq n)$);''',r'''se supone que $X$ e $Y$ tienen un mismo número \emph{finito} de componentes irreducibles $X_i$ (resp. $Y_i$) $(1\leq i\leq n)$;''')
for num in ['2.4.4','2.4.6']:
 replace(num,r', cuando $y$ recorre $Y$',r' $(y\in Y)$')
replace('2.4.5',r'''cuyo único punto se envía al punto cerrado $\mathfrak{m}$ corresponden''',r'''corresponden''')
replace('3.4.6',r'proyecciones sobre los $X_i$ estén',r'proyecciones estén')
replace('3.4.9',r'''estando $x$ e $y$ ambos situados sobre el mismo punto''',r'''sobre el mismo punto''')
replace('3.5.1',r'''mediante una extensión de base $S'\to S$''',r'''por extensión del preesquema de base''')
replace('3.5.1',r'''entonces el producto $f\times_S g$ también la posee, y por tanto (ii) implica (i)''',r'''entonces (ii) implica (i)''')
replace('3.5.1','vemos que','se ve que')
replace('3.5.7','Hemos visto','Se ha visto')
replace('3.6.3',r'$f^{-1}_V(y)$',r'$f_V^{-1}(y)$')
replace('3.6.3','y denotamos por','y se denota por')
for num in ['3.7.2','3.7.3']:
 replace(num,r'dimensión~$1$',r'dimensión 1')
replace('3.7.2',r'''todas las hipótesis hechas sobre $X_0$ se reducen''',r'''las hipótesis hechas se reducen''')
replace('4.1.3',r'\item[1.º]',r'\item[$1^\circ$]')
replace('4.1.3',r'\item[2.º]',r'\item[$2^\circ$]')
replace('4.1.5',r'''el mayor abierto $U$ en el que $Y$ es cerrado (y, por tanto, está contenido)''',r'''el mayor abierto $U$ que contiene a $Y$ y en el cual $Y$ es cerrado''')
replace('4.1.5','podemos, pues, reducirnos','se puede, pues, reducir')
replace('4.1.5','Definimos entonces','Se define entonces')
replace('4.1.6',r'''donde $A$ es un anillo, y $\mathfrak{J}$ y $\mathfrak{J}'$ son ideales de $A$''',r'''cuando $\mathfrak{J}$, $\mathfrak{J}'$ son dos ideales de un anillo $A$''')
# Split displays are restored from the source; their intervening connectors were read above.
for num in ['10.9.1','2.2.7','3.5.7']:
 for layer in ['CURRENT','DIPLOMATIC']:
  p,t=texts(layer);u=i_units(t)[num];fu=i_units((FR/layer.lower()/'BASE/native/ega1'/('ega1-'+num.split('.')[0]+'-fr.tex')).read_text())[num]
  if num=='10.9.1':
   old=r'''$X_n'=(X',\sh{O}_X/\sh{J}^{n+1})$ y $Y_n'=(Y',\sh{O}_Y/\sh{K}^{n+1})$'''
   new=next(s.text for s in math_spans(fu.text) if s.text.startswith('\\[') and "X'_n=" in s.text)
  elif num=='2.2.7':
   spans=[s for s in math_spans(u.text) if s.text.startswith('\\[')][:2]
   old=u.text[spans[0].start:spans[1].end];new=next(s.text for s in math_spans(fu.text) if s.text.startswith('\\['))
  else:
   spans=[s for s in math_spans(u.text) if s.text.startswith('\\[') and '(K)=' in s.text]
   if len(spans)==1:continue
   old=u.text[spans[0].start:spans[1].end];new=next(s.text for s in math_spans(fu.text) if s.text.startswith('\\[') and '(K)=' in s.text)
  replace(num,old,new,(layer,))
# Keep the exact existing Spanish note, merely move its marker to the source position.
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['3.2.2'];fu=i_units((FR/layer.lower()/'BASE/native/ega1/ega1-3-fr.tex').read_text())['3.2.2']
 oldformula=r'$\Hom_A(B\otimes_A C,L)\xrightarrow{\sim}\Hom_A(B,L)\times\Hom_A(C,L)$'
 if oldformula in u.text:
  a=u.text.index(oldformula);m=re.search(r'\\footnote\{',u.text[a+len(oldformula):]);na=a+len(oldformula)+m.start();nb=balanced_end(u.text,na+len('\\footnote'))
  note=u.text[na:nb].replace('\\footnote{','\\footnotetext{',1)
  new=next(s.text for s in math_spans(fu.text) if '\\footnotemark' in s.text)+'\n'+note
  replace('3.2.2',u.text[a:nb],new,(layer,))
# Plain-text condition primes follow source typography, without changing text.
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['1.4.1.1'];old=u.text;new=old.replace("d$'$","d'")
 if old!=new:replace('1.4.1.1',old,new,(layer,))
print('Clause restoration pass complete')

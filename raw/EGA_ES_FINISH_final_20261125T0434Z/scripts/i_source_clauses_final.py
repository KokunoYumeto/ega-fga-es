"""Remaining short source clauses in I, compared separately by layer."""
from i_edit_helper import replace
from audit_i_ch1 import texts,i_units
from tex_tools import balanced_end
import re
replace('10.15.2',r'''los espacios subyacentes a $\mathfrak{X}$ y $\mathfrak{X}\times_{\mathfrak{S}}\mathfrak{X}$ son respectivamente idénticos a los de $X_0$ y $X_0\times_{S_0}X_0$, y, bajo estas identificaciones, la imagen de $\mathfrak{X}$ por $\Delta_{\mathfrak{X}|\mathfrak{S}}$ es idéntica a la imagen de $X_0$ por $\Delta_{X_0|S_0}$''',r'''la imagen por $\Delta_{\mathfrak{X}|\mathfrak{S}}$ del espacio subyacente $\mathfrak{X}$ (resp. el espacio subyacente $\mathfrak{X}\times_{\mathfrak{S}}\mathfrak{X}$) es idéntica a la imagen por $\Delta_{X_0|S_0}$ del espacio subyacente $X_0$ (resp. al espacio subyacente $X_0\times_{S_0}X_0$)''')
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['4.2.3'];m=re.search(r'\\footnote\{',u.text)
 if m:
  e=balanced_end(u.text,m.end()-1);note=u.text[m.start():e]
  old=r'$\Gamma(\theta)$'+note+r'$:\Gamma(\sh{O}_X)\to\Gamma(\sh{O}_Y)$'
  if old in u.text:replace('4.2.3',old,r'$\Gamma(\theta):\Gamma(\mathscr{O}_X)\to\Gamma(\mathscr{O}_Y)$'+note,(layer,))
replace('4.2.4',r'''y, en el caso \emph{b)}, que $\psi$ es un homeomorfismo''',r'''y, en el caso \emph{b)}, un homeomorfismo''')
replace('4.3.1',r'''$\operatorname{Im}(\mathfrak{b}\otimes_A C\to B\otimes_A C)+\operatorname{Im}(B\otimes_A\mathfrak{c}\to B\otimes_A C)$,
o, equivalentemente, la suma''',r'''la suma''',('CURRENT',))
replace('4.3.1','podemos restringirnos','se puede restringir')
replace('4.3.1','podemos reducirnos','se reduce')
# The author's imperative remains first plural; its embedded impersonal remains se.
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['4.3.1'];old=u.text;new=old.replace('podemos suponer','se puede suponer').replace('sabemos que','se sabe que')
 if old!=new:replace('4.3.1',old,new,(layer,))
replace('4.4.1',r'''tomando $h=1_X$, vemos que \emph{el morfismo''',r'''por tanto, \emph{el morfismo''')
replace('4.4.3',r'relación de orden $\leq$ entre',r'relación de orden entre')
replace('5.1.1',r'$z/s=(tz)/(ts)\in\nilrad_x$',r'$z/s=(tz)/(ts)$ pertenece a $\mathfrak{N}_x$')
replace('5.1.2',r'''Sea $Y$ el subpreesquema cerrado de $X$ definido por $\mathscr{N}_X$.
Como su haz estructural es $\mathscr{O}_X/\mathscr{N}_X$,''',r'''Como el haz estructural del subpreesquema cerrado $Y$ definido por $\mathscr{N}_X$ es $\mathscr{O}_X/\mathscr{N}_X$,''')
replace('5.1.4','anillo de fracciones no nulo',r'anillo de fracciones $\ne\{0\}$')
replace('5.3.2',r'''$p_1:X\times X\to X$ y $q_1:Y\times Y\to Y$ son las proyecciones sobre el primer factor''',r'''$p_1$, $q_1$ son las primeras proyecciones $X\times X\to X$, $Y\times Y\to Y$''')
replace('5.3.9',r'\sref{I.4.2.4}[a]',r'\sref{I.4.2.4}[$a$]',('CURRENT',))
replace('5.4.2',r'''mediante la extensión de base $f\times_T g:X\times_T Y\to S\times_T S$''',r'''por la extensión $f\times_T g:X\times_T Y\to S\times_T S$ del preesquema de base $S\times_T S$''')
replace('5.4.7',r'''$S$-secciones $f$ y $g$ son''',r'''$S$-secciones $f$, $g$ de $X$ son''')
replace('5.5.11',r'$m,n\geq0$',r'$m\geq0$, $n\geq0$')
replace('6.1.2','El propio espacio subyacente es entonces también noetheriano.',r'El espacio subyacente de $X$ es entonces noetheriano.')
replace('6.1.10',r'''siendo $C$ distinta de $F$, no puede ser irreducible, pues, al no ser conexo, $F$ es la unión''',r'''y distinta de $C$, no puede ser irreducible, pues, al no ser conexo, este conjunto es la unión''')
replace('6.2.2',r'''al esquema afín $\Spec(A)$, donde $A$ es el producto directo''',r'''al esquema afín espectro primo del anillo $A$ producto directo''')
replace('6.4.2',r'''Podemos suponer que $X$ es afín, siendo su anillo $A$ un $K$-álgebra''',r'''Se puede suponer que $X$ es afín, siendo el anillo $A$ de $X$ una $K$-álgebra''')
replace('6.5.1',r'por este homomorfismo es $0$',r'por este homomorfismo es 0')
replace('6.6.4',r'Si el compuesto $g\circ f$ de dos',r'Si el compuesto de dos')
replace('6.6.6',r'''$T'$ la imagen inversa de $T$ en $S'$''',r'''$T'$ su imagen recíproca en $S'$''')
replace('6.6.6',r'''que es de tipo finito sobre $T$ y cuya imagen está contenida en $T$''',r'''cuya imagen está contenida en $T$ y que es de tipo finito sobre $T$''')
replace('6.6.7',r'''En efecto, como $S$ es localmente noetheriano y $X$ es localmente de tipo finito sobre $S$, $X$ es localmente noetheriano;''',r'''En efecto, siendo $X$ localmente de tipo finito sobre $S$, es localmente noetheriano;''')
replace('7.1.3',r'abierto denso de $X$ contenido',r'abierto denso contenido')
replace('7.1.4',r'todo abierto no vacío de $X$ es denso',r'todo abierto no vacío es denso')
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);u=i_units(t)['7.1.5'];old=u.text;new=old.replace('un abierto denso de $X$','un abierto denso')
 if old!=new:replace('7.1.5',old,new,(layer,))
replace('7.1.5','podemos reducirnos','se puede limitar')
replace('7.1.9.1','(por la inclusión inversa)',r'(para $\supset$)')
replace('7.1.11',r'todo abierto no vacío de $X$ es denso en $X$',r'todo abierto no vacío de $X$ es denso')
replace('7.2.1',r'un abierto denso $U$ de $X$ que',r'un abierto denso $U$ que')
replace('7.2.6',r'funciones racionales sobre $X$ definidas',r'funciones racionales $f$ sobre $X$ definidas')
replace('7.3.8',r'$X$ e $Y$ dos preesquemas',r'$X,Y$ dos preesquemas',('CURRENT',))
replace('7.3.8',r'$x$ e $y$ son los puntos genéricos',r'$x,y$ son los puntos genéricos',('CURRENT',))
replace('9.4.1',r'''denotamos por $\rho$ el homomorfismo canónico
$\sh{F}\to\psi_*(\psi^*(\sh{F}))$ \sref[0]{0.3.5.3}, y por''',r'''si se considera el homomorfismo canónico $\rho:\mathscr{F}\to\psi_*(\psi^*(\mathscr{F}))$ \sref[0]{0.3.5.3}, denotaremos por''')
replace('9.5.2',r'''primero debemos
tener $\psi(X)\subset X''$''',r'''se debe tener en primer lugar $X''\supset\psi(X)$''')
replace('9.6.4',r'''es necesario y suficiente que sea un $\mathscr{O}_X$-módulo cuasicoherente''',r'''es necesario y suficiente que $\mathscr{G}$ sea un $\mathscr{O}_X$-módulo cuasicoherente''')
print('Final short-clause pass complete')

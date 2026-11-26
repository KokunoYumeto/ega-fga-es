"""Reviewed IV3 §10 source omissions, formula readings and clause order."""
import re
from iv3_manual import patch,source_unit
from tex_tools import math_spans

patch('10.1.2',r'Sustituyendo respectivamente $X$ y $X_0$ por $U$ y $U\cap X_0$, podemos por tanto limitarnos',r'Reemplazando $X$ y $X_0$ por un abierto adecuado $U$ de $X$ y por $U\cap X_0$ respectivamente, se puede, por tanto, limitarse')
patch('10.1.2',r'$Z\cap\overline{X_0}\subset\overline{Z\cap X_0}$',r'$\overline{Z\cap X_0}\subset\overline{Z}$')
patch('10.1.2',r'en efecto, sustituyendo respectivamente $X$ y $X_0$ por $U$ y $U\cap X_0$, nos reducimos al caso',r'además, reemplazando $X$ y $X_0$ por un abierto $U$ de $X$ y por $U\cap X_0$ respectivamente, se reduce efectivamente al caso')
patch('10.2.1',r'Mostremos ahora que \emph{c)} implica que la topología de $X_0$ es la imagen inversa por $f$ de la de $X$',r'Mostremos ahora que \emph{c)} implica que la topología de $X_0$ es la imagen inversa de la de $X$ por $f$')
patch('10.3.2',r'entonces el subespacio $Z$ es un espacio de Jacobson',r'entonces el subespacio $Z$ de $X$ es un espacio de Jacobson')
patch('10.4.4',r'El punto genérico de $\operatorname{Spec}(B)$ es aislado.',r'El punto genérico de $\operatorname{Spec}(B)$ es aislado en $\operatorname{Spec}(B)$.')
patch('10.4.5.1',r'el conjunto $X_0$ de los puntos cerrados de $X$ coincide con el conjunto de los $x\in X$',r'el conjunto de los puntos cerrados de $X$ coincide con el conjunto $X_0$ de los $x\in X$')
patch('10.4.8',r'y los puntos cerrados son exactamente',r'y los puntos cerrados de $X$ son exactamente')
patch('10.4.11.1',r'Para que un punto $y\in Y$ sea cerrado,',r'Para que un punto $y\in Y$ sea cerrado en $Y$,')
patch('10.5.1',r'sin suponer que $B$ sea noetheriano',r'sin suponer que $A$ sea noetheriano',all=True)
patch('10.5.1',r'es la unión del conjunto de sus puntos cerrados',r'es la unión del conjunto finito de sus puntos cerrados')
patch('10.5.2',r'Para que un anillo noetheriano $A$ sea un anillo de Jacobson',r'Sea $A$ un anillo noetheriano. Para que $A$ sea un anillo de Jacobson')
patch('10.5.5',r'pues este es el espacio subyacente a un subpreesquema (noetheriano) de $X$',r'siendo $\overline{\{x\}}$ el espacio subyacente de un subpreesquema (noetheriano) de $X$')
patch('10.5.5',r'una unión finita de subpreesquemas $U_i$ abiertos (en $Y$) y afines',r'una unión finita de subpreesquemas abiertos (en $Y$) afines $U_i$')
patch('10.5.7',r'supongamos que existe en $X\setmin Y$ un subpreesquema $Z$',r'supongamos que existe un subpreesquema $Z$ de $X\setmin Y$')
patch('10.6.1',r'$n$ un entero no negativo',r'$n$ un entero $\geq0$')
patch('10.7.2',r'el complementario del \emph{punto cerrado} $a$ en $X=\operatorname{Spec}(A)$',r'el \emph{complementario en $X=\operatorname{Spec}(A)$ del punto cerrado} $a$')
patch('10.7.3',r"existen ideales maximales $\mathfrak m'$ y $\mathfrak n'$ de $A[T_1,\ldots,T_{n+1}]$ situados",r"existen en $A[T_1,\ldots,T_{n+1}]$ dos ideales maximales $\mathfrak m'$, $\mathfrak n'$ situados")
patch('10.7.3',r'además, para todo $s\in S$, el anillo local $\mathcal O_{S,s}=\mathcal O_{X,s}$ es universalmente catenario',r'además, los anillos locales $\mathcal O_{S,s}=\mathcal O_{X,s}$ son universalmente catenarios para todo $s\in S$')
patch('10.7.3',r"podemos por tanto suponer que el punto $a$ de $X'$ correspondiente a $\mathfrak p'$ tiene por adherencia $\{a,a'\}$ en $X'$",r"se puede, por tanto, suponer que el punto $a$ de $X'$ correspondiente a $\mathfrak p'$ es tal que su adherencia en $X'$ sea $\{a,a'\}$")
patch('10.8.2',r'cuando $x$ no es un punto cerrado de $X$',r'cuando $x$ no es cerrado')
patch('10.8.5',r'es semicontinua inferiormente; dicho de otro modo',r'es semicontinua inferiormente en $X$; dicho de otro modo')
patch('10.8.6',r'existe una vecindad abierta $U$ de $x$ tal que, para todo punto',r'existe una vecindad abierta $U$ de $x$ en $X$ tal que, para todo punto')
patch('10.8.6',r'podemos limitarnos al caso',r'se puede limitar al caso')
patch('10.8.6',r'$\operatorname{prof}^*_y(\sh{F})$',r'$y\leadsto\operatorname{prof}^{*}_{y}(\mathcal F)$')
patch('10.8.6',r'es \emph{cerrado} (puesto que la noción',r'es \emph{cerrado} en $U$ (puesto que la noción')
patch('10.9.1',r'''$\sh{L}|_U\simeq(\sh{O}_X|_U)^n$, entonces
\[
  j_X^*(\sh{L})|_{U\cap S(X)}
  \simeq \bigl(\sh{O}_{S(X)}|_{U\cap S(X)}\bigr)^n.
\]''',r'''$\mathcal L|U$ sea isomorfo a $(\mathcal O_X|U)^n$, $j_X^*(\mathcal L)$ es tal que
$j_X^*(\mathcal L)|(U\cap S(X))$ sea isomorfo a
$(\mathcal O_{S(X)}|(U\cap S(X)))^n$.''')
f=source_unit('10.9.2');diagram=next(s.text for s in math_spans(f) if 'tikzcd' in s.text)
patch('10.9.2',r'''\[
  \xymatrix{
    S(X)\ar[r]^{S(f)}\ar[d]_{j_X} & S(Y)\ar[d]^{j_Y}\\
    X\ar[r]^{f} & Y
  }
\]''',diagram)
patch('10.9.2',r'$g:Y\to Z$ un morfismo localmente de tipo finito, $S(g\circ f)=S(g)\circ S(f)$',r'$g:Y\to Z$ un morfismo localmente de tipo finito, está claro que $S(g\circ f)=S(g)\circ S(f)$')
patch('10.9.3',r'tales que $h\notin\mathfrak m$; $2^\circ$',r'tales que $h\notin\mathfrak m$, donde $h$ recorre $A$; $2^\circ$')
patch('10.9.6',r'se tiene $f^{-1}(V)\cap S(X)=g^{-1}(V)\cap S(X)$ para todo abierto $V$ de $Y$',r'esto implica primero que para todo abierto $V$ de $Y$, se tiene $f^{-1}(V)\cap S(X)=g^{-1}(V)\cap S(X)$')
patch('10.9.6',r'el homomorfismo de anillos correspondiente a la restricción $h_\lambda:U'+"'" +r'_\lambda\to V'+"'" +r'_\mu$ hace del segundo anillo un álgebra de tipo finito sobre el primero',r'''al morfismo $h_\lambda:U'_\lambda\to V'_\mu$, restricción de $h$, le corresponde un homomorfismo de anillos
$\Gamma(V'_\mu,\mathcal O_{S(Y)})\to
\Gamma(U'_\lambda,\mathcal O_{S(X)})$ que hace del segundo anillo un álgebra de tipo finito sobre el primero''')
patch('10.9.6',r'Podemos suponer',r'Se puede suponer')
patch('10.9.6',r'nos reducimos al caso',r'se reduce al caso')
patch('10.9.6',r'Quedamos así reducidos al caso',r'Se reduce así al caso')
patch('10.9.6',r'esta familia define un preesquema $X$; está claro entonces',r'esta familia define, por tanto, un preesquema $X$, tal que los $U_\alpha$ se identifiquen con abiertos afines de $X$; está claro entonces')
patch('10.10.3',r'puesto que $x\setmin\lambda.1$ es invertible.',r'puesto que $x\setmin\lambda.1$ es invertible en $A$.')
patch('10.10.3',r'De ello concluimos inmediatamente que',r'De ello se concluye inmediatamente que')
patch('10.10.3',r'el homomorfismo correspondiente hace de $B$',r'$\varphi$ hace de $B$')
print('Reviewed §10 patches complete')


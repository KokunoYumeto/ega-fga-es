"""Source-bound formulas, clause order and explicit hypotheses in IV3 §12."""
from iv3_manual import patch
patch('12.1.1.1',r"$x'\neq x$",r"$x'\ne x$")
patch('12.1.5',r'existe una vecindad $V$ de $x$ en $X$',r'existe una vecindad de $x$ en $X$')
patch('12.1.5',r'todos los puntos de $\Spec(\sh{O}_y)$',r"todos los puntos de $Y'=\operatorname{Spec}(\mathcal O_y)$")
patch('12.1.5',r"Sustituyendo $Y$ por $Y'=\operatorname{Spec}(\mathcal O_y)$",r"Reemplazando $Y$ por $Y'$")
patch('12.2.1',r'un $f$-plano $\mathcal O_X$-módulo de presentación finita',r'un $\mathcal O_X$-Módulo $f$-plano y de presentación finita')
patch('12.2.3',r'espacio proyectivo $P=\mathbf P^3_k=\operatorname{Proj}(C)$ de dimensión~$3$',r'espacio proyectivo de 3 dimensiones $P=\mathbf P^3_k=\operatorname{Proj}(C)$')
patch('12.2.3',r'''». En términos geométricos, esto significa que $X_0=\operatorname{Proj}(C/\mathfrak{a})$, donde el ideal graduado $\mathfrak{a}=\mathfrak{b}\mathfrak{c}$''',r'''», lo que describe en términos geométricos
el hecho de que $X_0$ es igual a $\operatorname{Proj}(C/\mathfrak a)$, donde el ideal
graduado $\mathfrak a$ es igual a $\mathfrak b\mathfrak c$''')
patch('12.3.2',r'$B\simeq B_0\otimes_{A_0}A$ y $M\simeq M_0\otimes_{A_0}A$',r'$B$ sea isomorfo a $B_0\otimes_{A_0}A$ y $M$ a $M_0\otimes_{A_0}A$')
patch('12.3.2',r'$(L_0)_i$',r'$L_{0i}$')
patch('12.3.2',r'''y la definición de dimensión proyectiva da inmediatamente
  \[
    \operatorname{dim.proj}_{B\otimes_A\mathbf{k}(y)}(M\otimes_A\boldsymbol k(y))
    \leqslant \operatorname{dim.proj}_B(M)
  \]
  para todo $y\in\operatorname{Spec}(A)$''',r'''y la definición de la dimensión proyectiva prueba inmediatamente que, para todo
$y\in\operatorname{Spec}(A)$, se tiene
$\operatorname{dim.proj}_{B\otimes_A\mathbf{k}(y)}(M\otimes_A\boldsymbol{k}(y))\leq\operatorname{dim.proj}_B(M)$''')
patch('12.3.2',r'''el $(B\otimes_A\boldsymbol k(y))$-módulo $R\otimes_A\boldsymbol{k}(y)$ es proyectivo''',r'''$R\otimes_A\boldsymbol{k}(y)$ es un $(B\otimes_A\boldsymbol{k}(y))$-módulo proyectivo''')
patch('12.3.3',r'$\sh{H}_n(\sh{L}_\bullet)|_U=0$',r'$\mathcal H_n(\mathcal L_\bullet)|U=0$')
patch('12.3.3',r'''Pongamos $S_\lambda=\Spec(A_\lambda)$,
$X_\lambda=X'\times_{S'}S_\lambda$, y''',r'''pongamos $X_\lambda=X'\times_{S'}S_\lambda$, donde
$S_\lambda=\operatorname{Spec}(A_\lambda)$,''')
patch('12.3.3',r'''Como los límites inductivos filtrantes son exactos en la categoría de grupos conmutativos,
\[
  \operatorname{Ker}(v)=\varinjlim_\lambda(\operatorname{Ker}(v_\lambda)),\qquad
  \operatorname{Im}(u)=\varinjlim_\lambda(\operatorname{Im}(u_\lambda)),\qquad
  \sh{H}_1(\sh{L}_\bullet)=\varinjlim_\lambda\sh{H}_1(\sh{L}_\bullet^{(\lambda)}).
\]''',r'''Ahora bien, como el funtor $\varinjlim$ es exacto en la categoría de los grupos conmutativos, se tiene
$\operatorname{Ker}(v)=\varinjlim(\operatorname{Ker}(v_\lambda))$,
$\operatorname{Im}(u)=\varinjlim(\operatorname{Im}(u_\lambda))$, y
$\mathcal H_1(\mathcal L_\bullet)
=\varinjlim\mathcal H_1(\mathcal L_\bullet^{(\lambda)})$.''')
patch('12.3.3',r'''toda \emph{generización} $x'$ en $X$ de un punto $x\in U$ pertenece también a $U$''',r'''para toda \emph{generización} $x'$ de $x\in U$ en $X$, se tiene también $x'\in U$''')
patch('12.3.3.1',r'''Sea $t$ un elemento del ideal maximal de $B$ que es $P$-regular.
Si la sucesión''',r'''Sea $t$ un elemento del ideal maximal de $B$ tal que $t$ sea $P$-regular y que la sucesión''')
patch('12.3.3.1',r'es exacta, entonces la sucesión',r'sea exacta. Entonces la sucesión')
patch('12.3.3.3',r'Sea $t$ un elemento de $B$ que es $P$-regular',r'Sea $t$ un elemento de $B$ tal que $t$ sea $P$-regular')
patch('12.3.3.3',r'Entonces se tiene, salvo isomorfismo canónico,',r'Entonces se tiene')
patch('12.3.3.3',r'para esta topología es $0$',r'para esta topología es 0')
patch('12.3.4',r'$\mathscr{E}\!xt^n_{\sh{O}_X}(\sh{F},\sh{G})|_U=0$',r'$\mathscr{E}\!xt^n_{\mathcal O_X}(\mathcal F,\mathcal G)|U=0$')
patch('12.3.4',r'$\mathscr{T}\!or_n^{\sh{O}_X}(\sh{F},\sh{G})|_U=0$',r'$\mathscr{T}\!or_n^{\mathcal O_X}(\mathcal F,\mathcal G)|U=0$')
patch('12.3.4',r"$, entonces $\sh{L}'_\bullet$ sigue siendo",r"$ sigue siendo")
print('Reviewed §12 source clauses complete')


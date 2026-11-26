"""Source-bound clause order, omitted variables and notation in IV3 §11.3."""
from iv3_manual import patch
patch('11.3.1',r'$f$-plano es abierto',r'$f$-plano en el punto $x$ es abierto')
patch('11.3.1',r'$f|_\mathrm{U}$',r'$f|U$')
patch('11.3.1',r'podemos suponer que ambos son afines',r'se puede suponer que $X$ y $Y$ son afines')
patch('11.3.1',r'un punto en el que $\mathcal F$ es $f$-plano',r'un punto tal que $\mathcal F$ sea $f$-plano en el punto $x$')
patch('11.3.1',r'''\[
  \mathrm{X}=\mathrm{X}_0\times_{\mathrm{Y}_0}\mathrm{Y},
  \qquad
  f=f_0\times 1,
  \qquad
  \sh{F}
  =\sh{F}_0\otimes_{\sh{O}_{\mathrm{Y}_0}}\sh{O}_\mathrm{Y},
\]''',r'''$X=X_0\times_{Y_0}Y$, $f=f_0\times1$,
$\mathcal F=\mathcal F_0\otimes_{\mathcal O_{Y_0}}\mathcal O_Y$,''')
patch('11.3.1',r'podemos asumir',r'se puede suponer')
patch('11.3.1',r'podemos suponer',r'se puede suponer')
patch('11.3.2',r'y por consiguiente $\mathrm{V}$ es ind-construible',r'por tanto ind-construible')
patch('11.3.4',r'''Generalizando la definición de (6.10.1), sea $Y$ un subpreesquema cerrado de un preesquema $X$, definido por un ideal cuasicoherente $\mathcal J$ de $\mathcal O_X$, y sea $\sh{F}$ un $\mathcal O_X$-módulo cuasicoherente. Se dice que''',r'''Generalizando la definición de (6.10.1), se dice que para un preesquema $X$, un
subpreesquema cerrado $Y$ de $X$ definido por un Ideal cuasicoherente $\mathcal J$
de $\mathcal O_X$, y un $\mathcal O_X$-Módulo cuasicoherente $\mathcal F$,''')
patch('11.3.7',r'$\sh{O}_{\mathrm{X}_0,x_0}$',r'$\mathcal O_{x_0}$',all=True)
patch('11.3.8',r'($0\leqslant i\leqslant n$)',r'$(0\leq i\leq n)$')
patch('11.3.9',r'Como la cuestión es local en $X$ y en $\mathrm{Y}$, podemos suponer',r'Como la cuestión es local en $X$, se puede suponer')
patch('11.3.9.1',r'$q_\mu=v_{\lambda\mu}^*(q_\lambda)$ y',r'$q_\mu=v_{\lambda\mu}^*(q_\lambda)$ para $\lambda\leq\mu$, y')
patch('11.3.9.1',r'y, por tanto, regular, ya que',r'y, por consiguiente, también $(\mathcal F_y)_x$-regular, puesto que')
patch('11.3.10',r'$(2.1.6$ y $2.1.4)$',r'(2.1.6 y 2.1.4)')
patch('11.3.12',r'\emph{no es nulo}',r'\emph{no se reduzca a} $0$')
patch('11.3.12',r'un submódulo cíclico no nulo de',r'un submódulo monógeno $\neq0$ de')
patch('11.3.13',r'''pongamos $\mathfrak{p}_\alpha=\mathfrak{m}\cap\mathrm{C}_\alpha$ y''',r'''sea $\mathfrak p_\alpha$ el ideal primo $\mathfrak m\cap C_\alpha$, y pongamos''')
patch('11.3.13',r'''Pongamos $\mathfrak{p}'_\alpha=\mathfrak{m}\cap\mathrm{C}'_\alpha$ y''',r'''Sea $\mathfrak p'_\alpha$ el ideal primo $\mathfrak m\cap C'_\alpha$, y pongamos''')
patch('11.3.15',r'''se elige $f_{i+1}\notin\mathfrak{J}_i$ de modo que''',r'''$f_{i+1}$ es un elemento que no pertenece a $\mathfrak J_i$ tal que''')
patch('11.3.15',r'y estos elementos satisfacen',r'y los $f_i$ satisfacen')
patch('11.3.15',r'es el anillo de un subpreesquema afín',r'es el anillo de un subesquema afín')
patch('11.3.16',r'''es la unión, cuando varían $h$ y $k$, de las imágenes $f(\mathrm{U}_{ih}\cap\mathrm{U}_{jk})$''',r'''es unión de las imágenes $f(U_{ih}\cap U_{jk})$ para $h$, $k$ variables''')
print('Reviewed §11.3 source clauses complete')


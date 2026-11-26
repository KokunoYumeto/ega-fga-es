from iv3_review_blocks import reviewed_math
from iv3_manual import patch
reviewed_math([0,1,2,5,6,7,9,10,11,12,13,17,20,21,22,23,24,25,26,27,28,30,31])
patch('15.6.4',r'$\mathbf{0}_{\mathrm{III}},~9.2.5$',r'$\mathbf{0}_{\mathrm{III}}$, 9.2.5')
patch('15.6.4',r"en los puntos situados sobre $X_y^0$,\footnote",r"en los puntos de $f'^{-1}(z)$,\footnote")
patch('15.6.4',r"$g'=g_{(Y')}:Y'\to X'$",r"$g'=g_{(Y')}$")
patch('15.6.4','Dicho de otro modo, quedamos reducidos al caso','Dicho de otro modo, se reduce al caso')
patch('15.6.5',r'además, como $f$ es plano, la hipótesis',r'además, la hipótesis')
patch('15.6.5','Quedamos así reducidos al caso en que','Se reduce así al caso en que se supone')
patch('15.6.6',r'además, si $f^{-1}(y_0)$ es geométricamente reducido sobre $\kappa(y_0)$ en el punto $x_0$',r'además, si $f^{-1}(y_0)$ es geométricamente reducido en el punto $x_0$')
patch('15.6.6',r'las proyecciones respectivas de $x_0$ e $y_0$ en $X_1$ e $Y_1$',r'las proyecciones respectivas en $X_1$ e $Y_1$ de $x_0$ e $y_0$')
patch('15.6.6',r'(suponiendo aún $Y$ noetheriano), entonces, como $X_{y_0}^0$ es la \emph{única} componente irreducible de $f^{-1}(y_0)$ que contiene a $x_0$,',r'''(suponiendo aún $Y$
\oldpage[IV-3]{240}
noetheriano), como $X_y^0$ es la \emph{única} componente irreducible de $f^{-1}(y)$ que contiene a $x$,''')
patch('15.6.6',r'''} se
\oldpage[IV-3]{240}
deduce de \sref{IV.15.6.3} y \sref{IV.15.2.3} que, si $\dim(X_{y_0}^0)$''',r'} se deduce de \sref{IV.15.6.3} y \sref{IV.15.2.3} que, si $\dim(X_y^0)$')
patch('15.6.6',r'se puede suponer que $V$ está elegido de modo que no encuentre',r'se puede suponer $V$ elegido de modo que $V$ no encuentre')
patch('15.6.6','quedamos entonces reducidos al caso','se reduce entonces al caso')
patch('15.6.10',r'una vecindad de $X_{y_0}^{0}$ en $X$',r'una vecindad de $X_{y_0}^{0}$')


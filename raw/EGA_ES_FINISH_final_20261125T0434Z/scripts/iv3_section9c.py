from iv3_manual import patch
patch('9.7.5',r'$K$ el cuerpo de fracciones de $A$',r'$K$ su cuerpo de fracciones')
patch('9.7.5.1',r'$\mathfrak a$ es un ideal de tipo finito en $B$',r'$\mathfrak a$ es un ideal de tipo finito')
patch('9.7.5.1',r"$B=A[\mathrm{T}'_\beta, \mathrm{T}''_\gamma \mid |\beta|\leqslant p, |\gamma|\leqslant q]: P_\alpha(\mathrm{T}'_\beta,\mathrm{T}''_\gamma)=\sum_{\beta+\gamma=\alpha}\mathrm{T}'_\beta \mathrm{T}''_\gamma\setmin c_\alpha$",r"""$B=A[\mathrm T'_\beta,\mathrm T''_\gamma]_{|\beta|\leqslant p,
  |\gamma|\leqslant q}:
P_\alpha(\mathrm T'_\beta,\mathrm T''_\gamma)
=\sum_{\beta+\gamma=\alpha}\mathrm T'_\beta\mathrm T''_\gamma\setmin c_\alpha$""")
patch('9.7.5.1',r'$V(\mathfrak{a}_s)=\varnothing$',r'$V(\mathfrak a_x)=\varnothing$')
patch('9.7.6',r'un $B_{(K)}$-submódulo no nulo',r'un sub-$B_{(K)}$-módulo $\neq0$')
patch('9.7.6',r'un $B_{(\mathbf{k}(s))}$-submódulo no nulo',r'un sub-$B_{(\mathbf{k}(s))}$-módulo $\neq0$')
patch('9.7.6',r'$g$ es un elemento no nulo de $A$',r'$g$ es un elemento $\neq0$ de $A$')
patch('9.7.6',r'una subálgebra de polinomios',r'una $A$-álgebra de polinomios')
patch('9.7.7',r'y de \sref{IV.4.6.1} que $X_s$ es geométricamente reducido',r'y de \sref{IV.4.6.1} que es geométricamente reducido')
patch('9.7.10',r'es igual a $1$.',r'es igual a 1.')
patch('9.7.12',r"Si $p:S\to S_0$ es el morfismo canónico, entonces,",r"Observemos ahora que, si $p$ es el morfismo $S\to S_0$, entonces,")
patch('9.7.12',r'es geométricamente conexa \sref{IV.4.5.13}',r'es \emph{geométricamente conexa} \sref{IV.4.5.13}')
patch('9.8.1',r'$S$ es afín, noetheriano e íntegro,',r'$S$ es afín, noetheriano e íntegro de punto genérico $\eta$,')
for n in ['9.8.1','9.8.2']:
 patch(n,r'\sref{IV.8.1.2},~$a$)',r'(8.1.2, \emph{a)})')
patch('9.8.3',r'\sref{IV.3.1.3},~$c$)',r"(3.1.3, \emph{c')})") if False else None
patch('9.8.3',r"\sref{IV.3.1.3},~$c'$)",r"(3.1.3, \emph{c')})",all=True)
patch('9.8.5',r'de los ciclos primos asociados maximales,',r'de los ciclos primos maximales asociados a $\mathcal F_s$,')
patch('9.8.8',r'$S$ es afín, noetheriano e íntegro,',r'$S$ es afín, noetheriano e íntegro de punto genérico $\eta$,')
patch('9.8.8',r'una vecindad del punto genérico $\eta$',r'una vecindad de $\eta$')
patch('9.8.9',r'$x\leadsto\operatorname{length}_{\sh{O}_x}\sh{F}_x$',r'$x\leadsto\operatorname{long}_{\mathcal O_x}\mathcal F_x$')
patch('9.8.9',r'una aplicación del conjunto de los elementos maximales de $Q$ en $\mathbf N$',r'una aplicación en $\mathbf N$ del conjunto de los elementos maximales de $Q$')
patch('9.8.9',r'Llamamos \emph{esqueleto virtual}',r'Llamemos, por otra parte, \emph{esqueleto virtual}')
patch('9.8.9',r'llamamos \emph{tipo primario}',r'llamemos \emph{tipo primario}')


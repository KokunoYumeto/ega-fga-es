from iv3_manual import patch
patch('15.3.2',r'\sref{IV.13.3.1},~$a)$',r'\sref{IV.13.3.1}, $a$)')
patch('15.4.1',r'\sref{IV.13.3.1},~$a)$',r'\sref{IV.13.3.1}, $a$)')
patch('15.4.3',r'\sref{IV.13.3.1},~$b)$',r'\sref{IV.13.3.1}, $b$)')
patch('15.5.2',r"$y\neq y'$",r"$y\ne y'$")
patch('15.5.2.2',r'$f^{-1}(y)\otimes_{\kappa(y)}k$',r'$f^{-1}(y)\otimes_{\mathbf{k}(y)}k$')
patch('15.5.2.2',r"$f^{-1}(y')\otimes_{\kappa(y')}K$",r"$f^{-1}(y')\otimes_{\mathbf{k}(y')}K$")
patch('15.5.3',r"la factorización de Stein $f=g\circ f'$",r"la factorización de Stein $f=g\circ f'$ de $f$")
patch('15.5.5',r'un punto $x$',r'un punto')
patch('15.5.6.1',r'que es denso en $X$ puesto que $Z$ tiene interior vacío',r'denso en todo $X$')
patch('15.5.6.1',r"$X'\cap X''\neq\varnothing$",r"$X'\cap X''\ne\varnothing$")
patch('15.5.6.1',r'$\mathbf{0}_{\mathrm{I}},~6.3.4$',r'$\mathbf{0}_{\mathrm I}$, 6.3.4')
for ref in ['16.4.7','17.1.4','16.4.6']:
 patch('15.5.6.1',r'$\mathbf{0},~'+ref+'$',r'$\mathbf{0}$, '+ref)
patch('15.5.6.1',r'$\operatorname{depth}(\sh{O}_x/t\sh{O}_x)\geq 1$',r'$\operatorname{prof}(\mathcal O_x/t\mathcal O_x)\geqslant 1$')
patch('15.5.6.1',r'$\operatorname{depth}(\sh{O}_x)\geq 2$',r'$\operatorname{prof}(\mathcal O_x)\geqslant 2$')
patch('15.5.7',r"la factorización de Stein $f=g\circ f'$",r"la factorización de Stein $f=g\circ f'$ de $f$")
patch('15.5.7',r"e $y'$ su punto genérico.",r"e $y'$ el punto genérico de $Y$.")
for old,new in [(r'$f^{-1}(y)\neq\varnothing$',r'$f^{-1}(y)\ne\varnothing$'),(r"$f^{-1}(y')\neq\varnothing$",r"$f^{-1}(y')\ne\varnothing$"),(r'$X\neq\varnothing$',r'$X\ne\varnothing$')]:
 patch('15.5.7',old,new,all=True)


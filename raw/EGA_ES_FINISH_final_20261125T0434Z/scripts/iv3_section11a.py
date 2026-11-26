"""Source-bound Spanish clause repairs in IV3 §§11.1–11.2."""
from iv3_manual import patch
patch('11.1.1.1',r'''Por
($\mathbf 0_{\mathrm{III}}$, 10.2.2), el $\mathrm{A}$-módulo
$M_{\mathfrak q'}$ es plano si y solo si''',r'''Se sabe entonces
($\mathbf 0_{\mathrm{III}}$, 10.2.2) que para que $M_{\mathfrak q'}$ sea
un $A$-módulo plano, es necesario y suficiente que''')
patch('11.1.1.2',r'''\[
  \operatorname{Tor}_1^\mathrm{A}
  (\mathrm{M}_{\mathfrak q},\mathrm{A}/\mathfrak p)=0,
  \qquad\text{o, equivalentemente,}\qquad
  \bigl(\operatorname{Tor}_1^\mathrm{A}
  (\mathrm{M},\mathrm{A}/\mathfrak p)\bigr)_{\mathfrak q}=0.
\]''',r'''se tiene $\operatorname{Tor}_1^A(M_{\mathfrak q},A/\mathfrak p)=0$, lo que también
se escribe $(\operatorname{Tor}_1^A(M,A/\mathfrak p))_{\mathfrak q}=0$.''')
patch('11.1.1.2',r'donde a la derecha el módulo se considera como $A$-módulo',r'donde en el segundo miembro $M/\mathfrak pM$ se considera como un $A$-módulo')
patch('11.1.1.2',r'$\mathrm{A}/\mathfrak p$',r'$(A/\mathfrak p)$')
patch('11.1.2',r'muestra que es plano sobre $A$',r'muestra que $Q$ es un $A$-módulo plano')
patch('11.1.2',r'Como la última aplicación es biyectiva',r'Puesto que $M\otimes k\to P\otimes k$ es biyectivo')
patch('11.1.2',r'el lugar donde',r'el conjunto de los $x$ donde',all=True)
patch('11.1.4',r'''\[
  \sh{G}_x,\qquad
  \sh{G}=\sh{F}\big/\Bigl(\sum_{i=1}^n g_i\sh{F}\Bigr),
\]''',r'$\mathcal G_x$ (donde $\mathcal G=\mathcal F/(\sum_{i=1}^n g_i\mathcal F)$)')
patch('11.1.5',r'''que $f^{-1}(y')\subset\mathrm{V}$ para toda generalización $y'$ de $y$''',r'''que para toda generalización $y'$ de $y$, se tiene $f^{-1}(y')\subset V$''')
patch('11.1.5',r'''\[
  \mathrm{W}=\mathrm{Y}\setminus f(\mathrm{X}\setminus\mathrm{V}).
\]
Es, por consiguiente,''',r'''igual a $Y\setmin f(X\setmin V)$, por tanto también es''')
patch('11.1.5',r'y por tanto que $\mathrm{U}$ es abierto',r'de donde la conclusión')
patch('11.2.1',r'obtenemos un morfismo de complejos',r'se deduce un homomorfismo de complejos de $A$-módulos')
patch('11.2.1',r'$(\mathrm{M},~\mathrm{V},~1.1)$',r'(M, V, 1.1)',all=True)
patch('11.2.3',r'$(\mathrm{M},~\mathrm{IV},~1)$',r'(M, IV, 1)')
patch('11.2.4',r'C-módulo',r'$C$-módulo',all=True)
patch('11.2.4',r'C-\emph{módulos}',r'$C$-\emph{módulos}')
patch('11.2.7',r'el S-preesquema',r'el $S$-preesquema')
patch('11.2.7',r'es S-isomorfo',r'es $S$-isomorfo')
patch('11.2.7',r'''$X$, que $\mathcal F$ es isomorfo''',r'''$X$ y que, si se identifica $X$ con $X_0\otimes_{S_0}S$, $\mathcal F$ es isomorfo''')
patch('11.2.7',r'''Podemos,
por tanto, escribir
\[
  \mathrm{X}=\varprojlim_\lambda \mathrm{X}_\lambda,\qquad
  \mathrm{X}_\lambda=\mathrm{X}_0\otimes_{\mathrm{A}_0}\mathrm{A}_\lambda,
\]
donde''',r'''se puede, por tanto, escribir
$X=\varprojlim X_\lambda$, donde $X_\lambda=X_0\otimes_{A_0}A_\lambda$,
y''')
patch('11.2.8',r'un S-morfismo',r'un $S$-morfismo')
patch('11.2.8','(11.2.6.1,~(\textup{ii}))','(11.2.6.1, (ii))')
patch('11.2.9',r'''\medskip
\noindent\emph{Demostración.}''',r'\begin{proof}')
patch('11.2.9.2',r'son $A$-módulos planos implica',r'son $A$-módulos planos para $k\geq0$ implica')
patch('11.2.9.4',r'de grado $0$',r'de grado 0')
patch('11.2.9.4',r'de $A$ y que los homomorfismos',r'de $A$, cuyo límite inductivo es $A$, y los homomorfismos')
patch('11.2.9.5',r'''y sustituyendo $B_0$, $\mathfrak J_0$ y $M_0$ por
\[
  \mathrm{B}'_0=\mathrm{B}_0\otimes_{\mathrm{A}_0}\mathrm{A}'_0,
  \qquad
  \mathfrak{J}'_0=\mathfrak{J}_0\mathrm{B}'_0,
  \qquad
  \mathrm{M}_0\otimes_{\mathrm{A}_0}\mathrm{A}'_0,
\]
respectivamente''',r'''$B_0$ por $B'_0=B_0\otimes_{A_0}A'_0$, $\mathfrak J_0$ por
$\mathfrak J'_0=\mathfrak J_0B'_0$ y $M_0$ por $M_0\otimes_{A_0}A'_0$''')
patch('11.2.9.5',r'este módulo se identifica con',r'$\operatorname{gr}_{\mathfrak J_0}^\bullet(M_0)\otimes_{A_0}A_{01}$ se identifica con')
patch('11.2.9.5',r'de grado $0$',r'de grado 0')
print('Reviewed §§11.1–11.2 clauses complete')


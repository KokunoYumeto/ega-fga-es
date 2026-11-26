"""Source-bound corrections of theorem IV.11.6.1, including author register."""
from iv3_manual import patch
n='11.6.1'
patch(n,r"$f'=f_{|\mathrm{Y}'}$",r"$f'=f_{(Y')}$")
patch(n,r"$u^{-1}(\mathfrak{p}')=(0)$",r"$u^{-1}(\mathfrak p')=0$")
patch(n,r"$\mathrm{A}\to\mathrm{A}'\to\mathrm{A}''=\mathrm{A}'/\mathfrak{p}'$",r"$A\xrightarrow{u}A'\to A''=A'/\mathfrak p'$")
patch(n,r'(\textbf{I},~$3.4.7$)',r'(\textbf I, 3.4.7)')
patch(n,r'(\textbf{I},~$3.6.4$)',r'(\textbf I, 3.6.4)')
patch(n,r'(\textbf{I},~$3.5.7$)',r'(\textbf I, 3.5.7)')
patch(n,r"$\mathrm{X}_{\alpha\lambda}\times_{\mathrm{Y}_{\alpha\lambda}}\mathrm{Y}'_\mu=\mathrm{X}'_\mu$",r"$X_{\alpha\lambda}\times_{Y_{\alpha\lambda}}Y'_{\mu}=X'_{\alpha\mu}$")
patch(n,r'''Más precisamente, escribamos $k_1=k[T]/(r)$, donde $r$ es un polinomio mónico irreducible separable de grado $n$, y sea $\mathrm{R}\in\mathrm{A}[\mathrm{T}]$ un polinomio mónico cuya imagen canónica es $r$; podemos tomar $A_1=A[T]/(R)$.''',r'''De manera precisa, se puede suponer
que $k_1=k[T]/(r)$, donde $r$ es un polinomio mónico irreducible y separable de
$k[T]$ de grado $n$; si $R$ es un polinomio mónico de $A[T]$ cuya imagen
canónica es $r$ (y que es, por tanto, de grado $n$), se puede tomar
$A_1=A[T]/(R)$.''')
patch(n,r'es no nula y que, por consiguiente, es invertible',r'es $\ne0$, y que es, por consiguiente, invertible')
patch(n,r'''Como $A\to A'$ es inyectivo y $A_1$ es un $A$-módulo plano, el homomorfismo $\mathrm{A}_1\to\mathrm{A}'_1$ es inyectivo.''',r'''Por otra parte, como $A\to A'$ es un homomorfismo
inyectivo, lo mismo ocurre con $A_1\to A'_1$, siendo $A_1$ un $A$-módulo plano;''')
patch(n,r"el homomorfismo compuesto de $\mathrm{A}_1$ en este producto",r"el compuesto $A_1\to\prod_{i=1}^{r}(A'_1)_{\mathfrak n_i}$")
patch(n,r'''y $\mathcal F'_1=\mathcal F'\otimes_{Y'}Y'_1$.
El módulo $\sh{F}'_1$ es''',r'''; $\mathcal F'_1=\mathcal F'\otimes_{Y'}Y'_1$ es''')
patch(n,r"todos estos puntos se proyectan en el punto cerrado $y'_1$ de $Y'_1$",r"todos estos puntos tienen por proyección en $Y'_1$ el punto cerrado $y'_1$")
patch(n,r"sus proyecciones en $X$ y $\mathrm{Y}_1$ son, respectivamente, $x$ y el punto cerrado $y_1$",r"la proyección de $x_1$ en $X$ es $x$ y su proyección en $Y_1$ es el punto cerrado $y_1$")
patch(n,r'''bajo las condiciones~(i) y~(ii), la topología $\mathfrak m$-ádica de $A$''',r'''bajo las condiciones (i) y (ii), si
$\mathfrak m$ y $\mathfrak m'$ son los ideales maximales de $A$ y $A'$
respectivamente, la topología $\mathfrak m$-ádica de $A$''')
patch(n,r'Podemos limitarnos',r'Se puede limitar')
patch(n,r'podemos suponer',r'se puede suponer',all=True)
patch(n,r'podemos, pues, suponer',r'se puede, por tanto, suponer')
patch(n,r'Si demostramos que',r'Si se prueba que',all=True)
patch(n,r'podremos aplicar',r'se podrá aplicar')
patch(n,r'Quedamos así reducidos',r'Se reduce así')
patch(n,r'Podemos considerar',r'Se puede considerar')
patch(n,r'podemos sustituir',r'se puede reemplazar')
patch(n,r'podemos tomar',r'se puede tomar')
patch(n,r'Podemos comenzar repitiendo',r'Se puede en primer lugar repetir')
patch(n,r'quedamos así reducidos',r'se reduce así')
patch(n,r'como supondremos en lo sucesivo',r'lo que se va a suponer en lo que sigue')
patch(n,r'hemos quedado efectivamente reducidos',r'se ha reducido efectivamente')
patch(n,r'Finalmente, quedamos reducidos',r'Finalmente, se reduce')
patch(n,r'Podemos, por tanto, aplicar \sref{IV.11.5.2}.',r'Se puede, por tanto, aplicar el resultado de \sref{IV.11.5.2}. C.Q.F.D.')
patch(n,r'anillo local integral',r'anillo local íntegro')
patch(n,r'$A$ es integral',r'$A$ es íntegro')
patch(n,r"$A'$ es \emph{integral}",r"$A'$ es \emph{íntegro}")
patch(n,r'anillo integral',r'anillo íntegro')
patch(n,r'$A_1$ es integral',r'$A_1$ es íntegro')
print('11.6.1 clauses, notation and register restored')


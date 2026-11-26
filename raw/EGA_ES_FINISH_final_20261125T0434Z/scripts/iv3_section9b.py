from iv3_manual import patch
patch('9.5.3',r'''\begin{enumerate}[label=\upshape{$\arabic{enumi}^\circ$}]
  \item''',r'$1^\circ$')
patch('9.5.3',r'\item\label{IV.9.5.3.case2}',r'\label{IV.9.5.3.case2}$2^\circ$')
patch('9.5.3',r'\end{enumerate}','')
patch('9.5.3',r'para todo $s$ en una vecindad de $\eta$ en $S$',r'para todo $s$ próximo a $\eta$')
patch('9.5.3',r'$Z_\eta$ es construible y denso en $X_\eta$',r'$Z_\eta$ es construible en $X_\eta$ y denso en $X_\eta$')
patch('9.5.3',r'$t$ es un elemento no nulo de $A$',r'$t$ es un elemento $\neq0$ de $A$')
patch('9.5.3',r'Sustituyendo $S$ por una vecindad de $\eta$ en $S$ si es necesario',r'Sustituyendo $S$ por una vecindad de $\eta$ si es necesario')
patch('9.5.3',r'el subpreesquema cuyo espacio subyacente reducido es $Z$',r'el subpreesquema reducido cuyo espacio subyacente es $Z$') if False else None
patch('9.5.3',r"el subpreesquema cuyo espacio subyacente reducido es $Z'$",r"el subpreesquema reducido cuyo espacio subyacente es $Z'$")
patch('9.5.3',r'$A$ es un anillo noetheriano íntegro',r'$A$ es un anillo noetheriano \emph{íntegro}')
patch('9.5.4',r'siendo este último cerrado.',r'siendo este último cerrado en $X_s$.')
patch('9.5.5',r'que es abierto en $Z$ y tal que $(U_i)_s$',r'que es abierto en $Z$ y tal que, para todo $s\in S$, $(U_i)_s$')
for n in ['9.6.1','9.6.2','9.6.3']:
 patch(n,'S-preesquema',r'$S$-preesquema',all=True)
 patch(n,'S-morfismo',r'$S$-morfismo',all=True)
patch('9.6.1',r'decir que $f_s$ es una inmersión equivale a decir que es una inmersión cerrada',r'decir que $f_s$ es una inmersión equivale a decir que $f_s$ es una inmersión cerrada')
patch('9.6.1',r'Se sigue entonces de (viii) que para $s$ próximo a $\eta$,',r'Se sigue entonces de (viii) que para $s$ próximo a $\eta$ en $S$,')
patch('9.6.1',r'\sref[I]{I.6.2}',r'\sref{IV.1.6.2}',all=True)
patch('9.6.3',r"Consideraremos separadamente los casos $E$ y $E'$.",r"Consideraremos separadamente el caso de $E'$ y el de $E$.")
patch('9.6.3',r'''\oldpage[IV-3]{75}

\emph{Caso de $E'$.} ---
Como $f$ es separado y $Y$ es cuasicompacto, existe un entero $h$ tal que
$R^qf_*(\sh{L})=0$ para $q>h$ \sref[III]{III.1.4.12}.
Por otra parte, como $f$ es propio y $Y$ es noetheriano, todos los
$R^qf_*(\mathcal L)$ son $\mathcal O_Y$-Módulos \emph{coherentes} \sref[III]{III.3.2.1}.
Se anulan salvo para un número finito de valores de $q$, por lo que el teorema de planitud genérica
\sref{IV.6.9.1} muestra que, tras restringir $S$ a una vecindad de $\eta$, podemos
suponer que $\mathcal L$ y los $R^qf_*(\mathcal L)$ son \emph{todos} \emph{planos} sobre $S$.
Se sigue entonces de \sref[III]{III.6.9.9} que el homomorfismo canónico''',r'''I) \emph{Caso de $E'$.} --- Señalemos que, puesto que $f$ es separado e $Y$
cuasicompacto, existe un entero $h$ tal que, para $q>h$, se tiene
$R^qf_*(\mathcal L)=0$ \sref[III]{III.1.4.12}; por otra parte, puesto que $f$ es
propio e $Y$ noetheriano, los $R^qf_*(\mathcal L)$ son todos
$\mathcal O_Y$-Módulos \emph{coherentes} \sref[III]{III.3.2.1}; como son nulos
salvo para un número finito de valores de $q$, el teorema de planitud genérica
\sref{IV.6.9.1} muestra que, restringiendo $S$ a una vecindad de $\eta$, se puede
suponer que $\mathcal L$ y los $R^qf_*(\mathcal L)$ son \emph{todos} $S$-\emph{planos}. Se
concluye entonces de \sref[III]{III.6.9.9} que el homomorfismo canónico''')
patch('9.6.3',r'''es un isomorfismo.

Se sigue de''',r'''es un \emph{isomorfismo}.

\oldpage[IV-3]{75}

Dicho esto, se deduce de''')
patch('9.6.3',r'la forma: 1$^\circ$',r'la forma: $1^\circ$')
patch('9.6.3',r'sobreyectivo; 2$^\circ$',r'sobreyectivo; $2^\circ$')
patch('9.6.3',r'en virtud de \sref{IV.9.6.1}, (viii), el morfismo $X_s\to\mathbf{P}((f_*(\sh{L}))_s)$ no es una inmersión para $s$ en una vecindad de $\eta$',r'en virtud de \sref{IV.9.6.1}, (viii), para $s$ suficientemente próximo a $\eta$, el morfismo $X_s\to\mathbf P((f_*(\mathcal L))_s)$ no es una inmersión')
patch('9.6.3',r'\emph{Caso de $E$.} ---',r'II) \emph{Caso de $E$.} ---')
patch('9.6.7',r'en la reducción al caso noetheriano,',r'en la reducción al caso en que $S$ es noetheriano,')


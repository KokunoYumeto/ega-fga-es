import iv3_full_translations as m
m.TRANSLATIONS={}
m.TRANSLATIONS['9.9.2']=r"""\begin{proposition}[9.9.2]
\label{IV.9.9.2}
Sean $f:X\to S$ un morfismo localmente de presentación finita, $\mathcal F$
un $\mathcal O_X$-Módulo cuasicoherente de presentación finita, $\Phi$ una
parte finita de $\mathbf Z\cup\{\pm\infty\}$. Las partes siguientes de $X$
son localmente construibles:
\begin{enumerate}
\item[\textup{(i)}] El conjunto de los puntos $x\in X$ tales que $\mathcal F_{f(x)}$ es
equidimensional en el punto $x$ \textup{(5.1.12)}.
\item[\textup{(ii)}] El conjunto de los $x\in X$ tales que las longitudes geométricas de
$\mathcal F_{f(x)}$ relativas a $\boldsymbol{k}(f(x))$, en los puntos genéricos de las componentes
irreducibles de $\operatorname{Supp}(\mathcal F_{f(x)})$ que contienen a $x$
\textup{(4.7.5)}, pertenecen a $\Phi$.
\item[\textup{(iii)}] El conjunto de los $x\in X$ tales que las dimensiones de los ciclos
primos asociados a $\mathcal F_{f(x)}$ y que contienen a $x$ pertenecen a
$\Phi$.
\item[\textup{(iv)}] El conjunto de los $x\in X$ tales que $\mathcal F_{f(x)}$ es
geométricamente reducido en el punto $x$ \textup{(4.6.17)}.
\item[\textup{(v)}] El conjunto de los $x\in X$ tales que $\mathcal F_{f(x)}$ es
geométricamente íntegro en el punto $x$ \textup{(4.6.22)}.
\item[\textup{(vi)}] El conjunto de los $x\in X$ tales que
$\operatorname{dim.proj}((\mathcal F_{f(x)})_x)\in\Phi$.
\item[\textup{(vii)}] El conjunto de los $x\in X$ tales que
$\operatorname{coprof}((\mathcal F_{f(x)})_x)\in\Phi$.
\item[\textup{(viii)}] El conjunto de los $x\in X$ tales que $\mathcal F_{f(x)}$ posee la
propiedad $(S_k)$ en el punto $x$ \textup{(5.7.2)}.
\item[\textup{(ix)}] El conjunto de los $x\in X$ tales que $\mathcal F_{f(x)}$ es un
$\mathcal O_{X_{f(x)}}$-Módulo de Cohen-Macaulay en el punto $x$ \textup{(5.7.1)}.
\end{enumerate}
\end{proposition}

(i) El soporte $Z$ de $\mathcal F$ es localmente construible y cerrado en
$X$ (8.9.1), y considerando un subpreesquema de $X$ que tenga a $Z$ como espacio
subyacente y que sea de presentación finita sobre $S$ (8.9.1), se ve que
la afirmación (i) es un caso particular de (9.9.1, (iii)).

(ii) Todas las propiedades consideradas son locales sobre $X$, y se limitará,
por tanto, al caso en que $X=\operatorname{Spec}(B)$ y $S=\operatorname{Spec}(A)$ son
afines y $f$ es un morfismo de presentación finita. Se conservan las notaciones del
comienzo de la demostración de (9.9.1), y se supone además $A_0$ elegido de
modo que exista un $\mathcal O_{X_0}$-Módulo coherente $\mathcal F_0$ tal que
$\mathcal F$ sea isomorfo a $\mathcal F_0\otimes_{A_0}A$. Entonces ((4.2.7) y
(4.7.9)), el conjunto de las longitudes geométricas de
$(\mathcal F_0)_{f(x_0)}$ en los puntos genéricos de las componentes irreducibles de
$\operatorname{Supp}((\mathcal F_0)_{f(x_0)})$ que contienen a $x_0$ es el
mismo que el conjunto análogo para $x$ y $\mathcal F_{f(x)}$; dicho de otro modo,
si $E$ (resp. $E_0$) es el conjunto de los $x\in X$ (resp. de los $x_0\in X_0$)
que satisfacen la condición (ii) del enunciado, se tiene $E=h^{-1}(E_0)$, y en virtud de
(1.8.2), se ve que se puede limitar a considerar el caso en que $A$ es
\emph{noetheriano}. Como en la demostración de (9.9.1), se ve que se
reduce a mostrar que, para todo $x\in X$, existe una vecindad $V$ de $x$
en $\overline{\{x\}}$ tal que, para todo $x'\in V$, el conjunto de las longitudes
geométricas de $\mathcal F_{f(x')}$ en los puntos genéricos de las componentes
irreducibles de su soporte que contienen a $x'$ es \emph{el mismo}. Además, si
$S'$ es el subpreesquema reducido de $S$ que tiene a $\overline{\{f(x)\}}$ como espacio
subyacente, y si $X'=f^{-1}(S')$, las fibras de $X$ y de $X'$ en los puntos de
$S'$ son las mismas,
\oldpage[IV-3]{91}
por lo que se puede reemplazar $S$ por $S'$ y $X$ por $X'$, es decir, suponer que
$S$ es \emph{íntegro} y que $\eta=f(x)$ es su punto genérico.

Ahora bien, si se pone $Z=\operatorname{Supp}(\mathcal F)$, el mismo razonamiento que
en la demostración de (9.9.1) muestra que, si $Z_i$ son las componentes
irreducibles de $Z$ que contienen a $x$, se puede suponer que son exactamente las
componentes irreducibles de $Z$ que encuentran $\overline{\{x\}}$ y que
$(Z_i)_s\cap\overline{\{x\}}\neq\varnothing$ para todo $s\in S$. La conclusión
se deduce entonces de (9.8.3) y (9.8.6).

(iii) Se reduce como en (ii) al caso en que $S$ es noetheriano e íntegro y
$\eta=f(x)$ su punto genérico, utilizando (4.2.7). Como en la
demostración de (9.9.1), se reduce a mostrar que existe una vecindad $V$
de $x$ en $\overline{\{x\}}$ tal que, para todo $x'\in V$, el conjunto de las
dimensiones de los ciclos primos asociados a $\mathcal F_{f(x')}$ que contienen a
$x'$ es \emph{el mismo}. Ahora bien, si $Z'_i$ son las adherencias en $X$ de los ciclos
primos asociados a $\mathcal F_\eta$ que contienen a $x$ (cf. (9.8.2)), se
deduce de (9.8.3) y (9.5.1) que, para todo $s$ suficientemente próximo a $\eta$, los
ciclos primos asociados a $\mathcal F_s$ que encuentran
$\overline{\{x\}}$ son componentes irreducibles de los $(Z'_i)_s$ y, en
virtud de (9.5.6), todas estas componentes irreducibles tienen la misma dimensión igual
a $\dim((Z'_i)_\eta)$, de donde la conclusión.

(iv) Se razona como en (iii), utilizando esta vez (4.7.11). Con las
mismas notaciones que en (iii), los ciclos primos asociados a $\mathcal F_s$
que son componentes irreducibles de $(Z'_i)_s$ son inmersos si y
solo si $(Z'_i)_\eta$ es un ciclo primo asociado inmerso de
$\mathcal F_\eta$. Se concluye ya que, si $x$ pertenece a un (resp.
no pertenece a ningún) ciclo primo asociado inmerso de $\mathcal F_\eta$,
el conjunto de los $x'\in\overline{\{x\}}$ tales que $x'$ pertenece a un (resp.
no pertenece a ningún) ciclo primo asociado inmerso de $\mathcal F_{f(x')}$
es una vecindad de $x$ en $\overline{\{x\}}$. La conclusión se deduce de esta
observación, de la caracterización de los puntos donde un Módulo es geométricamente
reducido (4.7.10), y de (ii).

(v) Teniendo en cuenta (4.7.11), se reduce de nuevo al caso en que $S$ es noetheriano
e íntegro y en que $\eta=f(x)$ es su punto genérico. Sea $Y$ un
subpreesquema cerrado de $X$ que tenga a $\operatorname{Supp}(\mathcal F)$ como espacio
subyacente. Razonando como al comienzo de la demostración de (9.7.7), se ve
que existe una $A$-álgebra íntegra finita $A'$ (de modo que, si
$S'=\operatorname{Spec}(A')$, el morfismo $S'\to S$ es finito y sobreyectivo)
tal que, si $Y'=Y_{(S')}$ y si $\eta'$ es el punto genérico de $S'$, las
componentes irreducibles de $Y'_{\eta'}$ son \emph{geométricamente irreducibles}.
Por otra parte, si $X'=X_{(S')}$, el morfismo proyección $h:X'\to X$ es finito
y sobreyectivo, por tanto cerrado; por consiguiente, si $x'$ es un punto de $X'$ situado sobre
$x$, se tiene $h(\overline{\{x'\}})=\overline{\{x\}}$ y la imagen por $h$ de una
vecindad de $x'$ en $\overline{\{x'\}}$ es una vecindad de $x$ en
$\overline{\{x\}}$. Teniendo en cuenta (4.7.11) y poniendo
$\mathcal F'=\mathcal F_{(S')}$, se reduce, pues, a probar que, si
$\mathcal F'_{\eta'}$ es (resp. no es) geométricamente íntegro en el punto
$x'$, el conjunto de los $y'\in\overline{\{x'\}}$ tales que
$\mathcal F'_{f'(y')}$ (donde $f'=f_{(S')}:X'\to S'$) es (resp. no es)
geométricamente íntegro en el punto $y'$ es una vecindad de $x'$ en
$\overline{\{x'\}}$. Se puede, por tanto, limitar al caso en que $X'=X$ y en que las
componentes irreducibles de $Y_\eta$ son \emph{geométricamente irreducibles}; si
se denota por $Z_i$ unas partes cerradas de $X$ tales que los
$Z_i\cap X_\eta$ son las
\oldpage[IV-3]{92}
componentes irreducibles de $Y_\eta$, se deduce de (9.7.7), (9.7.8) y
(9.5.3) que, para todo $s$ próximo a $\eta$, los $(Z_i)_s$ son las componentes
irreducibles de $Y_s$ y que son \emph{geométricamente irreducibles}.
Decir que, en un punto $y\in X_s$, $\mathcal F_s$ es geométricamente íntegro
significa entonces que $\mathcal F_s$ es geométricamente reducido en este punto y
además que $y$ solo pertenece a \emph{uno solo} de los $(Z_i)_s$ (4.6.22). La
conclusión se deduce, pues, por una parte de (iv) y por otra de (9.5.1) aplicado a
la intersección de $\overline{\{x\}}$ y de cada $Z_i$.

(vi) Conservando las mismas notaciones que en (ii), se deduce de (6.2.1) que se
tiene
$\operatorname{dim.proj}((\mathcal F_s)_x)=
\operatorname{dim.proj}(((\mathcal F_0)_{s_0})_{x_0})$;
se puede, por tanto, limitar de nuevo al caso en que $A$ es \emph{noetheriano}. Además,
se reduce de nuevo a mostrar que, para todo $x\in X$, existe una vecindad $V$
de $x$ en $\overline{\{x\}}$ tal que, para todo $x'\in V$, se tiene
$\operatorname{dim.proj}((\mathcal F_{f(x')})_{x'})=
\operatorname{dim.proj}((\mathcal F_{f(x)})_x)$;
y como antes, se puede suponer que $S$ es \emph{íntegro} y que
$\eta=f(x)$ es su punto genérico, de modo que se tiene
$(\mathcal F_\eta)_x=\mathcal F_x$. En virtud del teorema de planitud genérica
(6.9.1), se puede, reemplazando si es necesario $S$ por una vecindad abierta de
$\eta$, suponer que el morfismo $f$ es \emph{plano} y que $\mathcal F$ es
\emph{$f$-plano}; se tiene entonces
$\operatorname{dim.proj}((\mathcal F_{f(x')})_{x'})=
\operatorname{dim.proj}(\mathcal F_{x'})$ para \emph{todo} $x'\in X$ en virtud de
(6.2.3). Dicho esto, en virtud de (6.11.1), se puede (reemplazando si es necesario $X$
por una vecindad abierta de $x$) suponer que
$\operatorname{dim.proj}(\mathcal F_{x'})\leq
\operatorname{dim.proj}(\mathcal F_x)$ para \emph{todo} $x'\in X$. Por otra parte, si
$\operatorname{dim.proj}(\mathcal F_x)=n$, existe por hipótesis un
$\mathcal O_x$-módulo de tipo finito $M$ tal que
$\operatorname{Ext}_{\mathcal O_x}^n(\mathcal F_x,M)\neq0$
($\mathbf 0$, 17.2.4). Ahora bien, existe un $\mathcal O_X$-Módulo coherente
$\mathcal G$ tal que $M=\mathcal G_x$ (reemplazando si es necesario $X$ por una
vecindad abierta de $x$ ($\mathbf 0_{\mathrm I}$, 5.3.8)); en virtud de
(T, 4.2.2), se tiene, pues,
$(\mathcal{E}xt_{\mathcal O_X}^n(\mathcal F,\mathcal G))_x\neq0$. Pero
$\mathcal{E}xt_{\mathcal O_X}^n(\mathcal F,\mathcal G)$ es un
$\mathcal O_X$-Módulo coherente ($\mathbf 0_{\mathrm{III}}$, 12.3.3), por lo que su
soporte $Y$ es cerrado ($\mathbf 0_{\mathrm I}$, 5.2.2); como contiene a $x$,
contiene también $\overline{\{x\}}$, de donde se concluye (aplicando de nuevo
(T, 4.2.2)) que se tiene
$\operatorname{dim.proj}(\mathcal F_{x'})\geq n$ para todo
$x'\in\overline{\{x\}}$, lo que termina de probar la afirmación en el caso (vi).

(vii) Como $B$ es una $A$-álgebra de tipo finito, $X$ es $S$-isomorfo a un
\emph{subesquema cerrado} de un $S$-esquema de la forma
$Y=\operatorname{Spec}(A[T_1,\ldots,T_r])$; si $j:X\to Y$ es la inyección
canónica, y $\mathcal G=j_*(\mathcal F)$, se tiene
$\mathcal G_s=(j_s)_*(\mathcal F_s)$ para todo $s\in S$, y, en virtud de
($\mathbf 0$, 16.4.11), se puede limitar a demostrar la afirmación para $Y$ y
$\mathcal G$. Dicho de otro modo, se puede suponer que $B=A[T_1,\ldots,T_r]$, de
modo que cada uno de los esquemas $X_s=\operatorname{Spec}(\boldsymbol{k}(s)[T_1,\ldots,T_r])$
es \emph{regular} ($\mathbf 0$, 17.3.7). Sea entonces
$W=\operatorname{Supp}(\mathcal F)$, de modo que
$W_s=\operatorname{Supp}(\mathcal F_s)$ (\textbf{I}, 9.1.13); se tiene, por
(6.11.2.1),
\begin{equation}
\tag{9.9.2.1}
\label{IV.9.9.2.1}
\operatorname{coprof}((\mathcal F_{f(x)})_x)=
\operatorname{dim.proj}((\mathcal F_{f(x)})_x)\setmin
\operatorname{codim}_x(W_{f(x)},X_{f(x)}).
\end{equation}
Pero, como $W$ es construible (8.9.1) y cada $W_s$ cerrado, se deduce de
(vi) y de (9.9.1, (ii)) que las dos funciones del segundo miembro de (9.9.2.1)
son construibles; lo mismo ocurre, por tanto, con su diferencia, lo que termina
de probar la proposición en el caso (vii).

(viii) Sea $U_n$ el conjunto de los $x\in X$ tales que
$\operatorname{coprof}((\mathcal F_{f(x)})_x)\leq n$, y pongamos
$Z_n=X\setmin U_n$; se deduce de (vii) que los $Z_n$ son \emph{construibles}; además,
como
la fun%
\oldpage[IV-3]{93}
ción $x\leadsto\dim_x(W_{f(x)})$ es construible en virtud de
(9.9.1, (i)), solo toma un número finito de valores, por lo que los números
$\dim(W_{f(x)})$ tienen una cota superior finita $m$ cuando $x$ recorre $X$;
como
$\operatorname{coprof}((\mathcal F_{f(x)})_x)\leq
\dim((\mathcal F_{f(x)})_x)\leq\dim(W_{f(x)})$, se ve que se tiene
$Z_n=\varnothing$ para $n\geq m$. Finalmente, se deduce de (6.11.2, (i)) que, para
todo $n$ y todo $s\in S$, $(Z_n)_s$ es \emph{cerrado} en $X_s$. Según
(5.7.4), el conjunto de los $x\in X$ donde $(\mathcal F_{f(x)})_x$ posee la
propiedad $(S_k)$ es el conjunto de los $x\in X$ que satisfacen todas las relaciones
\begin{equation}
\tag{9.9.2.2}
\label{IV.9.9.2.2}
\operatorname{codim}_x((Z_n)_{f(x)},W_{f(x)})>n+k
\end{equation}
para todo $n\geq0$; como esta relación se satisface automáticamente para
$n\geq m$, solo se han de considerar las relaciones (9.9.2.2) para $0\leq n<m$.
Pero, en virtud de (9.9.1, (ii)), el conjunto $V_{n,k}$ de los $x$ que satisfacen (9.9.2.2)
es construible, y lo mismo ocurre con la intersección de estos conjuntos para
$0\leq n<m$.

(ix) La afirmación se deduce aquí inmediatamente de (vii), pues el conjunto de los $x\in X$ donde
$(\mathcal F_{f(x)})_x$ es un módulo de Cohen-Macaulay está definido por la
relación $\operatorname{coprof}((\mathcal F_{f(x)})_x)=0$.

"""
m.apply()


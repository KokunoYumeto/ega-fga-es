import iv3_full_translations as m
m.TRANSLATIONS={}
m.TRANSLATIONS['9.4.2']=r"""\begin{proposition}[9.4.2]
\label{IV.9.4.2}
Sean $S$ un preesquema íntegro de punto genérico $\eta$, $f:X\to S$ un
morfismo de presentación finita, $\mathcal F$, $\mathcal G$, $\mathcal H$
tres $\mathcal O_X$-Módulos cuasicoherentes de presentación finita. Sean
$u:\mathcal F\to\mathcal G$, $v:\mathcal G\to\mathcal H$ dos
homomorfismos de $\mathcal O_X$-Módulos, y supongamos que la sucesión
$\mathcal F_\eta\xrightarrow{u_\eta}\mathcal G_\eta
\xrightarrow{v_\eta}\mathcal H_\eta$ es exacta. Entonces existe una
vecindad abierta $U$ de $\eta$ en $S$ tal que, para todo $s\in U$, la sucesión
$\mathcal F_s\xrightarrow{u_s}\mathcal G_s
\xrightarrow{v_s}\mathcal H_s$ es exacta.
\end{proposition}

Con las notaciones generales de (9.2.1), se trata aquí de la relación
$\boldsymbol{P}(X,\mathcal F,\mathcal G,\mathcal H,u,v,k)$: «$X$ es un
preesquema algebraico sobre el cuerpo $k$,
$\mathcal F\xrightarrow{u}\mathcal G\xrightarrow{v}\mathcal H$ una sucesión
exacta de $\mathcal O_X$-Módulos cuasicoherentes». Como, para toda extensión
$k'$ de $k$, la proyección canónica $X_{(k')}\to X$ es un morfismo
fielmente plano (2.2.13), se satisface la condición (9.2.1, (i)) (2.2.7). En
virtud de (9.2.3), se puede limitar al caso en que $S$ es íntegro y
\emph{noetheriano}, en cuyo caso $X$ es noetheriano, y $\mathcal F$,
$\mathcal G$, $\mathcal H$ son $\mathcal O_X$-Módulos coherentes.
La hipótesis implica que existe una vecindad abierta $U$ de $\eta$ en $S$
tal que la sucesión
$\mathcal F|f^{-1}(U)\to\mathcal G|f^{-1}(U)\to\mathcal H|f^{-1}(U)$ es
\emph{exacta}, en virtud de (8.5.8, (i)) aplicado según el método general
de (8.1.2, \emph{a)}), y se puede, por tanto, suponer ya que la sucesión
$\mathcal F\xrightarrow{u}\mathcal G\xrightarrow{v}\mathcal H$ es exacta;
basta evidentemente probar que se tiene
$\operatorname{Ker}(v_s)=(\operatorname{Ker}v)_s$ y
$\operatorname{Im}(u_s)=(\operatorname{Im}u)_s$ para todo $s$ próximo a
$\eta$ en $S$; por consiguiente (teniendo en cuenta que los
$\mathcal O_X$-Módulos $\mathcal F$, $\mathcal G$, $\mathcal H$ son
\emph{coherentes} y $(\mathbf 0_{\mathrm I},5.3.4)$), se reduce a
probar la proposición en el caso particular en que la sucesión
$0\to\mathcal F\xrightarrow{u}\mathcal G\xrightarrow{v}\mathcal H\to0$
es exacta. Ahora bien, existe entonces un abierto $U$ en $S$ que contiene a $\eta$ y tal
que $\mathcal H|f^{-1}(U)$ es \emph{plano} sobre $U$ (6.9.1); se deduce, pues,
de (2.1.8) que, para todo $s\in U$, la sucesión
$0\to\mathcal F_s\to\mathcal G_s\to\mathcal H_s\to0$ es exacta, lo que
termina la demostración.

"""
m.TRANSLATIONS['9.4.3']=r"""\begin{corollary}[9.4.3]
\label{IV.9.4.3}
Sean $S$ un preesquema íntegro, de punto genérico $\eta$, $f:X\to S$ un
morfismo de presentación finita. Sea
$\mathcal L^\bullet=(\mathcal L^i)_{i\in\mathbf Z}$ un complejo de
$\mathcal O_X$-Módulos cuasicoherentes de presentación finita. Para todo $i$,
existe una vecindad abierta $U$ de $\eta$ en $S$ tal que los homomorfismos
canónicos
\begin{equation}
\label{IV.9.4.3.1}
(\mathcal H^i(\mathcal L^\bullet))_s\to
\mathcal H^i(\mathcal L_s^\bullet) \tag{9.4.3.1}
\end{equation}
son biyectivos para todo $s\in U$.
\end{corollary}

\oldpage[IV-3]{63}

Se puede evidentemente limitar a un complejo de tres términos de grados
$-1$, $0$, $+1$:
$\mathcal M\xrightarrow{u}\mathcal N\xrightarrow{v}\mathcal P$
y a $i=0$; el homomorfismo que se ha de considerar es entonces el homomorfismo canónico
$(\operatorname{Ker}v/\operatorname{Im}u)_s\to
\operatorname{Ker}(v_s)/\operatorname{Im}(u_s)$. Utilizando (8.9.1) y
(8.5.2, (i)), se ve que se puede reducir al caso en que $S$ (por tanto también $X$)
es \emph{noetheriano}, y por consiguiente $\mathcal M$, $\mathcal N$, $\mathcal P$
son $\mathcal O_X$-Módulos \emph{coherentes}; entonces
$\operatorname{Im}(u)$ y $\operatorname{Ker}(v)$ son también coherentes
$(\mathbf 0_{\mathrm I},5.3.4)$ y además existe una vecindad $U$ de
$\eta$ tal que, para $s\in U$, se tiene
$\operatorname{Ker}(v_s)=(\operatorname{Ker}(v))_s$ y
$\operatorname{Im}(u_s)=(\operatorname{Im}(u))_s$ (9.4.2); la conclusión
se deduce entonces de (9.4.2) aplicado a la sucesión exacta
$0\to\operatorname{Im}(u)\to\operatorname{Ker}(v)\to
\operatorname{Ker}(v)/\operatorname{Im}(u)\to0$,
teniendo en cuenta que $\mathcal O_\eta=\boldsymbol{k}(\eta)$ (puesto que $S$ es íntegro) y
por consiguiente la sucesión
\[
0\to(\operatorname{Im}u)_\eta\to(\operatorname{Ker}v)_\eta\to
(\operatorname{Ker}v/\operatorname{Im}u)_\eta\to0
\]
es exacta.

"""
m.apply()


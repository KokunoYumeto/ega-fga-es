import iv3_full_translations as m
m.TRANSLATIONS={}
m.TRANSLATIONS['9.9.1']=r"""\begin{proposition}[9.9.1]
\label{IV.9.9.1}
Sean $f:X\to S$ un morfismo localmente de presentación finita, $Z$ una
parte localmente construible de $X$ tal que, para todo $s\in S$, $Z_s$ es
cerrado en $X_s$, $\Phi$ una parte finita de $\mathbf Z\cup\{\pm\infty\}$.
Entonces las partes siguientes de $X$ son localmente construibles:
\begin{enumerate}
\item[\textup{(i)}] El conjunto de los $x\in X$ tales que
$\dim_x(Z_{f(x)})$ pertenece a $\Phi$.
\item[\textup{(ii)}] El conjunto de los $x\in X$ tales que
$\operatorname{codim}_x(Z_{f(x)},X_{f(x)})$ pertenece a $\Phi$.
\item[\textup{(iii)}] El conjunto de los $x\in X$ tales que el anillo local
$\mathcal O_{X_{f(x)},x}$ es equidimensional.
\end{enumerate}
\end{proposition}

Se señalará que las propiedades (i) y (ii) se expresan también diciendo que las
funciones $x\leadsto\dim_x(Z_{f(x)})$ y
$x\leadsto\operatorname{codim}_x(Z_{f(x)},X_{f(x)})$ son
\emph{localmente construibles} en $X$ ($\mathbf 0_{\mathrm{III}},9.3.1$).

Como las cuestiones son locales sobre $X$, se puede limitar al caso en que
$S=\operatorname{Spec}(A)$ y $X=\operatorname{Spec}(B)$ son afines y en que
$f$ es un morfismo de presentación finita; existe entonces un subanillo
$A_0$ de $A$ que es una $\mathbf Z$-álgebra de tipo finito, un
$A_0$-preesquema de tipo finito $X_0$ y una parte construible $Z_0$ de $X_0$
tales que $X=X_0\otimes_{A_0}A$ y $Z=h^{-1}(Z_0)$, donde $h:X\to X_0$ es la
proyección canónica ((8.9.1) y (8.3.11)). Además, para todo $s\in S$, si
$s_0$ es la proyección de $s$ en $S_0=\operatorname{Spec}(A_0)$, se tiene
$X_s=(X_0)_{s_0}\otimes_{\mathbf{k}(s_0)}\boldsymbol{k}(s)$,
y $h_s$ es la proyección $X_s\to(X_0)_{s_0}$, se tiene
$Z_s=h_s^{-1}((Z_0)_{s_0})$. Como el morfismo $h_s$ es fielmente plano y
cuasicompacto, la hipótesis de que $Z_s$ es cerrado en $X_s$ implica que
$(Z_0)_{s_0}$ es cerrado en $(X_0)_{s_0}$ (2.3.12).

Dicho esto, la transitividad de las fibras (\textbf{I}, 3.6.4) y la prop. (4.2.7)
implican que el conjunto de las dimensiones de las componentes irreducibles de
$Z_s$ que contienen a $x$ es el mismo que el conjunto de las dimensiones de las componentes
irreducibles de $(Z_0)_{s_0}$ que contienen a $x_0=h_s(x)$. En particular, se tiene
$\dim_x(Z_s)=\dim_{x_0}((Z_0)_{s_0})$. Por otra parte, si $Z_s^{(\beta)}$ son las
componentes irreducibles de $Z_s$ que contienen a $x$ y $X_s^{(\alpha)}$ las
componentes irreducibles de $X_s$
\oldpage[IV-3]{89}
que contienen a $x$, se tiene $\operatorname{codim}_x(Z_s,X_s)=
\inf_\beta(\sup_\alpha
(\operatorname{codim}(Z_s^{(\beta)},X_s^{(\alpha)})))$,
variando $(\alpha,\beta)$ en el conjunto de los pares tales que
$x\in Z_s^{(\beta)}\subset X_s^{(\alpha)}$ ($\mathbf 0$, 14.2.6). Como los
preesquemas algebraicos irreducibles son biequidimensionales (5.2.1), se puede
escribir, en virtud de ($\mathbf 0$, 14.3.3.1),
\begin{equation}
\tag{9.9.1.1}
\label{IV.9.9.1.1}
\operatorname{codim}_x(Z_s,X_s)=
\inf_\beta\left(\sup_\alpha
\bigl(\dim(X_s^{(\alpha)})\setmin\dim(Z_s^{(\beta)})\bigr)\right)
\end{equation}
con la misma elección de los pares $(\alpha,\beta)$. Como $h_s$ es fielmente
plano y cuasicompacto, para todo par formado por una componente irreducible
$(X_0)_{s_0}^{(\lambda)}$ de $(X_0)_{s_0}$ que contiene a $x_0$ y una componente
irreducible $(Z_0)_{s_0}^{(\mu)}$ de $(Z_0)_{s_0}$ que contiene a $x_0$ y está contenida
en $(X_0)_{s_0}^{(\lambda)}$, existe un par
$(X_s^{(\alpha)},Z_s^{(\beta)})$ del tipo descrito antes y tal que
$Z_s^{(\beta)}$ domina a $(Z_0)_{s_0}^{(\mu)}$ y $X_s^{(\alpha)}$ domina a
$(X_0)_{s_0}^{(\lambda)}$ (2.3.5). La fórmula (9.9.1.1) (y la fórmula análoga
aplicada a $(X_0)_{s_0}$) muestran entonces, en virtud de (4.2.7), que se tiene
\[
\operatorname{codim}_x(Z_s,X_s)=
\operatorname{codim}_{x_0}((Z_0)_{s_0},(X_0)_{s_0}).
\]

Se ve así que, si $E$ (resp. $E_0$) es el conjunto de los $x\in X$ (resp. de los
$x_0\in X_0$) que satisfacen una de las condiciones (i), (ii), (iii) del enunciado
(resp. la misma condición), se tiene $E=h^{-1}(E_0)$, y en virtud de (1.8.2), se
ve que se puede limitar al caso en que $A$ es \emph{noetheriano}, por tanto también $B$.
Teniendo en cuenta ($\mathbf 0_{\mathrm{III}},9.2.3$), así como (9.9.1.1), se
reduce a ver que, para todo $x\in X$, existe una vecindad $V$ de $x$ en
$\overline{\{x\}}$ tal que, para todo $x'\in V$, el conjunto de las dimensiones de las
componentes irreducibles de $X_{f(x')}$ (resp. $Z_{f(x')}$) que contienen a $x'$ es
\emph{el mismo}, y además que lo mismo ocurre con el conjunto de los pares
$(\dim(Z_{f(x')}^{(\beta)}),\dim(X_{f(x')}^{(\alpha)}))$
para los pares formados por una componente irreducible $X_{f(x')}^{(\alpha)}$
de $X_{f(x')}$ y una componente irreducible $Z_{f(x')}^{(\beta)}$ de
$Z_{f(x')}$ contenida en $X_{f(x')}^{(\alpha)}$ y que contiene a $x'$. Se puede
evidentemente, para ello, reemplazar $S$ por el subpreesquema reducido $S'$ de $S$
que tiene a $\overline{\{f(x)\}}$ como espacio subyacente, y $X$ por
$X'=f^{-1}(S')$, pues las fibras de $X$ y $X'$ en los puntos de $S'$ son las mismas.
Dicho de otro modo, se puede limitar al caso en que $S$ es \emph{íntegro} y en que
$\eta=f(x)$ es su punto genérico.

Por hipótesis, $Z_\eta$ es cerrado en $X_\eta$; como $Z$ es construible,
se deduce de (8.3.11), aplicado según el método de (8.1.2, \emph{a)}), que se
puede, reemplazando si es necesario $S$ por una vecindad abierta de $\eta$, suponer
que $Z$ es \emph{cerrado} en $X$. Sean $X_i$ (resp. $Z_j$) las componentes
irreducibles de $X$ (resp. $Z$) que contienen a $x$; en virtud de
($\mathbf 0_{\mathrm I},2.1.8$), los $X_i\cap X_\eta$ (resp.
$Z_j\cap X_\eta$) son las componentes irreducibles de $X_\eta$ (resp.
$Z_\eta$) que contienen a $x$; en virtud de (9.5.1), se puede suponer además,
restringiendo si es necesario $S$ a una vecindad de $\eta$, que los $X_i$ (resp.
$Z_j$) son exactamente las componentes irreducibles de $X$ (resp. $Z$)
que encuentran $\overline{\{x\}}$ y que los
$(X_i)_s\cap\overline{\{x\}}$ y $(Z_j)_s\cap\overline{\{x\}}$ son no vacíos
para todo $s\in S$. Dicho esto, se deduce también de (9.7.1) que se puede
suponer, restringiendo $S$, que los pares $(i,j)$ tales que
$(Z_j)_s\subset(X_i)_s$ son los mismos para todo $s\in S$. La conclusión
se deduce entonces de (9.5.6): para todo $s$ suficientemente próximo a $\eta$, todas las
componentes irreducibles de $(X_i)_s$ (resp. $(Z_j)_s$) tienen una misma dimensión
igual a la de $(X_i)_\eta$ (resp. $(Z_j)_\eta$). Además, si $(i,j)$ es un
par tal que $Z_j\not\subset X_i$, $(X_i)_\eta$ no contiene el
\oldpage[IV-3]{90}
punto genérico de $(Z_j)_\eta$, por lo que
$\dim((X_i\cap Z_j)_\eta)<\dim((Z_j)_\eta)$; por consiguiente, la dimensión común
de las componentes irreducibles de $(X_i)_s\cap(Z_j)_s$ es, para todo $s\in S$,
estrictamente inferior a la dimensión común de las componentes irreducibles de
$(Z_j)_s$, lo que prueba que ninguna de las componentes irreducibles de $(Z_j)_s$
está contenida en una componente irreducible de $(X_i)_s$ para $s\in S$.
C.Q.F.D.

"""
m.TRANSLATIONS['9.9.6']=r"""\begin{proposition}[9.9.6]
\label{IV.9.9.6}
Sean $f:X\to S$ un morfismo localmente de presentación finita,
$\mathcal L_\bullet$ un complejo formado por $\mathcal O_X$-Módulos
cuasicoherentes de presentación finita; para todo $s\in S$, sea
$(\mathcal L_\bullet)_s$ el complejo
$\mathcal L_\bullet\otimes_{\mathcal O_S}\boldsymbol{k}(s)$ de
$\mathcal O_{X_s}$-Módulos coherentes de tipo finito. Entonces, para un entero $n$
dado, el conjunto de los $x\in X$ tales que
$(\mathcal H_n((\mathcal L_\bullet)_{f(x)}))_x=0$ es localmente construible
en $X$.
\end{proposition}

Se puede limitar al caso en que $\mathcal L_i=0$ salvo para $i=0$, 1 o 2, y en que
$n=1$. Además, como la cuestión es local sobre $X$, se puede limitar al caso en que
$S=\operatorname{Spec}(A)$ y $X=\operatorname{Spec}(B)$ son afines, siendo $B$
una $A$-álgebra de presentación finita. Existe entonces un subanillo
noetheriano $A_0$ de $A$, un $A_0$-preesquema de tipo finito $X_0$ y un complejo
$\mathcal L_\bullet^{(0)}$ de $\mathcal O_{X_0}$-Módulos coherentes, nulos salvo en
dimensiones 0, 1 y 2 y tales que
$X=X_0\otimes_{A_0}A$ y
$\mathcal L_\bullet=\mathcal L_\bullet^{(0)}\otimes_{A_0}A$. Para todo
$s\in S$, si $s_0$ es la proyección de $s$ en
$S_0=\operatorname{Spec}(A_0)$, se tiene
$X_s=(X_0)_{s_0}\otimes_{\mathbf{k}(s_0)}\boldsymbol{k}(s)$, y el morfismo proyección
$X_s\to(X_0)_{s_0}$ es fielmente plano; se concluye de ello que se tiene
$\mathcal H_n((\mathcal L_\bullet)_s)=
\mathcal H_n((\mathcal L_\bullet^{(0)})_{s_0})
\otimes_{\mathbf{k}(s_0)}\boldsymbol{k}(s)$,
y por consiguiente, si $E$ (resp. $E_0$) es el conjunto de los $x\in X$ (resp.
$x_0\in X_0$) tales que
$(\mathcal H_n((\mathcal L_\bullet)_{f(x)}))_x=0$
(resp.
$(\mathcal H_n((\mathcal L_\bullet^{(0)})_{f_0(x_0)}))_{x_0}=0$),
se tiene $E=h^{-1}(E_0)$, donde $h:X\to X_0$ es la proyección canónica. En virtud
de (1.8.2), se puede, por tanto, limitar al caso en que $A$ es \emph{noetheriano}; se
trata de ver ($\mathbf 0_{\mathrm{III}},9.2.3$) que, si $x\in X$ es tal que
$(\mathcal H_n((\mathcal L_\bullet)_{f(x)}))_x=0$ (resp. $\neq0$), existe una
vecindad abierta $V$ de $x$ en $\overline{\{x\}}$ tal que, para todo
$x'\in V$, se tiene
$(\mathcal H_n((\mathcal L_\bullet)_{f(x')}))_{x'}=0$ (resp. $\neq0$).
Reemplazando $S$ por el subpreesquema reducido de $S$ que tiene a
$\overline{\{f(x)\}}$ como espacio subyacente, se puede suponer que $S$ es
íntegro y que $f(x)=\eta$ es su punto genérico. Entonces, restringiendo $S$
a una vecindad abierta de $\eta$, se puede suponer que, para todo $s\in S$, se tiene
$(\mathcal H_n(\mathcal L_\bullet))_s=
\mathcal H_n((\mathcal L_\bullet)_s)$ (9.4.3), y por consiguiente, si $Z$ es el
soporte de $\mathcal H_n(\mathcal L_\bullet)$, el soporte de
$\mathcal H_n((\mathcal L_\bullet)_s)$ es $Z_s=Z\cap X_s$
(\textbf{I}, 9.1.13.1). La hipótesis es que
$Z_\eta\cap\overline{\{x\}}=\varnothing$ (resp. $\neq\varnothing$). Como
$Z\cap\overline{\{x\}}$ es cerrado en el espacio noetheriano $X$, se concluye de
(9.5.1) que existe una vecindad $U$ de $\eta$ en $S$ tal que, para todo
$s\in U$, se tiene $Z_s\cap\overline{\{x\}}=\varnothing$ (resp.
$\neq\varnothing$). El conjunto $V=f^{-1}(U)\cap\overline{\{x\}}$ responde, pues, a
la cuestión.

"""
m.apply()


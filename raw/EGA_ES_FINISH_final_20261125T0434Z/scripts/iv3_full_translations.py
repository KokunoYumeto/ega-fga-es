"""Complete reviewed translations for IV3 units with inherited abridgments."""
import csv,re,json
from iv3_manual import whole,source_unit
from iv3_core import spans
from corpus import RESULT,write_tsv
from tex_tools import prose_segments
TRANSLATIONS={}
TRANSLATIONS['11.2.6.1']=r"""\begin{corollary}[11.2.6.1]
\label{IV.11.2.6.1}
Sean $A_0$ un anillo, $(A_\lambda)_{\lambda\in L}$ un sistema inductivo
filtrante de $A_0$-álgebras, $B_0$ una $A_0$-álgebra de presentación finita,
$M_0$ un $B_0$-módulo de presentación finita. Se pone
$B_\lambda=B_0\otimes_{A_0}A_\lambda$,
$M_\lambda=M_0\otimes_{A_0}A_\lambda=M_0\otimes_{B_0}B_\lambda$,
$A=\varinjlim A_\lambda$, $B=\varinjlim B_\lambda=B_0\otimes_{A_0}A$,
$M=\varinjlim M_\lambda=M_0\otimes_{A_0}A=M_0\otimes_{B_0}B$.
\begin{enumerate}[label=\emph{(\roman*)}]
\item Sea $\mathfrak p$ un ideal primo de $B$, y para todo $\lambda$,
sea $\mathfrak p_\lambda$ su imagen inversa en $B_\lambda$. Para que
$M_{\mathfrak p}$ sea un $A$-módulo plano, es necesario y suficiente que exista
$\lambda$ tal que $(M_\lambda)_{\mathfrak p_\lambda}$ sea un
$A_\lambda$-módulo plano.
\item Para que $M$ sea un $A$-módulo plano, es necesario y suficiente que exista
$\lambda$ tal que $M_\lambda$ sea un $A_\lambda$-módulo plano.
\end{enumerate}
\end{corollary}

Solo se debe demostrar que las condiciones son necesarias (2.1.4).
Procederemos en varias etapas.

\medskip
\noindent I) \emph{Reducción al caso en que los $A_\lambda$ son
noetherianos.} En virtud de (8.9.1), existen un subanillo $A'_0$ de $A_0$,
que es una $\mathbf Z$-álgebra de tipo finito, una $A'_0$-álgebra de tipo finito
$B'_0$ y un $B'_0$-módulo de tipo finito $M'_0$ tales que se tiene
$B_0=B'_0\otimes_{A'_0}A_0$ y $M_0=M'_0\otimes_{A'_0}A_0$; como se tiene
$B_\lambda=B'_0\otimes_{A'_0}A_\lambda$ y
$M_\lambda=M'_0\otimes_{A'_0}A_\lambda$, se puede reemplazar $A_0$, $B_0$,
$M_0$ por $A'_0$, $B'_0$, $M'_0$ en el enunciado de (11.2.6.1), considerando
los $A_\lambda$ como $A'_0$-álgebras; se puede, por tanto, suponer ya que
$A_0$ es \emph{noetheriano}. Sea $H$ el conjunto de los pares
$(\lambda,C_\lambda)$, donde $C_\lambda$ es una sub-$A_0$-álgebra \emph{de
tipo finito} de $A_\lambda$; ordenemos $H$ poniendo
$(\lambda,C_\lambda)\leq(\mu,D_\mu)$ si $\lambda\leq\mu$ y si
el homomorfismo $\varphi_{\mu\lambda}:A_\lambda\to A_\mu$ es tal que
$\varphi_{\mu\lambda}(C_\lambda)\subset D_\mu$; para este orden $H$ es
filtrante creciente, pues si $(\lambda,C_\lambda)$ y $(\mu,D_\mu)$ son dos
elementos cualesquiera de $H$, se los mayorará por un $(\nu,E_\nu)$ tomando
$\nu\geq\lambda$, $\nu\geq\mu$ en $L$, y luego $E_\nu$ igual a la
sub-$A_0$-álgebra de $A_\nu$ generada por
$\varphi_{\nu\lambda}(C_\lambda)$ y $\varphi_{\nu\mu}(D_\mu)$. Para un
elemento $\xi=(\lambda,C_\lambda)$ de $H$, se pondrá $A_\xi=C_\lambda$, y
para $\xi\leq\eta=(\mu,D_\mu)$ (por tanto $\lambda\leq\mu$ y
$\varphi_{\mu\lambda}(C_\lambda)\subset D_\mu$),
$\varphi_{\eta\xi}:A_\xi\to A_\eta$ será la restricción a $C_\lambda$ de
$\varphi_{\mu\lambda}$, considerado como homomorfismo en $D_\mu$; está
claro que así se obtiene un sistema inductivo filtrante de $A_0$-álgebras.
Se pone $B_\xi=B_0\otimes_{A_0}A_\xi$,
$M_\xi=M_0\otimes_{A_0}A_\xi$; esta vez los $A_\xi$ son
\emph{noetherianos}; además, la fórmula del doble límite inductivo (Bourbaki,
\emph{Alg.}, cap.~II, 3.ª ed., \S~6, n.º~4, prop.~7) prueba que
se tiene también
$\varinjlim_HA_\xi=A$, $\varinjlim_HB_\xi=B$,
$\varinjlim_HM_\xi=M$. Supongamos (11.2.6.1) demostrado para el sistema inductivo
$(A_\xi)_{\xi\in H}$; sea $\mathfrak p$ un ideal primo de $B$,
tal que $M_{\mathfrak p}$ sea un $A$-módulo plano; existe entonces
$\xi\in H$ tal que, si $\mathfrak p_\xi$ es la imagen
\oldpage[IV-3]{125}
inversa de
$\mathfrak p$ en $B_\xi$, $(M_\xi)_{\mathfrak p_\xi}$ sea un
$A_\xi$-módulo plano. Sea $\xi=(\lambda,C_\lambda)$, de modo que
la inyección $A_\xi=C_\lambda\to A_\lambda$ da un homomorfismo
$B_\xi=B_0\otimes_{A_0}C_\lambda\to B_\lambda=B_0\otimes_{A_0}A_\lambda$,
y si $\mathfrak p_\lambda$ es la imagen inversa de $\mathfrak p$ en
$B_\lambda$, $\mathfrak p_\xi$ es la imagen inversa de
$\mathfrak p_\lambda$ en $B_\xi$; se tiene, por consiguiente,
$(M_\lambda)_{\mathfrak p_\lambda}
=(M_\xi\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda}
=((M_\xi)_{\mathfrak p_\xi}\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda}$,
por tanto $(M_\lambda)_{\mathfrak p_\lambda}$ es un $A_\lambda$-módulo plano
($\mathbf 0_{\mathrm I}$, 6.2.1 y 6.3.2). Se trata del mismo modo el caso (ii) del
enunciado. Podemos, por tanto, en lo sucesivo suponer los $A_\lambda$
\emph{noetherianos} para $\lambda\in L$ (aunque no necesariamente el propio $A$).

\medskip
\noindent II) \emph{Reducción del enunciado global} (ii) \emph{al enunciado
puntual} (i). Supongamos que $\mathcal F$ es $f$-plano. Para todo $\lambda$,
sea $U_\lambda$ el conjunto de los $x_\lambda\in X_\lambda$ tales que
$\mathcal F_\lambda$ sea $f_\lambda$-plano en el punto $x_\lambda$; se sabe
que $U_\lambda$ es \emph{abierto} en $X_\lambda$ puesto que $S_\lambda$ es
noetheriano y $f_\lambda$ de tipo finito (11.1.1); sea
$V_\lambda=v_\lambda^{-1}(U_\lambda)$ su imagen inversa en $X$. Como,
por hipótesis, para todo $x\in X$, hay un $\lambda$ tal que
$\mathcal F_\lambda$ sea $f_\lambda$-plano en el punto $x_\lambda$, proyección
de $x$ en $X_\lambda$, esto significa que $x\in V_\lambda$ para un
$\lambda$; dicho de otro modo, $X$ es unión de los $V_\lambda$. Por otra parte
(2.1.4), para $\lambda\leq\mu$, se tiene $V_\lambda\subset V_\mu$, por tanto, como
$X$ es cuasicompacto, existe un índice $\mu$ tal que $X=V_\mu$. Como
los $X_\lambda$ son cuasicompactos, resulta de (8.3.4) que existe un
índice $\nu\geq\mu$ tal que $v_{\mu\nu}^{-1}(U_\mu)=X_\nu$; pero, por
(2.1.4), esto implica que $\mathcal F_\nu$ es $f_\nu$-plano.

\medskip
\noindent III) \emph{Fin de la demostración.} Queda por probar
(i) suponiendo $S_0$ afín y noetheriano; si $y_0$ es la proyección de
$x$ en $S_0$, se puede además, en virtud de (2.1.4) y de
($\mathbf I$, 3.6.5), reemplazar $S_0$ por
$\operatorname{Spec}(\mathcal O_{y_0})$, dicho de otro modo se puede limitar al
caso en que $A_0$ es un anillo \emph{local} noetheriano, de ideal maximal
$\mathfrak m_0=\mathfrak j_{y_0}$; por definición, $\mathfrak m_0$ es
la imagen inversa del ideal primo $\mathfrak p=\mathfrak j_x$ de $B$,
y se supone que $M_{\mathfrak p}$ es un $A$-módulo plano; se tiene, por tanto, en
particular $\operatorname{Tor}_1^A(A/\mathfrak m_0A,M_{\mathfrak p})=0$,
lo que también se escribe, puesto que los $\operatorname{Tor}_i^A(A/\mathfrak m_0A,M)$
son $B$-módulos y que $B_{\mathfrak p}$ es plano sobre $B$,
$(\operatorname{Tor}_1^A(A/\mathfrak m_0A,M))_{\mathfrak p}=0$.
Observemos ahora que $\operatorname{Tor}_1^{A_0}(A_0/\mathfrak m_0,M_0)$
es un $B_0$-\emph{módulo de tipo finito}, pues se puede definirlo tomando
una resolución de $A_0/\mathfrak m_0$ por $A_0$-módulos libres
\emph{de tipo finito} (siendo $A_0$ noetheriano) y tensorizando por $M_0$, lo
que da $B_0$-módulos de tipo finito; como $B_0$ es noetheriano,
la homología del complejo así obtenido está formada efectivamente por $B_0$-módulos de
tipo finito. Sea $(t_i^0)_{1\leq i\leq m}$ un sistema de generadores del
$B_0$-módulo $\operatorname{Tor}_1^{A_0}(A_0/\mathfrak m_0,M_0)$ y sea
$t_i$ la imagen canónica (11.2.1.1) de $t_i^0$ en
$\operatorname{Tor}_1^A(A/\mathfrak m_0A,M)$. La hipótesis implica que
existe un $h\in B\setmin\mathfrak p$ tal que $ht_i=0$ para $1\leq i\leq m$. Ahora bien,
se tiene (11.2.2.1)
$\operatorname{Tor}_1^A(A/\mathfrak m_0A,M)=
\varinjlim\operatorname{Tor}_1^{A_\lambda}
(A_\lambda/\mathfrak m_0A_\lambda,M_\lambda)$;
existe, por tanto, un $\lambda$ tal que, si los $t_i^\lambda$ son las imágenes
de los $t_i^0$ en
$\operatorname{Tor}_1^{A_\lambda}(A_\lambda/\mathfrak m_0A_\lambda,
M_\lambda)$, existe $h_\lambda\in B_\lambda$ de imagen $h$, tal que
$h_\lambda t_i^\lambda=0$ para $1\leq i\leq m$. Sea
$\mathfrak p_\lambda=\mathfrak j_{x_\lambda}$ el ideal primo de
$B_\lambda$ imagen inversa de $\mathfrak p$; se tiene
$h_\lambda\in B_\lambda\setmin\mathfrak p_\lambda$, por tanto las imágenes canónicas
de los $t_i^0$ en
$(\operatorname{Tor}_1^{A_\lambda}(A_\lambda/\mathfrak m_0A_\lambda,
M_\lambda))_{\mathfrak p_\lambda}$ son nulas y, por consiguiente,
el homomorfismo
$\operatorname{Tor}_1^{A_0}(A_0/\mathfrak m_0,M_0)\to
(\operatorname{Tor}_1^{A_\lambda}(A_\lambda/\mathfrak m_0A_\lambda,
M_\lambda))_{\mathfrak p_\lambda}$ es nulo. Se cumplen, por tanto, las condiciones del
lema (11.2.5) (siendo $A_0/\mathfrak m_0$ un cuerpo), y
$(M_\lambda)_{\mathfrak p_\lambda}$ es un $A_\lambda$-módulo plano, lo que
termina la demostración del teorema.


"""
TRANSLATIONS['11.2.5']=r"""\begin{lemma}[11.2.5]
\label{IV.11.2.5}
Sean $A$ un anillo, $\mathfrak J$ un ideal de $A$, $B$ una $A$-álgebra,
$M$ un $B$-módulo, $A\to A'$ un homomorfismo de anillos. Se pone
$\mathfrak J'=\mathfrak JA'$, $B'=B\otimes_AA'$,
$M'=M\otimes_AA'=M\otimes_BB'$. Sea $\mathfrak p'$ un ideal primo de
$B'$ que contiene $\mathfrak JB'$. Se supone verificada una de las hipótesis
siguientes:
\begin{enumerate}[label=\textit{\alph*)}]
\item $\mathfrak J$ es nilpotente.
\item $A'$ es noetheriano, $B'$ es una $A'$-álgebra de tipo finito, $M'$ un
$B'$-módulo de tipo finito.
\end{enumerate}
En estas condiciones, supongamos verificadas las dos propiedades siguientes:
\begin{enumerate}[label=\emph{(\roman*)}]
\item $M\otimes_A(A/\mathfrak J)$ es un $(A/\mathfrak J)$-módulo plano.
\item El homomorfismo canónico compuesto
\[
\operatorname{Tor}_1^A(M,A/\mathfrak J)\xrightarrow{\psi_1}
\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J')\xrightarrow{\theta}
(\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J'))_{\mathfrak p'}
\]
(donde $\psi_1$ es el homomorfismo (11.2.1.1) y $\theta$ el homomorfismo
canónico de un $B'$-módulo en su localizado en $\mathfrak p'$) es nulo.
\end{enumerate}
Entonces $M'_{\mathfrak p'}$ es un $A'$-módulo plano.
\end{lemma}

Observemos que bajo la hipótesis \emph{b)} $M'_{\mathfrak p'}$ es un
$B'_{\mathfrak p'}$-módulo de tipo finito, $B'_{\mathfrak p'}$ una
$A'$-álgebra noetheriana, y que $\mathfrak J'B'_{\mathfrak p'}$ está
contenido en el radical $\mathfrak p'B'_{\mathfrak p'}$ de
$B'_{\mathfrak p'}$; bajo la hipótesis \emph{a)}, $\mathfrak J'$ es nilpotente;
se va, por tanto, a poder aplicar el criterio de planitud
($\mathbf 0_{\mathrm{III}}$, 10.2.1) o ($\mathbf 0_{\mathrm{III}}$, 10.2.2)
según que \emph{a)} o \emph{b)} esté verificada. En primer lugar, se tiene
$M'_{\mathfrak p'}\otimes_{A'}(A'/\mathfrak J')
=(M'\otimes_{A'}(A'/\mathfrak J'))_{\mathfrak p'}
=((M\otimes_A(A/\mathfrak J))\otimes_{A/\mathfrak J}
(A'/\mathfrak J'))_{\mathfrak p'}$;
la hipótesis (i) implica, por tanto, que
$M'_{\mathfrak p'}\otimes_{A'}(A'/\mathfrak J')$ es un
$(A'/\mathfrak J')$-módulo plano, habida cuenta de
($\mathbf 0_{\mathrm I}$, 6.2.1 y 6.3.2). Queda, pues, por ver que
$\operatorname{Tor}_1^{A'}(M'_{\mathfrak p'},A'/\mathfrak J')=0$; ahora bien, este
$B'_{\mathfrak p'}$-módulo es igual a
$(\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J'))_{\mathfrak p'}$ en virtud
de la planitud de $B'_{\mathfrak p'}$ sobre $B'$. Pero, en virtud de
la hipótesis (ii), el homomorfismo compuesto
$\theta\circ\varphi_1:\operatorname{Tor}_1^A(M,A/\mathfrak J)\otimes_AA'
\to(\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J'))_{\mathfrak p'}$ es
nulo; por otra parte, (11.2.4) aplicado a $C=A/\mathfrak J$ y $N=C$ muestra
(habida cuenta de la hipótesis (i)) que $\varphi_1$ es \emph{sobreyectivo} (pues
$A'/\mathfrak J'=C\otimes_AA'$); por tanto, el homomorfismo $\theta$ es
\emph{nulo} y, como la imagen por $\theta$ de
$\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J')$ genera el
$B'_{\mathfrak p'}$-módulo
$(\operatorname{Tor}_1^{A'}(M',A'/\mathfrak J'))_{\mathfrak p'}$, este
último es nulo. C.Q.F.D.


"""
TRANSLATIONS['11.2.9.9']=r"""\begin{env}[11.2.9.9]
\label{IV.11.2.9.9}
\emph{Para $\lambda$ suficientemente grande, el homomorfismo canónico
$v_\lambda:N_\lambda\otimes_{A_\lambda}A\to N$ es biyectivo.}
\end{env}

Como los $C_\lambda$ son noetherianos y $N_\lambda$ un $C_\lambda$-módulo
de tipo finito, los $C$-módulos $N_\lambda\otimes_{A_\lambda}A$ son de
presentación finita y forman un sistema inductivo filtrante cuyo límite
inductivo se identifica canónicamente con $N$ en virtud del hecho de que $\varinjlim$
conmuta con los productos tensoriales. Además, los homomorfismos de transición
$v_{\mu\lambda}:N_\lambda\otimes_{A_\lambda}A
\to N_\mu\otimes_{A_\mu}A$
\oldpage[IV-3]{132}
para $\lambda\leq\mu$ y los homomorfismos $v_\lambda$ son \emph{sobreyectivos}.
Para un $\lambda$ fijo, consideremos los sub-$C$-módulos
$\operatorname{Ker}(v_{\mu\lambda})=N'_\mu$ de $N_\lambda\otimes_{A_\lambda}A$; por
definición del límite inductivo, forman una familia filtrante creciente
de sub-$C$-módulos de $\operatorname{Ker}(v_\lambda)$ cuya unión es
$\operatorname{Ker}(v_\lambda)$; pero se ha visto en V) que $N$ es un $C$-módulo de
presentación finita, por tanto (Bourbaki, \emph{Alg. comm.}, cap.~I, \S~2,
n.º~8, lema 9) $\operatorname{Ker}(v_\lambda)$ es un $C$-módulo \emph{de tipo finito}; existe,
por consiguiente, un índice $\mu\geq\lambda$ tal que
$N'_\mu=\operatorname{Ker}(v_\lambda)$, lo que significa (dado que $v_{\mu\lambda}$ es
sobreyectivo) que $v_\mu$ es \emph{inyectivo}; como es sobreyectivo, esto
prueba (11.2.9.9).

Reemplazando, si es preciso, $A_0$ y $M_0$ por $A_\lambda$ y $M_\lambda$ para
$\lambda$ suficientemente grande, se puede, por tanto, suponer que el homomorfismo canónico
$v_\lambda$ es biyectivo para \emph{todo} $\lambda$. Pongamos entonces
$P_\lambda=N_0\otimes_{C_0}C_\lambda=N_0\otimes_{A_0}A_\lambda$, de modo que
$N=\varinjlim P_\lambda$. Como $C_0$ es una $A_0$-álgebra de presentación
finita y $P_0$ un $C_0$-módulo de presentación finita, se puede aplicar a
$C$ y $N$ el resultado de (11.2.6.1) y se ve, por tanto, que existe un índice
$\lambda$ tal que, para $\mu\geq\lambda$, $P_\mu$ sea un $A_\mu$-módulo
\emph{plano}. Ahora bien, para $\mu\geq\lambda$, se tiene un diagrama conmutativo
\[
\xymatrix{
P_\mu \ar[r] \ar[d]_{w_\mu} & N \ar@{=}[d] \\
N_\mu \ar[r] & N
}
\]
donde resulta de las definiciones que $w_\mu$ es \emph{sobreyectivo}. Como, en
virtud de III), los homomorfismos $A_\mu\to A$ son inyectivos y $P_\mu$
es un $A_\mu$-módulo \emph{plano}, el homomorfismo canónico
$P_\mu\to N=P_\mu\otimes_{A_\mu}A$ es \emph{inyectivo}; se concluye, por tanto, del
diagrama conmutativo precedente que $w_\mu$ es también \emph{inyectivo}, por tanto biyectivo,
y, por consiguiente, $N_\mu$ es un $A_\mu$-módulo \emph{plano} para $\mu\geq\lambda$, lo que
termina de probar (11.2.9).
\end{proof}


"""
TRANSLATIONS['11.3.17']=r"""\begin{corollary}[11.3.17]
\label{IV.11.3.17}
Sean $A$ un anillo, $B$ una $A$-álgebra, $C$ una $B$-álgebra de presentación
finita y que sea un $B$-módulo fielmente plano. Entonces, si $C$ es una
$A$-álgebra de tipo finito \textup{(resp. \emph{de presentación finita})}, $B$ es una
$A$-álgebra de tipo finito \textup{(resp. \emph{de presentación finita})}.
\end{corollary}

\begin{proof}
Supongamos primero que $g\circ f$ es de tipo finito. Sea $(B_\lambda)$ la
familia filtrante creciente de las sub-$A$-álgebras de tipo finito de $B$; en
virtud de (8.8.2), existe un índice $\alpha$ tal que
$C=C_\alpha\otimes_{B_\alpha}B$, donde $C_\alpha$ es una
$B_\alpha$-álgebra de presentación finita; además (8.10.5 y 11.2.6), se puede
suponer que $C_\alpha$ es un $B_\alpha$-módulo fielmente plano. Para
$\lambda\geq\alpha$, se tiene, por tanto,
$C=C_\lambda\otimes_{B_\lambda}B$, donde $C_\lambda$ es un
$B_\lambda$-módulo fielmente plano; como la aplicación $B_\lambda\to B$ es
inyectiva, se deduce de ello que lo mismo ocurre con $C_\lambda\to C$. Además,
como $C=\varinjlim C_\lambda$, todo elemento de $C$ pertenece a un
$C_\lambda$, y, por consiguiente, existe $\lambda$ tal que la aplicación
$C_\lambda\to C$
\oldpage[IV-3]{143}
sea biyectiva, puesto que $C$ es una $A$-álgebra de tipo finito. Pero entonces
la aplicación $B_\lambda\to B$ es biyectiva por planitud fiel, por tanto
$B=B_\lambda$ es una $A$-álgebra de tipo finito.

Supongamos ahora que $g\circ f$ es de presentación finita, siendo, pues, $C$
una $A$-álgebra de presentación finita. Según la primera parte del
razonamiento, se tiene
$B=A[T_1,\ldots,T_n]/\mathfrak J$
para un ideal $\mathfrak J$; sea
$(\mathfrak J_\lambda)$ la familia filtrante de los ideales de tipo
finito de $A[T_1,\ldots,T_n]$ contenidos en $\mathfrak J$, de modo
que $\mathfrak J=\varinjlim\mathfrak J_\lambda$ y
$B=\varinjlim B_\lambda$, con
$B_\lambda=A[T_1,\ldots,T_n]/\mathfrak J_\lambda$. Aplicando,
como antes, (8.8.2), (8.10.5) y (11.2.6), se tiene
$C=C_\alpha\otimes_{B_\alpha}B$, donde $C_\alpha$ es una
$B_\alpha$-álgebra de presentación finita y un $B_\alpha$-módulo fielmente
plano; se pondrá de nuevo $C_\lambda=C_\alpha\otimes_{B_\alpha}B_\lambda$ para
$\lambda\geq\alpha$, de modo que
$C_\lambda=C_\alpha/(C_\alpha\otimes_{B_\alpha}
(\mathfrak J_\lambda/\mathfrak J_\alpha))$
por planitud, y de la misma manera
$C=C_\alpha/(C_\alpha\otimes_{B_\alpha}
(\mathfrak J/\mathfrak J_\alpha))$.
Como, por hipótesis, $C$ es una $A$-álgebra de presentación finita, así como
$C_\alpha$, $C_\alpha\otimes_{B_\alpha}
(\mathfrak J/\mathfrak J_\alpha)$ es un ideal de
tipo finito de $C_\alpha$ (1.4.4), y los
$C_\alpha\otimes_{B_\alpha}
(\mathfrak J_\lambda/\mathfrak J_\alpha)$
se identifican con ideales de tipo finito de $C_\alpha$ cuya
unión es $C_\alpha\otimes_{B_\alpha}
(\mathfrak J/\mathfrak J_\alpha)$. Existe,
por consiguiente, un $\lambda\geq\alpha$ tal que
$C_\alpha\otimes_{B_\alpha}
(\mathfrak J/\mathfrak J_\alpha)
=C_\alpha\otimes_{B_\alpha}
(\mathfrak J_\lambda/\mathfrak J_\alpha)$,
de donde $\mathfrak J=\mathfrak J_\lambda$ por planitud
fiel, lo que prueba que $B$ es una $A$-álgebra de presentación finita.
\end{proof}

\subsection{Descenso de la planitud por morfismos cualesquiera: caso de un preesquema base artiniano.}
\label{subsection:IV.11.4}


"""

TRANSLATIONS['14.3.10']=r"""\begin{lemma}[14.3.10]
\label{IV.14.3.10}
Sean $A$ un anillo de valoración (no necesariamente discreta), $k$ su cuerpo
residual, $K$ su cuerpo de fracciones, y pongamos $S=\operatorname{Spec}(A)$. Sean
$X$ un preesquema irreducible, $f:X\to S$ un morfismo dominante de tipo finito; sea
$X_0=X\otimes_A k$ \textup{(resp.} $X_1=X\otimes_A K$\textup{)} la fibra de $f$ en el punto cerrado
\textup{(resp.} en el punto genérico\textup{)} de $S$. Entonces, si $X_0\ne\varnothing$, se tiene
$\dim(X_0)=\dim(X_1)$.
\end{lemma}

Se puede limitar al caso en que $X$ es afín, reemplazando, si es preciso, $X$ por un
abierto afín que contenga un punto genérico de una componente irreducible de $X_0$,
de dimensión maximal, y utilizando (4.1.1.3). Sea $n=\dim(X_0)\geq 0$; resulta
de (13.3.1.1) que existe una vecindad $U$ de $X_0$ en $X$ y un $S$-morfismo
cuasifinito
$g:U\to S[T_1,\ldots,T_n]=Z$
tal que el morfismo restricción
$g_0:U_0=U\cap X_0\to Z_0=\operatorname{Spec}(k[T_1,\ldots,T_n])$ sea finito y
\emph{sobreyectivo}. Por cambio de base $\operatorname{Spec}(K)\to S$ y restricción
al abierto $U_1=U\cap X_1$ de $X_1$, se deduce de $g$ un morfismo cuasifinito
$g_1:U_1\to Z_1=\operatorname{Spec}(K[T_1,\ldots,T_n])$. Como $U_1$ es denso en
$X_1$, se tiene $\dim(U_1)=\dim(X_1)$ (4.1.1.3); la proposición quedará establecida, en virtud
de (4.1.2), si probamos que el morfismo $g_1$ es \emph{dominante}. Supongamos
lo contrario; existiría entonces un polinomio $F_1\ne 0$ en
$K[T_1,\ldots,T_n]$ tal que $g_1(U_1)\subset V(F_1)$. Si $\omega$ es una valoración
sobre $K$ asociada a $A$, y si $(a_\alpha)$ es la familia de los coeficientes de $F_1$,
se puede, tras multiplicar $F_1$ por un elemento $\ne 0$ de $K$, suponer que
se tiene $\inf_\alpha(\omega(a_\alpha))=0$; dicho de otro modo, $F_1$ proviene de un
polinomio $F\in A[T_1,\ldots,T_n]$ (con el que se identifica) tal que la imagen $F_0$
de $F$ en $k[T_1,\ldots,T_n]$ sea \emph{no nula}. Consideremos entonces \emph{en} $Z$
el conjunto cerrado $V(F)$; se tiene $V(F)\cap Z_1=V(F_1)$, y como $U_1$ es denso
en $U$ (puesto que contiene el punto genérico de $X$), $g(U)\subset V(F)$; en
parti%
\oldpage[IV-3]{208}
cular, se tendría $g_0(U_0)\subset V(F)\cap Z_0=V(F_0)$; pero, puesto que
$F_0\ne 0$, $V(F_0)$ es un subconjunto cerrado de $Z_0$ \emph{distinto de $Z_0$} y
se llega a una contradicción. C.Q.F.D.


"""

def apply():
 tp=RESULT/'records/TRADUCCION_iv3_supplements.tsv'
 cp=RESULT/'records/CHECK_EVENTS_iv3_supplements.tsv'
 tr=list(csv.DictReader(tp.open(),delimiter='\t')) if tp.exists() else []
 cr=list(csv.DictReader(cp.open(),delimiter='\t')) if cp.exists() else []
 for n,t in TRANSLATIONS.items():
  f=source_unit(n)
  fs=[re.sub(r'-fr(?=\})','',s.text) for s in spans(f)]
  ss=[s.text for s in spans(t)]
  assert fs==ss,(n,'Math differs',len(fs),len(ss),next(((i,a,b) for i,(a,b) in enumerate(zip(fs,ss)) if a!=b),None))
  whole(n,t)
  if not any(x['range']==n for x in tr):
   words=len(re.findall(r"\b[^\W\d_]+(?:['’][^\W\d_]+)*\b",''.join(s[2] for s in prose_segments(f))))
   tr.append({'file':f'tree/worktree/es/PORTED_20261109/IV3/sections/ega4-{n.split(".")[0]}.tex','french_source':f'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/ega4-{n.split(".")[0]}-fr.tex','range':n,'words':words})
   cr.append({'statement_id':'IV.'+n,'date':'2026-11-25','who':'GPT-6 Astra','type':'translation and source comparison','outcome':'Restored complete source clauses and literal formulas after identifying inherited abridgment; no proof verification.'})
 for r in tr:
  if 'french_file' in r:r['french_source']=r.pop('french_file')
 write_tsv(tp,['file','french_source','range','words'],[[r[k] for k in ['file','french_source','range','words']] for r in tr])
 write_tsv(cp,['statement_id','date','who','type','outcome'],[[r[k] for k in ['statement_id','date','who','type','outcome']] for r in cr])
 print('Complete translations applied:',', '.join(TRANSLATIONS))
if __name__=='__main__':apply()


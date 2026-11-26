"""Complete source-faithful replacement of identified abridged IV3 units."""
import re,json
from iv3_work import DIR,FR,replace
from iv3_align import units
from corpus import RESULT,write_tsv
from tex_tools import prose_segments

TRANSLATIONS={
'9.4.8':r'''\begin{proposition}[9.4.8]
\label{IV.9.4.8}
Sean $S$ un preesquema localmente noetheriano, $f:X\to S$ un morfismo de tipo
finito, $\mathcal F$ un $\mathcal O_X$-Módulo coherente. Se supone que para todo
$s\in S$, $X_s$ es un preesquema localmente íntegro. Entonces el conjunto $E$
\textnormal{(resp.} $E'$\textnormal{)} de los $s\in S$ tales que $\mathcal F_s$
sea un $\mathcal O_{X_s}$-Módulo de torsión \textnormal{(resp.} un
$\mathcal O_{X_s}$-Módulo sin torsión\textnormal{)} es localmente
construible.
\end{proposition}

Se puede evidentemente suponer que $S=\operatorname{Spec}(A)$ es afín y noetheriano y
probar que $E$ (resp. $E'$) es entonces construible utilizando el criterio
$(\mathbf 0_{\mathrm{III}},9.2.3)$; reemplazando $S$ por el subpreesquema cerrado
reducido de $S$ que tiene por espacio subyacente una parte cerrada irreducible $Y$
de $S$, y observando (\textbf{I}, 3.6.4) que para $s\in Y$, la fibra
$(X_{(Y)})_s$ se identifica canónicamente con $X_s$ y el haz
$(\mathcal F\otimes_{\mathcal O_S}\mathcal O_Y)_s$ con $\mathcal F_s$, se ve
que se reduce al caso en que $S$ es íntegro de punto genérico $\eta$, y a
probar que $E$ o $S\setmin E$ (resp. $E'$ o $S\setmin E'$) es una vecindad de $\eta$
en $S$. Observemos además que $X$ es unión finita de abiertos afines $U_i$,
de tipo finito sobre $S$, y cada uno de los $(U_i)_s$ está inducido sobre un abierto de
$X_s$, luego es localmente íntegro; además, si $(U_i)_\eta$ es vacío (resp. no
vacío), se sabe que $(U_i)_s$ también es vacío (resp. no vacío) en una vecindad
de $\eta$ (9.2.6). Se puede, por tanto, suponer que todos los $(U_i)_\eta$ son no vacíos e
íntegros, y decir que $\mathcal F_s$ es de torsión (resp. sin torsión)
equivale a decir que cada uno de los $\mathcal F_s|(U_i)_s$ es de torsión (resp.
sin torsión). Se reduce, por tanto, al caso en que $X=\operatorname{Spec}(B)$ es
afín, y $\mathcal F=\widetilde M$, donde $M$ es un $B$-módulo de tipo finito;
se pondrá $B_s=B\otimes_A \boldsymbol{k}(s)$, $M_s=M\otimes_A \boldsymbol{k}(s)$ y se puede suponer
que $B_\eta$ es íntegro. Tenemos cuatro casos que considerar:

$1^\circ$ $\eta\in E$; $M_\eta$ es, por tanto, un $B_\eta$-módulo de torsión de
tipo finito, y existe, por consiguiente, un $h\neq0$ en $B_\eta$ tal que
$hM_\eta=0$; en virtud de (8.5.2, (i)), aplicado siguiendo el método
\oldpage[IV-3]{66}
de (8.1.2, \emph{a)}), se puede (reemplazando, si es preciso, $S$ por una vecindad
de $\eta$) suponer que $h\in\Gamma(X_\eta,\mathcal O_{X_\eta})$ es de la
forma $g_\eta$, donde $g\in\Gamma(X,\mathcal O_X)$; sea
$u:\mathcal F\to\mathcal F$ el endomorfismo de $\mathcal F$ definido por la
multiplicación por $g$; por hipótesis, se tiene $u_\eta=0$, luego (9.4.5)
el endomorfismo $u_s:\mathcal F_s\to\mathcal F_s$, definido por la multiplicación
por $g_s$, es nulo en una vecindad de $\eta$. Por otra parte, sea
$v:\mathcal O_X\to\mathcal O_X$ el endomorfismo definido por la multiplicación
por $g$; como $B_\eta$ es íntegro y $h=g_\eta\neq0$, $v_\eta$ es inyectivo,
y resulta, por tanto, de (9.4.5) que $v_s$ es un endomorfismo inyectivo de
$\mathcal O_{X_s}$ para $s$ próximo a $\eta$, es decir, $g_s$ es un
elemento $\mathcal O_{X_s}$-regular para estos valores de $s$; luego
$\mathcal F_s$ es de torsión en una vecindad de $\eta$.

$2^\circ$ $\eta\in S\setmin E$. Decir que un $B_\eta$-módulo de tipo finito $M_\eta$
no es un módulo de torsión significa que su cociente $M_\eta/T$ por su
submódulo de torsión es $\neq0$, y como es un $B_\eta$-módulo sin
torsión de tipo finito, es isomorfo a un submódulo de un $B_\eta$-módulo
$B_\eta^n$; existe, por consiguiente, un homomorfismo
$w:M_\eta\to B_\eta$ que es $\neq0$. Aplicando (8.5.2, (i)) siguiendo el
método de (8.1.2, \emph{a)}), se deduce (reemplazando, si es preciso, $S$ por una
vecindad de $\eta$) que existe un homomorfismo
$v:\mathcal F\to\mathcal O_X$ tal que $v_\eta=\widetilde w$. La hipótesis
$v_\eta\neq0$ implica, por tanto, (9.4.5) que $v_s\neq0$ en una vecindad de
$\eta$, y como $X_s$ es localmente íntegro, $\mathcal F_s$ no es de
torsión para estos valores de $s$.

$3^\circ$ $\eta\in E'$. Como $M_\eta$ es un $B_\eta$-módulo de tipo finito
sin torsión, existe un homomorfismo inyectivo
$w:M_\eta\to B_\eta^n$. Utilizando (8.5.2, (i)) y (9.4.5) como en el
$2^\circ$ (restringiendo, si es preciso, $S$), se deduce que existe un
homomorfismo $v:\mathcal F\to\mathcal O_X^n$ tal que $v_\eta=\widetilde w$,
y que para $s$ próximo a $\eta$,
$v_s:\mathcal F_s\to\mathcal O_{X_s}^n$ es inyectivo; para estos valores de
$s$, $\mathcal F_s$ es, por tanto, sin torsión.

$4^\circ$ $\eta\in S\setmin E'$. Sea $T$ el submódulo de torsión de $M_\eta$;
por hipótesis $T\neq0$, y $T$ es de tipo finito puesto que $M_\eta$ es
noetheriano. Utilizando esta vez (8.5.2, (i) y (ii)), se ve (restringiendo,
si es preciso, $S$) que existe un $\mathcal O_X$-Módulo coherente $\mathcal G$ y
un homomorfismo inyectivo $u:\mathcal G\to\mathcal F$ tales que
$\mathcal G_\eta=\widetilde T$ y que $u_\eta$ sea la inyección canónica
$\widetilde T\to\mathcal F_\eta$. Resulta entonces del $1^\circ$ y de (1.8.6)
que en una vecindad de $\eta$, $\mathcal G_s$ es un
$\mathcal O_{X_s}$-Módulo de torsión $\neq0$, y por otra parte resulta de
(9.4.5) que en una vecindad de $\eta$, $u_s$ es inyectivo. Se concluye que
en una vecindad de $\eta$, el submódulo de torsión de $\mathcal F_s$ no es
nulo. C.Q.F.D.

''',
'8.10.5.2':r'''\begin{lemma}[8.10.5.2]
\label{IV.8.10.5.2}
Supongamos que $S_0$ es cuasicompacto, y sea $\mathcal L_\lambda$ un
$\mathcal O_{X_\lambda}$-Módulo invertible. Para que $\mathcal L$ sea un
$\mathcal O_X$-Módulo amplio para $f$ \textup{(resp.} muy amplio para $f$\textup{)}, es necesario y
suficiente que exista $\mu\geq\lambda$ tal que $\mathcal L_\mu$ sea amplio
para $f_\mu$ \textup{(resp.} muy amplio para $f_\mu$\textup{)}.
\end{lemma}

Siendo la condición evidentemente suficiente (\textbf{II}, 4.4.10 y 4.6.13), demostremos
que es necesaria; siendo los $S_\lambda$ cuasicompactos y los
$f_\lambda$ de tipo finito, se puede, reemplazando $\mathcal L$ por una potencia
tensorial adecuada, limitarse a considerar el caso en que $\mathcal L$ es muy
amplio (\textbf{II}, 4.6.11). Además, siendo aquí la cuestión local sobre $S_0$ (en virtud
de (\textbf{II}, 4.4.5) y del hecho de que $L$ es filtrante), se puede limitar al caso en que
$S_0$ (y por consiguiente $S$) es \emph{afín}. Entonces, en virtud de (\textbf{II}, 4.4.1, (ii) y
\textbf{II}, 4.1.2), existe una $S$-inmersión
$j:X\to\mathbf P_S^r=P$ tal que $\mathcal L$ sea isomorfo a
$j^*(\mathcal O_P(1))$. Teniendo en cuenta (8.8.2, (i)), (ii) y
(\textbf{II}, 4.1.3), existen, por tanto, un $\mu\geq\lambda$ y una inmersión
$j_\mu:X_\mu\to\mathbf P_{S_\mu}^r=P_\mu$ tales que
$j=j_\mu\times1_S$; utilizando luego (\textbf{II}, 4.1.3.2) y (8.5.2.5), se ve
que existe $\nu\geq\mu$ tal que $\mathcal L_\nu$ sea isomorfo a
$j_\nu^*(\mathcal O_{P_\nu}(1))$, lo que demuestra que $\mathcal L_\nu$ es muy
amplio para $f_\nu$ (\textbf{II}, 4.4.2).
\end{proof}

\subsection{Aplicación a los morfismos cuasifinitos.}
\label{subsection:IV.8.11}
\label{IV.8.11}

Nos proponemos en esta sección demostrar los dos teoremas
siguientes:

''',
'11.2.2':r'''\begin{env}[11.2.2]
\label{IV.11.2.2}
Con las notaciones de (11.2.1), consideremos ahora un
\emph{sistema inductivo} filtrante de $A$-álgebras
$(A_\alpha,g_{\beta\alpha})$, y para todo índice $\alpha$, pongamos
$M_\alpha=M\otimes_AA_\alpha$, $N_\alpha=N\otimes_AA_\alpha$; resulta
entonces de (11.2.1) que para cada $i$,
$(\operatorname{Tor}_i^{A_\alpha}(M_\alpha,N_\alpha),
\psi_{i\beta\alpha})$, donde $\psi_{i\beta\alpha}$ es el homomorfismo
canónico (11.2.1.1) correspondiente a $g_{\beta\alpha}$, es un \emph{sistema
\oldpage[IV-3]{121}
inductivo de $A_\alpha$-módulos}. Pongamos
$A'=\varinjlim A_\alpha$, $M'=\varinjlim M_\alpha=M\otimes_AA'$,
$N'=\varinjlim N_\alpha=N\otimes_AA'$; si se denota por
$g_\alpha:A_\alpha\to A'$ el homomorfismo canónico, se deducen homomorfismos
canónicos (11.2.1.1)
$\psi_{i\alpha}:\operatorname{Tor}_i^{A_\alpha}(M_\alpha,N_\alpha)
\to\operatorname{Tor}_i^{A'}(M',N')$ que (siempre en virtud de (11.2.1))
forman un sistema inductivo de homomorfismos; nos proponemos
completar el resultado de (M, V, 9.4$^*$) mostrando que los
\begin{equation}
\psi_i=\varinjlim_\alpha\psi_{i\alpha}:
\varinjlim_\alpha\operatorname{Tor}_i^{A_\alpha}(M_\alpha,N_\alpha)
\to\operatorname{Tor}_i^{A'}(M',N')
\label{IV.11.2.2.1}
\tag{11.2.2.1}
\end{equation}
son \emph{isomorfismos de $A'$-módulos}. Para ello, procedemos
como en (M, V, 9.5$^*$), asociando a cada $M_\alpha$ su
\emph{resolución libre canónica}. Todo se reduce (teniendo en cuenta la exactitud
del funtor $\varinjlim$) a probar el
\end{env}

'''
}

if __name__=='__main__':
 records=[];events=[]
 for n,new in TRANSLATIONS.items():
  k=n.split('.')[0];q=DIR/f'sections/ega4-{k}.tex';old=units(q.read_text())[n].text
  replace(q,old,new,n,f'ega4-{k}-fr.tex')
  words=len(re.findall(r'[A-Za-zÀ-ÿ]{2,}',' '.join(p for a,b,p in prose_segments(new))))
  records.append([str(q.relative_to(RESULT)),f'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/ega4-{k}-fr.tex',n,words])
  events.append(['IV.'+n,'2026-11-25','GPT-6 Astra','translation and source comparison','Restored complete source text and formula spelling after identifying abridged clauses; no proof verification.'])
 write_tsv(RESULT/'records/TRADUCCION_iv3_supplements.tsv',['file','french_file','range','words'],records)
 write_tsv(RESULT/'records/CHECK_EVENTS_iv3_supplements.tsv',['statement_id','date','who','type','outcome'],events)
 print('Completed',','.join(TRANSLATIONS))


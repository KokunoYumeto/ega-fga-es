import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
M={
('1','4.3.11'):r'''\begin{env}[4.3.11]
\label{III.4.3.11-fr}
\emph{Observaciones} (4.3.11). ---
\begin{enumerate}
\item[(i)] El razonamiento anterior se debe en sustancia a Zariski [20],
salvo que puede tomar como §0§ el cierre integral de
§1§, que es un anillo noetheriano para los anillos locales
de la geometría algebraica clásica. Por otra parte, Zariski prueba que si
§2§ es la variedad de Chow de un espacio proyectivo §3§ sobre un
cuerpo §4§, y si §5§ es la parte cerrada de §6§ que
define la correspondencia de Chow entre §7§ y §8§, entonces la
proyección §9§ es un morfismo universalmente abierto
(\emph{loc. cit.}, lema de la p. 82). Parece que esta es la única
propiedad formal de las «coordenadas de Chow» que se ha utilizado en
ciertas aplicaciones; interesa por tanto, en tal situación,
sustituir el lenguaje: fibras de un morfismo propio (eventualmente
supuesto universalmente abierto o sometido a otras restricciones análogas
de regularidad local) al lenguaje: especialización de ciclos en el espacio
proyectivo.

\item[(ii)] En el cap. IV veremos que un morfismo universalmente abierto
§10§ puede definirse también de la manera siguiente (que justifica la
terminología): para \emph{todo} morfismo §11§, el morfismo
§12§ es \emph{abierto}. Se puede mostrar además que si §13§
verifica las hipótesis de (\hyperref[III.4.3.10-fr]{4.3.10}), entonces, si
§14§ son dos puntos de §15§ tales que §16§ es una \emph{especialización} de §17§,
el número geométrico de componentes conexas de §18§ es a lo sumo
igual al de las componentes conexas de §19§.
\end{enumerate}
\end{env}

''',
('1','4.4.12'):r'''\begin{env}[4.4.12]
\label{III.4.4.12-fr}
\emph{Observaciones} (4.4.12). ---
\begin{enumerate}
\item[(i)] Como se ha anunciado en (\textbf{II}, 6.2.7), mostraremos en el cap. V
que si §0§ es localmente noetheriano, todo morfismo cuasifinito y separado
§1§ es cuasiafín, luego cuasiproyectivo. Resultará que, en el
Main Theorem (\hyperref[III.4.4.3-fr]{4.4.3}), la conclusión sigue siendo válida
cuando se supone solamente §2§ \emph{separado y de tipo finito}. En efecto, resulta
de (\hyperref[III.4.4.10-fr]{4.4.10}) que §3§ es abierto en §4§, y como
§5§ es localmente noetheriano, la restricción de §6§ a §7§ es también de
tipo finito (\textbf{I}, 6.3.5), luego cuasifinita por definición de §8§, y evidentemente
separada; se puede pues aplicar (\hyperref[III.4.4.3-fr]{4.4.3}) a esta
restricción, de donde la conclusión.

\item[(ii)] Daremos en el cap. IV una demostración más elemental de
(\hyperref[III.4.4.10-fr]{4.4.10}), utilizando la teoría de la dimensión.
\end{enumerate}
\end{env}

\subsection{Completados de módulos de homomorfismos}
\label{subsection:III.4.5-fr}

''',
('6','6.5.7'):r'''\begin{namedtheorem}[6.5.7]{Observaciones}
\textnormal{(i)} Consideremos en particular el caso en que §0§,
siendo pues §1§ y §2§ dos complejos de
§3§-Módulos cuasicoherentes; entonces los
§4§ son
§5§-Módulos cuasicoherentes; además, para todo punto §6§,
resulta de (6.5.6) que se tiene un isomorfismo canónico
§7§
pues la cuestión es local y se está reducido al caso de los módulos, en virtud de
(6.4.1.1).

\textnormal{(ii)} Se puede generalizar la definición de los hipertor al caso de
\emph{dos complejos de §8§-Módulos} §9§,
§10§ sobre un mismo \emph{espacio anillado} §11§; para todo
abierto §12§ de §13§, pongamos en efecto
§14§,
§15§,
§16§; los §17§-módulos
§18§
forman entonces un \emph{prehaz} sobre §19§, y se designa por
§20§ el
§21§-Módulo asociado a este prehaz. Cuando §22§ es un \emph{preesquema},
resulta de (6.3.12) que este §23§-Módulo es canónicamente isomorfo
al hipertor definido antes. No desarrollaremos más esta
generalización.
\end{namedtheorem}

''',
('6','6.5.10'):r'''\begin{namedtheorem}[6.5.10]{Corolario}
Supongamos que §0§ es plano sobre §1§ \textup{(§2§, 6.7.1)}, que
§3§ y §4§ están acotados inferiormente y
que todos los §5§ son §6§-Módulos localmente
libres (no necesariamente de tipo finito). Entonces el homomorfismo \textup{(6.5.9.1)} es
biyectivo.
\end{namedtheorem}

\begin{proof}
En efecto, se cumple la hipótesis de (6.5.9), al ser la planitud una propiedad
puntual sobre §7§ por definición y toda suma directa de módulos planos
un módulo plano (§8§, 6.1.2).
\end{proof}

''',
('6','6.5.12'):r'''\begin{namedtheorem}[6.5.12]{Observación}
Sean §0§, §1§ dos §2§-preesquemas y supongamos que §3§ es §4§-\emph{plano};
sean §5§ un subpreesquema cerrado de §6§, §7§ la inclusión canónica,
§8§ (resp. §9§) un complejo de
§10§-Módulos (resp. de §11§-Módulos) cuasicoherentes,
acotado inferiormente. Sea finalmente §12§ una resolución
de §13§ formada por §14§-Módulos localmente
libres, tal que todo punto de §15§ tiene una vecindad abierta afín §16§ para
la cual §17§ es una resolución libre de
§18§ para todo §19§. Se tiene entonces un isomorfismo canónico
§20§

Si §21§, §22§, §23§ son afines y si §24§ es una
resolución libre de §25§ para todo §26§, se está reducido, en virtud
de (6.5.11), al caso en que §27§ es §28§-plano, y basta aplicar (6.3.4).
En el caso general, se define localmente el isomorfismo (6.5.12.1), y se
trata de verificar que esta definición da efectivamente un isomorfismo global.
Para ello, hay que remitirse a la definición del primer isomorfismo
(6.3.4.1), que procede de un isomorfismo de sucesiones espectrales (\textbf{0}, 11.6.5 y
11.5.3), obtenido a su vez a partir de un morfismo de bicomplejos
§29§, donde §30§ es la
resolución dada de §31§, §32§ una resolución
proyectiva de §33§ en la categoría de complejos de §34§-módulos
acotados
\oldpage[III]{152}
inferiormente (cf. (\textbf{0}, 11.5.2.2)); nuestra afirmación resulta de que
el isomorfismo (6.3.4.1) no depende de la resolución proyectiva
§35§ elegida, en virtud de la existencia de un homotopismo entre
dos de tales resoluciones (M, V, 1.2).
\end{namedtheorem}

'''
}
apply_units(M)
# Two source subsection boundaries share the next physical input.
for ed in ['current','diplomatic']:
 f=source(ed,'1').read_text();e,b=aggregate(ed,'1');fa,fb=next((a,z) for k,a,z in sections(f) if k=='4.4.12');ea,eb=next((a,z) for k,a,z in sections(e) if k=='4.4.12')
 if not any(ea<q[0]<eb for q in b):continue
 new=expand(M['1','4.4.12'],f[fa:fb]);head,tail=new.split(r'\subsection',1);mid=next(q[0] for q in b if ea<q[0]<eb);apply_edits(ed,'1',[(ea,mid-1,head,'4.4.12',e[ea:mid-1]),(mid,eb,r'\subsection'+tail,'4.4.12 subsection',e[mid:eb])],b)

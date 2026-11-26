import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','5.2.3'):r'''\begin{proposition}[5.2.3]
\label{III.5.2.3-fr}
Sean §0§ un anillo ádico noetheriano, §1§ un ideal de definición de
§2§, §3§,
§4§ un morfismo propio de preesquemas formales. Se pone
§5§,
§6§, y para todo
§7§-Módulo §8§,
§9§.
Sea §10§ un §11§-Módulo invertible, y supongamos que
§12§ es un
§13§-Módulo amplio; para todo §14§-Módulo
§15§ y todo entero §16§, pongamos
§17§. Entonces, para todo
§18§-Módulo coherente §19§, existe un entero §20§
tal que, para todo §21§, se verifican las propiedades siguientes:
\begin{enumerate}
\item[\textup{(i)}] El homomorfismo canónico
§22§ es sobreyectivo para todo §23§.
\item[\textup{(ii)}] Se tiene §24§ para todo §25§.
\end{enumerate}
\end{proposition}

\begin{proof}
Se sabe que los espacios subyacentes a §26§ y a §27§ son los mismos;
los haces
§28§,
al estar anulados por §29§, pueden considerarse como
§30§-Módulos coherentes (§31§, 5.3.10); además, si se
pone §32§, se ve inmediatamente que
§33§.
Observemos que, puesto que §34§ es amplio para §35§, y
\oldpage[III]{152}
§36§ es propio, se concluye que §37§ es \emph{proyectivo} (\textbf{II}, 5.5.4). Sea §38§ la §39§-álgebra
graduada §40§ asociada a la filtración §41§-ádica de §42§, que es
de tipo finito puesto que §43§ es noetheriano; si se pone
§44§,
§45§ es una
§46§-Álgebra cuasicoherente de tipo finito, y
§47§ un
§48§-Módulo graduado cuasicoherente y de tipo finito (puesto que §49§
es coherente y genera el §50§-Módulo §51§). Se está pues en las
condiciones de aplicación del teorema (2.4.1, (ii)), y se concluye que existe
§52§ tal que, para §53§ y para \emph{todo} §54§, se tiene
§55§
Se tiene pues también §56§ para §57§ y
§58§, considerando esta vez §59§ como
§60§-Módulo. Aplicando la sucesión exacta de cohomología a
§61§
se deduce ante todo que para §62§, §63§ y §64§ se tiene, por
inducción sobre §65§,
§66§
y en particular para §67§
§68§
Otra porción de la sucesión exacta de cohomología, para §69§, da la sucesión
exacta
§70§
de donde se deduce que para §71§ la aplicación canónica
§72§
es \emph{sobreyectiva}. Para \emph{todo} §73§, el sistema proyectivo
§74§ verifica pues la condición
(ML) para §75§. Por otra parte, todo abierto formal afín §76§ de §77§
es también un abierto afín en cada uno de los §78§ (\textbf{I}, 10.5.2), luego se tiene
§79§ para todo §80§ (1.3.1), y
§81§ es sobreyectiva
para §82§ (\textbf{I}, 1.3.9). Las condiciones de aplicación de (\textbf{0}, 13.3.1) se
cumplen por tanto, y se concluye que, para §83§:
\begin{enumerate}
\item[§84§] Para todo §85§,
§86§
es biyectivo, luego, en virtud de (\ref{III.5.2.3.3-fr}),
§87§.
\item[§88§] El homomorfismo
§89§
es biyectivo; por otra parte, como los homomorfismos
(\ref{III.5.2.3.5-fr}) son sobreyectivos, lo mismo ocurre con cada uno de los
homomorfismos
§90§
\end{enumerate}
lo que termina la demostración.
\end{proof}

''',
('1','5.2.4'):r'''\begin{corollary}[5.2.4]
\label{III.5.2.4-fr}
Siendo las hipótesis las de \textup{(\hyperref[III.5.2.3-fr]{5.2.3})}, para todo
§0§-Módulo coherente §1§ existe un entero §2§
tal que para §3§, §4§ está generado por sus secciones sobre
\oldpage[III]{153}
§5§; en otros términos, §6§ es isomorfo al cociente de un
§7§-Módulo de la forma
§8§.
\end{corollary}

\begin{proof}
Como §9§ es noetheriano, resulta de la hipótesis sobre §10§ y de
(\textbf{II}, 4.5.5) que existe §11§ tal que, para §12§, §13§ está
generado por sus secciones sobre §14§; por otra parte, se puede suponer
§15§ suficientemente grande para que el homomorfismo
§16§
sea sobreyectivo para §17§ (\hyperref[III.5.2.3-fr]{5.2.3}). Existe pues
un número finito de secciones §18§ cuyas
imágenes en §19§ generan §20§
(§21§, 5.2.3). Como §22§ está contenido en el ideal maximal del
anillo local en todo punto de §23§, resulta del lema de Nakayama,
aplicado a estos anillos locales, que los §24§ generan §25§
(§26§, 5.1.1).
\end{proof}

''',
('1','5.3.4'):r'''\begin{lemma}[5.3.4]
\label{III.5.3.4-fr}
Sean §0§ un esquema (usual) noetheriano, §1§ una parte cerrada de §2§,
§3§ un morfismo propio, §4§,
§5§, §6§,
§7§ la prolongación de §8§ a los completados. Sea
§9§ un Ideal coherente de §10§ tal que, si
§11§, la restricción
§12§ de §13§ es un isomorfismo. Entonces, para todo
§14§-Módulo coherente §15§ existe un entero §16§
tal que el núcleo y el conúcleo del homomorfismo canónico
§17§
\textup{(§18§, 4.4.3)} están anulados por §19§.
\end{lemma}

\begin{proof}
Se puede limitar al caso en que §20§, donde §21§ es un anillo
noetheriano, luego §22§, donde §23§ es un ideal de
§24§. Vamos a ver que se puede reducir al caso en que §25§ es un anillo \emph{ádico}
noetheriano y §26§ un ideal de definición de §27§. Sea en efecto §28§ el
separado completado de §29§ para la topología §30§-preádica; si
§31§, §32§ es pues un
\oldpage[III]{155}
anillo ádico noetheriano del cual §33§ es un ideal de definición. Pongamos
§34§ y sea §35§ el morfismo correspondiente al
homomorfismo canónico §36§; si §37§, se tiene pues
§38§. Pongamos finalmente
§39§, §40§, que es un morfismo
propio (\textbf{II}, 5.4.2), y designemos por §41§ el completado de §42§ a lo largo
de §43§, por
§44§ el completado de §45§ a lo largo de
§46§, por §47§ la prolongación de §48§ a los completados.
Es inmediato que la prolongación §49§ de §50§
a los completados es un isomorfismo, correspondiente a la aplicación identidad de §51§
(\textbf{I}, 10.9.1); se concluye que el homomorfismo correspondiente
§52§ es también un isomorfismo, identificando estos isomorfismos
§53§ y §54§. Finalmente,
§55§ es un Ideal coherente de §56§ y
§57§
(\textbf{I}, 9.1.13), luego, si
§58§, se tiene
§59§, de donde resulta inmediatamente que la restricción
§60§ de §61§ es un isomorfismo (\textbf{I}, 3.2.7); además, los
completados §62§ y §63§ se identifican por
§64§ (\textbf{I}, 10.9.5). Todas las hipótesis de
(\hyperref[III.5.3.4-fr]{5.3.4}) se cumplen pues para §65§, §66§, §67§ y
§68§, y se puede por tanto suponer en adelante §69§ ádico noetheriano y
§70§ un ideal de definición de §71§. Se tiene entonces
§72§, y §73§, donde §74§ es un
§75§-módulo de tipo finito, de donde §76§, donde §77§
es el §78§-Módulo coherente §79§ (\textbf{I}, 10.10.5), y por tanto
§80§
(\textbf{I}, 10.9.5). Además, en virtud del primer teorema de comparación (4.1.5),
§81§ se identifica canónicamente con
§82§,
y el homomorfismo canónico §83§ no es otro que
§84§ en virtud de
(\hyperref[III.5.1.3-fr]{5.1.3}). Ahora bien, el núcleo §85§ y el conúcleo
§86§ de
§87§
son §88§-Módulos coherentes, y por hipótesis sus restricciones a
§89§ son evidentemente nulas. Existe por tanto un entero §90§ tal que
§91§ (\textbf{I}, 9.3.4); se concluye que
§92§
(\textbf{I}, 10.8.8 y 10.8.10).
\end{proof}

''',
('1','5.4.1'):r'''\begin{theorem}[5.4.1]
\label{III.5.4.1-fr}
Sean §0§ un anillo ádico noetheriano, §1§ un ideal de definición de
§2§, §3§, §4§. Sean
§5§ un morfismo propio, §6§ un morfismo separado de tipo finito, y
sean §7§, §8§, §9§ los completados de §10§, §11§, §12§ a lo
largo de §13§, §14§, §15§ respectivamente. Si, para todo
§16§-morfismo §17§, §18§ es la
prolongación de §19§ a los completados, la aplicación §20§ es una
biyección
§21§
\end{theorem}

\begin{proof}
Mostremos primero que §22§ es inyectiva. Supongamos en efecto que dos
§23§-morfismos §24§, §25§ de §26§ en §27§ son tales que §28§.
Se sabe entonces (\textbf{I}, 10.9.4) que existe una vecindad abierta §29§ de
§30§ en la que §31§ y §32§ coinciden. Ahora bien, como §33§ es una aplicación
cerrada, se tiene §34§ (\hyperref[III.5.1.3.1-fr]{5.1.3.1}), de donde §35§.

Probemos ahora que §36§ es sobreyectiva, y sea pues §37§ un
§38§-morfismo §39§. Sea §40§, y
designemos por §41§ y §42§ las proyecciones canónicas; §43§ es de
tipo finito sobre §44§ (\textbf{I}, 6.3.4), luego noetheriano; designemos por §45§ su
completado a lo largo de §46§; se sabe que §47§ se identifica
canónicamente con §48§, identificándose las proyecciones
§49§ y §50§ con las
prolongaciones §51§ y §52§ (\textbf{I}, 10.9.7). Como §53§ es separado sobre
§54§, §55§ es separado sobre §56§ (\textbf{I}, 10.15.7), luego el morfismo
grafo
§57§
es una inmersión cerrada (\textbf{I}, 10.15.4). Sean §58§ el subpreesquema
formal cerrado de §59§ asociado a esta inmersión, y
§60§ la inclusión canónica, de modo que
§61§, donde §62§ es un isomorfismo
(\textbf{I}, 10.14.3) cuyo isomorfismo inverso es §63§; además,
§64§ es evidentemente propio sobre §65§, puesto que §66§ lo es;
se concluye (\hyperref[III.5.1.8-fr]{5.1.8}) que existe un subpreesquema
cerrado §67§ de §68§ tal que
§69§, y que §70§, donde §71§ es
la inclusión canónica §72§ (\textbf{I}, 10.14.7). Entonces §73§ es un
isomorfismo, pues lo mismo ocurre con
§74§ por hipótesis, y basta
aplicar
\oldpage[III]{157}
(4.6.8) observando como antes que §75§ es la única vecindad de §76§ en §77§.
Sea §78§ el isomorfismo inverso de §79§, y pongamos
§80§, que es un morfismo §81§ cuyo grafo, por definición, es
§82§. Como §83§ es el isomorfismo inverso de
§84§, se tiene
§85§.
Pero se sabe que §86§ (\textbf{I}, 10.9.8), de donde
finalmente §87§, lo que termina la demostración.
\end{proof}

Se puede pues decir, en el lenguaje de las categorías, que el funtor
§88§ es \emph{plenamente fiel} (\textbf{0}, 8.1.6) de la categoría de los
esquemas propios sobre §89§ en la categoría de los esquemas formales
propios sobre §90§, para todo anillo ádico noetheriano §91§;
establece por tanto una equivalencia entre la primera de estas categorías y una
\emph{subcategoría} de la segunda; los objetos de esta última se llamarán
\emph{esquemas formales algebraizables}. Para tal esquema §92§, existe
un esquema usual §93§, propio sobre §94§, determinado salvo isomorfismo
único, tal que §95§ es isomorfo a §96§.

''',
('1','5.4.5'):r'''\begin{theorem}[5.4.5]
\label{III.5.4.5-fr}
Sean §0§ un anillo ádico noetheriano, §1§ un ideal de definición de
§2§, §3§,
§4§,
§5§ un morfismo propio de esquemas formales. Se pone
§6§,
§7§, y para todo
§8§-Módulo §9§,
§10§.
\oldpage[III]{158}
Sea §11§ un §12§-Módulo invertible, y supongamos
que §13§ es un
§14§-Módulo amplio. Entonces §15§ es algebraizable, y si
§16§ es un §17§-esquema propio tal que §18§ es isomorfo a
§19§, existe un §20§-Módulo amplio §21§ tal que
§22§ es isomorfo a §23§ \textup{(lo que implica que
§24§ es \emph{proyectivo} sobre §25§)}.
\end{theorem}

\begin{proof}
Apliquemos (\hyperref[III.5.2.3-fr]{5.2.3}) a
§26§: existe pues un entero §27§ tal que
para §28§ el homomorfismo canónico
§29§ es \emph{sobreyectivo}. Se puede suponer
§30§ suficientemente grande para que §31§ sea \emph{muy
amplio} para §32§ (\textbf{II}, 4.5.10). Como el morfismo §33§ es propio,
§34§ es un §35§-módulo de tipo finito (3.2.1),
luego existe un sub-§36§-módulo de tipo finito §37§ de
§38§ cuya imagen en
§39§ es este último módulo entero.
Dicho esto, para todo §40§, consideremos el homomorfismo
§41§
deducido de la inclusión canónica
§42§. Observemos que
§43§ es cuasicoherente, y como
§44§, §45§ define un homomorfismo
§46§,
y por tanto también un homomorfismo
§47§.
Por lo demás, si se pone
§48§, se tiene
§49§ (\textbf{I}, 9.1.5), luego
§50§ se deduce
de §51§ por paso a los cocientes. Ahora bien, por definición de
§52§, §53§ no es otro que el homomorfismo canónico
§54§,
y la hipótesis de que §55§ es muy amplio implica que
§56§ es \emph{sobreyectivo} (\textbf{II}, 4.4.3); se deduce entonces del lema
de Nakayama que cada uno de los §57§ es también \emph{sobreyectivo}.
Cada uno de los §58§ define pues (\textbf{II}, 4.2.2) un
§59§-morfismo
§60§,
y como §61§ para §62§ en virtud de (\textbf{II}, 4.1.3),
§63§ es un §64§-\emph{sistema inductivo ádico} (\textbf{I}, 10.12.2) en virtud de las
relaciones entre los §65§ y de (\textbf{II}, 4.2.10). Los §66§
definen pues un §67§-morfismo de esquemas formales
§68§, donde §69§ es el límite inductivo del
sistema §70§, o también el completado §71§, donde §72§.
Además, la hipótesis de que §73§ es muy amplio implica que
§74§ es una \emph{inmersión cerrada} (\textbf{II}, 4.4.3); se concluye que §75§ es una
inmersión cerrada de esquemas formales (4.8.10), luego §76§ es
algebraizable (5.1.8). El hecho de que §77§ sea isomorfo al completado
§78§ de un §79§-Módulo invertible resulta entonces del
teorema de existencia (5.1.6). Además, §80§ es entonces el
completado de §81§ (\textbf{I}, 10.8.10), y los homomorfismos
§82§ definen un homomorfismo bien determinado
§83§
(5.1.7); por lo demás, como §84§ es sobreyectivo, lo mismo ocurre con
§85§ (\textbf{I}, 10.11.5), luego con §86§ (5.1.3); además, el morfismo
§87§ definido por §88§ (\textbf{II}, 4.2.2) tiene por prolongación a los completados §89§,
y como §90§ es una inmersión cerrada, lo mismo ocurre con §91§, por (5.1.8)
y (5.4.1); se concluye que §92§ es muy amplio
(\textbf{II}, 4.4.6) y §93§ es amplio (\textbf{II}, 4.5.10).
\end{proof}

''',
('1','5.5.1'):r'''\begin{proposition}[5.5.1]
\label{III.5.5.1-fr}
Sean §0§ un anillo ádico noetheriano, §1§ un ideal de definición
de §2§, §3§. Sea §4§ un morfismo separado de
tipo finito; se pone §5§,
§6§. Sea §7§ una parte abierta de §8§,
propia sobre §9§; existe entonces en §10§ una parte abierta y cerrada §11§,
propia sobre §12§ y tal que §13§.
\end{proposition}

\begin{proof}
Por hipótesis, hay un abierto §14§ de §15§ tal que §16§; sea
§17§ el completado a lo largo de §18§ del esquema inducido por §19§ sobre
el abierto §20§; al ser el soporte de §21§ igual a §22§, que es
propio sobre §23§, §24§ es propio sobre
§25§ (3.4.1). Resulta de (5.1.8) que existe
un subesquema cerrado §26§ de §27§ \emph{propio} sobre §28§, tal que, si §29§ es
la inclusión canónica, §30§ es un
isomorfismo (siendo §31§ el completado de §32§ a lo largo de §33§). Se
concluye (4.6.8) que existe en §34§ una vecindad abierta §35§ de §36§ tal que
la restricción §37§ de §38§ es un isomorfismo. Pero
§39§ es una vecindad de §40§ en §41§, luego es necesariamente
idéntico a §42§ (5.1.3.1). Se concluye que §43§ es abierto en §44§, luego
en §45§, lo que termina la demostración.
\end{proof}

'''
})

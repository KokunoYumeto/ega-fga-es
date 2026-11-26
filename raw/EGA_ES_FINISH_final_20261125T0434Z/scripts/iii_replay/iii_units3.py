import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import apply_units
D={('1','2.2.1'):r'''\begin{theorem}[2.2.1]
\label{III.2.2.1-fr}
(Serre). Sean §0§ un preesquema noetheriano, §1§ un morfismo propio, §2§ un §3§-módulo invertible amplio para §4§. Para todo §5§-módulo §6§, pongamos
§7§
para todo §8§. Entonces, para todo §9§-módulo coherente §10§:
\begin{enumerate}
\item[{\rm(i)}] Los §11§ son §12§-módulos coherentes.
\item[{\rm(ii)}] Existe un entero §13§ tal que para §14§ se tenga §15§ para todo §16§.
\item[{\rm(iii)}] Existe un entero §17§ tal que, para §18§, el homomorfismo canónico
§19§
sea sobreyectivo.
\end{enumerate}
\end{theorem}

\begin{proof}
Observemos primero que si el teorema es verdadero cuando en él se reemplaza §20§ por §21§ §22§, es verdadero en su forma inicial. En efecto, se puede entonces escribir §23§ con un §24§ y §25§, y por hipótesis para cada §26§ hay un entero §27§ tal que para §28§ las propiedades (ii) y (iii) se cumplan para el §29§-módulo §30§; tomando para §31§ el mayor de los §32§, (ii) y (iii) se cumplirán para §33§. Se puede, pues, suponer §34§ \emph{muy amplio} relativamente a §35§ (\textbf{II}, 4.6.11); existe, por consiguiente, una §36§-inmersión abierta dominante §37§, donde §38§, donde §39§ es una §40§-álgebra cuasicoherente graduada en grados positivos, en la que §41§ es de tipo finito y engendra §42§; además, §43§ es isomorfo a §44§ (\textbf{II}, 4.4.7). Pero como §45§ es propio, lo mismo ocurre con §46§ (\textbf{II}, 5.4.4), por tanto §47§ es un \emph{isomorfismo} §48§. Se puede, pues, limitarse al caso en que §49§ y §50§. El teorema (2.2.1) es entonces consecuencia de la
\end{proof}

''',
('1','2.2.2'):r'''\begin{proposition}[2.2.2]
\label{III.2.2.2-fr}
Sean §0§ un anillo noetheriano, §1§ una §2§-álgebra graduada en grados positivos, en la que §3§ es un §4§-módulo que tiene un sistema de §5§ generadores, y que engendra el álgebra §6§. Sea §7§. Para todo §8§-módulo coherente §9§:
\begin{enumerate}
\item[{\rm(i)}] Los §10§-módulos §11§ son de tipo finito.
\item[{\rm(ii)}] Se tiene §12§ para §13§.
\item[{\rm(iii)}] Existe un entero §14§ tal que para §15§ se tenga §16§ para todo §17§.
\item[{\rm(iv)}] Existe un entero §18§ tal que para §19§, §20§ esté engendrado por sus secciones sobre §21§.
\end{enumerate}
\end{proposition}

\begin{proof}
Mostremos primero cómo (2.2.2) implica (2.2.1): en (2.2.1) (reducido al caso particular §22§ considerado más arriba), §23§ es cuasicompacto, por tanto puede recubrirse por un número finito de abiertos afines, de anillos noetherianos, tales que la restricción de §24§ a cada uno de estos abiertos §25§ esté engendrada por un número finito de secciones de §26§ sobre §27§. Si se supone demostrado (2.2.2), bastará entonces tomar para §28§ en las partes (ii) y (iii) de (2.2.1) el mayor de los enteros análogos correspondientes a los §29§ (teniendo en cuenta (1.4.11) y (\textbf{II}, 3.4.7)).

Para demostrar (2.2.2), observemos que §30§ se identifica con un subesquema cerrado de §31§ (\textbf{II}, 3.6.2); además, si §32§ es la inyección canónica, §33§ es un §34§-módulo coherente y se tiene §35§ (\textbf{II}, 3.4.5 y 3.5.2). Habida cuenta de (G, \textbf{II}, cor. del teorema 4.9.1), se reduce, pues, a demostrar (2.2.2) en el caso particular en que §36§ y §37§. Como §38§ está recubierto por los abiertos
\oldpage[III]{101}
afines §39§ en número §40§, (ii) resulta de (1.4.12). Observemos por otra parte que (iv) ya ha sido demostrado (\textbf{II}, 2.7.9).

Vamos a demostrar simultáneamente (i) y (iii). Observemos que estas aserciones son verdaderas para §41§ (\hyperref[III.2.1.13-fr]{2.1.13}); lo son, pues, también cuando §42§ es suma directa de un número finito de §43§-módulos de la forma §44§. Por otra parte, (i) y (iii) son trivialmente verdaderas para §45§ en virtud de (ii). Vamos a proceder por \emph{inducción descendente} sobre §46§. Se sabe que §47§ es isomorfo a un cociente de una suma directa §48§ de un número finito de haces §49§ (\textbf{II}, 2.7.10); es decir, se tiene una sucesión exacta
§50§
donde §51§ es coherente (\textbf{0}\textsubscript{I}, 5.3.3) y donde §52§ satisface (i) y (iii). Como §53§ es un funtor exacto en §54§, se tiene también la sucesión exacta
§55§
para todo §56§. Se deduce de ella la sucesión exacta de cohomología
§57§

Como §58§ es suma directa de los §59§ (\textbf{II}, 2.5.14), §60§ es de tipo finito, y lo mismo ocurre con §61§ por la hipótesis de inducción; como §62§ es noetheriano, se concluye que §63§ es de tipo finito para todo §64§, y en particular para §65§. Por otra parte, por la hipótesis de inducción, existe un entero §66§ tal que para §67§ se tenga §68§; además, se puede suponer también §69§ elegido de modo que §70§ para §71§, puesto que §72§ satisface (iii); se concluye que §73§ para §74§, lo que termina la demostración.
\end{proof}

''',
('1','2.3.4'):r'''\begin{proposition}[2.3.4]
\label{III.2.3.4-fr}
Sea §0§ un preesquema noetheriano.
\begin{enumerate}
\item[{\rm(i)}] Sea §1§ una §2§-álgebra graduada en grados positivos, cuasicoherente de tipo finito. Sean §3§, y
§4§
Entonces §5§ es una §6§-álgebra graduada periódica \textup{(\textbf{II}, 8.14.12)} cuyos componentes homogéneos §7§ son §8§-módulos coherentes, y si §9§ es un período de §10§, §11§ es un §12§-módulo invertible §13§-amplio. Además, el homomorfismo canónico
§14§
es un \textup{\textbf{(TN)}}-isomorfismo.
\item[{\rm(ii)}] Recíprocamente, sea §15§ un morfismo proyectivo, y sea §16§ una §17§-álgebra graduada, cuyos componentes homogéneos §18§ §19§ son §20§-módulos coherentes, y que admite un período §21§ tal que §22§ sea un §23§-módulo invertible amplio para §24§. Entonces
§25§
es una §26§-álgebra graduada en grados positivos cuasicoherente y de tipo finito, y existe un §27§-isomorfismo
§28§
tal que §29§ sea isomorfo (como §30§-álgebra graduada) a §31§.
\end{enumerate}
\end{proposition}

\begin{proof}
(i) Todas las aserciones ya han sido prácticamente demostradas, no siendo la última sino un caso particular de (\hyperref[III.2.3.1-fr]{2.3.1}). El hecho de que §32§ es periódico se ha visto en (\textbf{II}, 8.14.14) y el hecho de que hay un período §33§ tal que §34§ sea invertible y §35§-amplio no es sino (\textbf{II}, 4.6.18). Finalmente, para §36§, §37§ es un §38§-módulo de tipo finito (\textbf{II}, 8.14.14), por tanto cada uno de los §39§ es un §40§-módulo cuasicoherente de tipo finito en virtud de (\textbf{II}, 2.1.6, (ii)), siendo la cuestión local; como §41§ es coherente, lo mismo ocurre con los §42§.

(ii) Reemplazando, si es preciso, el período §43§ por uno de sus múltiplos, se puede suponer que §44§ es un §45§-módulo \emph{muy amplio} relativamente a §46§ (\textbf{II}, 4.6.11). Se tiene además
§47§
se sabe (\textbf{II}, 3.1.8 y 3.2.9) que hay un §48§-isomorfismo §49§ de §50§ sobre §51§ tal que
\oldpage[III]{105}
§52§
Se establecerá, pues, la existencia de un §53§-isomorfismo §54§ si se demuestra la

\begin{proposition}[2.3.4.1]
\label{III.2.3.4.1-fr}
Sean §55§ un preesquema noetheriano, §56§ un morfismo proyectivo, §57§ un §58§-módulo invertible muy amplio para §59§. Entonces §60§ es una §61§-álgebra graduada cuasicoherente de tipo finito, tal que §62§ para §63§ suficientemente grande, y existe un §64§-isomorfismo §65§ tal que §66§.
\end{proposition}

Como §67§ es un morfismo proyectivo, resulta de (\textbf{II}, 5.4.4 y 4.4.7) que existe un §68§-isomorfismo §69§, donde §70§ es una §71§-álgebra cuasicoherente tal que §72§ sea un §73§-módulo de tipo finito y engendre §74§, y se tiene §75§. Se tiene entonces
§76§
donde §77§ es el morfismo estructural, y resulta de (\hyperref[III.2.3.1-fr]{2.3.1}) que para §78§ suficientemente grande, el homomorfismo canónico §79§ es \emph{biyectivo}; como §80§, se tiene \emph{a fortiori} §81§ en cuanto §82§ es suficientemente grande. Además, como el homomorfismo canónico §83§ de §84§-álgebras graduadas es un \textbf{(TN)}-isomorfismo,
\phantomsection\label{III.2.3.5.1-fr}
§85§
es un isomorfismo (\textbf{II}, 3.6.1) y se tiene §86§ (\textbf{II}, 3.5.2); pero como los §87§-módulos graduados §88§ y §89§ son \textbf{(TN)}-isomorfos, se tiene §90§ para todo §91§ (\textbf{II}, 3.4.2); para terminar de demostrar (\hyperref[III.2.3.4.1-fr]{2.3.4.1}), queda por mostrar que §92§ es una §93§-álgebra de tipo finito; ahora bien, los §94§ son §95§-módulos \emph{coherentes} en virtud de (\hyperref[III.2.2.1-fr]{2.2.1}) y como §96§ para §97§, §98§ está engendrada por §99§, que es coherente, de donde nuestra aserción (\textbf{I}, 9.6.2).

Volvamos a la demostración de (\hyperref[III.2.3.4-fr]{2.3.4}), cuyas notaciones retomamos. Hemos demostrado la existencia de un §100§-isomorfismo §101§ tal que §102§ para todo §103§; denotaremos por §104§ el morfismo estructural §105§. Observemos ahora que §106§ es suma directa de los §107§-módulos graduados §108§; cada uno de estos últimos es un §109§-módulo cuasicoherente de tipo finito, en virtud de la periodicidad de §110§ y de la hipótesis de que los §111§ son §112§-módulos de tipo finito (\textbf{II}, 8.14.12). Pongamos §113§, de modo que los §114§ son §115§-módulos graduados cuasicoherentes de tipo finito; por consiguiente (\textbf{II}, 8.14.8), el homomorfismo canónico
§116§
es un isomorfismo de §117§-módulos. Pero se tiene §118§ y para §119§, este último §120§-módulo es por definición igual a §121§. Es decir, la inyección canónica §122§ es un \textbf{(TN)}-isomorfismo, por tanto (\textbf{II}, 3.4.2) se tiene §123§ y por consiguiente §124§. Basta observar que §125§ salvo un isomorfismo canónico (\textbf{II}, 8.14.13.1) para haber demostrado la isomorfía de §126§ y de §127§. Finalmente, en virtud de (\hyperref[III.2.3.2-fr]{2.3.2}), cada uno de los §128§ satisface la condición \textbf{(TF)}, por tanto lo mismo ocurre con cada uno de los §129§; además, como los §130§ son coherentes, lo mismo ocurre con los §131§ por (\hyperref[III.2.2.1-fr]{2.2.1}), y se concluye inmediatamente que los §132§ son §133§-módulos de tipo finito. Como se ha visto en (\hyperref[III.2.3.4.1-fr]{2.3.4.1}) que §134§ es una §135§-álgebra de tipo finito, se concluye que §136§ es también una §137§-álgebra de tipo finito.
\end{proof}

\oldpage[III]{106}

''',
('1','2.3.5'):r'''\begin{proposition}[2.3.5]
\label{III.2.3.5-fr}
Sean §0§ un preesquema íntegro noetheriano, §1§ un preesquema íntegro, §2§ un morfismo \textup{proyectivo birracional}. Existe entonces un ideal fraccionario coherente §3§ \textup{(\textbf{II}, 8.1.2)} tal que §4§ sea §5§-isomorfo al preesquema obtenido por explosión de §6§ \textup{(\textbf{II}, 8.1.3)}. Además, existe un abierto §7§ de §8§ tal que la restricción de §9§ a §10§ sea un isomorfismo de §11§ sobre §12§ \textup{(cf. \textbf{I}, 6.5.5)}, y que §13§ sea invertible.
\end{proposition}

\begin{proof}
Como existe un §14§-módulo invertible §15§ muy amplio para §16§ (\textbf{II}, 4.4.2 y 5.3.2), se puede aplicar (\hyperref[III.2.3.4.1-fr]{2.3.4.1}), y se ve que §17§ se identifica con §18§, donde §19§. Se sabe además que los §20§ son §21§-módulos sin torsión (\textbf{I}, 7.4.5), por tanto lo mismo ocurre con el §22§-módulo §23§, y por consiguiente §24§ se identifica canónicamente con un sub-§25§-módulo de §26§ (\textbf{I}, 7.4.1); este último es un haz \emph{simple} (\textbf{I}, 7.3.6) que queda determinado cuando se conoce su restricción a un abierto no vacío, por ejemplo a un abierto no vacío §27§ tal que §28§ sea isomorfo a §29§. Como por hipótesis los §30§ son entonces isomorfos a §31§, se ve que §32§ es un §33§-módulo isomorfo a §34§, donde §35§ es una indeterminada, y §36§ es \textbf{(TN)}-isomorfo a la sub-§37§-álgebra engendrada por la imagen canónica de §38§ en §39§ (\hyperref[III.2.3.4.1-fr]{2.3.4.1}); pero si se identifica §40§ con §41§, la imagen de §42§ se identifica con §43§, donde §44§ es un sub-§45§-módulo coherente (\hyperref[III.2.2.1-fr]{2.2.1}) de §46§, cuya restricción a §47§ es isomorfa a §48§, y que por consiguiente es tal que §49§ sea invertible. Se ve entonces que §50§ es \textbf{(TN)}-isomorfo a §51§, lo que termina la demostración.
\end{proof}

'''}
apply_units(D)

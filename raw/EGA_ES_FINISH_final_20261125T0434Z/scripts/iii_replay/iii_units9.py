import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('7','7.2.2'):r'''\begin{env}[7.2.2]
Sea §0§ un funtor covariante aditivo. Vamos
a definir, para todo §1§-módulo por la izquierda §2§, un \emph{homomorfismo canónico
funtorial en} §3§, \emph{de} §4§-\emph{módulos}
§5§

Para ello bastará, en virtud de (7.2.1), definir un
§6§-homomorfismo §7§ de §8§ en
§9§, tal que se tenga
§10§ para §11§, §12§ y §13§.
Observemos para ello que
§14§ está canónicamente provisto de una
estructura de §15§-módulo por la izquierda procedente de la estructura de §16§-módulo por la
derecha de §17§, siendo la ley externa tal que si
§18§, §19§,
§20§ para §21§.
Dicho esto, definiremos §22§ como compuesto de los dos homomorfismos
canónicos
§23§
siendo la segunda flecha la aplicación §24§, la primera
el isomorfismo canónico de §25§-módulos §26§ tal que
§27§ para §28§, §29§. Se tiene
§30§, luego
§31§
y por tanto, para §32§,
§33§
por definición de la ley externa sobre §34§, lo que prueba la existencia de
§35§; es inmediato verificar que este homomorfismo es funtorial en
§36§, es decir, que para todo homomorfismo §37§ de §38§-módulos por la
izquierda, el diagrama
§39§
es conmutativo.

La funtorialidad del homomorfismo (7.2.2.1) muestra que cuando §40§ es
\emph{conmutativo}, es un homomorfismo de §41§-\emph{módulos} (cf. (7.1.2)).
\end{env}

''',
('7','7.2.5'):r'''\begin{proposition}[7.2.5]
Sea §0§ un funtor covariante aditivo de §1§ en
§2§, que conmuta con las sumas directas. Las condiciones siguientes son
equivalentes:
\begin{enumerate}
  \item[a)] §3§ es exacto por la derecha.
  \item[b)] El homomorfismo canónico §4§ \textup{(7.2.2.1)} es un isomorfismo para
    todo §5§-módulo por la izquierda §6§.
  \item[§7§)] §8§ es semiexacto y el homomorfismo §9§ es sobreyectivo para
    todo §10§-módulo por la izquierda §11§.
  \item[c)] §12§ es isomorfo a un funtor en §13§ de la forma
    §14§, donde §15§ es un §16§-módulo por la derecha.
\end{enumerate}
\end{proposition}

\begin{proof}
Está claro que §17§ implica §18§ y que §19§ implica §20§; mostremos que
§21§ implica §22§.
\oldpage[III]{179}
Pongamos
§23§
para todo §24§-módulo por la izquierda §25§. Existe una sucesión exacta
§26§,
donde §27§ y §28§ son dos §29§-módulos por la izquierda \emph{libres}; como §30§ y §31§ son
exactos por la derecha, se tiene pues el diagrama conmutativo
§32§
donde las dos filas son exactas; como §33§ y §34§ son
isomorfismos en virtud de (7.2.4), lo mismo ocurre con §35§ por el lema de los
cinco. Finalmente, está claro que §36§ implica §37§. Para mostrar que §38§
implica §39§, basta probar el
\end{proof}

\begin{lemma}[7.2.5.1]
Sean §40§, §41§ dos categorías abelianas, §42§, §43§ dos
funtores covariantes aditivos de §44§ en §45§,
§46§ un morfismo funtorial \textup{(T, I, 1.2)} tal que, para todo objeto §47§
de la categoría §48§,
§49§
es un epimorfismo. Entonces, si §50§ es exacto por la derecha y §51§ semiexacto,
§52§ es exacto por la derecha.
\end{lemma}

\begin{proof}
Todo se reduce en efecto a demostrar que para todo epimorfismo
§53§ en §54§,
§55§
es un epimorfismo; ahora bien, se tiene el diagrama conmutativo
§56§
en el cual §57§, §58§ y §59§ son epimorfismos; lo mismo ocurre pues
con §60§.
\end{proof}

''',
('7','7.3.5'):r'''\begin{proposition}[7.3.5]
Supongamos que §0§ es un anillo artiniano por la izquierda cuyo cociente por su
radical §1§ es un cuerpo §2§. Entonces las condiciones de \textup{(7.3.3)} son
también equivalentes a cada una de las siguientes:
\begin{enumerate}
  \item[g)] El homomorfismo canónico
    §3§
    es un epimorfismo para §4§ y §5§.
  \item[h)] §6§ es un epimorfismo y §7§ es un
    §8§-módulo por la derecha plano \textup{(o, lo que equivale a lo mismo (Bourbaki,
    \emph{Alg. comm.}, cap. II, \S 3, n\textsuperscript{o} 2, cor. 2 de la
    prop. 5), un §9§-módulo} libre).
\end{enumerate}
Supongamos además que §10§ es conmutativo y el §11§-módulo §12§ de
longitud finita §13§. Entonces las condiciones anteriores equivalen también a
cada una de las siguientes:
\begin{enumerate}
  \item[i)] Para todo §14§-módulo §15§ de longitud finita, se tiene
    §16§
  \item[j)] Se tiene
    §17§
\end{enumerate}
\end{proposition}

La equivalencia de §18§ y §19§ con las condiciones de (7.3.3) se deduce inmediatamente
de (7.2.7). Para demostrar las demás afirmaciones, utilizaremos el lema
siguiente:

\begin{lemma}[7.3.5.3]
Sean §20§, §21§ dos categorías abelianas,
§22§ un funtor
covariante aditivo; se supone que §23§ es semiexacto, y que, para todo objeto
simple §24§ de §25§, §26§ es un objeto de longitud finita en
§27§. Entonces, para todo objeto §28§ de longitud finita en §29§,
§30§ es de longitud finita en §31§. Para toda sucesión exacta
§32§
de objetos de longitud finita en §33§, se tiene
§34§
y para que los dos miembros de \textup{(7.3.5.4)} sean iguales, es necesario y suficiente
que la sucesión
§35§
sea exacta.
\end{lemma}

\begin{proof}
En efecto, la sucesión
§36§
es exacta por hipótesis; si se supone §37§ y §38§ de longitud
finita, lo mismo ocurre con §39§ y con
§40§ y como
§41§, §42§ es de longitud
finita y se tiene
§43§

\oldpage[III]{183}
Por inducción sobre la longitud de §44§, esto prueba ya la primera afirmación;
además, los dos miembros de (7.3.5.5) solo pueden ser iguales si
§45§
(lo que equivale a
§46§, o
§47§) y
§48§
(lo que equivale a
§49§, o
§50§).
\end{proof}

Observemos ahora que si §51§ es un §52§-módulo de longitud finita (siendo §53§
conmutativo), los cocientes de una sucesión de Jordan-Hölder de §54§ son
necesariamente isomorfos al §55§-módulo §56§, luego se deduce de (7.3.5.4), por
inducción sobre la longitud de §57§,
§58§

Además, resulta de (7.3.5.3) que si §59§ es exacto, se tiene la igualdad
(7.3.5.1); luego la condición §60§ de (7.3.3) implica §61§; está claro que
§62§ implica §63§, y queda por probar el

\begin{lemma}[7.3.5.7]
La relación
§64§
implica que §65§ es un epimorfismo y §66§ es un
§67§-módulo plano.
\end{lemma}

\begin{proof}
En efecto, partiendo de la sucesión exacta
§68§,
resulta de (7.3.5.4) y (7.3.5.6) que se tiene
§69§
y que la igualdad solo puede darse (7.3.5.3) si la sucesión
§70§
es exacta. En virtud de (7.2.7) y (7.2.5), §71§ es isomorfo a un funtor
§72§, y la exactitud de la sucesión (7.3.5.8) muestra, en virtud
de la sucesión exacta de los §73§, que se tiene
§74§. Se concluye que §75§ es un
§76§-módulo plano (\textbf{0}, 10.1.3).
\end{proof}

''',
('7','7.3.10'):r'''\begin{corollary}[7.3.10]
Supongamos que §0§ verifica las condiciones generales de \textup{(7.3.7)} y
conmuta con los límites inductivos, que §1§ es conmutativo y noetheriano y los
§2§ son §3§-módulos de tipo finito. Entonces, para todo entero §4§, existe
un abierto denso §5§ de §6§ tal que, para todo §7§,
la función
§8§
es constante en §9§.
\end{corollary}

\begin{proof}
Sea §10§ un ideal primo minimal de §11§; por hipótesis, el anillo
§12§ es íntegro y §13§ se identifica con una
componente irreducible del espacio topológico §14§. Vamos
a mostrar por inducción sobre §15§ que existe
§16§ tal que si se pone §17§, §18§ es \emph{exacto} y
los §19§ son §20§-módulos \emph{de tipo finito} para §21§. La proposición es
verdadera para §22§ en virtud de la hipótesis, tomando §23§ (luego
§24§), pues al ser entonces §25§ exacto, §26§ es isomorfo a
§27§, luego es un §28§-módulo (y \emph{a fortiori} un
§29§-módulo) de tipo finito. Razonemos por inducción sobre §30§; §31§ es la imagen
canónica en §32§ de un elemento §33§, y si se pone §34§, se tiene
§35§ donde §36§ es un ideal primo minimal de §37§,
igual a §38§. Como se tiene
§39§,
los §40§ son §41§-módulos de tipo finito, luego el funtor
§42§ verifica las mismas hipótesis que §43§, pero
reemplazando §44§ por §45§. Se puede pues limitar al caso en que §46§, y §47§
es exacto; la sucesión exacta
§48§
da entonces la sucesión exacta
§49§,
y como §50§ es exacto, la última flecha de la derecha es inyectiva, luego
§51§ es un cociente de §52§ y es por tanto de
tipo finito. Observemos ahora que el razonamiento de (7.3.9) solo utilizó el hecho
de que los §53§ son de tipo finito para §54§; se puede pues aplicar
al anillo íntegro §55§, al funtor §56§ y a §57§, lo que
termina el razonamiento por inducción. Dicho esto, hay un
§58§ tal que §59§ es un abierto §60§
denso en §61§ que no interseca ninguna otra
componente irreducible de §62§. Si la proposición queda
\oldpage[III]{185}
demostrada para §63§, se tendrá un abierto §64§ denso en §65§ en
el que las funciones del enunciado serán constantes, puesto que
§66§ para todo §67§. Haciendo el mismo razonamiento para
toda componente irreducible de §68§, el corolario quedará
demostrado. Se puede pues limitar al caso en que §69§ es \emph{íntegro}; el razonamiento de
(7.3.9) prueba entonces la existencia de un §70§ tal que los §71§
son §72§-módulos \emph{libres} de tipo finito para §73§, lo que implica
la conclusión de (7.3.10) en virtud de (7.3.4).
\end{proof}

''',
('7','7.3.11'):r'''\begin{proposition}[7.3.11]
Sean §0§ un anillo conmutativo local, §1§ su cuerpo residual, §2§ un
funtor homológico covariante de §3§ en §4§,
que conmuta con las sumas directas. Se supone que existe §5§ tal que §6§ es
exacto para §7§, y que todos los §8§ son §9§-módulos de
presentación finita. Entonces las condiciones equivalentes §10§, §11§, §12§ de
\textup{(7.3.7)} implican las dos siguientes, y son equivalentes a ellas cuando
el anillo es además reducido:
\begin{enumerate}
  \item[d)] Para todo §13§, se tiene
    §14§
    para §15§.
  \item[§16§)] Para todo punto genérico §17§ de una componente irreducible
    de §18§, se tiene
    §19§
\end{enumerate}
\end{proposition}

\begin{proof}
Como §20§ es un §21§-módulo de presentación finita, la condición §22§ de
(7.3.7) equivale a decir que §23§ es un §24§-módulo \emph{libre} para §25§
(Bourbaki, \emph{Alg. comm.}, cap. II, \S 3, n\textsuperscript{o} 2, cor. 2
de la prop. 5); la condición §26§ implica que
§27§ para §28§,
luego las condiciones equivalentes de (7.3.7) implican §29§, y es trivial
que §30§ implica §31§. Queda por probar que §32§ implica §33§ cuando §34§
es \emph{reducido}. Razonemos por inducción sobre §35§, puesto que §36§ es exacto
para §37§. Supongamos pues §38§ exacto para §39§ y mostremos que
§40§ es un §41§-módulo \emph{libre}. En virtud de la hipótesis de inducción,
§42§ es isomorfo a §43§ para todo §44§-módulo §45§,
por la condición §46§ de (7.3.7) y (7.3.3); aplicando esta propiedad a
§47§ y §48§, se obtiene, en virtud de la hipótesis §49§, que
§50§
para todo §51§; pero esto implica que §52§ es libre (Bourbaki,
\emph{Alg. comm.}, cap. II, \S 3, n\textsuperscript{o} 2, prop. 7), lo que
termina la demostración.
\end{proof}

Los resultados anteriores se mejorarán considerablemente para los funtores
homológicos del tipo particular que vamos a estudiar en (7.4); se
obtendrán en efecto criterios de exactitud en los que solo interviene \emph{uno solo}
de los §53§.

\subsection{Criterios de exactitud para los funtores
§54§.}
\label{subsection:III.7.4.fr}

''',
('7','7.4.2'):r'''\begin{proposition}[7.4.2]
Bajo las condiciones generales de \textup{(7.4.1)}, y para un entero §0§
dado, las propiedades siguientes son equivalentes:
\begin{enumerate}
  \item[a)] §1§ es exacto por la izquierda \textup{(o, lo que equivale a lo mismo,} §2§
    es exacto por la derecha).
  \item[b)] §3§
    es un §4§-módulo por la derecha plano.
  \item[c)] Existe un complejo §5§ de §6§-módulos por la derecha planos
    tal que la diferencial
    §7§
    es nula, y un isomorfismo de funtores homológicos de
    §8§ sobre
    §9§.
\end{enumerate}
\end{proposition}

\begin{proof}
Por definición se tiene una sucesión exacta funtorial en §10§
§11§
donde
§12§
en virtud de la exactitud por la derecha del producto tensorial. Para todo homomorfismo
§13§, se tiene pues un diagrama conmutativo
§14§
cuyas filas son exactas. Si §15§ es un monomorfismo, lo mismo ocurre
con §16§ puesto que §17§ es plano; si §18§ es exacto por la izquierda, §19§ es
también un monomorfismo; se concluye que §20§ es un monomorfismo, lo que
implica que §21§ es plano. Recíprocamente, si es así, §22§
es un monomorfismo para todo monomorfismo §23§, luego el diagrama
(7.4.2.1) muestra que §24§ es un monomorfismo, y por tanto §25§ (que ya es
semiexacto) es exacto por la izquierda. Así, §26§ y §27§ son equivalentes. Es
inmediato que §28§ implica §29§, pues si
§30§ es nula, y
§31§ es una sucesión exacta de §32§-módulos, el operador
borde en la sucesión exacta
§33§
\oldpage[III]{187}
es nulo por definición (M, IV, 1), luego §34§ es exacto por la izquierda. Mostremos
recíprocamente que §35§ implica §36§. Si
§37§,
se tiene una sucesión exacta
§38§
en la cual §39§ y §40§ son planos, luego
§41§ es plano (§42§, 6.1.2). Se tomará
§43§
como diferencial §44§, se tomará la del complejo
§45§ para §46§ y §47§, §48§ para §49§ y para §50§
el homomorfismo §51§ deducido de §52§ por paso al
cociente. Como los §53§ son planos, se tiene
§54§
(poniendo §55§); se deducen
inmediatamente para todo §56§ isomorfismos funtoriales
§57§
para todo §58§, y la verificación del hecho de que se trata de un isomorfismo de
§59§-funtores se deduce sin dificultad de la definición de §60§
(M, IV, 1).
\end{proof}

Se observará que las condiciones de (7.4.2) implican también que
§61§ es \emph{plano}, pues se tiene una sucesión exacta
§62§,
en la cual §63§ y §64§ son planos (§65§, 6.1.2).

'''
})

import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','3.1.2'):r'''\begin{theorem}[3.1.2]
\label{III.3.1.2-fr}
Sea §0§ un preesquema noetheriano; se designa por §1§ la categoría abeliana
de los §2§-Módulos coherentes. Sean §3§ un subconjunto exacto de
§4§, §5§ una parte cerrada del espacio subyacente a §6§. Se supone que
para toda parte cerrada irreducible §7§ de §8§, de punto genérico §9§,
existe un §10§-Módulo §11§ de soporte §12§ tal que §13§ es
un §14§-espacio vectorial de dimensión §15§. Entonces todo §16§-Módulo
coherente de soporte contenido en §17§ pertenece a §18§ (y en particular,
si §19§, se tiene §20§).
\end{theorem}

\begin{proof}
Consideremos la propiedad siguiente §21§ de una parte cerrada §22§ de §23§:
todo §24§-Módulo coherente de soporte contenido en §25§ pertenece a
§26§. En virtud del principio de inducción noetheriana (\textbf{0}\textsubscript{I},
2.2.2), se ve que se está reducido a demostrar que \emph{si §27§ es una parte
cerrada de §28§ tal que la propiedad §29§ es verdadera para toda parte
cerrada §30§ de §31§, distinta de §32§, entonces §33§ es verdadera}.

Sea pues §34§ de soporte contenido en §35§ y probemos que
§36§. Designemos también por §37§ el subpreesquema cerrado reducido de
§38§ cuyo espacio subyacente es §39§ (\textbf{I}, 5.2.1); está definido por un Ideal
coherente §40§ de §41§. Se sabe (\textbf{I}, 9.3.4) que existe un
entero §42§ tal que §43§; para §44§ se tiene
pues una sucesión exacta
§45§
de §46§-Módulos coherentes (\textbf{0}\textsubscript{I}, 5.3.6 y 5.3.3);
como §47§ es exacto, se ve, por inducción sobre §48§, que basta mostrar
que cada uno de los
§49§ está en
§50§. Se está pues reducido a probar que §51§ bajo la hipótesis
suplementaria de que §52§; equivale a decir que
§53§, donde §54§ es la inclusión canónica
§55§. Distingamos ahora dos casos:
\begin{enumerate}
\item[\textit{a)}] §56§ es \emph{reducible}. Sean §57§, siendo §58§ y §59§
partes cerradas de §60§, distintas de §61§; sean también §62§,
§63§ los subpreesquemas cerrados reducidos de §64§ cuyos espacios
subyacentes son §65§, §66§ respectivamente, que están definidos respectivamente por
los Ideales coherentes §67§, §68§ de §69§. Pongamos
§70§,
§71§.
Los homomorfismos canónicos §72§,
§73§ definen pues un homomorfismo
§74§. Mostremos que para todo
§75§ el homomorfismo
§76§ es \emph{biyectivo}.
En efecto, se tiene §77§, pues la cuestión es
local y
\oldpage[III]{116}
la igualdad anterior resulta de (\textbf{I}, 5.2.1 y 1.1.5); si §78§, se tiene
pues §79§, de donde §80§ y
§81§, lo que establece nuestra afirmación en este caso; se razona
del mismo modo si §82§. Por tanto, el núcleo y el conúcleo de §83§, que están
en §84§ (\textbf{0}\textsubscript{I}, 5.3.4), tienen sus soportes en §85§,
y están pues en §86§ por hipótesis; por la misma razón, §87§ y
§88§ están en §89§, luego también §90§,
puesto que §91§ es exacto. La conclusión resulta entonces de considerar las
dos sucesiones exactas
§92§
§93§
y de la hipótesis de que §94§ es exacto.

\item[\textit{b)}] §95§ es irreducible, y por tanto el subpreesquema §96§ de §97§ es
\emph{íntegro}. Si §98§ es su punto genérico, se tiene
§99§, y como §100§ es un
§101§-Módulo coherente, §102§ es un
§103§-espacio vectorial de dimensión finita §104§. Por hipótesis, hay un
§105§-Módulo coherente §106§ (necesariamente de soporte §107§)
tal que §108§ es un §109§-espacio vectorial de dimensión §110§. Por
tanto, hay un §111§-isomorfismo
§112§, que es también un
§113§-isomorfismo, y como §114§ y §115§ son
coherentes, existe una vecindad abierta §116§ de §117§ en §118§ y un
isomorfismo §119§
(\textbf{0}\textsubscript{I}, 5.2.7). Sea §120§ el grafo de este isomorfismo,
que es un sub-§121§-Módulo coherente de
§122§, canónicamente isomorfo a
§123§ y a §124§; existe pues un sub-§125§-%
Módulo coherente §126§ de §127§, que induce
§128§ sobre §129§ y §130§ sobre §131§ puesto que §132§ y
§133§ tienen por soporte §134§ (\textbf{I}, 9.4.7). Las restricciones
§135§ y §136§ de las
proyecciones canónicas de §137§ son entonces
homomorfismos de §138§-Módulos coherentes, que en §139§ y en
§140§ se reducen a isomorfismos; en otros términos, los núcleos y
conúcleos de §141§ y §142§ tienen su soporte en el conjunto cerrado
§143§, distinto de §144§. Pertenecen pues a §145§; por otra
parte, se tiene §146§ puesto que §147§ y §148§ es
exacto. Se concluye sucesivamente, por la exactitud de §149§, que
§150§ y después que §151§. C.Q.D.
\end{enumerate}
\end{proof}

''',
('1','3.2.1'):r'''\begin{theorem}[3.2.1]
\label{III.3.2.1-fr}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo
propio. Para todo §2§-Módulo coherente §3§, los
§4§-Módulos §5§ son coherentes para §6§.
\end{theorem}

\begin{proof}
Al ser la cuestión local sobre §7§, se puede suponer §8§ noetheriano, luego §9§
noetheriano (\textbf{I}, 6.3.7). Los §10§-Módulos coherentes §11§ para
los cuales la conclusión del teorema (\hyperref[III.3.2.1-fr]{3.2.1}) es verdadera
forman un subconjunto \emph{exacto} §12§ de la categoría §13§ de los
§14§-Módulos coherentes.
\oldpage[III]{117}
En efecto, sea
§15§ una sucesión exacta de
§16§-Módulos coherentes; supongamos por ejemplo que §17§
y §18§ pertenecen a §19§; se tiene la sucesión exacta de cohomología
§20§
en la que, por hipótesis, los cuatro términos extremos son coherentes;
lo mismo ocurre pues con el término central §21§ por
(\textbf{0}\textsubscript{I}, 5.3.4 y 5.3.3). Se muestra de la misma manera que
cuando §22§ y §23§ (resp. §24§ y
§25§) están en §26§, lo mismo ocurre con §27§ (resp.
§28§). Además, todo \emph{factor directo} coherente §29§
de un §30§-Módulo §31§ pertenece también a §32§: en
efecto, §33§ es entonces factor directo de
§34§ (G, II, 4.4.4), luego es de tipo finito, y como es
cuasicoherente (\hyperref[III.1.4.10-fr]{1.4.10}), es coherente, al ser §35§
noetheriano. En virtud de (\hyperref[III.3.1.3-fr]{3.1.3}), se está
reducido a probar que cuando §36§ es \emph{irreducible} de punto genérico
§37§, existe \emph{un} §38§-Módulo coherente §39§ que pertenece a
§40§, tal que §41§: en efecto, si se establece este punto, se
podrá aplicar a todo subpreesquema cerrado irreducible §42§ de §43§, pues
si §44§ es la inclusión canónica, §45§ es propio (\textbf{II}, 5.4.2),
y si §46§ es un §47§-Módulo coherente de soporte §48§,
§49§ es un §50§-Módulo coherente tal que
§51§
(G, II, 4.9.1), luego se está efectivamente en las condiciones de aplicación de
(\hyperref[III.3.1.3-fr]{3.1.3}).

Ahora bien, en virtud del lema de Chow (\textbf{II}, 5.6.2), existe un preesquema
irreducible §52§ y un morfismo \emph{proyectivo} y sobreyectivo
§53§ tal que §54§ es \emph{proyectivo}. Existe un
§55§-Módulo §56§ amplio para §57§ (\textbf{II}, 5.3.1);
apliquemos el teorema fundamental de los morfismos proyectivos
(\hyperref[III.2.2.1-fr]{2.2.1}) a §58§ y a §59§:
existe pues un entero §60§ tal que
§61§ es un §62§-Módulo coherente
y §63§ para todo §64§; además, como
§65§
es sobreyectivo para §66§ suficientemente grande (\hyperref[III.2.2.1-fr]{2.2.1}), se
ve que se puede suponer que, en el punto genérico §67§ de §68§, se tiene
§69§ (\textbf{II}, 3.4.7). Por otra parte, como §70§ es
proyectivo y §71§ noetheriano, los
§72§ son \emph{coherentes}
(\hyperref[III.2.2.1-fr]{2.2.1}). Dicho esto,
§73§ es el resultado de una sucesión
espectral de Leray, cuyo término §74§ viene dado por
§75§
lo anterior muestra que esta sucesión espectral es degenerada, y se sabe
entonces (\textbf{0}, 11.1.6) que §76§ es isomorfo a
§77§, lo que termina la demostración.
\end{proof}

''',
('1','4.1.7'):r'''\begin{corollary}[4.1.7]
\label{III.4.1.7-fr}
Siendo las hipótesis las de \textup{(\hyperref[III.4.1.5-fr]{4.1.5})}, supongamos
además §0§, donde §1§ es noetheriano, y
§2§, donde §3§ es un ideal de
§4§, de modo que
§5§.
El homomorfismo canónico
§6§
(donde el primer miembro es el separado completado de §7§ para
la topología §8§-preádica) es un isomorfismo. El sistema
proyectivo §9§ verifica para todo §10§ la
condición \textup{(ML)}, y el homomorfismo canónico
§11§
es un isomorfismo. Finalmente, la filtración sobre §12§, definida
por los núcleos de los homomor%
\oldpage[III]{126}
fismos canónicos
§13§, es §14§-buena
\textup{(\textbf{0}, 13.7.7)} y §15§ es un isomorfismo topológico\footnote{La demostración que sigue, más sencilla que la demostración
inicial, y el complemento relativo a la filtración de
§16§, nos fueron comunicados por J.-P. Serre.}.
\end{corollary}

\begin{proof}
Al estar fijado el entero §17§ en esta demostración, pondremos para
simplificar
§18§
§19§

La sucesión exacta de cohomología
§20§
muestra que se tiene también
§21§;
pondremos
§22§

Se tiene pues la sucesión exacta
§23§

\begin{env}[4.1.7.7]
\label{III.4.1.7.7-fr}
Sea §24§ un elemento de §25§ (§26§); la multiplicación por
§27§ en §28§ es un homomorfismo
§29§, y da lugar
por tanto a un homomorfismo
§30§

Si se designa por §31§ la §32§-álgebra graduada
§33§, se sabe que las multiplicaciones
§34§ definen sobre
§35§ una
estructura de \emph{módulo graduado de tipo finito} sobre el anillo graduado §36§
(\hyperref[III.3.3.2-fr]{3.3.2}), que es \emph{noetheriano} (\textbf{II}, 2.1.5).
\end{env}

\begin{lemma}[4.1.7.9]
\label{III.4.1.7.9-fr}
Los submódulos §37§ de §38§ definen sobre §39§
una filtración §40§-buena.
\end{lemma}

\begin{proof}
En primer lugar, mostremos que se tiene
§41§
siendo pues la multiplicación en §42§ por un elemento
§43§ la aplicación §44§.

Para todo
§45§, el diagrama
§46§
\oldpage[III]{127}
(donde las flechas horizontales son la multiplicación por §47§, y las
flechas verticales las inclusiones canónicas) es conmutativo; luego el
diagrama correspondiente
§48§
es conmutativo, lo que, teniendo en cuenta la interpretación de §49§
como imagen de
§50§, prueba
(\hyperref[III.4.1.7.10-fr]{4.1.7.10}) y muestra además que el §51§-módulo
graduado §52§ es un \emph{cociente} del
sub-§53§-módulo
§54§ de
§55§; la observación hecha más arriba muestra pues que §56§ es
un §57§-módulo \emph{de tipo finito}, lo que equivale a la afirmación de
(\hyperref[III.4.1.7.9-fr]{4.1.7.9}) (Bourbaki, \emph{Alg. comm.},
cap. III, §~3, n\textsuperscript{o}~1, teorema~1).
\end{proof}

\begin{env}[4.1.7.12]
\label{III.4.1.7.12-fr}
Consideremos ahora el §58§-módulo graduado
§59§
definido como en (4.1.7.8); es también un §60§-módulo \emph{de tipo finito} en
virtud de (\hyperref[III.3.3.2-fr]{3.3.2}); se tiene
§61§ para todo §62§ por
(\hyperref[III.4.1.7.5-fr]{4.1.7.5}) y el diagrama
(\hyperref[III.4.1.7.11-fr]{4.1.7.11}), donde se reemplaza §63§ por §64§,
muestra que
§65§.
En otros términos, §66§ es un \emph{sub-§67§-módulo graduado} de §68§,
y por tanto es \emph{de tipo finito}.
\end{env}

\begin{env}[4.1.7.13]
\label{III.4.1.7.13-fr}
Designemos por §69§ la inclusión canónica
§70§, que se puede escribir §71§. Como
§72§, el §73§-módulo
§74§ está anulado por §75§; como
§76§ es la imagen del §77§-homomorfismo
§78§,
§79§, como §80§-módulo, está también anulado por
§81§; esto significa también que, en el §82§-\emph{módulo}
§83§, se tiene
§84§

Como §85§ es un §86§-módulo de tipo finito, existe un entero
§87§ y un entero §88§ tales que
§89§ para §90§ (\textbf{II}, 2.1.6, (ii));
se deduce de esta relación y de
(\hyperref[III.4.1.7.14-fr]{4.1.7.14}) que existe un entero §91§ tal
que
§92§
\end{env}

\begin{env}[4.1.7.16]
\label{III.4.1.7.16-fr}
Observemos ahora que la inclusión canónica
§93§ da, pasando
a la cohomología, un §94§-homomorfismo
§95§
y, para todo §96§, se tiene evidentemente la factorización
§97§
\oldpage[III]{128}
de donde se concluye que, para todo sub-§98§-módulo §99§ de
§100§, se tiene, en el §101§-módulo
§102§,
§103§
\end{env}

\begin{lemma}[4.1.7.20]
\label{III.4.1.7.20-fr}
Existe un entero §104§ tal que §105§ para todo
§106§.
\end{lemma}

\begin{proof}
Tomemos en efecto como §107§ un múltiplo de §108§ que sea §109§; como
§110§ para §111§, se tiene en virtud de
(\hyperref[III.4.1.7.19-fr]{4.1.7.19}) y
(\hyperref[III.4.1.7.15-fr]{4.1.7.15})
§112§.
\end{proof}

\begin{env}[4.1.7.21]
\label{III.4.1.7.21-fr}
Observemos que del diagrama conmutativo
§113§
procedente a su vez del diagrama conmutativo
§114§
donde las flechas verticales son las aplicaciones canónicas, se deduce un
diagrama conmutativo
§115§
donde las filas son exactas. Como la última flecha vertical es nula
para §116§ (\hyperref[III.4.1.7.20-fr]{4.1.7.20}), la imagen de
§117§ en §118§ está contenida en
§119§, pero por otra parte
contiene §120§ por la conmutatividad
del diagrama, luego es igual a él; lo mismo ocurre pues con las imágenes
en §121§ de los §122§ para §123§, lo que demuestra
la condición (ML) para el sistema proyectivo §124§. Además,
para todo abierto afín §125§ de §126§ se tiene
§127§ para §128§
(\hyperref[III.1.3.1-fr]{1.3.1}), y para §129§ la aplicación
§130§ es sobreyectiva
(\textbf{I}, 1.3.9). Se puede pues apli%
\oldpage[III]{129}
car (\textbf{0}, 13.3.1), y el homomorfismo canónico
§131§ es \emph{biyectivo} para todo §132§.

Como el sistema proyectivo §133§ es estricto,
se puede pasar al límite proyectivo en las sucesiones exactas
§134§
(\textbf{0}, 13.2.2); como §135§, se tiene
§136§, de donde un isomorfismo topológico
§137§.
Pero como la filtración §138§ de §139§ es
§140§-buena, define sobre §141§ la topología
§142§-preádica; luego §143§ es
el separado completado de §144§ para la topología
§145§-preádica, lo que termina de demostrar
(\hyperref[III.4.1.7-fr]{4.1.7}).
\end{env}
\end{proof}

''',
('1','4.2.1'):r'''\begin{proposition}[4.2.1]
\label{III.4.2.1-fr}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo
propio, §2§ un §3§-Módulo coherente. Entonces, para todo
§4§ y todo §5§, §6§ es
\oldpage[III]{130}
un §7§-módulo de tipo finito, luego separado para la topología
§8§-preádica, y se tiene un isomorfismo topológico canónico
§9§
donde el primer miembro es el completado de §10§ para la
topología §11§-preádica, y en el segundo miembro §12§ se
considera, para todo §13§, como espacio subyacente al preesquema
§14§
\textup{(\textbf{I}, 3.6.1)}.
\end{proposition}

\begin{proof}
Como §15§ es un anillo local noetheriano y
§16§ un §17§-módulo de tipo finito
(\hyperref[III.3.2.1-fr]{3.2.1}), la topología §18§-preádica
sobre §19§ es separada (\textbf{0}\textsubscript{I}, 7.3.5). Las
demás afirmaciones son consecuencias de (\hyperref[III.4.1.7-fr]{4.1.7})
cuando §20§ es noetheriano y el punto §21§ cerrado, reemplazando §22§ por una
vecindad afín de §23§ y tomando §24§, teniendo en cuenta
(G, II, 4.9.1). En el caso general, pongamos
§25§, §26§,
§27§
y sea §28§; §29§ es noetheriano y §30§
propio (\textbf{II}, 5.4.2, (iii)) y §31§ es coherente
(\textbf{0}\textsubscript{I}, 5.3.11). Sea §32§ el único punto cerrado de §33§;
la proposición es válida para §34§, §35§ y §36§; se tiene
§37§, §38§ (\textbf{I}, 3.6.5),
estando canónicamente identificados los preesquemas
§39§ y
§40§
(\textbf{I}, 3.3.9); además,
§41§ se identifica con
§42§
(\textbf{I}, 9.1.6). Queda por ver que §43§ es
canónicamente isomorfo a
§44§, lo que
resulta de (\hyperref[III.1.4.15-fr]{1.4.15}), siendo plano el morfismo local
§45§
(\textbf{0}\textsubscript{I}, 6.7.1 y \textbf{I}, 2.4.2).
\end{proof}

El corolario siguiente utiliza la terminología de la teoría de la dimensión
(cap. IV) y no se aplicará antes del cap. IV.

''',
('1','4.3.13'):r'''\begin{proposition}[4.3.13]
\label{III.4.3.13-fr}
Sean §0§ un anillo local noetheriano unirramificado, §1§ un ideal de
definición de §2§, §3§,
§4§ el anillo graduado asociado a §5§ para
la filtración §6§-preádica; §7§ es una §8§-álgebra graduada
generada por §9§, siendo §10§ un §11§-módulo de tipo finito. Entonces
§12§ es un §13§-esquema conexo.
\end{proposition}

\begin{proof}
Sea §14§ el ideal maximal de §15§; §16§ es
un esquema íntegro cuyo punto §17§ correspondiente a §18§ es
el único punto cerrado. Por hipótesis se tiene
§19§ para un entero §20§,
luego §21§. Sea
§22§, y sea
§23§, que es el §24§-esquema obtenido haciendo explotar
el ideal §25§; §26§ es íntegro y el morfismo estructural
§27§ es birracional (\textbf{II}, 8.1.4) y evidentemente proyectivo. Por tanto,
(\hyperref[III.4.3.7-fr]{4.3.7}) es aplicable y muestra que §28§
es conexo; pero el espacio §29§ es subyacente a
§30§ (\textbf{I}, 3.6.1 y \textbf{II}, 2.8.10); como
§31§ por definición, la proposición queda demostrada.
\end{proof}

\subsection{El «main theorem» de Zariski.}
\label{subsection:III.4.4-fr}

'''
})

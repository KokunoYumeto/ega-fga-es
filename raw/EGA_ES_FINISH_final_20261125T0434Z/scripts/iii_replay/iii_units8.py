import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('6','6.4.1'):r'''\begin{env}[6.4.1]
Sean §0§ un esquema afín de anillo §1§, §2§, §3§ dos §4§-esquemas afines
de anillos §5§, §6§ respectivamente, de modo que §7§ y §8§ son álgebras
sobre §9§. Todo complejo §10§ (resp. §11§) de
§12§-Módulos (resp. §13§-Módulos) cuasicoherentes es de
la forma §14§ (resp. §15§), donde
§16§ (resp. §17§) es un complejo de §18§-módulos (resp.
§19§-módulos) (\textbf{I}, 1.3.7 y 1.3.8). Se puede evidentemente considerar §20§
y §21§ como complejos de §22§-módulos y formar los
§23§; además, en virtud del carácter
bifuntorial de §24§, las §25§-álgebras
§26§ y §27§ operan en este §28§-módulo, y estas operaciones hacen de él un
§29§-bimódulo, o, lo que equivale a lo mismo, un módulo sobre
§30§. Se ha definido pues de este modo un
§31§-Módulo cuasicoherente
§32§
que se llama el \emph{hipertor local} de índice §33§ de los complejos
§34§ y §35§ y que se denota también por
§36§.
\end{env}

''',
('6','6.4.5'):r'''\begin{namedtheorem}[6.4.5]{Lema}
Con las notaciones de \textup{(6.4.4)}, supongamos que §0§ y §1§ son inmersiones
abiertas; entonces el homomorfismo \textup{(6.4.4.2)} es biyectivo.
\end{namedtheorem}

\begin{proof}
Identifiquemos §2§ (resp. §3§) con un abierto de §4§ (resp. §5§);
§6§ (resp. §7§) es entonces unión de abiertos de la forma
§8§ (resp. §9§), donde §10§ (resp. §11§), y los
preesquemas inducidos §12§ y §13§ (resp.
§14§ y §15§) son isomorfos. Bastará probar
el lema cuando §16§ (resp. §17§) es de la forma §18§
(resp. §19§); en efecto, si se establece este punto, y se vuelve al
caso general, bastará probar que la restricción de §20§ a
cada abierto §21§ es un isomorfismo; ahora bien, si
§22§, §23§ son las
inclusiones canónicas, la restricción anterior no es otra que
§24§; pero es inmediato, en virtud de las
definiciones (6.4.4) y de (§25§, 4.4.8), que al componerla con
el homomorfismo canónico
§26§
donde §27§ y §28§, se obtiene el homomorfismo canónico
§29§
y si se sabe que (6.4.5.1) y (6.4.5.2) son isomorfismos,
resultará que lo mismo ocurre con §30§.

Supongamos pues que §31§ y §32§, de modo
que §33§ y §34§; §35§ (resp.
§36§) se identifica entonces con
§37§ (resp. §38§); por otra parte,
§39§ se identifica con el subesquema abierto
§40§ de
§41§ (\textbf{II}, 4.3.2.4); se trata de
probar que el homomorfismo
§42§
\oldpage[III]{148}
deducido por funtorialidad de los homomorfismos canónicos
§43§, §44§, es biyectivo. Ahora bien
(§45§, 1.6.1), se puede escribir
§46§, donde los §47§ son todos
complejos de §48§-módulos idénticos a §49§, siendo la aplicación
§50§ para §51§ la
multiplicación por §52§; se tiene un resultado análogo para §53§
reemplazando §54§ por §55§; por otra parte, está claro que el homomorfismo
§56§
correspondiente a los homomorfismos
§57§ y
§58§ es por definición la multiplicación
por §59§. La conclusión resulta entonces de (§60§,
1.6.1) aplicado al primer miembro de (6.4.5.3) y de (6.3.6).
\end{proof}

''',
('6','6.5.2'):r'''\begin{env}[6.5.2]
Supongamos primero §0§ \emph{afín}, y sean §1§, §2§
recubrimientos de §3§ y §4§ respectivamente por abiertos afines; entonces los
§5§ forman un recubrimiento abierto afín
de §6§. Pongamos
§7§,
§8§; tenemos pues para todo
par §9§ un §10§-Módulo cuasicoherente
§11§,
y hay que mostrar que los §12§ verifican la condición de
pegado (§13§, 3.3.1). Para ello, basta verificar que para
todo abierto afín §14§ (resp.
§15§), las restricciones de
§16§ y de §17§ a §18§
son canónicamente isomorfas; pero esto se deduce inmediatamente de la existencia
de isomorfismos canónicos de estas restricciones sobre
§19§ (6.4.5).
Además, resulta inmediatamente de esta definición y de (6.4.5) que el
§20§-Módulo así definido no depende (salvo isomorfismo) de los
recubrimientos abiertos §21§, §22§ consi\oldpage[III]{149}derados;
lo denotaremos pues por
§23§; resulta finalmente
de (6.4.5) que para \emph{toda} parte abierta §24§ (resp. §25§) de §26§ (resp. §27§), la
restricción de §28§ a
§29§ es canónicamente isomorfa a
§30§.
\end{env}

''',
('6','6.5.3'):r'''\begin{env}[6.5.3]
Pasemos ahora al caso general en que §0§ es arbitrario, y sea §1§
un recubrimiento de §2§ formado por abiertos afines; designemos por §3§
(resp. §4§) la imagen inversa de §5§ en §6§ (resp. §7§);
hay que probar también que los haces
§8§
verifican la condición de pegado. Basta definir, para todo abierto
afín §9§ contenido en §10§, isomorfismos canónicos de las
restricciones de §11§ y §12§ a §13§ (designando
por §14§ y §15§ las imágenes inversas de §16§ en §17§ y §18§
respectivamente) sobre
§19§; se puede,
además, limitar al caso en que §20§ se escribe a la vez §21§ y
§22§, siendo §23§ (resp. §24§) una sección de
§25§ sobre §26§ (resp. §27§); pero entonces
§28§ es
canónicamente isomorfo a
§29§
por una parte, a
§30§
por otra, en virtud de (6.4.2); como se acaban de definir isomorfismos
canónicos de §31§ sobre
§32§ y
de §33§ sobre
§34§
(6.5.2), esto termina de definir el §35§-Módulo
§36§. Además, para
toda parte abierta §37§ (resp. §38§) de §39§ (resp. §40§),
§41§ es
canónicamente isomorfo a la restricción de
§42§ a §43§.

Es inmediato que se ha definido así (en las categorías de complejos de
Módulos cuasicoherentes acotados inferiormente) un \emph{bi-§44§-funtor}
§45§ con valores
en la categoría de los §46§-Módulos, pues está claro que la cuestión
es local sobre §47§, §48§ y §49§, en virtud de (6.4.5) y de la observación de que
(6.4.4.2) es un morfismo de bi-§50§-funtores. Se observará que si
§51§ y §52§ se reducen respectivamente a
sus términos de grado 0, §53§ y §54§,
§55§ no es otro, en virtud de
(6.4.1.1), que el producto tensorial externo §56§
definido en (\textbf{I}, 9.1.2); esto resulta en efecto de (\textbf{I}, 9.1.3).
\end{env}

''',
('6','6.5.5'):r'''\begin{env}[6.5.5]
Diremos que sobre un espacio topológico §0§ un haz de anillos
§1§ es \emph{de dimensión cohomológica §2§} si, para todo
§3§, el anillo §4§ es de dimensión cohomológica §5§;
se dirá entonces también que el \emph{espacio anillado} §6§ es
\emph{de dimensión cohomológica §7§}. Se dirá que un haz
de anillos (resp. un espacio anillado) es de dimensión cohomológica \emph{finita}
si existe un entero §8§ tal que es de dimensión cohomológica
§9§. Se observará que si los §10§ son \emph{anillos locales
(conmutativos) noetherianos},
\oldpage[III]{150}
decir que son de dimensión cohomológica §11§ significa que son
\emph{regulares} y de \emph{dimensión} (de Krull) §12§ (§13§, 17.3.1).
Con la terminología de la teoría de la dimensión que introduciremos en el
cap. IV, equivale a decir que un \emph{preesquema localmente noetheriano} §14§
es de \emph{dimensión cohomológica} §15§, o a decir que es \emph{regular}
(§16§, 4.1.4) y de \emph{dimensión} §17§; esto significa que para
todo abierto afín §18§ de §19§, el anillo §20§ es \emph{de
dimensión cohomológica} §21§ (§22§, 17.2.6). Dicho esto,
esta última observación, junto con (6.3.2), prueba que si §23§ es \emph{localmente
noetheriano y de dimensión cohomológica finita}, las sucesiones espectrales
§24§ y
§25§ son \emph{birregulares}.

Está claro que
§26§ se
transforma en
§27§ (salvo
isomorfismo) por el isomorfismo canónico de §28§ sobre
§29§.
\end{env}

''',
('6','6.5.8'):r'''\begin{proposition}[6.5.8]
Sean §0§, §1§ dos §2§-preesquemas, §3§ \textup{(resp.} §4§\textup{)} un
§5§-Módulo \textup{(resp.} un §6§-Módulo\textup{)} cuasicoherente. Si
§7§ o §8§ es §9§-plano, se tiene
§10§ para §11§.
\end{proposition}

\begin{proof}
Al ser la cuestión local sobre §12§ y §13§, se puede suponer §14§, §15§ y §16§
afines, de anillos respectivos §17§, §18§, §19§, y
§20§, §21§, siendo §22§ (resp. §23§)
un §24§-módulo (resp. un §25§-módulo). Supongamos por ejemplo que §26§
es §27§-plano, lo que significa que para todo §28§, §29§ es un
§30§-módulo plano (§31§, 6.7.1); por tanto §32§ es un §33§-módulo plano
(§34§, 6.3.3), y se sabe que
§35§ para §36§ y para todo §37§-módulo §38§
(§39§, 6.1.1), de donde la conclusión por (6.4.1.1).
\end{proof}

''',
('6','6.5.14'):r'''\begin{corollary}[6.5.14]
Supongamos verificada una de las condiciones \textup{(i), (ii)} de \textup{(6.5.13)}, y sea
§0§ \textup{(resp.} §1§) un §2§-Módulo \textup{(resp.} un
§3§-Módulo) cuasicoherente de tipo finito; entonces los
§4§ son §5§-Módulos
coherentes.
\end{corollary}

\begin{proof}
Al ser la cuestión local sobre §6§ y §7§, se puede suponer §8§, §9§, §10§
afines.

\textnormal{(i)} Bajo las hipótesis de (i), §11§, §12§ y §13§ son noetherianos.
Existe pues una resolución localmente libre §14§ de
§15§ formada por §16§-Módulos de tipo finito (\textbf{I}, 1.3.7); como
§17§ es plano sobre §18§, resulta de (6.3.4) que se tiene
§19§;
ahora bien, los §20§ son §21§-Módulos
cuasicoherentes de tipo finito (\textbf{I}, 9.1.1), luego coherentes. Se concluye que
§22§ es coherente
(§23§, 5.3.4).

\textnormal{(ii)} Supongamos ahora verificadas las condiciones (ii). Como
el anillo §24§ es cociente de una §25§-álgebra de polinomios en un número finito
de indeterminadas (\textbf{I}, 6.3.3), §26§ es un sub-§27§-preesquema cerrado de un
§28§-preesquema afín §29§, plano y de tipo finito sobre §30§; al ser §31§ noetheriano
(\textbf{I}, 6.3.7), existe una resolución localmente libre §32§ de
§33§ por §34§-Módulos de tipo finito
(siendo §35§ la inclusión canónica); en virtud de (6.5.12),
§36§ es la imagen inversa por
§37§ del §38§-Módulo
§39§ (donde
§40§); se ve como en (i) que los
§41§ son §42§-Módulos
coherentes, y se obtiene también la conclusión por (§43§, 5.3.4).
\end{proof}

''',
('6','6.10.1'):r'''\begin{proposition}[6.10.1]
Sean §0§ un esquema afín,
§1§ (§2§) una familia finita de §3§-esquemas afines, \textup{planos}
sobre §4§; para cada §5§, sea §6§ un §7§-morfismo
separado y cuasicompacto, y sea §8§ un complejo de
§9§-Módulos cuasicoherentes acotado inferiormente. Sea
§10§ el producto de los §11§-esquemas §12§. Existe un complejo
§13§ de §14§-Módulos cuasicoherentes y \textup{planos} sobre
§15§, con la propiedad siguiente: para todo §16§-esquema afín §17§ y todo
complejo de §18§-Módulos cuasicoherentes
§19§ acotado inferiormente, hay un isomorfismo
§20§
que es un isomorfismo de §21§-funtores en §22§.
Además, para todo §23§-morfismo §24§ de §25§-esquemas afines, el
diagrama
§26§
(donde las flechas verticales son los §27§-morfismos canónicos
definidos en \textup{(6.7.10)}) es conmutativo.
\end{proposition}

\begin{proof}
\oldpage[III]{172}
Calculemos los hipertor por el método de (6.6.2), teniendo en cuenta la observación
(6.6.6); con las notaciones de (6.6.2), cada
§28§ es un bicomplejo de §29§-módulos, designando por
§30§ el anillo de §31§; admite pues una resolución de Cartan-Eilenberg
proyectiva §32§ (en el sentido de (\textbf{0}, 11.7.1)) formada por
§33§-\emph{módulos}, y en virtud de (6.6.6), el primer miembro de (6.10.1.1) es
canónicamente isomorfo a
§34§, donde
§35§
y §36§. Como, por hipótesis, los
anillos §37§ son §38§-módulos \emph{planos}, los
§39§ son tricomplejos de §40§-módulos planos
(§41§, 6.2.1), y lo mismo ocurre con
§42§; además, si §43§ es el anillo de §44§, producto
tensorial de los §45§, §46§ es un tricomplejo de
§47§-\emph{módulos}; el complejo
§48§ de §49§-Módulos (donde §50§ se considera como
complejo simple) responde pues a la cuestión, como resulta fácilmente de
(6.7.10).
\end{proof}

''',
('6','6.10.5'):r'''\begin{theorem}[6.10.5]
Sean §0§ un esquema afín noetheriano,
§1§ un morfismo propio, §2§ un complejo de
§3§-Módulos coherentes, \textup{planos} sobre §4§, acotado inferiormente.
Existe entonces un complejo §5§ de §6§-Módulos,
acotado inferiormente, cuyos términos §7§ son
§8§-Módulos de la forma §9§, y un isomorfismo
§10§
de §11§-funtores en el complejo §12§ de
§13§-Módulos cuasicoherentes, acotado inferiormente. Además, para
todo morfismo §14§, se tiene, poniendo
§15§
\oldpage[III]{174}
(que es un complejo de §16§-Módulos localmente libres de tipo
finito), un isomorfismo
§17§
de §18§-funtores en el complejo §19§ de
§20§-Módulos cuasicoherentes, acotado inferiormente, de modo que
el diagrama
§21§
es conmutativo.
\end{theorem}

\begin{proof}
La aplicación de (6.10.1) da primero un complejo acotado inferiormente
(6.10.2) §22§ de §23§-Módulos cuasicoherentes y
§24§-libres (6.10.3, (iii)) y un isomorfismo
§25§
de §26§-funtores en §27§, pero \emph{a priori} los
términos de §28§ no son necesariamente
§29§-Módulos \emph{de tipo finito}. Pero si se aplica (6.10.5.4) al caso
en que §30§ es un complejo reducido a un solo término
§31§, se ve que §32§ es
isomorfo a §33§, y está por tanto formado
por §34§-Módulos \emph{coherentes} (6.2.5). Se sabe entonces (\textbf{0}, 11.9.2) que
existe un complejo §35§ acotado inferiormente, formado por
§36§-Módulos asociados a §37§-módulos libres \emph{de tipo finito}, y un
homomorfismo §38§,
tales que el homomorfismo correspondiente para la homología,
§39§,
es biyectivo; de donde el isomorfismo (6.10.5.1), en virtud de (6.10.3, (ii)).
Las demás afirmaciones de (6.10.5) resultan de (6.10.1) y (6.10.3, (ii))
cuando §40§ es \emph{afín}; en el caso general, basta verificar que
cuando se considera un recubrimiento §41§ de §42§ por abiertos
afines, y el isomorfismo correspondiente (6.10.5.2) relativo a cada uno de los
§43§, las restricciones a un abierto afín
§44§ de los isomorfismos correspondientes a
§45§ y a §46§ coinciden con el isomorfismo correspondiente a
§47§, lo que resulta de la conmutatividad del diagrama (6.10.1.2) aplicado a las
inclusiones canónicas §48§ y §49§.
\end{proof}

'''
})

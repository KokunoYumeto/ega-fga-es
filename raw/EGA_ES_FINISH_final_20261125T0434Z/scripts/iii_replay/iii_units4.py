import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','2.4.1'):r'''\begin{theorem}[2.4.1]
\label{III.2.4.1-fr}
Sean §0§ un preesquema noetheriano, §1§ una
§2§-Álgebra cuasicoherente de tipo finito. Sean
§3§ un morfismo proyectivo, §4§,
§5§ un §6§-Módulo cuasicoherente de tipo finito.
Entonces:
\begin{enumerate}
\item[\textup{(i)}] Para todo §7§, §8§ es un
§9§-Módulo de tipo finito.
\item[\textup{(ii)}] Sea además §10§ un §11§-Módulo invertible
amplio para §12§, y pongamos
§13§ para todo
§14§. Existe un entero §15§ tal que, para §16§, se tiene
§17§
para todo §18§, y el homomorfismo canónico
§19§
\textup{(\textbf{0}\textsubscript{I}, 4.4.3)} es sobreyectivo.
\end{enumerate}
\end{theorem}

\begin{proof}
Pongamos §20§,
§21§ de modo que
§22§ (\textbf{II}, 1.5.5); sean §23§,
§24§ los morfismos estructurales, que son afines por
definición, y §25§; se tiene pues un diagrama
conmutativo
§26§
y el morfismo §27§ es proyectivo (\textbf{II}, 5.5.5, (iii)); pongamos
§28§.

(i) Sea §29§ el §30§-Módulo asociado al
§31§-Módulo cuasicoherente §32§, cuando §33§ se
considera como un §34§-esquema afín (\textbf{II}, 1.4.3), de modo que se tiene
§35§; como §36§ es un
§37§-Módulo de tipo finito, §38§ es un
§39§-Módulo de tipo finito (\textbf{II}, 1.4.5); como §40§ es de tipo
finito, puesto que §41§ y §42§ lo son (\textbf{II}, 1.3.7 y \textbf{I}, 6.3.4, (ii)), §43§ es
noetheriano (\textbf{I}, 6.3.7) y §44§ es por tanto coherente.
Dicho esto, como §45§ es afín, el homomorfismo canónico
§46§ es biyectivo
(\hyperref[III.1.3.4-fr]{1.3.4}). Además, este homomorfismo es un
homomorfismo de §47§-\emph{Módulos}; en efecto, del homomorfismo
canónico
§48§
que define la estructura de §49§-Módulo de §50§ (recordando
que §51§), se deduce
canónicamente un homomorfismo
§52§

\oldpage[III]{108}
(\textbf{0}, 12.2.2), y como (\hyperref[III.2.4.1.2-fr]{2.4.1.2}) procede
a su vez (por aplicación de (\textbf{0}\textsubscript{I}, 4.2.2.1)) del
homomorfismo
§53§
que define la estructura de §54§-Módulo de
§55§, el diagrama
§56§
es conmutativo (\textbf{0}, 12.2.6); componiendo las flechas horizontales con
el homomorfismo procedente del homomorfismo canónico
§57§,
se obtiene nuestra afirmación. Por otra parte, puesto que §58§ es afín y
§59§ es separado y cuasicompacto, el homomorfismo canónico
§60§ es biyectivo
(\hyperref[III.1.4.14-fr]{1.4.14}), y se demuestra como antes que
es un isomorfismo de §61§-\emph{Módulos} (utilizando esta vez la
conmutatividad de (\textbf{0}, 12.2.6.2)). Ahora bien, al ser §62§ proyectivo y
§63§ coherente,
§64§ es un
§65§-Módulo coherente en virtud de
(\hyperref[III.2.2.1-fr]{2.2.1}); se concluye que
§66§ es un §67§-Módulo \emph{de tipo
finito} (\textbf{II}, 1.4.5).

(ii) Sea §68§, que es un
§69§-Módulo invertible; para todo §70§, se tiene
§71§
(\textbf{0}\textsubscript{I}, 5.4.10) salvo isomorfismo; se puede aplicar
a §72§ el
razonamiento hecho en (i) para §73§, que prueba que
§74§
es isomorfo a
§75§.
Ahora bien, §76§ es amplio para §77§ (\textbf{II}, 4.6.13, (iii)), luego resulta
de (\hyperref[III.2.2.1-fr]{2.2.1}) que existe un entero §78§ tal que
§79§
para todo §80§ y todo §81§, lo que prueba
(\hyperref[III.2.4.1.1-fr]{2.4.1.1}). Finalmente, resulta también de
(\hyperref[III.2.2.1-fr]{2.2.1}) que se puede suponer §82§ tal que para
§83§ el homomorfismo canónico
§84§
sea sobreyectivo; como §85§ es un funtor exacto (\textbf{II}, 1.4.4),
el homomorfismo correspondiente
§86§
es sobreyectivo. Ahora bien, se tiene
§87§
(\textbf{II}, 1.5.2) y como §88§, se ve
finalmente que se tiene
§89§
lo que termina la demostración.
\end{proof}

''',
('1','2.5.3'):r'''\begin{theorem}[2.5.3]
\label{III.2.5.3-fr}
Sean §0§ un anillo local artiniano, §1§ un esquema proyectivo sobre
§2§, §3§ un §4§-Módulo
invertible muy amplio con respecto a §5§, §6§ un
§7§-Módulo coherente; se pone
§8§
para todo §9§.
\begin{enumerate}
\item[\textup{(i)}] Existe un polinomio único §10§ tal que
§11§ para todo §12§ \textup{(se dice que §13§
es el \emph{polinomio de Hilbert} de §14§ con respecto a §15§)}.
\item[\textup{(ii)}] Para §16§ suficientemente grande, se tiene
§17§.
\item[\textup{(iii)}] El término de mayor grado de §18§ tiene un
coeficiente §19§.
\end{enumerate}
\end{theorem}

Añadamos que en el cap. IV, en el parágrafo dedicado a la noción de
dimensión, demostraremos además que \emph{el grado de
§20§ es igual a la dimensión del soporte de}
§21§.

\begin{proof}
Como se tiene §22§ para todo §23§ en cuanto §24§ es
suficientemente grande (\hyperref[III.2.2.1-fr]{2.2.1}),

\oldpage[III]{110}
se tiene
§25§
para §26§ suficientemente grande, de donde (ii); esto implica
§27§ para §28§ suficientemente grande, y (iii) resulta pues
de (i); como, por lo demás, la afirmación de unicidad de (i) es inmediata,
queda por probar la existencia del polinomio §29§.

Mostremos primero que se puede suponer §30§, donde
§31§ es el ideal maximal de §32§. En efecto, existe un entero
§33§ tal que §34§, y §35§ admite por tanto una
filtración finita
§36§
Por inducción, se deduce de
(\hyperref[III.2.5.2.1-fr]{2.5.2.1}) que
§37§
como
§38§, donde
§39§,
esto prueba nuestra afirmación.

Supongamos pues §40§; si §41§ es el subesquema
cerrado de §42§, imagen inversa por el morfismo estructural
§43§ del único punto cerrado de
§44§, y §45§ la inclusión canónica, se tiene
§46§, donde §47§ es un
§48§-Módulo coherente; §49§ es un esquema proyectivo sobre
§50§, donde §51§. Si
§52§, §53§ es muy amplio con respecto
a §54§ (\textbf{II}, 4.4.10), y se tiene
§55§, donde
§56§ (\textbf{0}\textsubscript{I}, 5.4.10). Se concluye que
§57§ (G, II, 4.9.1), y se está
pues reducido al caso en que §58§ es un \emph{cuerpo}.

Observemos ahora que §59§ puede considerarse como un subesquema
cerrado de §60§ para un §61§ apropiado (\textbf{II}, 5.5.4, (ii));
si §62§ es la inclusión canónica, se ve como antes que se
tiene §63§, de modo que se
puede limitar al caso en que §64§ con
§65§, siendo §66§ un cuerpo.

Dicho esto, se tiene §67§, donde §68§ es un §69§-módulo
graduado de tipo finito (\textbf{II}, 2.7.8); existe por tanto una resolución finita
de §70§ por §71§-módulos graduados \emph{libres} de tipo finito
§72§
en virtud del teorema de las sicigias de Hilbert (M, VIII, 6.5); como
§73§ es un funtor exacto en §74§ (\textbf{II}, 2.5.4), se tiene
también una sucesión exacta
§75§
y por tanto, para todo §76§, la sucesión
§77§
es exacta; aplicando por inducción sobre §78§ la prop. (2.5.2), resulta
§79§
y para probar (i), se está pues reducido al caso en que §80§ es \emph{libre} y graduado
de tipo finito, luego al caso en que §81§ para un §82§. Como
entonces §83§ (\textbf{II}, 2.5.15), se ve
finalmente que el teorema resultará del
\end{proof}

\oldpage[III]{111}
\begin{lemma}[2.5.3.1]
\label{III.2.5.3.1-fr}
Sean §84§ un cuerpo, §85§ un entero §86§, y §87§; se tiene
entonces
§88§
para todo §89§.
\end{lemma}

\begin{proof}
En efecto, para §90§, se tiene
§91§, que
es el número de monomios en los §92§ de grado total §93§, es decir,
§94§ (\hyperref[III.2.1.12-fr]{2.1.12}). Para
§95§, se tiene análogamente
§96§;
si §97§, la dimensión de §98§ sobre §99§ es el
número de sucesiones §100§ de enteros §101§ tales que
§102§ (\hyperref[III.2.1.12-fr]{2.1.12}), o también el
número de sucesiones de enteros §103§ §104§ tales que
§105§; es pues el número
§106§.
Finalmente, para §107§, se tiene §108§ y por otra parte
§109§ para todo §110§
(\hyperref[III.2.1.12-fr]{2.1.12}), lo que prueba el lema.
\end{proof}

''',
('1','2.6.1'):r'''\begin{proposition}[2.6.1]
\label{III.2.6.1-fr}
Sean §0§ un preesquema noetheriano, §1§ un morfismo propio,
§2§ un §3§-Módulo invertible. Las condiciones
siguientes son equivalentes:
\begin{enumerate}
\item[\textup{a)}] §4§ es amplio para §5§.
\item[\textup{b)}] Para todo §6§-Módulo coherente §7§,
existe un entero §8§ tal que para §9§ se tiene
§10§
para todo §11§.
\item[\textup{c)}] Para todo Ideal coherente §12§ de §13§,
existe un entero §14§ tal que para §15§ se tiene
§16§.
\end{enumerate}
\end{proposition}

\begin{proof}
Se ha visto que \emph{a)} implica \emph{b)} (\hyperref[III.2.2.1-fr]{2.2.1}, (ii)). Es
trivial que \emph{b)} implica \emph{c)}, y queda por probar que \emph{c)} implica
\emph{a)}. Se puede limitar al caso en que §17§ es afín (\textbf{II}, 4.6.4), y probar
en este caso que §18§ es amplio; bastará mostrar que cuando
§19§ recorre el conjunto de secciones de los §20§
§21§ sobre §22§, aquellos §23§ que son afines forman un
recubrimiento de §24§ (\textbf{II}, 4.5.2). Para ello, mostremos que para todo punto
\emph{cerrado} §25§ de §26§ y toda vecindad abierta afín §27§ de §28§, existe un
§29§ y un §30§ tales que
§31§; §32§ será necesariamente afín (\textbf{I}, 1.3.6) y la
unión de estos §33§ será un abierto de §34§ que contiene todos los puntos
cerrados de §35§, y por tanto el propio §36§ puesto que §37§ es noetheriano
(\textbf{I}, 6.3.7 y \textbf{0}\textsubscript{I}, 2.1.3). Sea §38§ (resp.
§39§) el haz cuasicoherente de ideales de §40§
que define el subpreesquema cerrado reducido de §41§ cuyo espacio
subyacente es §42§ (resp. §43§) (\textbf{I}, 5.2.1); está claro que
§44§ y §45§ son coherentes (\textbf{I}, 6.1.1), que
§46§ y que
§47§ es un §48§-Módulo
coherente (\textbf{0}\textsubscript{I}, 5.3.3) cuyo soporte es §49§ y tal
que §50§. Como §51§ es localmente libre, la
sucesión
§52§
es exacta para todo §53§, y por hipótesis existe §54§ suficientemente grande tal
que §55§; la sucesión
exacta de cohomología
\oldpage[III]{112}
prueba pues que el homomorfismo
§56§
es \emph{sobreyectivo}. Una sección §57§ de
§58§ sobre §59§ tal que
§60§ es pues la imagen de una sección
§61§ (pues en virtud de
(\textbf{0}\textsubscript{I}, 5.4.1),
§62§ es un sub-§63§-Módulo
de §64§); se tiene por definición §65§ y
§66§ para §67§, lo que termina la demostración.
\end{proof}

''',
('1','2.6.2'):r'''\begin{proposition}[2.6.2]
\label{III.2.6.2-fr}
Sean §0§ un preesquema noetheriano, §1§ un morfismo de tipo
finito, §2§ un morfismo finito sobreyectivo, §3§ un
§4§-Módulo invertible y §5§. Se
supone verificada la condición siguiente: Existe una parte §6§ de
§7§, propia sobre §8§ (\textbf{II}, 5.4.10) tal que para todo §9§, o bien
§10§ es normal en el punto §11§, o bien §12§ es un
§13§-módulo libre. En estas condiciones, para que §14§
sea amplio para §15§, es necesario y suficiente que §16§ sea amplio
para §17§.
\end{proposition}

\begin{proof}
\begin{env}[2.6.2.1]
\label{III.2.6.2.1-fr}
Puesto que §18§ es afín, la condición es necesaria (\textbf{II}, 5.1.12). Para
ver que es suficiente, se puede suponer §19§ afín (\textbf{II}, 4.6.4).
Mostremos además que se puede limitar al caso en que §20§ es \emph{reducido}. En
efecto, sea §21§ la inclusión canónica, y pongamos
§22§, §23§, de modo que se tiene el
diagrama conmutativo
§24§

El morfismo §25§ es entonces de tipo finito (\textbf{I}, 6.3.4) y §26§ es
un morfismo finito (\textbf{II}, 6.1.5, (iii)); si §27§ es amplio para
§28§, §29§ es amplio para §30§ puesto que
§31§ es una inmersión cerrada (\textbf{II}, 5.1.12 y \textbf{I}, 4.3.2). Si se pone
§32§, §33§ es propio sobre §34§ (\textbf{II}, 5.4.10); por otra parte,
si §35§ es normal en un punto §36§, lo mismo ocurre evidentemente con
§37§; finalmente, si §38§ es un
§39§-módulo libre, resulta inmediatamente de (\textbf{II}, 1.5.2) que
§40§ es un §41§-módulo
libre. Finalmente, como §42§ es noetheriano (\textbf{I}, 6.3.7), si
§43§ es amplio, §44§ es amplio (\textbf{II}, 4.5.14), y
como §45§, esto termina la
reducción anunciada. Suponemos pues en adelante §46§ \emph{afín} y §47§
\emph{reducido}.
\end{env}

Al verificarse entonces las hipótesis de (\textbf{II}, 6.6.11), existe un
§48§-preesquema reducido §49§, y un §50§-morfismo §51§ \emph{finito} y
\emph{birracional} tal que la restricción de §52§ a §53§ es un
\emph{isomorfismo} sobre §54§ y §55§ es amplio. Reemplazando
§56§ por §57§, se ve que se está reducido a demostrar la proposición
suponiendo además que \emph{§58§ posee las propiedades que se acaban de
enumerar para §59§}. Designaremos también por §60§ un subpreesquema de
§61§ cuyo espacio subyacente es §62§, que es propio sobre §63§
(\textbf{II}, 5.4.10).

\begin{env}[2.6.2.3]
\label{III.2.6.2.3-fr}
Sean ahora §64§ un \emph{subpreesquema cerrado} de §65§,
§66§ la inclusión canónica,
§67§ su imagen inversa,
§68§ la inclusión canónica, de modo que se tiene el diagrama
conmutativo (\hyperref[III.2.6.2.2-fr]{2.6.2.2}); pongamos
§69§,
§70§, de modo que
§71§ es amplio para §72§ (\textbf{II}, 5.1.12). Si se
pone §73§, el subpreesquema cerrado §74§ de §75§ es propio
sobre §76§ (\textbf{II}, 5.4.2, (ii)). En otros términos, \emph{las hipótesis de}
(\hyperref[III.2.6.2-fr]{2.6.2}) \emph{se verifican para} §77§,
§78§, §79§ y §80§.
\end{env}

\oldpage[III]{113}
Esto nos permitirá demostrar
(\hyperref[III.2.6.2-fr]{2.6.2}) por \emph{inducción noetheriana}
(\textbf{0}\textsubscript{I}, 2.2.2) en el caso en que la restricción de §81§ a
§82§ es un \emph{isomorfismo} sobre §83§ (lo que es suficiente para
nuestro propósito, como se ha visto en
(\hyperref[III.2.6.2.2-fr]{2.6.2.2})): bastará establecer que si, para
todo subpreesquema cerrado §84§ de §85§ cuyo espacio subyacente es
§86§, la conclusión de (\hyperref[III.2.6.2-fr]{2.6.2}) es verdadera
para el haz §87§, entonces también es verdadera para el
haz §88§.

\begin{env}[2.6.2.4]
\label{III.2.6.2.4-fr}
Sean entonces §89§, §90§,
de modo que §91§ es una sub-§92§-Álgebra de
§93§, que es un §94§-Módulo coherente; además, la
restricción §95§ es igual a §96§. Sea
§97§ el \emph{conductor} de §98§ sobre §99§, es decir,
el mayor sub-§100§-Módulo cuasicoherente de §101§ tal
que §102§ (o también el \emph{anulador} del
§103§-Módulo §104§
(\textbf{0}\textsubscript{I}, 5.3.7)), lo que implica
§105§. Está claro que
§106§ en todos los puntos que admiten una vecindad
§107§ tal que §108§ es un isomorfismo de §109§ sobre §110§, y en
particular en todos los puntos de §111§ y en una vecindad de todo
punto genérico de una componente irreducible de §112§. Consideremos entonces
el subpreesquema cerrado §113§
de §114§ definido por §115§; es también \emph{propio} sobre §116§ pues el
subespacio §117§ es cerrado en §118§ (\textbf{II}, 5.4.10). Además, la definición
de §119§ muestra que
§120§; se ve pues que siempre es posible
reducirse al caso en que
§121§, y como se ha visto que
§122§ es un abierto no vacío de §123§, siempre se puede suponer que
el espacio §124§ es \emph{distinto} de §125§.
\end{env}

\begin{env}[2.6.2.5]
\label{III.2.6.2.5-fr}
Consideremos §126§ como igual a §127§ (puesto que
§128§ es afín) y sea §129§, Ideal
coherente de §130§ tal que §131§
(\textbf{II}, 1.4.1); el subpreesquema cerrado
§132§ de §133§ está definido por §134§ y es igual
a §135§ (\textbf{II}, 1.4.10); como
§136§ es un morfismo finito (\textbf{II}, 6.1.5, (iii)), §137§ es \emph{propio}
sobre §138§ (\textbf{II}, 6.1.11 y 5.4.2, (ii)).

Dicho esto, debemos probar que para todo §139§ y toda vecindad
abierta §140§ de §141§, existe una sección §142§ de un
§143§ §144§ sobre §145§ tal que
§146§ (\textbf{II}, 4.5.2); distinguiremos dos casos:

§147§ Se tiene §148§; se puede evidentemente suponer entonces que se tiene
también §149§, luego el abierto §150§ no interseca
§151§. Como §152§ es amplio por hipótesis, existe un §153§ y
una sección §154§ de §155§ sobre §156§ tal
que §157§ (\textbf{II}, 4.5.2). Además, se
puede suponer que §158§ esté
generado por sus secciones sobre §159§ (\textbf{II}, 4.5.5), luego, como
§160§, hay una de estas secciones §161§
tal que §162§; multiplicándola por §163§ (lo que equivale a
reemplazar §164§ por §165§), se ve que se puede suponer también que
§166§. Dicho esto, resulta de
(\textbf{0}\textsubscript{I}, 5.4.10) que se tiene un isomorfismo canónico
§167§

La sección §168§ de §169§ que
corresponde a §170§ por este isomorfismo tiene evidentemente las propiedades
requeridas.

§171§ Se tiene §172§. Sea §173§ el Ideal coherente de
§174§ que define el subpreesquema cerrado reducido de §175§ cuyo
espacio subyacente es §176§, y consideremos \emph{en} §177§ los Ideales
\oldpage[III]{114}
coherentes §178§ y
§179§, de modo que se tiene el diagrama
de inclusiones
§180§

Sea §181§ el Ideal coherente §182§ de
§183§ de modo que §184§,
§185§, y por
tanto
§186§
(\textbf{II}, 1.4.4). Como §187§ para todo
abierto §188§ que no interseca §189§, se ve que el soporte de
§190§ está \emph{contenido en} §191§. Como §192§ es
propio sobre §193§, se puede aplicar (\hyperref[III.2.2.4-fr]{2.2.4}) y se
ve que para §194§ suficientemente grande, la aplicación canónica
§195§
es \emph{sobreyectiva}.

Pero en virtud de (\textbf{0}\textsubscript{I}, 5.4.10), se
concluye que la aplicación canónica
§196§
es \emph{sobreyectiva}.

Dicho esto, sean §197§ la inclusión canónica,
§198§ la inclusión canónica, de modo que se tiene el diagrama
conmutativo
§199§

Sean §200§, §201§;
como §202§ es amplio, §203§ es amplio (\textbf{II}, 5.1.12), y
por otra parte §204§; se concluye pues de
la hipótesis de inducción noetheriana (puesto que §205§) que
§206§ es \emph{amplio}. Por tanto
§207§ está
generado por sus secciones sobre §208§ para §209§ suficientemente grande
(\textbf{II}, 4.5.5). Como
§210§,
se deduce también de (\textbf{0}\textsubscript{I}, 5.4.10) que existe una sección
§211§ de §212§ sobre §213§ (para un §214§ suficientemente grande) tal
que §215§, puesto que se tiene §216§ por
definición de §217§ y §218§ por
hipótesis. El diagrama (\hyperref[III.2.6.2.6-fr]{2.6.2.6}) muestra que
§219§ es también una sección de
§220§ sobre §221§, luego §222§ es la \emph{imagen
canónica de una sección §223§ de}
§224§ sobre §225§.
Pero por definición, la imagen canónica §226§ de §227§ mód.
§228§ está
en
§229§
luego, en virtud de (\hyperref[III.2.6.2.6-fr]{2.6.2.6}), esto implica que
§230§ es una \emph{sección de} §231§
sobre §232§, y \emph{a fortiori} una sección de
§233§. Se ha visto antes que §234§, luego
§235§, y por definición de §236§, §237§ en §238§ que
es el soporte de §239§; luego §240§, lo que
termina la demostración.
\end{env}
\end{proof}

\oldpage[III]{115}

'''
})

import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','4.5.1'):r'''\begin{proposition}[4.5.1]
\label{III.4.5.1-fr}
Sean §0§ un anillo noetheriano, §1§ un ideal de §2§, §3§ un
§4§-preesquema de tipo finito, §5§, §6§ dos
§7§-Módulos coherentes cuyos soportes tienen una intersección
propia sobre §8§ \textup{(\textbf{II}, 5.4.10)}. Entonces, para todo entero
§9§, §10§ es un §11§-módulo
de tipo finito, y su separado completado para la topología §12§-preádica
se identifica canónicamente (con las notaciones de
\textup{(\hyperref[III.4.1.7-fr]{4.1.7})}) con
§13§.
\end{proposition}

\begin{proof}
Se sabe (T, 4.2) que existe una sucesión espectral birregular
§14§ cuyo resultado es
§15§ y cuyos términos
§16§ vienen dados por
§17§.
Se sabe que §18§ es un
§19§-Módulo coherente (\textbf{0}, 12.3.3) cuyo soporte está contenido en
la intersección de los de §20§ y §21§ (T, 4.2.2), y es
por tanto propio sobre §22§ (\textbf{II}, 5.4.10). Se concluye de
(\hyperref[III.3.2.4-fr]{3.2.4}) que los §23§ son
§24§-módulos de tipo finito, y por tanto (\textbf{0}, 11.1.8) lo mismo ocurre con todos
los términos §25§ de la sucesión espectral y con su resultado.
Por otra parte, si §26§ es el morfismo canónico,
§27§ y §28§ se identifican canónicamente
con §29§ y §30§, y §31§ es \emph{plano} (\textbf{I}, 10.8.8 y
10.8.9). Se sabe entonces (\textbf{0}, 12.3.4) que existe, para todo §32§, un
§33§-morfismo canónico
§34§,
y que el §35§-homomorfismo correspondiente
§36§
es un \emph{isomorfismo} (\textbf{0}, 12.3.5); en otros términos (\textbf{I}, 10.8.8),
§37§ se identifica canónicamente con el
completado §38§ (con las
notaciones de (\hyperref[III.4.1.7-fr]{4.1.7})). Se concluye entonces del teorema de
comparación (\hyperref[III.4.1.10-fr]{4.1.10}) que para todo §39§,
§40§
se identifica canónicamente con el separado completado
\oldpage[III]{139}
de
§41§ para la topología §42§-preádica.
Si se designa por §43§ la sucesión espectral birregular definida en (T, 4.2)
relativa a §44§ y §45§, se ve pues que
si §46§ designa el separado completado de §47§ para la topología
§48§-preádica, se tiene, salvo isomorfismo canónico,
§49§
(\textbf{0}\textsubscript{I}, 7.3.3).

Dicho esto, se sabe que el dato del morfismo plano §50§ define un
homomorfismo canónico de sucesiones espectrales
§51§
que, para los términos §52§ (resp. el resultado), se reduce al
homomorfismo
§53§
§54§
deducido de §55§ (resp. §56§) por funtorialidad (\textbf{0}, 12.3.4). Por
tensorización con §57§, los §58§ y §59§ dan
homomorfismos de §60§-módulos
§61§
§62§

Como §63§ es un §64§-módulo \emph{plano} (\textbf{0}\textsubscript{I}, 7.3.3), los
§65§-módulos
§66§ forman una
sucesión espectral birregular cuyo resultado son los
§67§, y los
§68§ y §69§ un morfismo de sucesiones espectrales. Como los
§70§ son \emph{isomorfismos}, lo mismo ocurre con los §71§
(\textbf{0}, 11.1.5).
\end{proof}

''',
('1','4.6.1'):r'''\begin{proposition}[4.6.1]
\label{III.4.6.1-fr}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo
propio, §2§ un §3§-Módulo coherente y §4§-plano, §5§ un
punto de §6§. Supongamos que para un
\oldpage[III]{140}
entero §7§ se tiene
§8§.
Entonces existe una vecindad §9§ de §10§ en §11§ tal que
§12§, y para todo entero §13§ el homomorfismo
canónico
§14§
\textup{(\hyperref[III.4.2.1.1-fr]{4.2.1.1})} es sobreyectivo.
\end{proposition}

\begin{proof}
Como §15§ es un §16§-Módulo coherente
(\hyperref[III.3.2.1-fr]{3.2.1}), la primera afirmación de la proposición
quedará establecida si se prueba que se tiene
§17§ (\textbf{0}\textsubscript{I}, 5.2.2); en virtud de
(\hyperref[III.4.2.1-fr]{4.2.1}), bastará probar que
§18§
para todo §19§. Esto es verdadero por hipótesis para §20§; vamos a demostrarlo
por inducción sobre §21§. Pongamos
§22§,
de modo que §23§ es un subpreesquema cerrado de §24§, con el mismo
espacio subyacente (\textbf{I}, 3.6.1); la hipótesis de inducción
§25§
implica pues
§26§;
por otra parte, la sucesión exacta de cohomología da, a partir de la sucesión
exacta
§27§
de §28§-Módulos, la sucesión exacta
§29§
y bastará mostrar que se tiene
§30§
pues entonces §31§ será un
submódulo de §32§, luego §33§ en
virtud de la hipótesis de inducción.

Observemos ahora que la fibra
§34§ es un subpreesquema cerrado
de §35§, y que
§36§ está anulado por
§37§, luego puede considerarse como un §38§-Módulo, de
modo que
§39§.
Dicho esto, vamos a mostrar que el §40§-homomorfismo canónico
§41§
es \emph{biyectivo}; establecido esto, resultará, puesto que
§42§ es un §43§-módulo libre, que se tiene
§44§
(\textbf{0}, 12.2.3), puesto que
§45§ por hipótesis, de donde
(\hyperref[III.4.6.1.1-fr]{4.6.1.1}). Para establecer la primera afirmación,
queda pues por probar que (\hyperref[III.4.6.1.2-fr]{4.6.1.2}) es biyectivo;
como la cuestión es puntual sobre §46§ y §47§ es un
§48§-módulo \emph{plano} por hipótesis para todo §49§,
basta aplicar (\textbf{0}, 10.2.1, \emph{c)}), pues
§50§ es un módulo plano sobre el cuerpo
§51§.

Para demostrar la segunda afirmación de (\hyperref[III.4.6.1-fr]{4.6.1}), se
reduce inmediatamente, como en (\hyperref[III.4.2.1-fr]{4.2.1}), al caso en que
§52§ es afín y §53§ cerrado. Observemos que
(\hyperref[III.4.6.1.1-fr]{4.6.1.1}) da, por un razonamiento análogo,
para todo §54§, la relación
§55§
\oldpage[III]{141}
de donde se deduce, por (\hyperref[III.4.2.1-fr]{4.2.1}), que se tiene también
§56§

Dicho esto, se obtiene de la sucesión exacta de cohomología la exactitud de la
sucesión
§57§
y como §58§ es cerrado y §59§ afín, se tiene (\hyperref[III.1.4.11-fr]{1.4.11})
§60§
(G, II, 4.9.1); ahora bien,
§61§ es un
§62§-módulo, de donde
§63§
y esto termina de probar (\hyperref[III.4.6.1-fr]{4.6.1}).
\end{proof}

''',
('1','4.6.2'):r'''\begin{corollary}[4.6.2]
\label{III.4.6.2-fr}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo propio
y plano, §2§, §3§ dos §4§-Módulos localmente
libres, §5§ un punto de §6§. Pongamos
§7§,
§8§,
§9§,
y supongamos que se tiene
§10§

Entonces, para todo homomorfismo §11§, existe
una vecindad abierta §12§ de §13§ y un homomorfismo
§14§
tales que §15§ es igual al homomorfismo §16§.
\end{corollary}

\begin{proof}
En efecto, la hipótesis permite aplicar (\hyperref[III.4.6.1-fr]{4.6.1}) al
§17§-Módulo coherente
§18§ para
§19§ y §20§, pues §21§ es localmente libre y \emph{a fortiori}
§22§-plano, y el §23§-Módulo
§24§ se identifica entonces con
§25§
(\textbf{0}\textsubscript{I}, 6.2.2). Se puede suponer §26§
afín, y entonces (\hyperref[III.1.4.11-fr]{1.4.11})
§27§,
luego
§28§;
al ser el homomorfismo canónico
§29§
sobreyectivo por (\hyperref[III.4.6.1-fr]{4.6.1}), esto establece el
corolario, pues todo elemento de
§30§ puede siempre ponerse en la forma
§31§, donde §32§ es un elemento de §33§.
\end{proof}

Este corolario puede completarse con el siguiente:

''',
('1','4.6.7'):r'''\begin{proposition}[4.6.7]
\label{III.4.6.7-fr}
Sean §0§ un preesquema localmente noetheriano, §1§, §2§ dos §3§-preesquemas
tales que los morfismos estructurales §4§, §5§ son propios.
Sean §6§ un §7§-morfismo, §8§ un punto de §9§, y sea
§10§.
\begin{enumerate}
\item[\textup{(i)}] Si §11§ es un morfismo finito \textup{(resp.} una inmersión cerrada),
existe una vecindad abierta §12§ de §13§ tal que el morfismo
§14§, restricción de §15§, es un morfismo finito \textup{(resp.}
una inmersión cerrada).
\item[\textup{(ii)}] Se supone además que §16§ es un morfismo plano. Entonces, si
§17§ es un isomorfismo, existe una vecindad abierta §18§ de §19§ tal que
el morfismo §20§, restricción de §21§, es un
isomorfismo.
\end{enumerate}
\end{proposition}

\begin{proof}
En ambos casos, bastará probar que para todo §22§
existe una vecindad §23§ de §24§ tal que la restricción
§25§ de §26§ es un morfismo finito (resp. una inmersión
cerrada, un isomorfismo); resultará entonces en efecto que si §27§ es la
unión de los §28§, la restricción §29§ de §30§ es un morfismo
finito (resp. una inmersión cerrada, un isomorfismo) (\textbf{II}, 6.1.1 y \textbf{I}, 4.2.4).
Como §31§ es un morfismo cerrado, existirá una vecindad abierta §32§ de §33§
tal que §34§, y la proposición quedará demostrada.

\noindent (i) Observemos ante todo que §35§ es un morfismo propio
(\textbf{II}, 5.4.3); si se
\oldpage[III]{143}
supone §36§ finito, la existencia para todo
§37§ de una vecindad §38§ tal que §39§ es finito
resulta de (\hyperref[III.4.4.11-fr]{4.4.11}).
Para tratar el caso en que §40§ es una inmersión cerrada, se puede pues ya
suponer que el morfismo §41§ es \emph{finito}, luego que
§42§, donde §43§ es una
§44§-Álgebra coherente, correspondiendo el morfismo §45§ (\textbf{II}, 1.2.7)
al homomorfismo canónico §46§. Si se prueba
que para todo §47§ el homomorfismo
§48§ es sobreyectivo, resultará que para una
vecindad §49§ de §50§, §51§ será sobreyectivo, al ser el haz
§52§ coherente (\textbf{0}\textsubscript{I}, 5.3.4 y 5.2.2).
Dicho esto, el morfismo finito §53§ corresponde al homomorfismo
§54§,
y la hipótesis de que §55§ es una inmersión cerrada implica que
el homomorfismo
§56§
es sobreyectivo. Como §57§ es un §58§-módulo de tipo
finito y §59§ un anillo local noetheriano, la conclusión resulta,
como en (\hyperref[III.4.6.3-fr]{4.6.3}), del lema de Nakayama.

\noindent (ii) El mismo razonamiento que antes muestra que
esta vez basta probar que §60§ es biyectivo, sabiendo que
§61§ es biyectivo.

Esto resultará del lema siguiente:
\end{proof}

\begin{lemma}[4.6.7.1]
\label{III.4.6.7.1-fr}
Sean §62§, §63§ dos anillos locales noetherianos,
§64§ un homomorfismo local, §65§ un homomorfismo de
§66§-módulos. Se supone que §67§ es un §68§-módulo plano, §69§ un §70§-módulo
de tipo finito y que
§71§
(donde §72§ es el cuerpo residual de §73§) es inyectivo. Entonces §74§ es un
§75§-módulo plano y §76§ es inyectivo.
\end{lemma}

\begin{proof}
Para establecer la primera afirmación, hay que mostrar que para todo par de
§77§-módulos \emph{de tipo finito} §78§, §79§ y todo §80§-homomorfismo inyectivo
§81§,
§82§ es inyectivo. Ahora bien, se tiene el
diagrama conmutativo
§83§
y como §84§ es inyectivo por hipótesis, bastará probar
que lo mismo ocurre con §85§. Sea §86§ el ideal maximal
de §87§; la filtración §88§-ádica sobre el §89§-módulo
§90§ es también su filtración §91§-ádica como
§92§-módulo; la topología definida por esta filtración es pues \emph{separada},
puesto que §93§ es noetheriano, §94§ está contenido en el radical de
§95§, y §96§ es un §97§-módulo de tipo finito, al ser §98§ un
§99§-módulo de tipo finito y §100§ un §101§-módulo de tipo finito
(\textbf{0}\textsubscript{I}, 7.3.5). Basta pues probar que el homomorfismo
§102§
(donde los módulos graduados son relativos a las filtraciones §103§-ádicas)
es inyectivo (Bourbaki, \emph{Alg. comm.}, cap. III, \S\,2, n\textsuperscript{o}~8, cor. 1 del
teorema 1). Observemos ahora que, puesto que §104§ es un §105§-módulo plano, los
homomorfismos
§106§
son biyectivos; lo mismo ocurre pues con el homomorfismo canónico
§107§

\oldpage[III]{144}

Ahora bien, se tiene un diagrama conmutativo
§108§
en el cual §109§ es biyectivo, §110§ sobreyectivo; además,
§111§ es inyectivo por hipótesis, y como
§112§,
§113§,
§114§ es también inyectivo. Se concluye que
§115§ es inyectivo, lo que termina de demostrar la
primera afirmación. La segunda se deduce del razonamiento anterior haciendo
§116§.
\end{proof}

''',
('1','4.6.8'):r'''\begin{proposition}[4.6.8]
\label{III.4.6.8-fr}
Sean §0§ un preesquema localmente noetheriano, §1§, §2§, dos §3§-preesquemas
tales que los morfismos estructurales §4§, §5§ son propios,
§6§ una parte cerrada de §7§, §8§, §9§ sus imágenes
inversas,
§10§, §11§, §12§
los completados formales de §13§, §14§, §15§ a lo largo de estas partes cerradas,
§16§ un §17§-morfismo, §18§ su
prolongación a los completados. Para que §19§ sea un isomorfismo (\textup{resp.}
una inmersión cerrada), es necesario y suficiente que exista una vecindad abierta
§20§ de §21§ tal que el morfismo §22§, restricción de
§23§, sea un isomorfismo (\textup{resp.} una inmersión cerrada).
\end{proposition}

\begin{proof}
La suficiencia de la condición es inmediata (\textbf{I}, 10.14.7). Para mostrar su
necesidad, basta también probar que para todo §24§ existe una
vecindad abierta §25§ de §26§ tal que la restricción
§27§ de §28§ es un isomorfismo (resp. una inmersión
cerrada), por el mismo razonamiento que en
(\hyperref[III.4.6.7-fr]{4.6.7}). Se está así reducido al caso en que §29§,
siendo §30§ afín noetheriano. Por hipótesis
(\textbf{I}, 10.9.1 y 10.14.2), la fibra §31§ se reduce a un punto para
§32§, luego, como §33§ es propio (\textbf{II}, 5.4.3), existe una vecindad
abierta §34§ de §35§ tal que la restricción §36§ de §37§ es un
morfismo \emph{finito} (\hyperref[III.4.4.11-fr]{4.4.11}). Se puede pues ya suponer
que §38§ es un morfismo finito, luego §39§, donde §40§ es
una §41§-álgebra \emph{finita} sobre §42§. Si §43§, se tiene entonces
§44§, §45§,
siendo §46§ el separado completado de §47§ para la topología
§48§-preádica, §49§ el separado completado de §50§ para la
topología §51§-preádica, o (lo que equivale a lo mismo), el separado
completado del §52§-módulo §53§ para la topología §54§-preádica;
además, §55§ es el morfismo de esquemas formales afines correspondiente
a la prolongación continua §56§ del
homomorfismo canónico de anillos §57§, y la hipótesis es que
§58§ es sobreyectivo (resp. biyectivo) (\textbf{I}, 10.14.2). Ahora bien,
§59§ es también la prolongación continua de §60§ considerado
como homomorfismo de §61§-módulos; se sabe entonces (\textbf{I}, 10.8.14) que existe
una vecindad abierta §62§ de §63§ tal que la restricción a §64§ del
homomorfismo §65§ de
§66§-Módulos es sobreyectiva (resp. biyectiva), lo que termina la
demostración.
\end{proof}

\oldpage[III]{145}

\subsection{Un criterio de amplitud}

''',
('1','4.7.1'):r'''\begin{theorem}[4.7.1]
\label{III.4.7.1-fr}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo
propio, §2§ un §3§-Módulo invertible, §4§ un punto de
§5§, §6§, §7§ la proyección de §8§ en §9§.
Si §10§ es
amplio sobre §11§, existe una vecindad abierta §12§ de §13§ en §14§ tal que
§15§ es amplio para la restricción de §16§ a §17§.
\end{theorem}

\begin{proof}
\noindent I) Pongamos
§18§, §19§, y sea
§20§;
vamos primero a probar que §21§ es \emph{amplio para}
§22§. Se tiene el diagrama conmutativo
§23§
Como §24§ es propio (\textbf{II}, 5.4.2, (iii)) y §25§ noetheriano, se
ve que se puede limitar al caso en que
§26§, luego §27§, suponer que
§28§ es amplio para §29§ y probar que §30§ es amplio
para §31§ (\textbf{II}, 4.6.6). Vamos a aplicar el criterio
(\hyperref[III.2.6.1-fr]{2.6.1, \emph{c)}}) y a mostrar de hecho que para todo
§32§-Módulo coherente §33§ existe un entero §34§ tal que
§35§ para todo §36§, con
§37§.
Observemos que §38§ es un punto cerrado de §39§ correspondiente al ideal maximal
§40§ de §41§; §42§ es pues un subpreesquema cerrado de
§43§ definido por el Ideal coherente
§44§ de §45§ (\textbf{I}, 4.4.5), y §46§ la inclusión
canónica. Consideremos entonces la §47§-álgebra graduada
§48§,
que es de tipo finito puesto que §49§ es noetheriano; la
§50§-Álgebra §51§ es pues
cuasicoherente y de tipo finito, y está evidentemente anulada por
§52§, luego, si se pone §53§,
§54§ es una §55§-Álgebra cuasicoherente de tipo
finito, y §56§. Pongamos por otra parte
§57§ y
§58§;
como §59§ es coherente, §60§ es un §61§-Módulo
cuasicoherente de tipo finito (\textbf{0}, 10.1.1) que está también anulado por
§62§, de modo que si se pone
§63§, §64§
es un §65§-Módulo graduado cuasicoherente de tipo
finito tal que §66§. Además, si se pone
§67§, se tiene
§68§. Dicho esto, §69§ es propio
(\textbf{II}, 5.4.2, (iii)) y §70§ es amplio, luego §71§ es \emph{proyectivo}
(\textbf{II}, 5.5.4 y 4.6.11), y se puede aplicar a
§72§, §73§, §74§, §75§ y
§76§ el teorema (\hyperref[III.2.4.1-fr]{2.4.1, (ii)}):
existe un entero §77§ tal que para §78§ se tiene
§79§ para todo §80§ \emph{y todo} §81§; por tanto, se tiene
también §82§ para todo §83§ y todo §84§
(G, II, 4.9.1). Pongamos entonces
§85§,
de modo que §86§ para
§87§ y §88§. Se tiene
§89§, y, por la sucesión exacta de cohomología,
§90§ para todo §91§,
luego §92§ para todo §93§. Se concluye pues de
(\hyperref[III.4.2.1-fr]{4.2.1}) que §94§, lo que
termina de probar nuestra afirmación.

\noindent II) Volvamos a las notaciones del comienzo de la demostración,
y observemos que
\oldpage[III]{146}
siempre se puede suponer §95§
afín; como §96§ es de tipo finito y §97§ amplio para §98§,
existe un entero §99§ tal que §100§ es muy amplio para
§101§ (\textbf{II}, 4.6.11); reemplazando si es necesario §102§ por
§103§, se puede limitar a considerar el caso en que
§104§ es \emph{muy amplio} para §105§, y a probar que
§106§ es entonces muy amplio para §107§. Como §108§ es propio,
existe entonces una §109§-inmersión \emph{cerrada}
§110§ para un entero §111§ apropiado, tal que
§112§ es isomorfo a §113§ (\textbf{II}, 5.5.4, (ii));
esta inmersión corresponde canónicamente a un §114§-homomorfismo
\emph{sobreyectivo}
§115§
(\textbf{II}, 4.2.3). Este último corresponde (\textbf{0}\textsubscript{I}, 5.1.1) al dato
de §116§ secciones §117§ (§118§) de §119§ sobre
§120§ que generan este §121§-Módulo. Estas secciones son también por
definición secciones de §122§ sobre §123§; se tiene
§124§
(\textbf{0}\textsubscript{I}, 5.4.10), §125§ es afín y §126§ es el anillo
local en el ideal primo §127§ de §128§, luego se tiene
§129§, donde los §130§ son secciones de §131§
sobre §132§ y los §133§ elementos de §134§ que no pertenecen a
§135§; se concluye que existe una vecindad abierta afín §136§
de §137§ en §138§ y secciones §139§ de §140§ tales que
§141§ (se recuerda que el espacio §142§ está contenido en §143§, cf. \textbf{I},
2.4.2). Los §144§ son entonces secciones de §145§ sobre
§146§, que definen pues un homomorfismo
§147§
que, por hipótesis, es sobreyectivo en todos los puntos de §148§; como
§149§ es coherente (\textbf{0}\textsubscript{I}, 5.3.4), su
soporte es cerrado (\textbf{0}\textsubscript{I}, 5.2.2) y por tanto existe una
vecindad abierta §150§ de §151§ tal que la restricción
de §152§ a §153§ es un homomorfismo \emph{sobreyectivo}. Puesto que el morfismo §154§ es
cerrado, se puede suponer que §155§ es de la forma §156§, donde §157§ es una
vecindad abierta de §158§, y la conclusión resulta entonces de (\textbf{II}, 4.2.3).
\end{proof}

\subsection{Morfismos finitos de preesquemas formales}

'''
})

import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','5.1.3'):r'''\begin{corollary}[5.1.3]
\label{III.5.1.3-fr}
Sean §0§, §1§ dos §2§-Módulos coherentes tales que
la intersección de sus soportes sea propia sobre §3§. Entonces el homomorfismo canónico
§4§
que, a todo homomorfismo §5§, hace corresponder su
completado §6§, es un
isomorfismo. Además, cuando el morfismo §7§ es cerrado, para que §8§ sea
inyectivo (\textup{resp.} sobreyectivo), es necesario y suficiente que §9§ lo sea.
\end{corollary}

\begin{proof}
La primera aserción es un caso particular de (4.5.3), debido también a que el
primer miembro de (\ref{III.5.1.3.1.eq-fr}) es un §10§-módulo de tipo finito, luego
idéntico a su separado completado. Para demostrar la segunda, observemos en virtud de
(\textbf{I}, 10.8.14) que §11§ es inyectivo (resp. sobreyectivo) si y solo si existe
una vecindad de §12§ en la cual §13§ sea inyectivo (resp. sobreyectivo).

\oldpage[III]{150}
La conclusión
resulta pues del lema siguiente:
\end{proof}

\begin{lemma}[5.1.3.1]
\label{III.5.1.3.1-fr}
Bajo las hipótesis de \textup{(\hyperref[III.5.1.1-fr]{5.1.1})}, si se supone además el
morfismo §14§ cerrado, toda vecindad de §15§ en §16§ es idéntica a §17§.
\end{lemma}

\begin{proof}
En primer lugar, se puede reducir al caso en que §18§. En efecto, por hipótesis,
§19§ es una parte cerrada §20§ de §21§; se puede además reemplazar §22§ por
§23§ (\textbf{I}, 6.3.4), y suponer por consiguiente §24§ e §25§ reducidos; se puede entonces
reemplazar §26§ por el subpreesquema cerrado reducido de §27§ que tiene §28§ por espacio
subyacente (\textbf{I}, 5.2.2), pues todo ideal de §29§ es cerrado, y todo anillo cociente de
§30§ es por tanto ádico y noetheriano. Se tiene entonces §31§; si §32§ es una vecindad
abierta de §33§ en §34§, §35§ es cerrado en §36§ por hipótesis, y no corta
a §37§; pero esto es imposible a menos que §38§ sea vacío, puesto que
§39§ está contenido en el radical de §40§ (\textbf{I}, 1.1.15 y §41§,
7.1.10), de donde la conclusión.
\end{proof}

Cuando se limita a los §42§-Módulos coherentes cuyo soporte es propio
sobre §43§, (\hyperref[III.5.1.3-fr]{5.1.3}) puede enunciarse, en el lenguaje de las
categorías, diciendo que el funtor
§44§ es \emph{plenamente fiel} de la categoría de los
§45§-Módulos del tipo precedente en la categoría de los
§46§-Módulos coherentes, y establece por consiguiente una \emph{equivalencia} de
la primera de estas categorías con una subcategoría \emph{plena} de la segunda
(\textbf{0}, 8.1.6). El teorema de existencia probará que, cuando §47§ es propio sobre §48§,
esta subcategoría es de hecho la categoría de \emph{todos} los
§49§-Módulos coherentes. De manera precisa:

''',
('1','4.3.2'):r'''\begin{corollary}[4.3.2]
\label{III.4.3.2-fr}
Bajo las hipótesis de \textup{(\hyperref[III.4.3.1-fr]{4.3.1})}, supongamos además
que §0§ sea isomorfo a §1§. Entonces las fibras
§2§ de §3§ son conexas y no vacías para todo §4§.
\end{corollary}

\begin{proof}
La hipótesis de que §5§ es isomorfo a §6§
implica ya que §7§ es dominante, luego sobreyectivo puesto que §8§ es una
aplicación cerrada. Se puede reducir, como en
(\hyperref[III.4.2.1-fr]{4.2.1}), al caso en que §9§ es \emph{cerrado} en §10§;
§11§, siendo un espacio noetheriano, tiene un número finito de componentes
conexas, y es el espacio subyacente del completado §12§ a lo largo de
§13§. Si §14§ (§15§) son estas componentes conexas, está
claro que §16§ es compuesto
directo de los anillos §17§, y ninguno de estos
últimos se reduce a §18§, puesto que la sección unidad es distinta de
§19§ en cada punto de §20§. Ahora bien, si se aplica
(\hyperref[III.4.1.5-fr]{4.1.5}) a §21§, cuyo
completado a lo largo de §22§ es §23§, se ve que
§24§ es isomorfo al separado
completado §25§-ádico §26§ del anillo local
§27§; es por tanto un \emph{anillo local} que no puede ser compuesto
directo de varios anillos no reducidos a §28§ (pues tendría
varios ideales maximales distintos). Se tiene pues §29§, lo que demuestra el
corolario.
\end{proof}

''',
('1','12.2.1'):r'''\begin{env}[12.2.1]
\label{0.12.2.1-fr}
Sean §0§, §1§ dos espacios anillados,
§2§ un morfismo de §3§ en §4§, que define el funtor
\emph{imagen directa}
§5§,
idéntico además a la restricción a §6§ del funtor §7§ definido
en la categoría de los haces de grupos abelianos sobre §8§. Este último
funtor es aditivo y exacto por la izquierda, y como todo haz de grupos
abelianos sobre §9§ es isomorfo a un subhaz de un haz \emph{inyectivo} de
grupos abelianos, se definen los \emph{funtores derivados} derechos
§10§ del funtor §11§; los
§12§ son haces de grupos abelianos sobre §13§, y
los §14§ forman un \emph{funtor cohomológico universal} (T, 2.3).

Además, el haz §15§ es el haz asociado al
prehaz §16§ (T, 3.7.2). Si ahora
se supone que §17§ es un §18§-\emph{Módulo},
§19§ está naturalmente provisto de una estructura de
§20§-módulo, luego de
§21§-módulo, y el dato del homomorfismo
§22§ permite deducir una
estructura de §23§-módulo. Para las estructuras así
definidas, está claro que la restricción de un abierto §24§ a un abierto
§25§ define un dihomomorfismo, y esto permite por tanto definir sobre
cada uno de los §26§ una estructura de §27§-\emph{Módulo};
es este §28§-Módulo el que denotaremos por §29§,
quedando así §30§ definido como un funtor aditivo de §31§ en
§32§. Además, los §33§ forman un \emph{§34§-funtor}, pues si
§35§
es una sucesión exacta de §36§-Módulos, la descripción de los
§37§ y de la estructura de §38§-Módulo sobre
§39§ dada arriba muestra inmediatamente que
el homomorfismo
§40§
es en este caso un homomorfismo de §41§-\emph{Módulos}. Finalmente, los
§42§ se identifican con los funtores \emph{derivados} derechos de §43§: en efecto,
todo §44§-Módulo admite una resolución \emph{inyectiva} formada por
§45§-Módulos, y como tal resolución está formada por haces
\emph{flácidos} de grupos abelianos (G, II, 7.1), puede servir para calcular los
§46§, puesto que §47§ para §48§ y
para todo haz \emph{flácido} §49§ (T, 2.4.1, Observación 3, y cor. de la
prop. 3.3.2). Se concluye pues que los §50§ forman un \emph{funtor
cohomológico universal de} §51§ en §52§ (T, 2.3).
\end{env}

''',
('1','11.3.5'):r'''\begin{env}[11.3.5]
\label{0.11.3.5-fr}
Sea ahora §0§ un bicomplejo de
§1§ cuyos dos operadores de derivación son de grado §2§. Escribiremos
entonces §3§ (resp. §4§) para el complejo simple
§5§ (resp. §6§),
§7§ (resp.
§8§) para su objeto de homología de grado §9§,
§10§ (resp.
§11§) para el complejo
§12§ (resp.
§13§),
§14§
(resp.
§15§)
para su objeto de homología de grado §16§; notaciones análogas para los objetos de ciclos
y objetos de bordes; finalmente, §17§ designará
(cuando exista) el objeto de homología de grado §18§ del complejo simple (con
operador de derivación de grado §19§) definido por §20§.

Sea §21§ con
§22§ el bicomplejo con operadores de derivación de grados
§23§ asociado a §24§; por definición, las
\emph{sucesiones espectrales} de §25§ son las de
§26§, que se escriben §27§ y
§28§, donde sin embargo se cambian las notaciones, poniendo
§29§
para §30§. Con estas notaciones, se tiene
§31§
Para evitar errores de signo, será en general preferible, para las
relaciones entre estas sucesiones espectrales y su término límite, volver al
complejo §32§. Señalemos no obstante los criterios
correspondientes a (\hyperref[0.11.3.3-fr]{11.3.3}):
\end{env}

''',
})

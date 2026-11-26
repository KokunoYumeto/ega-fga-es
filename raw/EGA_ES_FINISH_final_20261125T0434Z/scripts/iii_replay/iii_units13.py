import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','1.1.3'):r'''\begin{env}[1.1.3]
\label{III.1.1.3-fr}
De los complejos precedentes se deducen, como de costumbre, los \emph{§0§-módulos
de homología y de cohomología} (G, I, 2.2)
§1§
Se define además un §2§-\emph{isomorfismo}
§3§ haciendo
corresponder a toda cadena
§4§ la cocadena §5§ tal que
§6§, donde
§7§ es la sucesión estrictamente creciente complementaria
de la sucesión estrictamente creciente §8§ en §9§ y
§10§, siendo §11§ el número de inversiones de la permutación
§12§ de §13§. Se verifica que
§14§, lo que da un isomorfismo
§15§
En este capítulo tendremos que considerar sobre todo los módulos de cohomología
§16§.

Para un §17§ dado, es inmediato (G, I, 2.1) que
§18§ es un \emph{funtor cohomológico}
(T, II, 2.1), de la categoría de los §19§-módulos en la de los §20§-módulos
graduados, nulo para los grados §21§ y §22§. Además, se tiene
§23§
designando por §24§ el ideal de §25§ engendrado por
§26§; esto resulta inmediatamente de
(\hyperref[III.1.1.2.3-fr]{1.1.2.3}), y está claro que
§27§ se identifica con el submódulo de §28§ \emph{anulado por
§29§}. Análogamente, se tiene según
(\hyperref[III.1.1.2.3-fr]{1.1.2.3})
§30§
Utilizaremos el siguiente resultado conocido, del que recordaremos una
demostración para ser completos:
\end{env}

''',
('1','5.4.4'):r'''\begin{proposition}[5.4.4]
\label{III.5.4.4-fr}
Sean §0§ un anillo ádico noetheriano, §1§,
§2§, §3§ dos morfismos
propios de esquemas formales, §4§ un
§5§-morfismo. Si §6§ es finito y si §7§ es algebraizable,
entonces §8§ es algebraizable.
\end{proposition}

\begin{proof}
Se observará que las hipótesis sobre §9§ y §10§ implican ya que §11§ es propio
(3.4.1), y para que §12§ sea finito, basta que para todo §13§ la
fibra §14§ sea \emph{finita} (\hyperref[III.4.8.11-fr]{4.8.11}). La hipótesis
implica que §15§ es una
§16§-Álgebra coherente
(\hyperref[III.4.8.6-fr]{4.8.6}), luego resulta del teorema de existencia que, si
§17§ y §18§, donde
§19§ es un morfismo propio de esquemas usuales,
existe una §20§-Álgebra coherente §21§ tal que
§22§. Sean §23§, y
§24§ el morfismo estructural; entonces resulta inmediatamente de la definición de
§25§ a partir de §26§
(\hyperref[III.4.8.7-fr]{4.8.7}) que §27§ es canónicamente isomorfo a
§28§ y que §29§ se identifica con §30§ (basta para verlo
considerar el caso en que §31§ es afín).

Se observará que (\hyperref[III.5.1.8-fr]{5.1.8}) es un caso particular de
(\hyperref[III.5.4.4-fr]{5.4.4}).
\end{proof}

''',
('6','6.8.1'):r'''\begin{env}[6.8.1]
Siendo las hipótesis y notaciones las de (6.7.11) (y en particular los
§0§ supuestos \emph{acotados inferiormente}), supongamos
dada una partición §1§ del conjunto de índices §2§; nos
proponemos dar una relación de «asociatividad» entre los hipertor
§3§ y
cada uno de los hipertor «parciales»
§4§

\oldpage[III]{165}
Para simplificar la escritura, nos limitaremos al caso en que §5§ es
el intervalo §6§, y en que la partición §7§ se compone de los dos
intervalos §8§ y §9§.
\end{env}

''',
('6','6.8.3'):r'''\begin{corollary}[6.8.3]
Sean §0§ un anillo, §1§, §2§
(§3§) unos §4§-esquemas cuasicompactos y, para cada §5§, sea
§6§ un complejo de
§7§-Módulos cuasicoherentes acotado inferiormente. Existe
un funtor espectral canónico birregular que tiene por término límite
§8§
y cuyo término §9§ está dado por
§10§
\end{corollary}

\begin{proof}
Según la definición dada en (6.6.2), el cálculo del hipertor considerado se
hace tomando para cada §11§ un recubrimiento abierto afín finito
§12§ de §13§, considerando los bicomplejos
§14§, una resolución proyectiva
§15§ de Cartan-Eilenberg de cada uno de estos
bicomplejos (en el sentido de (\textbf{0}, 11.7.1)), el producto tensorial
§16§
de estos tricomplejos, y tomando la homología de
§17§. Consideremos §18§ como
un complejo simple §19§, producto tensorial de los dos complejos simples
§20§
donde §21§ y §22§ están graduados por la suma de los grados totales
de los §23§. Además, los §24§-módulos de los
complejos §25§ y §26§ son \emph{proyectivos}, luego resulta de
(6.5.9) que se tiene
§27§;
la sucesión espectral buscada no es entonces sino la sucesión (6.3.2.2)
aplicada a los complejos §28§ y §29§, teniendo en cuenta
la interpretación de los módulos de homología de estos complejos que resulta de lo
que precede (cuando se aplican las observaciones del comienzo a cada uno de los productos
parciales
§30§ y
§31§). Finalmente, las propiedades de
regularidad resultan de (6.3.2) y del hecho de que, al estar los
§32§ acotados inferiormente, lo mismo ocurre
con los §33§; por consiguiente, §34§ y
§35§ están acotados inferiormente.
\end{proof}

\oldpage[III]{166}
\subsection{Las sucesiones espectrales de cambio de base en los hipertor
globales.}

''',
('7','7.1.3'):r'''\begin{env}[7.1.3]
Suponiendo siempre conmutativo el anillo §0§, sea §1§ una §2§-\emph{álgebra} (no
necesariamente conmutativa), y sea §3§ el homomorfismo de anillos
correspondiente a esta estructura de álgebra; este homomorfismo define un
funtor covariante
\oldpage[III]{176}
aditivo §4§
de la categoría §5§ de los §6§-módulos izquierdos en la categoría
§7§ de los §8§-módulos. Por composición, se deduce un funtor §9§,
evidentemente covariante y aditivo, que denotaremos también por §10§ (por
razones tipográficas) o §11§, y que diremos obtenido a partir
de §12§ por \emph{extensión de escalares} de §13§ a §14§. Por supuesto, si §15§ es
conmutativa, se puede considerar §16§ como un funtor de
§17§ en sí misma (7.1.2). Cuando §18§ es conmutativa, y §19§
una §20§-álgebra, se ve inmediatamente que §21§;
es inmediato que la extensión de escalares es \emph{funtorial} y \emph{aditiva} en
§22§; además, cuando §23§ conmuta con los límites inductivos o con las sumas
directas (resp. es exacto por la izquierda, exacto por la derecha, exacto), lo mismo ocurre
con §24§: en efecto, §25§ es exacto y conmuta con los límites inductivos
y las sumas directas.
\end{env}

''',
('7','7.5.6'):r'''\begin{corollary}[7.5.6]
Supongamos verificadas las hipótesis generales de \textup{(7.5.4)}, y supongamos además
que §0§ sea un anillo de valuación discreta.
\begin{enumerate}
  \item[\textup{(i)}] Para que §1§ sea exacto por la derecha, es necesario y suficiente que
    §2§ sea un §3§-módulo libre.
  \item[\textup{(ii)}] Para que §4§ sea exacto, es necesario y suficiente que §5§ y
    §6§ sean §7§-módulos libres.
\end{enumerate}
\end{corollary}

\begin{proof}
\oldpage[III]{192}
Está claro que (i) implica (ii) (cf. (7.3.3)). Para probar (i), observemos
que si §8§ es un generador del ideal maximal de §9§ («uniformizante» de
§10§), para que un §11§-módulo de tipo finito §12§ sea libre (o plano, lo que viene
a ser lo mismo), es necesario y suficiente que la homotecia §13§ de §14§ sea
inyectiva, pues esto equivale aquí a decir que §15§ es sin torsión
(§16§, 6.3.4). Consideremos entonces la sucesión exacta
§17§,
que proporciona la sucesión exacta de homología
§18§

Se ve que §19§ es libre si y solo si
§20§ es sobreyectivo; la conclusión resulta entonces de (7.5.2).
\end{proof}

''',
})

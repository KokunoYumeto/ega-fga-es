import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply({
'current:1:1.2.4:0':r''' tales que
§0§. Entonces, para todo
§1§-Módulo cuasicoherente ''',
'current:1:1.2.4:1':r'''; la hipótesis implica entonces
§0§ para todo ''',
'current:1:1.4.5:0':r''' por abiertos afines tales que la restricción
§0§ es isomorfa a §1§ para cada
''',
'current:1:1.4.15:0':r''', donde
§0§,
es canónicamente isomorfo a
''',
'current:1:1.4.15:1':r'''.
\end{proposition}

\oldpage[III]{93}
\begin{proof}
El homomorfismo canónico
''',
'current:1:2.1.1:0':r''', se pondrá
§0§

Los grupos abelianos (\hyperref[III.2.1.1.2-fr]{2.1.1.2}) y
(\hyperref[III.2.1.1.3-fr]{2.1.1.3}) son \emph{bigraduados}, tomando
''',
'current:1:2.1.8:0':r'''
§0§
El ''',
'current:1:2.1.8:1':r''' de los monomios
§0§ con
§1§, §2§ para todo §3§.
\end{lemma}

\begin{proof}
Es una consecuencia inmediata de (1.1.3.5) y de la prop. (1.1.4), cuyas
hipótesis se verifican trivialmente.
\end{proof}

''',
'current:1:2.1.9:0':r''', siendo el homomorfismo
§0§
para §1§
la multiplicación por ''',
'current:1:2.1.9:1':r''', designemos por
§0§ la clase de
§1§; se tiene entonces
''',
'current:1:2.1.11:0':r'''; el razonamiento de
(\hyperref[III.2.1.8-fr]{2.1.8}) muestra que se tiene más generalmente
§0§
pues la última fórmula se deduce directamente de (1.1.3.5), y por otra
parte está claro que
''',
'current:1:2.1.12:0':r''', y siendo el producto
§0§ igual a
§1§.
\end{enumerate}
\end{proposition}

\begin{proof}
Observemos en efecto que, en la sucesión exacta
(\hyperref[III.2.1.5.2-fr]{2.1.5.2}) aplicada a
§2§,
se tiene
''',
'current:1:2.1.13:0':r''' para los pares enumerados en
(\hyperref[III.2.1.13-fr]{2.1.13}); esto resulta de
(\hyperref[III.2.1.12-fr]{2.1.12}), puesto que §0§ es entonces §1§ para
todos los grados ''',
'current:1:2.1.16:0':r'''-Módulo invertible. Entonces:
\begin{enumerate}
\item[{\rm(i)}] Se tiene un isomorfismo canónico
§0§
\item[{\rm(ii)}] El apareamiento por producto cup (\textbf{0}, 12.2.2)
''',
'current:1:2.2.3:0':r'''-Módulos son
coherentes (\textbf{0}\textsubscript{I}, 5.3.4). Como §0§ es un
funtor exacto en §1§, basta probar que para ''',
'current:1:2.2.4:0':r''', se pone
§0§
(para §1§). Sea
''',
'current:1:2.2.4:1':r''', donde §0§ es la inmersión
canónica §1§ (\textbf{II}, 4.4.7). Pongamos
''',
'current:1:2.2.4:2':r''' de
haces tal que §0§ es el homomorfismo sobreyectivo dado
''',
'current:1:2.2.4:3':r'''
donde §0§ y §1§ son los homomorfismos de restricción. La definición de
''',
'current:1:2.2.5:0':r''' (\textbf{II}, 5.1.6). Pero el anillo
§0§ se identifica con la intersección de los anillos de
fracciones §1§ para §2§
(\textbf{I}, 8.2.1.1), es decir, con §3§. Por tanto, resulta
de las fórmulas (1.4.3.1) y (1.1.3.5) que se tiene
''',
'current:1:2.3.1:0':r''' es noetheriano, el mismo razonamiento que al comienzo de
(\hyperref[III.2.2.2-fr]{2.2.2}) muestra que se puede limitar al caso en que
§0§, §1§,
§2§, ''',
'current:1:2.3.1:1':r''' (\textbf{II}, 2.9.2). Si §0§ es la inclusión canónica
§1§, ''',
'current:1:2.3.6:0':r'''-Módulo coherente
§0§ de §1§, existe un
''',
'current:1:2.3.6:1':r'''
la hipótesis significa pues que hay un homomorfismo no nulo §0§ de
§1§ en §2§. Como, para todo
''',
'current:1:2.3.6:2':r''' es
coherente y §0§, puesto que existe un abierto ''',
'current:1:2.5.1:0':r''', los §0§ §1§ son ''',
'current:1:2.5.1:1':r'''-módulos de
tipo finito (\hyperref[III.2.2.1-fr]{2.2.1}), luego aquí \emph{de longitud finita}
puesto que ''',
'current:1:2.5.4:0':r'''. Se tiene entonces
§0§
para ''',
'current:1:2.5.4:1':r''' suficientemente grande.
\end{corollary}

\begin{proof}
Esto resulta de que §0§ y §1§ son
isomorfos para ''',
'current:1:2.5.4:2':r''' suficientemente grande
(\hyperref[III.2.3.1-fr]{2.3.1}).
\end{proof}

\subsection{Aplicación: criterios de amplitud}
\label{subsection:III.2.6-fr}

''',
'current:1:3.1.1:0':r'''\begin{definition}[3.1.1]
\label{III.3.1.1-fr}
Sea §0§ una categoría abeliana. Se dice que un subconjunto §1§ del
conjunto de objetos de §2§ es exacto si §3§ y si, para toda
sucesión exacta
''',
'current:1:3.1.1:1':r'''
en §0§ tal que dos de los objetos ''',
'current:1:3.1.1:2':r''' están en §0§, entonces el
tercero está también en §1§.
\end{definition}

''',
'current:1:3.1.3:0':r'''\begin{corollary}[3.1.3]
\label{III.3.1.3-fr}
Supongamos que el subconjunto exacto §0§ de §1§ tiene además la propiedad
de que todo factor directo coherente de un ''',
'current:1:3.1.3:1':r'''-Módulo coherente
§0§ pertenece también a §1§. En estas condiciones, la
conclusión de (\hyperref[III.3.1.2-fr]{3.1.2}) sigue siendo válida cuando la
condición «''',
'current:1:3.1.3:2':r'''; el final
del razonamiento de (\hyperref[III.3.1.2-fr]{3.1.2}) prueba entonces que
§0§, y la hipótesis adicional sobre §1§ implica que
§2§.
\end{proof}

\subsection{El teorema de finitud: caso de los esquemas usuales}
\label{subsection:III.3.2-fr}

''',
'current:1:3.4.1:0':r''' es un morfismo \emph{propio} si
verifica las condiciones siguientes:
\begin{enumerate}
\item[§0§] \emph{''',
'current:1:3.4.1:1':r''' es un morfismo de tipo finito} (\textbf{I}, 10.13.3).
\item[§0§] \emph{Si ''',
'current:1:3.4.4:0':r'''-módulo graduado \emph{de
tipo finito}. Esto prueba que la condición §0§ de (\textbf{0}, 13.7.7) se
verifica para \emph{todo ''',
'current:1:3.4.4:1':r'''-módulo filtrado». Se puede pues aplicar (\textbf{0}, 13.7.7), que prueba que:
\begin{enumerate}
\item[§0§] El sistema proyectivo
''',
'current:1:3.4.4:2':r''' verifica la condición (ML).
\item[§0§] Si
''',
'current:1:3.4.4:3':r'''-módulo de tipo finito.
\item[§0§] La filtración definida sobre ''',
'current:1:4.1.1:0':r''', §0§ su imagen inversa
§1§. Designaremos por ''',
'current:1:4.1.1:1':r''' respectivamente (\textbf{I}, 10.8.5), por §0§ la \emph{prolongación}
de ''',
'current:1:4.1.1:2':r''' a estos completados (\textbf{I}, 10.9.1), que es un morfismo
§0§ de preesquemas formales. Para todo
''',
'current:1:4.1.1:3':r''',
\oldpage[III]{123}
designaremos por §0§ su \emph{completado} §1§ a lo
largo de ''',
'current:1:4.1.2:0':r'''-Módulos §0§ y
§1§ son \emph{coherentes} para todo ''',
'current:1:4.1.8:0':r'''-Módulo coherente (\textbf{I}, 10.8.4),
y §0§ es igual a
§1§
(\textbf{0}\textsubscript{I}, 3.2.6); el hecho de que ''',
'current:1:4.1.8:1':r''' de
(\hyperref[III.4.1.3.5-fr]{4.1.3.5}) es un \emph{isomorfismo}, luego ''',
'current:1:4.1.8:2':r'''
es un isomorfismo por definición de
§0§.
\end{env}

''',
'current:1:4.1.10:0':r'''. Además, se puede
siempre suponer que §0§, donde
§1§ es un ''',
'current:1:4.1.10:1':r''',
se tiene §0§,
§1§ y
''',
'current:1:4.2.2:0':r''' un morfismo
propio, §0§ un punto de §1§, ''',
'current:1:4.2.2:1':r'''.
\end{corollary}

\begin{proof}
En efecto, se tiene entonces
''',
'current:1:4.2.2:2':r'''
(G, II, 4.15.2) para todo §0§, luego
(\hyperref[III.4.2.1-fr]{4.2.1}) el separado completado de
''',
'current:1:4.3.1:0':r''' el §0§-esquema finito sobre ''',
'current:1:4.3.1:1':r''' del morfismo §0§ son conexas y no vacías para todo
''',
'current:1:4.3.2:0':r''' son conexas y no vacías para todo §0§.
\end{corollary}

\begin{proof}
La hipótesis de que ''',
'current:1:4.3.2:1':r''') son estas componentes conexas,
está claro que §0§ es producto
directo de los anillos §1§, y ninguno de estos
últimos se reduce a §2§, puesto que la sección unidad es distinta de
§3§ en cada punto de ''',
'current:1:4.3.2:2':r'''; es pues un \emph{anillo local} que no puede ser producto
directo de varios anillos no reducidos a §0§ (pues tendría entonces
varios ideales maximales distintos). Se tiene pues ''',
'current:1:4.3.4:0':r''' (\textbf{I}, 2.4.1); pongamos
§0§, y §1§; ''',
'current:1:4.3.4:1':r''' es un morfismo \emph{plano},
como resulta de (\textbf{I}, 2.4.2) y de
(\hyperref[III.1.4.15-fr]{1.4.15.5}); se tiene pues
''',
'current:1:4.3.4:2':r'''
en virtud de (\hyperref[III.1.4.15-fr]{1.4.15}) aplicado para §0§.

En el caso general (\hyperref[III.4.3.1-fr]{4.3.1}), el mismo razonamiento
muestra que se tiene (con las notaciones de
(\hyperref[III.4.3.1-fr]{4.3.1}))
''',
'current:1:4.3.4:3':r''' una extensión \emph{algebraicamente cerrada} de §0§, este número
es independiente de la extensión algebraicamente cerrada considerada e igual al
\emph{número geométrico de puntos de} ''',
'current:1:4.3.5:0':r'''; se
sabe ([13], vol. I, pp. 257 y 259) que todo ideal maximal de tal anillo
§0§ es la intersección de §1§ y de un ideal maximal de ''',
'current:1:4.3.6:0':r''' es la traza
de un ideal maximal de ''',
'current:1:4.3.6:1':r''' es un anillo local, el ideal maximal
de §0§ es la traza sobre ''',
'current:1:4.3.6:2':r''' para
§0§ por el mismo razonamiento que antes, luego ''',
'current:1:4.3.7:0':r'''; pero se sabe que si ''',
'current:1:4.3.9:0':r''' respectivamente (de modo que
§0§), y si se pone §1§, toda componente irreducible
de ''',
'current:1:4.3.9:1':r''', restricción de §0§, es universalmente abierto.

''',
'current:1:4.3.10:0':r'''. Sean
\oldpage[III]{134}
§0§, §1§; designemos por §2§, §3§,
§4§ los puntos genéricos de §5§, §6§ y §7§ respectivamente, de modo
que §8§ y §9§; además,
§10§, luego §11§ es isomorfo a
§12§ (\textbf{I}, 3.6.4) y en particular, puesto que §13§ es el punto
genérico de §14§ (\textbf{0}\textsubscript{I}, 2.1.8),
§15§ tiene un solo punto genérico. Pero por hipótesis, toda
componente irreducible de §16§ tiene su punto genérico en
§17§, luego §18§ es necesariamente irreducible, su punto
genérico §19§ es el punto genérico de §20§ y se tiene
§21§.
Pongamos ''',
'current:1:4.3.11:0':r'''
verifica las hipótesis de (\hyperref[III.4.3.10-fr]{4.3.10}), entonces, si
§0§ son dos puntos de §1§ tales que ''',
'current:1:4.3.12:0':r''' tal que
§0§ es isomorfo a §1§. Si, más
particularmente, se supone ''',
'current:1:4.3.12:1':r'''), §0§ es isomorfo a
§1§.
\end{corollary}

\begin{proof}
La primera afirmación relativa a ''',
})

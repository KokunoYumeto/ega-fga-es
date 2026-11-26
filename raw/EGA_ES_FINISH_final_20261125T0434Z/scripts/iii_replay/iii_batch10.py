import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply({
'current:7:7.7.4:0':r'''-planos \emph{acotado inferiormente}, se ha
visto (6.10.5) que se puede escribir, salvo isomorfismo,
§0§,
con §1§,
donde ''',
'current:7:7.7.5:0':r'''-Módulos cuasicoherentes tal que
§0§, §1§, §2§;
ahora bien, esto resulta inmediatamente de la hipótesis de que ''',
'current:7:7.7.9:0':r'''
lo que no es sino (§0§, 4.4.3.1). Del mismo modo, cuando en (7.7.7)
se reemplaza ''',
'current:7:7.7.9:1':r''': esto resulta de que se tiene también una
sucesión exacta
§0§ con
§1§
y de que
§2§ (§3§).

\medskip
\textnormal{(ii)} La condición (ii) del enunciado de (7.7.8) relativa a
''',
'current:7:7.7.12:0':r'''}, tal que
§0§ para todos los pares §1§.
Se concluye que existe ''',
'current:7:7.7.12:1':r'''-módulos tal que
§0§ para §1§, §2§ y §3§ para
§4§ y sea ''',
'current:7:7.7.12:2':r''', de grado 0 (en cuyo caso
''',
'current:7:7.7.12:3':r''' es afín, se tiene
§0§,
con §1§,
donde ''',
'current:7:7.8.2:0':r'''\begin{env}[7.8.2]
Por definición, la noción de planitud homológica sobre ''',
'current:7:7.8.4:0':r''' \textup{(§0§, 4.1.4)}, e) es
equivalente a las demás condiciones.
\end{proposition}

\oldpage[III]{206}
\begin{proof}
En efecto, la condición \emph{b)} equivale a decir que ''',
'current:7:7.8.4:1':r''' es artiniano, y que
§0§ y
§1§ son
''',
'current:7:7.8.4:2':r'''
(§0§, 5.2.7). Recíprocamente, está claro que \emph{d)} implica \emph{a)} por
definición del funtor ''',
'current:7:7.8.8:0':r''' que figura en (7.8.7,
(i)) es necesariamente igual a 1.
\end{proof}

''',
'current:7:7.8.9:0':r'''
apropiado; basta pues aplicar la equivalencia de (7.7.5, \emph{a)}) y
(7.7.5, \emph{b§0§)}) al caso ''',
'current:7:7.8.9:1':r''' el complejo
reducido a su término de grado 0 igual a ''',
'current:7:7.8.10:0':r''' (bajo estas
condiciones) no es necesariamente cohomológicamente plano en \emph{dimensión
1} sobre ''',
'current:7:7.8.10:1':r''' como el
haz de las 1-diferenciales del esquema de Picard de ''',
'current:7:7.9.1:0':r''' sobre
''',
'current:7:7.9.4:0':r'''-planos. Si se pone
§0§ \textup{(cf. (7.7.1.1))},
la función
\oldpage[III]{209}
''',
'current:7:7.9.5:0':r''' es conexo y no vacío, se designa
el valor único (entero) de (7.9.4.1) por §0§ o §1§, o simplemente
§2§
si no puede resultar confusión, y se dice que este entero es la
\emph{característica de Euler-Poincaré} de ''',
'current:7:7.9.5:1':r'''). En el caso general, se denotará también por §0§ o §1§ o
§2§
el segundo miembro de (7.9.4.1).
\end{env}

''',
'current:7:7.9.6:0':r''' cuyo único término §0§ es de grado ''',
'current:7:7.9.6:1':r''' e igual a
§0§. Se ve pues que se puede reducir al estudio de las características
de Euler-Poincaré de complejos reducidos a un solo término.
\end{env}

''',
'current:7:7.9.7:0':r''' un morfismo, §0§, §1§,
§2§ el complejo finito
§3§
de ''',
'current:7:7.9.7:1':r'''-planos en
virtud de (§0§, 6.2.1) y (I, 4.14.5), al ser la cuestión local sobre
''',
'current:7:7.9.8:0':r''' tal que §0§ para §1§ y todo §2§.
Entonces §3§
es un ''',
'current:7:7.9.10:0':r''' reducido a su término
de grado ''',
'current:7:7.9.10:1':r''' igual a §0§, se tiene en efecto
''',
'current:7:7.9.12:0':r'''\begin{env}[7.9.12]
\label{III.7.9.12.fr}
Con las notaciones de (7.9.6) y (7.9.11), se tiene
''',
'current:7:7.9.13:0':r'''
\oldpage[III]{212}
se tiene §0§ para todo §1§ (2.2.1); la conclusión
resulta pues de (7.9.10).
\end{proof}

El criterio de planitud siguiente será importante en la teoría de los «módulos»
de los haces coherentes del cap. V:

''',
'current:7:7.9.14:0':r''', y pongamos
§0§ para todo
''',
'current:7:7.9.14:1':r'''. Para que un
''',
'current:7:7.9.14:2':r'''-Módulo localmente libre.
\end{proposition}

\begin{proof}
La necesidad de la condición se demuestra como en (7.9.13) (aplicándose el resultado de
(2.2.1) a un haz amplio §0§, puesto que ''',
'current:7:7.9.14:3':r''' es
proyectivo). Para demostrar el recíproco, se puede limitar al caso en que §0§ es
afín de anillo §1§; en virtud de la hipótesis y de (2.2.2, (i)), los
''',
'current:7:7.9.14:4':r''' son de tipo finito y proyectivos (Bourbaki,
\emph{Alg. comm.}, cap. II, \S~5, n\textsuperscript{o}~2, teorema 1). Sea §0§
el anillo graduado §1§;
se sabe que ''',
'current:7:7.9.14:5':r''' está generado por un número finito de elementos de grado 1
(2.3.5.1), y resulta entonces de (\textbf{II}, 2.7.5 y 2.7.2) que ''',
'current:7:7.9.14:6':r''' de
grado §0§, se tiene pues ''',
'current:7:7.9.14:7':r''' (§0§, 6.3.2), y por tanto también de ''',
'current:7:7.9.14:8':r''' (§0§, 6.1.2). Se concluye (I, 4.14.5) que
''',
})

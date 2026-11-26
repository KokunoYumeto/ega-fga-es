import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
M={
('7','7.6.3'):r'''\begin{proposition}[7.6.3]
Bajo las condiciones de \textup{(7.4.1)}, supongamos que §0§ es un anillo noetheriano
regular de dimensión 1 (en otros términos, que §1§ es noetheriano y que, para todo
§2§, §3§ es un cuerpo o un anillo de valuación
discreta). Entonces, para todo entero §4§ y todo §5§-módulo §6§, se tiene una sucesión
exacta canónica funtorial en §7§
§8§
\end{proposition}

\begin{proof}
En lo que sigue, suprimiremos para simplificar la mención del complejo
§9§ en las notaciones homológicas usuales §10§,
§11§, §12§ y §13§. Se tienen las tres sucesiones
exactas
§14§

Como §15§ y §16§ son planos, lo mismo ocurre con sus
\emph{submódulos} respectivos §17§, §18§ y §19§ puesto que hay
identidad entre §20§-módulos planos y §21§-módulos sin torsión (para todo
§22§); por tensorización con §23§, se tienen pues las sucesiones
exactas
§24§
§25§
§26§

Por definición,
§27§;
es pues el núcleo del homomorfismo
§28§
obtenido a partir de §29§ por paso al cociente, homomorfismo que
se escribe también §30§ por definición de
§31§; ahora bien, este homomorfismo puede considerarse como el compuesto
§32§

Como §33§ es inyectivo según (7.6.3.4), se tiene una sucesión exacta
§34§
que no es otra que (7.6.3.1), teniendo en cuenta (7.6.3.2) y (7.6.3.3) y
que §35§ por definición.
\end{proof}

''',
('7','7.6.11'):r'''\begin{remark}[7.6.11]
Cabe preguntarse si la afirmación de (7.6.9, (i)) no puede reforzarse con
la desigualdad
§0§
para todo §1§, que se verifica efectivamente cuando §2§
es un anillo de valuación discreta y §3§ su ideal maximal (7.6.5).
Limitémonos al caso en que §4§ es un anillo \emph{local} noetheriano, de ideal maximal
§5§ y de cuerpo residual §6§. Entonces las condiciones siguientes son
\emph{equivalentes}:
\begin{enumerate}
  \item[\emph{a)}] Para \emph{todo} complejo §7§ de §8§-módulos planos de tipo finito,
    se tiene
    §9§
  \item[\emph{b)}] Para todo §10§-módulo §11§ de tipo finito, se tiene
    §12§
  \item[\emph{c)}] Para todo §13§-módulo §14§ de tipo finito, se tiene
    §15§
\end{enumerate}

Se observará que equivale, por desplazamiento (M, V, 7.2), a decir que se tiene,
para todo §16§,
§17§

Demos brevemente algunas indicaciones sobre la demostración. Para ver que \emph{a)}
implica \emph{b)}, se considera una sucesión exacta
§18§
donde §19§ y §20§ son libres de tipo finito, y se aplica \emph{a)} al complejo
§21§ con §22§, §23§,
siendo nulos los demás términos; se tiene entonces §24§ y
§25§,
en otros términos, §26§ es el dual del espacio vectorial §27§, y tiene
pues el mismo rango que este último. Para probar que \emph{b)} implica \emph{c)}, estableceremos
primero el lema siguiente:

\begin{lemma}[7.6.11.6]
Dado un complejo
§28§
de §29§-módulos planos, se tiene una sucesión exacta
§30§
\end{lemma}

\begin{proof}
\oldpage[III]{197}
En efecto, partiendo de la sucesión exacta
§31§, se obtiene la sucesión exacta
§32§.
De la sucesión exacta §33§ se obtiene, puesto que §34§
es plano,
§35§; por definición,
se tiene §36§; finalmente, se tiene §37§, y
§38§ se factoriza en
§39§;
se tiene §40§, donde §41§, y como §42§ es
sobreyectivo, §43§; finalmente,
§44§ por definición de §45§, lo que termina
de establecer la sucesión exacta (7.6.11.7).
\end{proof}

Para deducir entonces \emph{c)} de \emph{b)}, se considera una sucesión exacta
§46§,
donde §47§ y §48§ son módulos libres de tipo finito; consideremos el funtor
§49§ asociado al complejo formado por §50§ y §51§; como §52§ y §53§ son
libres, se identifican con sus biduales; luego si
§54§, §55§;
por otra parte, §56§ tiene el mismo rango
sobre §57§ que §58§. La hipótesis \emph{b)} implica por tanto
que
§59§
como §60§, la desigualdad (7.6.11.4) resulta pues de la sucesión exacta
(7.6.11.7).
Finalmente, para probar que \emph{c)} implica \emph{a)}, apliquemos (7.6.11.6) reemplazando
§61§ y §62§ por §63§ y §64§; la hipótesis \emph{c)} aplicada al módulo
§65§ da §66§, donde
§67§ y §68§.
Ahora bien, si se factoriza §69§ en
§70§,
se tiene
§71§.
Como
§72§
y
§73§,
se concluye efectivamente la desigualdad (7.6.11.2).

Dicho esto, supongamos que el anillo local §74§ es \emph{regular} de dimensión §75§;
se sabe entonces [17] que el §76§-módulo
§77§ es isomorfo a la potencia exterior
§78§;
se ve pues que la condición (7.6.11.4) no se verifica para §79§ en cuanto
§80§.
En cambio, si el anillo local íntegro §81§ es tal que todo §82§-módulo \emph{reflexivo}
de tipo finito es \emph{libre} (lo que ocurre cuando §83§ es un anillo regular
de dimensión 2), la condición (7.6.11.3) se verifica: en efecto, se sabe que el
dual §84§ de un §85§-módulo §86§ de tipo finito es reflexivo, luego libre, y
por tanto
§87§
(§88§ cuerpo de fracciones de §89§); por otra parte, se sabe que toda base sobre §90§
de §91§ está formada por imágenes de un sistema de generadores de §92§
(Bourbaki, \emph{Alg. comm.}, cap. II, \S 3, n\textsuperscript{o} 2, cor. 2 de
la prop. 4), luego
§93§, lo que
prueba nuestra afirmación.
\end{remark}

\subsection{Aplicación a los morfismos propios: I. La propiedad de intercambio.}
\label{subsection:III.7.7.fr}

Los tres números que siguen son, en lo esencial, traducciones, al
lenguaje de los morfismos de preesquemas, de los resultados de los números anteriores.

''',
('7','7.7.8'):r'''\begin{corollary}[7.7.8]
Bajo las hipótesis de \textup{(7.7.6)} relativas a §0§, §1§ y §2§, sean §3§,
§4§ dos §5§-Módulos coherentes que verifican las condiciones
siguientes: \textup{(i)} §6§ es §7§-plano; \textup{(ii)} §8§ es isomorfo al
conúcleo de un homomorfismo de §9§-Módulos localmente libres de tipo
finito §10§. Consideremos los dos funtores en el
§11§-Módulo cuasicoherente §12§:
§13§

Entonces existe un §14§-Módulo coherente §15§ (determinado salvo
isomorfismo único) e isomorfismos de funtores
§16§
§17§
\end{corollary}

\begin{proof}
En virtud del isomorfismo funtorial (§18§, 5.4.2.1), se tienen
isomorfismos funtoriales en §19§
§20§
para §21§. Pongamos
§22§ para
§23§; son §24§-Módulos coherentes (§25§, 5.3.5)
y §26§-planos (§27§, 5.4.2); sea
§28§. En virtud de
la exactitud por la izquierda del funtor
§29§, se tienen isomorfismos
funtoriales en §30§
§31§

Puesto que §32§ es exacto por la izquierda, se deduce un isomorfismo funtorial
§33§
y basta entonces aplicar (7.7.7).
\end{proof}

\oldpage[III]{203}

''',
('7','7.8.6'):r'''\begin{proposition}[7.8.6]
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo propio
y plano, §2§ un punto de §3§; designemos por §4§ la fibra
§5§. Supongamos que
§6§ es una §7§-álgebra separable
\textup{(Bourbaki, \emph{Alg.}, cap. VIII, § 7, n\textsuperscript{o} 5)}, en otros términos,
compuesta por un número finito de extensiones separables de grado finito de §8§.
Entonces §9§ es cohomológicamente plano sobre §10§ en el punto §11§ en
dimensión 0.
\end{proposition}

\begin{proof}
En virtud de (7.8.4), se puede limitar al caso en que §12§ es el espectro del anillo
local §13§; la hipótesis de que §14§ es plano implica
§15§, luego se ve ya que §16§ es exacto por la izquierda y todo
se reduce a ver que es exacto por la derecha; en virtud de (7.7.10 \emph{c)}), se está incluso
reducido al caso en que §17§ es \emph{artiniano}. Sea §18§ una extensión
finita de §19§ que sea un cuerpo de descomposición de §20§, de modo que
§21§ es producto directo de un número finito de cuerpos
isomorfos a §22§. Se sabe que existe un homomorfismo local de §23§ en un
anillo local §24§, que hace de §25§ una §26§-álgebra \emph{libre} finita sobre §27§,
y tal que el cuerpo residual de §28§ es isomorfo a §29§ (\textbf{0},
10.3.2). En virtud de (7.6.1), se está reducido a probar que §30§ es exacto
por la derecha, en otros términos, se puede suponer que §31§ es producto directo de §32§
cuerpos isomorfos a §33§. Observemos ahora el lema elemental
siguiente:

\begin{lemma}[7.8.6.1]
Sea §34§ un espacio anillado en anillos locales; para que §35§ sea conexo,
\oldpage[III]{207}
es necesario y suficiente que el anillo §36§ no sea un producto
de dos anillos no reducidos a 0.
\end{lemma}

\begin{proof}
Está claro en efecto que si §37§ es unión de dos abiertos no vacíos disjuntos,
§38§ es isomorfo al producto de los dos anillos
§39§ y §40§ no reducidos a 0.
Recíprocamente, decir que §41§ es tal producto equivale a
decir que hay en §42§ un idempotente §43§ distinto de 0 y
de 1; para todo §44§, §45§ es entonces un idempotente en §46§,
luego igual a 0 o 1. Pero está claro que el conjunto de los §47§ tales que §48§
es abierto; por otra parte, si §49§, se tiene por definición §50§, luego
el conjunto de los §51§ donde §52§ es también abierto (§53§, 5.5.2); de donde
la conclusión.
\end{proof}

Resulta de este lema que §54§ tiene exactamente §55§ componentes conexas §56§
y que §57§ para todo §58§. Como §59§ se ha
supuesto local y artiniano, su espectro se reduce a un punto, luego §60§ y §61§
tienen el mismo espacio subyacente; §62§ tiene pues §63§ componentes conexas §64§ tales
que §65§. Se está así finalmente reducido al caso en que
§66§; en virtud de (7.7.10, \emph{b)}), se está reducido a probar que
el homomorfismo canónico
§67§
es sobreyectivo; pero esto es trivial, pues el compuesto
§68§
ya es sobreyectivo.
\end{proof}

''',
('7','7.9.11'):r'''\begin{proposition}[7.9.11]
\label{III.7.9.11.fr}
Siendo las hipótesis las de \textup{(7.9.4)}, sea §0§ un
§1§-Módulo invertible muy amplio para §2§, y pongamos
§3§ para todo §4§. Entonces, para todo §5§,
la función
§6§
es un polinomio con coeficientes en §7§, que es el mismo para todos los
puntos de una misma componente conexa de §8§.
\end{proposition}

\begin{proof}
Está claro que §9§ es un complejo de
§10§-Módulos §11§-\emph{planos}. En virtud de (7.9.6.2), se puede limitar al caso
en que §12§ se reduce a un solo término §13§ de grado 0;
además, como se trata de cuestiones locales sobre §14§, se puede suponer §15§
afín y §16§ proyectivo (\textbf{II}, 5.5.3); pongamos §17§, y sea
§18§, que es un
§19§-Módulo muy amplio (\textbf{II}, 4.4.10); en virtud de (7.7.2), se tiene,
para el funtor §20§ relativo al complejo
§21§, §22§
(donde §23§);
de donde resulta que §24§ no es otra que la
característica de Euler-Poincaré §25§ definida en
(2.5.1); el hecho de que (7.9.11.1) sea un polinomio resulta entonces de (2.5.3);
además, para cada §26§, su valor es constante en una componente conexa de
§27§ (7.9.4), lo que termina la demostración.
\end{proof}

Designaremos por §28§ o
§29§ el polinomio (7.9.11.1), con coeficientes
racionales, y diremos que es el \emph{polinomio de Hilbert} en §30§
relativo a §31§, §32§ y §33§ (o simplemente el
\emph{polinomio de Hilbert en §34§ de §35§}, o \emph{de} §36§, si no
resulta confusión); cuando §37§ es conexo no vacío, se suprime la
mención de §38§ en la notación y la terminología. El invariante así obtenido
desempeñará un papel esencial en el cap. V, en la teoría de los «módulos» de los
haces coherentes cocientes de un haz coherente dado.

'''
}
apply_units(M)
# The end of 7.6.11 includes the next input's subsection title.
f=source('current','7').read_text();e,b=aggregate('current','7');fa,fb=next((a,z) for k,a,z in sections(f) if k=='7.6.11');ea,eb=next((a,z) for k,a,z in sections(e) if k=='7.6.11')
if any(ea<q[0]<eb for q in b):
 new=expand(M['7','7.6.11'],f[fa:fb]);head,tail=new.split(r'\subsection',1);mid=next(q[0] for q in b if ea<q[0]<eb);apply_edits('current','7',[(ea,mid-1,head,'7.6.11',e[ea:mid-1]),(mid,eb,r'\subsection'+tail,'7.6.11 subsection',e[mid:eb])],b)
 with (ROOT/'records/III_BRIDGE_TRANSLATIONS.jsonl').open('a') as o:o.write(json.dumps(dict(edition='current',part='7',place='7.6.11',before=e[ea:eb],after=new,kind='complete unit source translation across input boundary'),ensure_ascii=False)+'\n')

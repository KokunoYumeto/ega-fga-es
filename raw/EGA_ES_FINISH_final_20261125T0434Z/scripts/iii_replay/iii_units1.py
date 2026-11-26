import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import apply_units
D={('1','11.3.4'):r'''\begin{env}[11.3.4]
\label{0.11.3.4-fr}
Supongamos que el bicomplejo §0§ sea tal que §1§ para §2§ o §3§. Se sabe que se puede entonces definir para todo §4§ un «homomorfismo de borde» canónico
§5§
(M, XV, 6). Recordemos brevemente que esto se debe, por una parte, a que se tiene en la sucesión espectral §6§, §7§ para §8§, y por otra al hecho de que §9§, de modo que el isomorfismo §10§ da un homomorfismo §11§; la igualdad de todos los §12§ permite entonces definir homomorfismos canónicos §13§ para §14§, y en particular un homomorfismo §15§, de donde, por composición, el homomorfismo de borde §16§; además, se verifica inmediatamente que, a la clase mód. §17§ de un elemento §18§ tal que §19§, el homomorfismo de borde así definido hace corresponder en §20§ la clase de §21§ mód. §22§, y después a esta última la clase de cohomología de §23§ en §24§. Se ve, pues, finalmente que el \emph{homomorfismo de borde} (\hyperref[0.11.3.4.1-fr]{11.3.4.1}) \emph{proviene, por paso a la cohomología, de la inyección canónica} §25§ (donde §26§ se considera como complejo simple). Naturalmente, se interpreta del mismo modo el homomorfismo de borde
§27§
como proveniente de la inyección canónica §28§.
\end{env}

''',
('1','11.5.1'):r'''\begin{lemma}[11.5.1]
\label{0.11.5.1-fr}
Sea §0§ un complejo de §1§, y para todo entero §2§, sea §3§ el complejo tal que §4§ para §5§, §6§ para §7§. Sea §8§ un funtor covariante aditivo
\oldpage[0\textsubscript{III}]{36}
de §9§ en §10§, que conmuta con los límites inductivos (se supone que los límites inductivos filtrantes existen y son exactos en §11§ y §12§). Entonces §13§ es isomorfo al límite inductivo §14§ cuando §15§ tiende a §16§.
\end{lemma}

La construcción de una resolución inyectiva de Cartan-Eilenberg de §17§ se hace eligiendo \emph{arbitrariamente}, para cada §18§, una resolución inyectiva §19§ de §20§ y una resolución inyectiva §21§ de §22§; hecho esto, el método de construcción muestra que la resolución inyectiva §23§ de §24§ y los operadores de derivación §25§ \emph{solo dependen de las resoluciones} §26§, §27§ \emph{y} §28§ (M, XVII, 1.2). Ahora bien, está claro que se tiene §29§ y §30§ para §31§. Por otra parte, para cada §32§, se tiene una inyección canónica §33§, siendo §34§ la identidad para §35§. La observación precedente muestra que, si §36§ es una resolución inyectiva de Cartan-Eilenberg de §37§, se puede para cada §38§ definir una resolución inyectiva de Cartan-Eilenberg §39§ de §40§ tal que §41§ para §42§ y §43§ para §44§. Por otra parte, se puede definir un morfismo de bicomplejos §45§ correspondiente a §46§, y el método de definición de este morfismo (\emph{loc. cit.}) muestra además que puede construirse de modo que §47§ sea la identidad para §48§ y §49§. Se ha definido así un sistema inductivo §50§ de bicomplejos de §51§, del que §52§ es evidentemente el límite inductivo cuando §53§ tiende a §54§; por la permutabilidad de las sumas directas y de los límites inductivos, el complejo simple asociado a §55§ es también límite inductivo del complejo simple asociado a §56§. Como §57§ conmuta por hipótesis con los límites inductivos y lo mismo ocurre con la cohomología (por la exactitud del funtor §58§), se tiene en efecto §59§ salvo isomorfismo.

El lema (\hyperref[0.11.5.1-fr]{11.5.1}) permite extender a complejos §60§ cualesquiera, por paso al límite inductivo, propiedades válidas para los complejos \emph{acotados inferiormente}. Como primer ejemplo, demostraremos:

''',
('1','11.5.5'):r'''\begin{env}[11.5.5]
\label{0.11.5.5-fr}
El resultado de (\hyperref[0.11.5.2-fr]{11.5.2}) se generaliza a los multifuntores covariantes. Consideremos por ejemplo la situación de (\hyperref[0.11.4.6-fr]{11.4.6}), donde se supone que en §0§, §1§ y §2§
\oldpage[0\textsubscript{III}]{39}
los límites inductivos filtrantes existen y son exactos, y que §3§ conmuta con los límites inductivos. Entonces §4§ es un bifuntor \emph{cohomológico} en cada uno de los complejos §5§, §6§; para verlo, se reduce, como en (\hyperref[0.11.5.2-fr]{11.5.2}), al caso en que §7§ y §8§ están acotados inferiormente; tomando entonces para §9§ y §10§ resoluciones inyectivas del tipo descrito en (\hyperref[0.11.5.2.2-fr]{11.5.2.2}), se reduce a la propiedad general demostrada en (M, V, 4.1).
\end{env}

''',
('1','11.8.1'):r'''\begin{env}[11.8.1]
\label{0.11.8.1-fr}
Sean §0§ un conjunto finito, §1§ el conjunto de las sucesiones finitas §2§ de elementos de §3§ («símplices» de §4§); se pone §5§; se recuerda que el complejo de cadenas §6§ es el grupo abeliano libre graduado engendrado por los elementos de §7§, siendo §8§ de \emph{grado} §9§, con una diferencial definida por §10§. El subgrupo §11§ de §12§ engendrado por las cadenas §13§ para las que dos de los §14§ son iguales, y por las cadenas §15§, donde para toda permutación §16§, §17§ y §18§ es el signo de §19§, es un subcomplejo de §20§ cuyos elementos se llaman cadenas \emph{degeneradas}; se pone §21§, y se tiene un homomorfismo natural de complejos §22§. Por otra parte, se define un homomorfismo de complejos §23§ del modo siguiente: se ordena totalmente §24§; a la clase mód. §25§ de un símplex §26§, se hace corresponder §27§ si dos de los §28§ son iguales, y §29§ en caso contrario, donde §30§ es la sucesión de los §31§ ordenados \emph{en orden creciente}. Está claro que §32§ es la \emph{identidad} de §33§.
\end{env}

'''}
apply_units(D)

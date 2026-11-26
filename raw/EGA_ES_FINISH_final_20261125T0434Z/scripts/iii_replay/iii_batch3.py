import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import apply
D={
'current:1:11.5.3:0':r''' el bicomplejo tal que §0§ para §1§, §2§ para §3§; es inmediato que ''',
'current:1:11.5.4:0':r''' admita una resolución inyectiva \emph{de longitud} §0§. En efecto, en la demostración de (\hyperref[0.11.5.1-fr]{11.5.1}), todas las resoluciones inyectivas de objetos de ''',
'current:1:11.5.4:1':r''' que intervienen pueden tomarse de longitud §0§, de donde resulta inmediatamente que los términos de grado total ''',
'current:1:11.5.4:2':r''' y en número \emph{finito}, en cuanto §0§ es suficientemente grande, lo que implica que para todo §1§,
''',
'current:1:11.5.4:3':r''' son de longitud §0§.
\end{remark}

''',
'current:1:11.5.6:0':r'''\begin{env}[11.5.6]
\label{0.11.5.6-fr}
Del mismo modo, los resultados de (\hyperref[0.11.4.7-fr]{11.4.7}) y (\hyperref[0.11.5.3-fr]{11.5.3}) se generalizan como sigue. Supongamos (bajo las hipótesis de (\hyperref[0.11.5.5-fr]{11.5.5})) que se tienen dos bicomplejos §0§, §1§ tales que §2§ y §3§ para ''',
'current:1:11.5.6:1':r''', los funtores §0§ y §1§ sean exactos en ''',
'current:1:11.5.7:0':r''' conmuta con los límites inductivos, con tal de restringirse a los complejos §0§, §1§ acotados inferiormente, o de suponer que todo objeto de ''',
'current:1:11.6.1:0':r''' admite una resolución proyectiva de longitud §0§, se puede suponer que ''',
'current:1:11.6.2:0':r''', y §0§ para ''',
'current:1:11.6.2:1':r''' admita una resolución proyectiva de longitud §0§, entonces las \emph{dos} sucesiones espectrales de hiperhomología existen (sin hipótesis sobre ''',
'current:1:11.6.5:0':r''' es un bifuntor homológico en cada uno de los complejos acotados inferiormente §0§, §1§, formados respectivamente por objetos de ''',
'current:1:11.6.5:1':r''' dos bicomplejos tales que §0§ y §1§ para ''',
'current:1:11.6.5:2':r''', los funtores §0§ y §1§ sean exactos en ''',
'current:1:11.7.1:0':r''', con grados todos §0§, formado por objetos proyectivos, tal que para todo ''',
'current:1:11.7.1:1':r''', §0§, §1§, §2§, §3§ constituyen \emph{resoluciones proyectivas} de §4§, §5§, §6§, §7§ respectivamente en la categoría ''',
'current:1:11.7.1:2':r'''; en particular, para todo par ''',
'current:1:11.7.2:0':r''' están dados por las fórmulas
§0§
\end{proposition}

(Se recuerda que utilizamos la notación ''',
'current:1:11.7.2:1':r''' para todo complejo §0§; por ejemplo ''',
'current:1:11.7.2:2':r''' es una resolución \emph{proyectiva} del complejo simple ''',
'current:1:11.7.2:3':r''' en la categoría §0§; aplicando (\hyperref[0.11.6.3-fr]{11.6.3}), se ve que se tiene
''',
'current:1:11.8.2:0':r''', con la diferencial §0§ si §1§.

Los homomorfismos naturales
''',
'current:1:11.8.3:0':r''', pues se puede tomar ''',
'current:1:11.8.3:1':r''' cuando esta suma es §0§. Sea
''',
'current:1:11.8.3:2':r'''
en virtud de (\hyperref[0.11.8.3.1-fr]{11.8.3.1}) y de la hipótesis de inducción. Ahora bien, se tiene §0§ para §1§ (G, I, 3.7.4), por tanto también §2§ para §3§, en virtud de la fórmula de Künneth (G, I, 5.5.2). Aplicando esta observación al reemplazar ''',
'current:1:11.8.3:3':r''', se ve que existe un elemento §0§ de §1§ tal que ''',
'current:1:11.8.4:0':r''', y una familia de homomorfismos §0§, para §1§, que forman un \emph{sistema inductivo} para esta relación de preorden. Se define entonces un \emph{complejo de cocadenas} ''',
'current:1:11.8.4:1':r''' como el conjunto de las familias §0§, donde ''',
'current:1:11.8.4:2':r''', con §0§ para todo par §1§. La diferencial está dada del modo siguiente: si
''',
'current:1:11.8.4:3':r''' tiene dos términos iguales, y si se tiene §0§ y §1§ para permutaciones cualesquiera ''',
'current:1:11.8.5:0':r''' tienen el sentido definido en (\hyperref[0.11.8.2-fr]{11.8.2}), las aplicaciones §0§ y §1§ están definidas en ''',
'current:1:11.8.6:0':r''' si §0§ y §1§; se tienen entonces dos homomorfismos canónicos de complejos
''',
'current:1:11.8.6:1':r'''
Además, se tiene §0§ y §1§ y las homotopías §2§, §3§ \emph{pueden tomarse de modo que} §4§ \emph{y} §5§. Este punto proviene de que la definición de ''',
'current:1:11.8.6:2':r''', y de que los §0§ y §1§ son \emph{nulos} para ''',
'current:1:11.8.6:3':r''' como el conjunto de las familias §0§ donde ''',
'current:1:11.8.6:4':r''' recorre los pares cuyos términos tienen el mismo grado, con §0§, y como se tiene §1§ y §2§,
''',
'current:1:11.8.6:5':r'''. Dicho esto, las aplicaciones §0§, §1§, §2§ y §3§ están todas \emph{definidas} en virtud de las observaciones precedentes;
''',
'current:1:11.8.8:0':r''', y se tienen los diagramas conmutativos
''',
'current:1:11.8.8:1':r'''
\oldpage[0\textsubscript{III}]{46}
para §0§. Entonces se verifica inmediatamente que
''',
'current:1:11.8.9:0':r''' define un isomorfismo para la cohomología de estos dos bicomplejos.
\end{proposition}

\begin{proof}
Pongamos §0§ y §1§ para simplificar, y observemos que, puesto que ''',
'current:1:11.9.1:0':r''' tales que §0§ sea un epimorfismo.
\item[{\rm(ii)}] Para todo par de objetos §1§, §2§ y todo epimorfismo ''',
'current:1:11.9.1:1':r''' y las proyecciones canónicas §0§, §1§, que hacen conmutativo el diagrama
\oldpage[0\textsubscript{III}]{47}
''',
'current:1:11.9.1:2':r''' tales que §0§ sea un epimorfismo; se tomará §1§, §2§.

Dicho esto, para demostrar la proposición, procedamos por inducción. Supongamos, para un ''',
'current:1:11.9.1:3':r''', los morfismos §0§ y los morfismos §1§ de modo que ''',
'current:1:11.9.1:4':r''', que §0§ y §1§ para §2§; además, suponemos satisfechas las condiciones siguientes:
\begin{enumerate}
\item[''',
'current:1:11.9.1:5':r''', núcleo del epimorfismo ''',
'current:1:11.9.1:6':r''', pertenece a §0§ en virtud de la hipótesis ''',
'current:1:11.9.1:7':r'''. Se deduce además de (ii) que
''',
'current:1:11.9.1:8':r''', habida cuenta de la hipótesis §0§. En virtud de (i \emph{bis}), existe un ''',
'current:1:11.9.1:9':r''' igual a §0§, el diagrama
§1§
\oldpage[0\textsubscript{III}]{48}
es conmutativo, siendo la flecha horizontal inferior §2§. Tomemos entonces §3§, que pertenece a ''',
'current:1:11.9.1:10':r''' en virtud de (iii), y §0§, §1§. Como §2§, se tiene §3§ y, con las notaciones usuales,
''',
'current:1:11.9.1:11':r''' por paso a los cocientes, por tanto es un isomorfismo puesto que §0§ es un epimorfismo, de donde ''',
}
apply(D)

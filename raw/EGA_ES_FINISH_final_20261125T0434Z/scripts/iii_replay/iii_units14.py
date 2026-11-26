import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import *
apply_units({
('1','11.1.1'):r'''\begin{env}[11.1.1]
\label{0.11.1.1-fr}
Utilizaremos en lo que sigue una noción de sucesión espectral más general que
la definida en (T, 2.4); conservando las notaciones de (T, 2.4),
llamaremos \emph{sucesión espectral} en una categoría abeliana §0§ a un
sistema E formado por los elementos siguientes:
\begin{enumerate}
  \item[§1§] Una familia §2§ de objetos de §3§ definidos para
    §4§, §5§ y §6§.
  \item[§7§] Una familia de morfismos
    §8§ tales que
    §9§. Se pone
    §10§,
    §11§, de modo que
    §12§
  \item[§13§] Una familia de isomorfismos
    §14§.
\end{enumerate}

Se definen entonces para §15§, por inducción sobre §16§, los subobjetos
§17§ y §18§ como imágenes inversas, por el morfismo
canónico §19§, de los subobjetos de este
cociente identificados por §20§ con los subobjetos §21§ y
§22§ respectivamente. Está claro que se tiene entonces, salvo
isomorfismo,
§23§
y, si se pone además §24§ y §25§, se tienen
las relaciones de inclusión
§26§

Los otros elementos del dato de E son entonces:
\begin{enumerate}
  \item[§27§] Dos subobjetos §28§ y
    §29§ de §30§ tales que se tenga
    §31§ y, para todo §32§,
    §33§
    Se pone
    §34§
  \item[§35§]
    \oldpage[0\textsubscript{III}]{24}
    Una familia §36§ de objetos de §37§, cada uno provisto de una
    \emph{filtración decreciente} §38§. Se designa
    como de costumbre por §39§ el objeto graduado asociado al
    objeto filtrado §40§, suma directa de los
    §41§.
  \item[§42§] Para todo par §43§, un
    isomorfismo
    §44§.
\end{enumerate}

La familia §45§, sin las filtraciones, se llama el \emph{término límite}
de la sucesión espectral E.

Supongamos que la categoría §46§ admite sumas directas infinitas,
o que para todo §47§ y todo §48§ los pares §49§ tales
que §50§ y §51§ son en número finito (basta que sea así
para §52§). Entonces los
§53§
están definidos, y designando por §54§ el morfismo
§55§ cuya restricción a §56§ es §57§
para cada par §58§ tal que §59§, se tiene
§60§, en otros términos §61§
es un \emph{complejo §62§} en §63§, con operador de
derivación de grado §64§, y resulta de \emph{c)} que
§65§ es \emph{isomorfo a} §66§ para todo
§67§.
\end{env}

''',
('1','4.3.1'):r'''\begin{theorem}[4.3.1]
\label{III.4.3.1-fr}
\textnormal{(teorema de conexión).}
Sean §0§ un preesquema localmente noetheriano, §1§ un morfismo
propio. Entonces §2§ es una
§3§-Álgebra coherente.
\oldpage[III]{131}
Sea §4§ el §5§-esquema finito sobre §6§ tal que
§7§, que está determinado salvo §8§-isomorfismo
\textup{(\textbf{II}, 1.3.1 y 6.1.3)}; si §9§ es el §10§-morfismo
§11§ deducido del isomorfismo identidad
§12§ \textup{(\textbf{II}, 1.2.7)}, §13§ es propio,
§14§ es isomorfo a §15§, y las fibras
§16§ del morfismo §17§ son conexas y no vacías para todo
§18§.
\end{theorem}

\begin{proof}
Sea §19§ el morfismo estructural. Para probar que el homomorfismo
§20§ que interviene en la definición
del morfismo §21§ es biyectivo, basta, puesto que §22§ es afín sobre §23§,
probar que
§24§
es la identidad (\textbf{II}, 1.4.2); pero esto resulta de las definiciones puesto que
§25§ y
§26§. El hecho de que §27§ es
coherente es un caso particular del teorema de finitud
(\hyperref[III.3.2.1-fr]{3.2.1}). Como §28§ es propio y §29§ separado,
§30§ es propio (\textbf{II}, 5.4.3, (i)); para terminar la demostración de
(\hyperref[III.4.3.1-fr]{4.3.1}), basta pues probar el corolario
siguiente.
\end{proof}

''',
('1','4.3.9'):r'''\begin{definition}[4.3.9]
\label{III.4.3.9-fr}
Dado un preesquema localmente noetheriano §0§, se dice que un morfismo \textup{de
tipo finito} §1§ es universalmente abierto si, para todo
preesquema irreducible localmente noetheriano §2§ y todo morfismo dominante
§3§, toda componente irreducible de §4§ domina a §5§.
\end{definition}

Si §6§ es irreducible, esto equivale a decir que si §7§, §8§ son los
puntos genéricos de §9§ y §10§ respectivamente (de modo que
§11§), y si se pone §12§, toda componente irreducible
de §13§ corta a §14§ (\textbf{0}\textsubscript{I}, 2.1.8); esto
implica pues que para todo abierto §15§ de §16§ el morfismo
§17§, restricción de §18§, es universalmente abierto.

''',
('1','4.4.3'):r'''\begin{theorem}[4.4.3]
\label{III.4.4.3-fr}
\textnormal{(«Teorema principal» de Zariski).}
Sean §0§ un preesquema noetheriano, §1§ un morfismo cuasiproyectivo,
§2§ el conjunto de los puntos §3§ que están aislados en su fibra
§4§. Entonces §5§ es una parte abierta de §6§, y el
subpreesquema inducido §7§ es isomorfo a un preesquema inducido sobre una parte
abierta de un §8§-preesquema §9§ finito sobre §10§.
\end{theorem}

\begin{proof}
La hipótesis implica que existe un §11§-preesquema proyectivo §12§ tal que §13§
sea §14§-isomorfo a un subpreesquema inducido sobre un abierto de §15§
(\textbf{II}, 5.3.2 y 5.5.1). Se reduce pues a demostrar el teorema cuando §16§
es un morfismo proyectivo, luego propio (\textbf{II}, 5.5.3), y resulta entonces
inmediatamente de (\hyperref[III.4.4.1-fr]{4.4.1}).
\end{proof}

''',
('6','6.5.1'):r'''\begin{env}[6.5.1]
Consideremos ahora un preesquema §0§ cualquiera y dos §1§-preesquemas
cualesquiera §2§, §3§; sea §4§ (resp. §5§)
un complejo de §6§-Módulos (resp. §7§-Módulos)
cuasicoherentes. Pongamos §8§; vamos a definir
§9§-Módulos cuasicoherentes
§10§ llamados
\emph{hipertor locales} de §11§ y §12§, que se
reducirán a los ya definidos en (6.4) cuando §13§, §14§ y §15§ sean afines.

Cuando §16§ y §17§ se reducen
respectivamente a sus términos de grado 0, §18§ y §19§, (siendo
nulos los demás), se escribirá
§20§ en lugar de
§21§.
\end{env}

''',
})

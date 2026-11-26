import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import apply_units
apply_units({('1','11.9.2'):r'''\begin{corollary}[11.9.2]
\label{0.11.9.2-fr}
Sean §0§ un anillo noetheriano (no necesariamente conmutativo), §1§ un complejo de §2§-módulos por la derecha. Se supone que los §3§ son §4§-módulos de tipo finito y que existe §5§ tal que §6§ para §7§. Entonces existe un complejo §8§ formado por §9§-módulos por la derecha libres de rango finito, tal que §10§ para §11§, y un homomorfismo §12§ de complejos, tal que el homomorfismo §13§ correspondiente a §14§ sea biyectivo.
\end{corollary}

\begin{proof}
Se aplica (\hyperref[0.11.9.1-fr]{11.9.1}) tomando para §15§ la categoría de los §16§-módulos por la derecha, para §17§ (resp. §18§) el conjunto de los §19§-módulos de tipo finito (resp. el conjunto de los §20§-módulos libres de rango finito); la verificación de las condiciones (i), (ii) y (iii) de (\hyperref[0.11.9.1-fr]{11.9.1}) es inmediata, habida cuenta de la hipótesis de que §21§ es noetheriano.
\end{proof}

''',('1','12.3.1'):r'''\begin{env}[12.3.1]
\label{0.12.3.1-fr}
Consideremos un espacio anillado §0§; no volveremos sobre la definición y las principales propiedades de los bifuntores §1§ de la categoría de los §2§-módulos en la de los §3§-módulos, y §4§ de la categoría de los §5§-módulos en sí misma, ni sobre la sucesión espectral birregular §6§ que los relaciona (T, 4.2 y G, II, 7.3).
\end{env}

'''})

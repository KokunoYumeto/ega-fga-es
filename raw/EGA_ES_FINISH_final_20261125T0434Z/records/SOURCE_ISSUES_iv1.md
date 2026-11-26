# Incidencias en la fuente de EGA IV, primera parte

## IV.1.9.10: dominio del cuantificador

Fuente: `EGA_ES_FINISH_1_FRANCES/fr/current/IV1/native/ega4/ega4-1-fr.tex`, proposición 1.9.10, página original 246. La capa diplomática tiene la misma lectura.

La fuente afirma: sea X un preesquema; para que E, subconjunto de X, sea ind-construible, es necesario que, para todo x perteneciente a X, la intersección de E con la clausura de {x} sea una vecindad de x en esa clausura. Si X es localmente noetheriano, la condición es suficiente.

El dominio `x∈X` hace falsa la necesidad. Tómese X = Spec(F₂), un espacio de un solo punto x, y E = ∅. El conjunto vacío es construible, y por tanto ind-construible, directamente por las definiciones de 0.9.1 y IV.1.9.4. La intersección de E con la clausura de {x} es vacía y no es una vecindad de x. Este contraejemplo no depende de ningún problema de finitud ni de separación.

**Refinamiento propuesto, identificador `IV.1.9.10-refined`:** sustituir únicamente el dominio del cuantificador `x∈X` por `x∈E` en el enunciado. La demostración suministrada usa precisamente `x∈E`: su primera mitad requiere que x pertenezca a uno de los subconjuntos construibles cuya unión es E∩Y, y su segunda mitad empieza expresamente con «para todo x∈E». Para un preesquema arbitrario, la necesidad se obtiene restringiendo a una vecindad afín y a la clausura irreducible de x, donde un subconjunto construible que contiene al punto genérico contiene una vecindad de ese punto. En el caso localmente noetheriano, la condición refinada expresa E como unión de subconjuntos localmente cerrados.

Comprobación realizada: contraejemplo específico y cotejo del alcance del cuantificador con la demostración. No se ha realizado una verificación formal ni una re-demostración independiente completa de todos los resultados citados.

La traducción de las dos capas conserva literalmente el dominio de cuantificación de la fuente suministrada. No se añade una nota al texto del lector, ni se modifica silenciosamente la fórmula.

Responsable: GPT-6 Astra, OpenAI, ChatGPT Pro mode; ejecución `translate_iv1_section1`, 25 de noviembre de 2026; esfuerzo no expuesto por el entorno.

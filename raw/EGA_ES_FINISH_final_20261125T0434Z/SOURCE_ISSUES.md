# Incidencias matemáticas de la fuente conservadas en la traducción

Estas incidencias no se corrigen silenciosamente en el cuerpo de los lectores: la tarea exige la lectura de las fuentes francesas suministradas y la conservación de las notas heredadas. El cotejo general del corpus no constituye una verificación independiente de todas sus demostraciones.

## IV.1.9.10: dominio del cuantificador

Fuente: `EGA_ES_FINISH_1_FRANCES/fr/current/IV1/native/ega4/ega4-1-fr.tex`, proposición 1.9.10, página original 246. La capa diplomática tiene la misma lectura.

La fuente afirma: sea X un preesquema; para que E, subconjunto de X, sea ind-construible, es necesario que, para todo x perteneciente a X, la intersección de E con la clausura de {x} sea una vecindad de x en esa clausura. Si X es localmente noetheriano, la condición es suficiente.

El dominio `x∈X` hace falsa la necesidad. Tómese X = Spec(F₂), un espacio de un solo punto x, y E = ∅. El conjunto vacío es construible, y por tanto ind-construible, directamente por las definiciones de 0.9.1 y IV.1.9.4. La intersección de E con la clausura de {x} es vacía y no es una vecindad de x. Este contraejemplo no depende de ningún problema de finitud ni de separación.

**Refinamiento propuesto, identificador `IV.1.9.10-refined`:** sustituir únicamente el dominio del cuantificador `x∈X` por `x∈E` en el enunciado. La demostración suministrada usa precisamente `x∈E`: su primera mitad requiere que x pertenezca a uno de los subconjuntos construibles cuya unión es E∩Y, y su segunda mitad empieza expresamente con «para todo x∈E». Para un preesquema arbitrario, la necesidad se obtiene restringiendo a una vecindad afín y a la clausura irreducible de x, donde un subconjunto construible que contiene al punto genérico contiene una vecindad de ese punto. En el caso localmente noetheriano, la condición refinada expresa E como unión de subconjuntos localmente cerrados.

Comprobación realizada: contraejemplo específico y cotejo del alcance del cuantificador con la demostración. No se ha realizado una verificación formal ni una re-demostración independiente completa de todos los resultados citados.

La traducción de las dos capas conserva literalmente el dominio de cuantificación de la fuente suministrada. No se añade una nota al texto del lector, ni se modifica silenciosamente la fórmula.

Responsable: GPT-6 Astra, OpenAI, ChatGPT Pro mode; ejecución `translate_iv1_section1`, 25 de noviembre de 2026; esfuerzo no expuesto por el entorno.


## IV.16.8.8: signo en una frase de la demostración

Fuente: `EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-16-fr.tex`, demostración de 16.8.8, página original 43.

El desarrollo del producto impreso tiene coeficiente $(-1)^{n+1-|H|}$. La frase siguiente identifica su evaluación por $D'$ con el primer miembro de (16.8.8.2), cuyo coeficiente es $(-1)^{|H|}$. Puesto que los exponentes difieren en $n+1-2|H|$, la evaluación es en realidad $(-1)^{n+1}$ veces aquel primer miembro.

Contraejemplo a esa igualdad literal: $n=0$, $A=\mathbb Q$, $B=\mathbb Q[x]$, $M=N=B$, $D=d/dx$, $a_1=x$, $t=1$. Entonces $D'(x\otimes1-1\otimes x)=-1$, mientras que $D(x)-xD(1)=1$.

**Identificador del fragmento refutado:** `IV.16.8.8.proof.evaluation`. **Refinamiento:** `IV.16.8.8.proof.evaluation-refined`: la evaluación es $(-1)^{n+1}$ veces el primer miembro de (16.8.8.2). La condición de anulación y la equivalencia argumentada no cambian por ese factor invertible. No se afirma que la proposición 16.8.8 sea falsa ni que se haya verificado independientemente toda su demostración.

Se conserva la fórmula francesa, su frase y la nota editorial española preexistente que discute el signo. La incidencia queda documentada aquí y en CHECK_EVENTS.tsv. `scripts/verify_source_issues.py` reproduce los dos contraejemplos específicos mediante cálculos exactos; `records/SOURCE_ISSUES_CERTIFICATE.json` guarda el resultado.

Responsable de esta comprobación: GPT-6 Astra, OpenAI, ChatGPT Pro mode; esfuerzo no expuesto por el entorno; ejecución principal, 25 de noviembre de 2026.

## Nota editorial heredada de IV1, 0.23.2.8(ii)

La revisión de conservación de notas detectó una contradicción ya presente en
una nota editorial: describe como inexistente una referencia y, en la misma
frase, cita ese mismo número como el resultado usado. Además, su descripción
de la lectura diplomática no coincide con el testigo francés diplomático
suministrado. La nota se conservó sin modificación, como exige la tarea.
`records/INHERITED_NOTE_SOURCE_CONFLICTS.md` y su tabla acompañante identifican
las lecturas exactas, la igualdad antes/después y las fuentes pertinentes.
Se trata de una incidencia de la nota heredada, no de una nueva demostración
ni de una corrección silenciosa del texto de los autores.

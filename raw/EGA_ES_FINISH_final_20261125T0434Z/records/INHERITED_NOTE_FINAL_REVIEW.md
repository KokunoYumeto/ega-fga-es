# Revisión final de notas heredadas

## Resultado

Se cerraron los 20 avisos del cotejo de notas: **cero notas heredadas perdidas, cero alteraciones semánticas no autorizadas detectadas y cero pendientes de esta revisión**. No se modificó ningún archivo de la edición. El cotejo es textual y editorial; no comprueba demostraciones ni valida las afirmaciones matemáticas de las notas.

El script `audit_editorial_notes.py --all` encontró, en los archivos que tienen un antecedente español comparable, 264 notas originales y 268 actuales: 244 conservadas salvo espacios, 19 candidatas modificadas y una supuesta ausencia. Se leyeron íntegramente los 20 avisos contra el español original y el francés correspondiente. El recuento describe esas notas codificadas mediante footnote/footnotetext; no es un censo de todas las anotaciones de cualquier clase de la edición.

## Clasificación de las diferencias

| Clase | Casos | Resultado |
|---|---:|---|
| Notas autorales francesas | 14 | Traducción fiel a la fuente y conservación de atribuciones, condiciones y referencias. Las fórmulas de cada nota coinciden con el francés, salvo espacios. |
| Nota mixta autoral y editorial | 1 | La parte autoral de III1 CURRENT sigue el francés; la apóstilla del traductor se conserva literalmente con su marcado. |
| Notas editoriales españolas con normalización terminológica | 5 | Texto original íntegro y fórmulas idénticas; solo se aplican vecindad, suave o suavidad, conforme al estándar de toda la edición. |

Las cinco normalizaciones editoriales son: I.6.6.3 en CURRENT y DIPLOMATIC, «un entorno» → «una vecindad»; IV.17.13.4, «lisura» → «suavidad»; IV.17.13.5, «liso» → «suave»; IV.21.13.10, «al entorno» → «a la vecindad». Se registran como conservación íntegra con normalización terminológica, no como identidad byte a byte. Sus afirmaciones editoriales heredadas no se han convertido en nuevas conclusiones de esta revisión. La mención «de x» de la nota I.6.6.3 se cotejó con el francés diplomático; el francés corregido ya lee «de y».

La nota de Bourbaki en IV.11.1.2 es el **falso faltante**: está completa. La similitud textual baja se debe principalmente al restablecimiento de la notación francesa M, N, P, Q, R, A y B frente a las macros antiguas. Se cotejaron la nota completa, su secuencia de afirmaciones y todas sus fórmulas; no se verificó la demostración matemática.

En I.0.3.2.2 se distingue expresamente la antigua traducción de una nota autoral de una nota editorial española: la cláusula sobre los componentes añadida por la traducción anterior no está en el francés corregido. El texto actual traduce la condición que la fuente enuncia. En IV.8.1.3, «On notera» se traduce por «Se observará», y la relación entre espacios subyacentes y espacios analíticos sigue el francés. En IV.21.14.4 se conserva el plural autoral de «Notons aussi»: «Obsérvese también» pasa a «Observemos también», sin cambiar ninguna otra palabra ni fórmula de la nota. Los cambios de macros de nota y de marcas manuales de I.3.2.2 e IV.8.12.8 no suprimen contenido.

## Las cuatro notas adicionales del recuento

También se documentó el aumento de 264 a 268 notas en esos archivos comparables:

- III1 CURRENT y DIPLOMATIC: dos traducciones de la nota autoral inicial sobre la referencia al capítulo 0 publicado con I.
- I CURRENT, 5.3.9: una frase editorial heredada del cuerpo español se conserva literalmente como nota al restituir el cuerpo francés.
- IV1 CURRENT, 0.15.1.8: una nota editorial del francés corregido, antes ausente, se tradujo íntegramente.

## Evidencia

`INHERITED_NOTE_FINAL_REVIEW.tsv` contiene los 20 casos con before/after completos, clase de nota, fuente española de origen, testigo francés, motivo, control de fórmulas, riesgo y cierre. `INHERITED_NOTE_FINAL_EVIDENCE.json` conserva los pasajes franceses exactos y la ubicación de cada nota actual. `INHERITED_NOTE_ADDITIONS_REVIEW.tsv` documenta las cuatro adiciones o reubicaciones. `INHERITED_NOTE_FINAL_COUNTS.json` contiene los recuentos. El registro bruto del script no se alteró: su supuesto missing se resuelve en esta revisión documentada.

## Discordancia heredada documentada por separado

La lectura incidental de una nota conservada literalmente en IV1 CURRENT, 0.23.2.8(ii), detectó una contradicción interna y una discordancia con la referencia francesa diplomática. Se conserva intacta por la instrucción de preservación; los dos testigos y su riesgo se documentan en `INHERITED_NOTE_SOURCE_CONFLICTS.tsv` y su resumen Markdown. No es uno de los 20 cambios comparados ni una alteración introducida por esta ejecución.

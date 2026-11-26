# Cierre independiente de calidad

## Resultado

Se verificaron los **14 lectores finales** a partir de los 14 informes `BUILD_final_*.json`, los PDF actuales y los registros de revisión. Los 14 TeX, PDF y archivos `build.log` existen; los PDF se abren y sus **3373 páginas en total** coinciden con los recuentos de los informes. Esa suma incluye ambas capas y el acumulativo, por lo que no representa páginas de contenido único.

Los 14 códigos de salida son cero. Hay **dos cajas verticales overfull de 1,08224 pt**, una en IV3 y su repetición en el acumulativo; ninguna supera 2 pt. No se detectaron avisos de citas bibliográficas indefinidas ni de etiquetas o destinos duplicados. La extracción de texto de las 3373 páginas no contiene marcadores `??` ni citas que comiencen por `[?`.

No se reejecutaron traducciones ni compilaciones, y no se modificaron fuentes, PDF ni lectores. Se reconstruyó `BUILD_final_SUMMARY.tsv` con las 14 filas a partir de los JSON individuales; el último proceso con `--only` lo había reducido a una fila.

## Compilaciones y páginas

| Lector | Páginas PDF | Salida | Cajas overfull | Máximo pt | Avisos de referencias, incluido resumen |
|---|---:|---:|---:|---:|---:|
| EGA_COMPLETA_CURRENT | 1278 | 0 | 1 | 1.08224 | 0 |
| EGA_III1_CURRENT | 122 | 0 | 0 | 0 | 28 |
| EGA_III1_DIPLOMATIC | 121 | 0 | 0 | 0 | 28 |
| EGA_III2 | 68 | 0 | 0 | 0 | 0 |
| EGA_II_CURRENT | 158 | 0 | 0 | 0 | 10 |
| EGA_II_DIPLOMATIC | 158 | 0 | 0 | 0 | 6 |
| EGA_IV1_CURRENT | 188 | 0 | 0 | 0 | 0 |
| EGA_IV1_DIPLOMATIC | 188 | 0 | 0 | 0 | 0 |
| EGA_IV2_CURRENT | 164 | 0 | 0 | 0 | 0 |
| EGA_IV2_DIPLOMATIC | 164 | 0 | 0 | 0 | 0 |
| EGA_IV3 | 177 | 0 | 1 | 1.08224 | 2 |
| EGA_IV4 | 250 | 0 | 0 | 0 | 7 |
| EGA_I_CURRENT | 169 | 0 | 0 | 0 | 0 |
| EGA_I_DIPLOMATIC | 168 | 0 | 0 | 0 | 0 |

## Referencias y avisos conservados

El acumulativo CURRENT tiene **1278 páginas**, cero avisos de referencias indefinidas, cero avisos de citas indefinidas y cero avisos de etiquetas o destinos duplicados. Tampoco aparecen marcadores `??` o `[?` en su texto extraído.

En los lectores independientes permanecen **81 avisos de referencias**, correspondientes a **75 advertencias concretas y seis avisos de resumen**: III1 CURRENT y DIPLOMATIC, 28 cada uno; II CURRENT, 10; II DIPLOMATIC, 6; IV3, 2; IV4, 7. Son avisos de hiperreferencias externas cuyo texto numérico se conserva. Se distinguen de las citas bibliográficas: estas últimas no generan ningún aviso de cita indefinida. La ausencia de marcadores visibles no demuestra por sí sola que todos los enlaces interactivos funcionen; no se afirma una prueba exhaustiva de navegación.

Los 537 avisos de compilación se distribuyen en 440 de cadenas de marcadores PDF, 16 de recursos o expansión de fuentes de pdfTeX y los 81 de referencias ya descritos. Permanecen en los informes originales. Los recuentos exactos por clase están en `FINAL_INDEPENDENT_QA.json`. Código de salida cero no se presenta como ausencia de avisos.

## Correspondencia con la inspección visual

Se cotejaron las tres tablas de revisión visual con los PDF actuales y sus imágenes:

| Registro | Filas | Lectores | Páginas físicas distintas |
|---|---:|---:|---:|
| PDF_VISUAL_I_II_IV1.tsv | 42 | 6 | 40 |
| PDF_VISUAL_III_IV34.tsv | 35 | 5 | 35 |
| PDF_VISUAL_ROOT.tsv | 28 | 3 | 28 |

En total, **105 observaciones corresponden a 103 páginas físicas distintas de los 14 lectores**. Los SHA-256 de los PDF coinciden en todas las filas; todas las imágenes existen. Cuando el registro original proporciona hash de imagen, también coincide. La fila de IV3 página física 9 contiene dos rutas separadas por punto y coma; se comprobaron ambas por separado. Se calcularon hashes actuales para las imágenes de registros que no los incluían, sin atribuirles una comprobación histórica que el registro no hizo.

Este cierre vincula las observaciones ya realizadas mediante `view_image` a los archivos finales; no afirma una nueva inspección visual de todas las páginas. Las cajas verticales de 1,08224 pt tienen inspecciones ampliadas registradas: IV3 página física 9 y acumulativo página física 864.

## Créditos y derechos

Las **767 comprobaciones de créditos** están conformes, sin pendientes. Los 14 frentes actuales coinciden con los SHA-256 de `CREDITS_FINAL_REVIEW.tsv`, incluida la última recompilación de II DIPLOMATIC. Se conservan los párrafos y alcances heredados de README/ATTRIBUTION/FUENTES, los nombres humanos, versiones, enlaces y créditos de IA, junto con la declaración de derechos literal exigida por el usuario.

El registro de créditos documenta 188 comprobaciones de enlaces externos, correspondientes a diez URL distintas; 70 enlaces relativos que resuelven a archivos del paquete; y 93 apariciones de identidades SHA-256 de módulos. Se cotejó identidad con las fuentes suministradas, no disponibilidad de las páginas externas en Internet.

## Conservación de notas heredadas

Se volvió a contar cada nota original de los archivos comparables y se exigió una correspondencia exacta, ignorando espacios, o una pareja antes/después explícitamente cerrada en la revisión. Las **264 notas originales** quedan contabilizadas: **244 conservadas salvo espacios y 20 diferencias revisadas**. Las **268 notas actuales** incluyen cuatro adiciones o reubicaciones ya explicadas, y esas cuatro notas restantes corresponden exactamente a `INHERITED_NOTE_ADDITIONS_REVIEW.tsv`. **No queda ninguna nota original sin correspondencia.**

Se mantiene una discordancia heredada documentada por separado: la nota española de IV1 CURRENT, 0.23.2.8(ii), dice «inexistente 23.2.7» y a la vez «Proposición 23.2.7»; el francés CURRENT suministrado lee (23.2.7) y el DIPLOMATIC (23.1.13). La nota está intacta y el conflicto está en `INHERITED_NOTE_SOURCE_CONFLICTS.tsv/md`. No se introdujo ni se corrigió en esta ejecución. Preservar una nota editorial no equivale a confirmar su afirmación matemática o histórica.

## Evidencia y alcance

`FINAL_INDEPENDENT_QA.json` contiene hashes de los PDF, TeX, informes y logs, resultados por lector, correspondencias visuales, recuentos de créditos y contabilidad de notas. `FINAL_INDEPENDENT_PDF_EVIDENCE.json` conserva el control de marcadores visibles y los avisos de referencias. `BUILD_final_SUMMARY.tsv` vuelve a contener los 14 lectores.

No hay fallos abiertos en las comprobaciones de este cierre. Permanecen documentados los avisos de hiperreferencias externas y el conflicto de la nota heredada. Esta revisión no constituye una comprobación matemática, un censo de todas las anotaciones posibles ni una garantía de todos los enlaces interactivos.

## Saneamiento final de logs

Después de esta revisión se suprimieron las continuaciones partidas de rutas de instalación de fuentes tipográficas en los catorce logs. No contenían datos personales, pero se eliminaron para cumplir la regla de no copiar rutas locales. Los SHA-256 de log de `FINAL_INDEPENDENT_QA.json` se actualizaron. `FINAL_LOG_SANITIZATION.tsv` registra los hashes anterior y final. Se verificó que páginas, cajas y recuentos de avisos permanecen idénticos; PDF, TeX e informes de compilación no cambiaron.

El prefijo de salida temporal se sustituyó después por `readers/`, la ubicación portátil de los lectores en el ZIP. `FINAL_LOG_PATH_PORTABILITY.tsv` registra este paso, también sin cambios en páginas, cajas o recuentos de avisos. Los hashes finales de log reflejan ambos saneamientos.

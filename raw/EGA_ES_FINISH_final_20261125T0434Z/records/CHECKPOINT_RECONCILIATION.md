# Conciliación documental de checkpoints 01–04

**Se conservaron las 24 rutas documentales ausentes: 21 JSON históricos saneados y tres TSV históricos.** La unión de nombres de los cuatro checkpoints no presenta ninguna otra baja documental tras esta conciliación.

## Restauraciones

- `CAMBIOS_iii_manual.tsv` y `CAMBIOS_iii_math_aligned.tsv` son copias byte a byte de `III_CHANGES_manual.tsv` y `III_CHANGES_math_aligned.tsv`. El registro consolidado autoritativo sigue siendo `CAMBIOS_iii.tsv`.
- Los 21 JSON recuperan sus nombres anteriores. Sus extractos franceses `f`, `f_context` y contextos fuente adyacentes se sustituyen por SHA-256, longitud en caracteres/bytes y localizadores de archivo, unidad, líneas y posiciones cuando hay coincidencia literal. Se conservan español, identificadores, offsets y decisiones. Los términos franceses breves del glosario permanecen como testigos terminológicos.
- `CAMBIOS_standard_model.tsv` se conserva exactamente como en checkpoint01. Sus 2 330 propuestas corresponden íntegramente a las 2 184 filas de `CAMBIOS_standard_model_applied_01.tsv` y 146 de `_02.tsv`. Se verificó igualdad del multiconjunto sobre archivo, lugar, antes, después y fuente; solo cambia `standard_proposed` a `standard`.

## Estado y autoridad

Los JSON tienen una envoltura explícita `historical_snapshot_redacted`, con `authoritative: false`, la lista histórica en `records` y enlaces a `III_AUDIT.md`, `III_COMPLETE_COUNTS.json`, `III_COMPLETE_FIDELITY.tsv` y `CAMBIOS_iii.tsv`. Las incidencias antiguas no representan incidencias abiertas del texto final. Los scripts que esperaban una lista desnuda no deben consumir estos archivos como colas activas; el cambio de forma es intencional para señalar su estado histórico.

Los tres TSV históricos quedan expresamente excluidos por `HISTORICAL_CHANGE_RECORDS` en `merge_records.py`. No se ejecutó el merge. Las copias conservan los metadatos originales, incluidas descripciones provisionales; los registros finales y su normalización siguen siendo autoritativos.

## Alcance y comprobaciones

- Rutas documentales distintas en la unión: **676**.
- Registros JSON históricos conservados: **4441**.
- Cadenas fuente reemplazadas por metadatos: **10421**, con **700008** caracteres.
- Contextos históricos sin coincidencia literal actual: **0**; conservan la unidad y los localizadores históricos, sin fabricar una coincidencia.
- Ningún PDF, lector, fuente, corpus ni README raíz se modificó. No se restauraron archivos de `tree`, `readers` ni `qa` desde los checkpoints.

Las columnas del TSV identifican la procedencia, los hashes, el estado histórico, el sucesor autoritativo y la política de merge de cada ruta. La conservación de nombres no certifica que las antiguas propuestas o diagnósticos sean válidos para el estado final.

# Comprobación técnica final

Todos los controles siguientes terminaron conformes. Son controles editoriales, de registros y de compilación; no certifican las demostraciones matemáticas.

- Final table schemas and unique rows: PASS.
- Every supplied HAND and RESPELL identifier has exactly one disposition: PASS.
- Map closure: PASS.
- Received manifest verification: PASS.
- Final standard inventory: PASS.
- Final standalone reader builds, rights and single TOC: PASS.
- Visual observations bound to final PDF bytes: PASS.
- Credits and inherited note audit closure: PASS.
- Every previous checkpoint path retained in its current version: PASS.
- Package boundary: PASS.

Los detalles, recuentos y hashes están en `FINAL_PREFLIGHT.json`. La validación del ZIP se ejecuta después de crearlo: comprueba CRC, la lista de miembros y el tamaño y SHA-256 de cada miembro contra `OUTPUT_MANIFEST.tsv`. El resultado del ZIP no se inserta en el mismo archivo ya cerrado, para evitar alterar aquello que se acaba de verificar.

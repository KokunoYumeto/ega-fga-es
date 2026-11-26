# Auditoría focalizada de prosa: EGA I, capítulo I, y EGA IV-4

## Resultado

No se detectaron omisiones sustantivas en los candidatos del barrido. No se modificó ningún archivo de traducción.

El cotejo abarca 1.785 unidades del capítulo I de EGA I, capas current y diplomatic, y de EGA IV-4, capa current. Se examinaron 51.955 intervalos entre 50.170 fórmulas enlazadas. Se usaron las parejas de root_scope_pairs.py y mask_notes: este barrido se centra en el cuerpo de la prosa y excluye las notas, que tienen sus cotejos separados.

## Umbrales

- Barrido principal: francés con al menos 20 palabras y español con menos del 50%; umbral auxiliar de al menos 12 palabras francesas y como máximo 3 españolas.
- Lectura ampliada: francés con al menos 15 palabras y español con menos del 65%.
- Unidades completas: al menos 40 palabras francesas y español con menos del 70%.

El barrido principal produjo dos candidatos: I.5.1.8 en ambas capas. La lectura ampliada produjo cinco: I.10.11.8 en ambas capas, IV.18.8.8, IV.20.5.3 e IV.21.4.10. Ninguna unidad completa rebasó el umbral de brevedad.

Los siete candidatos se leyeron junto con las fórmulas y las frases contiguas. En I.5.1.8, la negación aparece después de la fórmula en español; en I.10.11.8, la descripción del sistema fundamental de vecindades sigue a los subgrupos. En IV.18.8.8, la suficiencia figura antes de la cita; en IV.20.5.3, la justificación mediante las definiciones precede a la condición; IV.21.4.10 conserva las condiciones y la igualdad por demostrar con una redacción más compacta.

## Evidencia y alcance

PROSE_I_IV4_REVIEW.tsv conserva las ubicaciones y los contextos franceses y españoles exactos observados, junto con cada disposición. Los informes ALL_UNITS, PAIR_SUMMARY y SOURCE_HASHES permiten reconstruir el alcance; PROSE_I_IV4_TRUE_OMISSIONS.json está vacío.

Este es un control dirigido de posibles omisiones de prosa, no una afirmación de equivalencia palabra por palabra ni una comprobación de las demostraciones matemáticas. El resultado negativo se refiere a los umbrales y a los candidatos leídos.

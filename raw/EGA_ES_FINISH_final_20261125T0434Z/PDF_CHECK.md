# Comprobación final de los PDF

Estado final: 25 de noviembre de 2026. Los catorce lectores compilaron con
pdfLaTeX en tres pasadas, con código de salida 0. Los registros de la fase
`final` corresponden a los PDF entregados. Las fases `baseline`, `interim` e
`interim_fixed` se conservan como historia y no certifican el estado final.

## Compilación y cajas

| Lector | Páginas físicas | Errores / salida | Avisos | Cajas desbordadas | Máximo (pt) |
|---|---|---|---|---|---|
| EGA_I_CURRENT | 169 | 0 | 11 | 0 | 0 |
| EGA_I_DIPLOMATIC | 168 | 0 | 11 | 0 | 0 |
| EGA_II_CURRENT | 158 | 0 | 55 | 0 | 0 |
| EGA_II_DIPLOMATIC | 158 | 0 | 51 | 0 | 0 |
| EGA_III1_CURRENT | 122 | 0 | 41 | 0 | 0 |
| EGA_III1_DIPLOMATIC | 121 | 0 | 41 | 0 | 0 |
| EGA_III2 | 68 | 0 | 11 | 0 | 0 |
| EGA_IV1_CURRENT | 188 | 0 | 4 | 0 | 0 |
| EGA_IV1_DIPLOMATIC | 188 | 0 | 4 | 0 | 0 |
| EGA_IV2_CURRENT | 164 | 0 | 68 | 0 | 0 |
| EGA_IV2_DIPLOMATIC | 164 | 0 | 68 | 0 | 0 |
| EGA_IV3 | 177 | 0 | 2 | 1 | 1,08224 |
| EGA_IV4 | 250 | 0 | 16 | 0 | 0 |
| EGA_COMPLETA_CURRENT | 1.278 | 0 | 154 | 1 | 1,08224 |

Doce lectores no tienen cajas desbordadas. EGA IV3 y el acumulativo tienen una
caja vertical de 1,08224 pt cada uno, por debajo del límite aproximado de 2 pt.
No quedan desbordamientos horizontales. El acumulativo contiene 1.278 páginas
físicas y una sola tabla de contenidos. La suma de páginas de los catorce PDF
es 3.373; incluye las capas alternativas y vuelve
a contar los volúmenes incluidos en el acumulativo.

Los lectores son archivos TeX autónomos: sus entradas de proyecto y preámbulos
están incorporados. Solo requieren los paquetes y fuentes ordinarios de TeX Live.
No necesitan los archivos franceses para compilar. Los espejos modulares de
`tree/repo/editions/` se distinguen de estos catorce lectores; no se atribuye a
cada wrapper histórico una compilación independiente que no se haya realizado.

## Avisos restantes

| Lector | Referencias externas y avisos resumen | Marcadores PDF | Recursos / fuentes pdfTeX |
|---|---|---|---|
| EGA_I_CURRENT | 0 | 11 | 0 |
| EGA_I_DIPLOMATIC | 0 | 11 | 0 |
| EGA_II_CURRENT | 10 | 44 | 1 |
| EGA_II_DIPLOMATIC | 6 | 44 | 1 |
| EGA_III1_CURRENT | 28 | 13 | 0 |
| EGA_III1_DIPLOMATIC | 28 | 13 | 0 |
| EGA_III2 | 0 | 10 | 1 |
| EGA_IV1_CURRENT | 0 | 2 | 2 |
| EGA_IV1_DIPLOMATIC | 0 | 2 | 2 |
| EGA_IV2_CURRENT | 0 | 66 | 2 |
| EGA_IV2_DIPLOMATIC | 0 | 66 | 2 |
| EGA_IV3 | 2 | 0 | 0 |
| EGA_IV4 | 7 | 6 | 3 |
| EGA_COMPLETA_CURRENT | 0 | 152 | 2 |

Hay cero avisos de citas bibliográficas indefinidas en los catorce lectores.
El acumulativo tiene cero referencias indefinidas y cero destinos duplicados.
En los lectores parciales, los avisos de referencias corresponden a otros
volúmenes que ese PDF no contiene; el número de la referencia sigue visible.
Los recuentos incluyen los mensajes resumen de LaTeX, por lo que no equivalen
al número de referencias distintas. La extracción de los catorce PDF no muestra
marcadores de cita o referencia `??` ni `[?]`.

Los avisos de marcadores PDF indican que `hyperref` elimina tokens matemáticos
de la cadena de texto de un marcador; no elimina la fórmula del cuerpo. La
categoría genérica de recursos pdfTeX corresponde aquí a avisos de expansión o
configuración de fuentes. No se han presentado como cero avisos. La lista
literal, saneada de rutas locales y direcciones de correo, está en cada
`readers/<lector>/build.log` y en `records/BUILD_final_<lector>.json`.

En EGA II diplomático se comprobó la numeración bibliográfica heredada de EGA I:
las referencias con detalle opcional conservan sus números impresos sin exigir
que ese volumen repita entradas bibliográficas que su fuente no vuelve a listar.
Los alias de referencias, los destinos de tablas y la desambiguación de claves
bibliográficas se aplicaron en la composición del lector, sin cambiar las
fórmulas ni las lecturas autorales.

## Páginas con más de 10 pt antes del ajuste

Se renderizaron y examinaron todas las páginas afectadas y sus vecinas:

| Lector de referencia | Página física con la fórmula afectada | Páginas examinadas | Desbordamiento inicial | Posición final examinada |
|---|---:|---|---:|---:|
| EGA IV1 actual | 90 | 89, 90, 91 | 17,24384 pt horizontal | 89 |
| EGA IV1 diplomático | 90 | 89, 90, 91 | 17,24384 pt horizontal | 89 |
| Acumulativo actual | 644 | 643, 644, 645 | 17,24384 pt horizontal | 600 |

La sucesión exacta 0.20.3.7.1 queda completa en dos líneas, con el número de
ecuación separado y sin invasión del margen en la composición final. Se amplió
la caja del lector a márgenes laterales de 18 mm y se ajustó la composición,
sin editar la fórmula francesa. La tabla de la introducción de I, que también
produjo un desbordamiento menor de 10 pt, se corrigió suprimiendo su sangría de
composición. Las capturas iniciales se conservan en `qa/overflow_baseline_contact.png`
y `qa/IV1_initial_contact.png`.

Las dos cajas verticales finales corresponden al mismo pasaje: IV3 página física
9 y acumulativo página física 864, folio 3 del cuerpo. Se examinó la página
completa, incluidos el diagrama inferior, la nota al pie y la paginación, sin
recorte ni colisión. La página física 871 del acumulativo también se examinó,
pero no es la posición del desbordamiento; los contadores internos de TeX no se
confunden aquí con la numeración física del PDF.

## Muestra visual final

Se inspeccionaron explícitamente 103 páginas
físicas distintas, con 105 observaciones, en los
catorce lectores. No se observaron defectos de recorte o solapamiento en esas
muestras. Los registros guardan el SHA-256 del PDF final, la imagen examinada,
la página física, el método y la observación. Se usaron hojas de contacto y
ampliaciones de fórmulas, títulos propios y zonas con desbordamiento.

| Lector | Páginas físicas examinadas |
|---|---|
| EGA_I_CURRENT | 1, 5, 34, 50, 84, 135, 169 |
| EGA_I_DIPLOMATIC | 1, 5, 34, 50, 84, 134, 168 |
| EGA_II_CURRENT | 1, 5, 32, 79, 126, 158 |
| EGA_II_DIPLOMATIC | 1, 5, 32, 79, 126, 158 |
| EGA_III1_CURRENT | 1, 5, 24, 61, 98, 122 |
| EGA_III1_DIPLOMATIC | 1, 5, 24, 60, 97, 121 |
| EGA_III2 | 1, 5, 13, 14, 34, 54, 68 |
| EGA_IV1_CURRENT | 1, 5, 38, 89, 94, 150, 188 |
| EGA_IV1_DIPLOMATIC | 1, 5, 38, 89, 94, 150, 188 |
| EGA_IV2_CURRENT | 1, 5, 33, 82, 131, 164 |
| EGA_IV2_DIPLOMATIC | 1, 5, 33, 82, 131, 164 |
| EGA_IV3 | 1, 3, 4, 5, 9, 10, 35, 88, 142, 177 |
| EGA_IV4 | 1, 5, 50, 125, 200, 250 |
| EGA_COMPLETA_CURRENT | 1, 8, 128, 256, 383, 480, 511, 600, 639, 767, 864, 871, 895, 1022, 1150, 1278 |

Las páginas físicas 50 de ambas capas de I muestran completos los títulos de
Krull 7.3.2 y Artin–Rees 7.3.2.1. III2 página 13 muestra correctamente el título
del Lema 6.4.2. En el acumulativo, la página física 511 está en blanco por mandato
explícito de la fuente francesa (página impresa III | 216); no es una omisión.

Evidencia: `records/PDF_VISUAL_FINAL.tsv`, `records/PDF_VISUAL_FINAL_COUNTS.json`,
las tres tablas `PDF_VISUAL_I_II_IV1.tsv`, `PDF_VISUAL_III_IV34.tsv` y
`PDF_VISUAL_ROOT.tsv`, sus informes y las imágenes de `qa/final/`.
`records/FINAL_INDEPENDENT_QA.md` registra la comprobación cruzada de los archivos.

## Alcance del control

Esta comprobación certifica los resultados de compilación, la medida de las
cajas y lo observado en las páginas indicadas. No afirma que se hayan leído
visualmente todas las páginas ni que se hayan verificado matemáticamente todas
las demostraciones. Las comprobaciones matemáticas puntuales se identifican
por separado en `CHECK_EVENTS.tsv` y `SOURCE_ISSUES.md`.

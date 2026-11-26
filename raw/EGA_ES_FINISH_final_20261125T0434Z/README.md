# EGA en español — entrega final

**25 de noviembre de 2026.** Se completaron las traducciones pendientes, el
cotejo y ensamblaje de IV2, las disposiciones heredadas, la aplicación del
estándar y los catorce lectores pedidos. El mapa final no registra secciones
solicitadas ausentes. Los lectores compilan sin errores y satisfacen el límite
aproximado de 2 pt de desbordamiento; la revisión visual está documentada.

## 1. Cobertura y trabajo realizado

Se verificaron bytes y SHA-256 de las 1.226 entradas de los
manifiestos recibidos. La extracción de los adjuntos se hizo una sola vez.
`records/MANIFEST_VERIFICATION.tsv` conserva esa comprobación.

- **EGA I, capítulo 0:** traducción desde 0.4.4.3 hasta 7.8.3 en las capas actual
  y diplomática, dentro del orden y las convenciones del árbol. El capítulo 0
  completo tiene por capa 78 archivos de unidades, 258 enunciados numerados,
  322 etiquetas, 5.805 expresiones matemáticas y 420 marcadores cotejados.
- **EGA IV1, capítulo IV §1:** traducción completa en ambas capas, con el frente
  de capítulo y once subsecciones, doce entradas por capa. Las diferencias de
  las fuentes actual y diplomática están registradas. Se revisó también el
  capítulo 0, §§14–23, ya existente.
- **EGA IV2, §§2–7:** auditoría de 684 entradas de capa, 342 por edición, en el
  orden francés. Hay 582 entornos numerados por capa y 18.865 expresiones
  matemáticas en la actual, 18.851 en la diplomática, sin desajustes pendientes
  en el cotejo. Se reconstruyeron 150 entradas diplomáticas de ensamblaje.
  La cifra heredada de 343 unidades no se usa como orden de compilación:
  `records/IV2_UNIT_AUDIT.tsv` y los manifiestos de orden documentan las 342
  entradas efectivas de cada capa.
- **Resto de EGA:** revisión de introducción, frentes, textos existentes,
  fórmulas, referencias, páginas, abreviaturas, términos y notas de I, II,
  III1, III2, IV1, IV3 e IV4. Los informes de cada ámbito separan cambios,
  restituciones, pasajes ya presentes y simples diferencias de maquetación.
- **Lectores:** I, II, III1, IV1 e IV2 en ambas capas; III2, IV3 e IV4; y un
  acumulativo actual con todos los volúmenes en orden y una tabla de contenidos.

El mapa contiene 91 archivos fuente por capa/parte,
10.415 anclas emparejadas y
14 piezas completas sin ancla:
10.429 filas, cero anclas sin correspondencia y cero filas
marcadas como ausentes. Cada fila enlaza el ámbito de cotejo correspondiente.
Encontrar una etiqueta no se considera por sí solo una prueba de traducción
íntegra ni una comprobación matemática. Véanse `MAPA.tsv`,
`records/MAPA_FINAL_COUNTS.json` y los informes enlazados desde el mapa.

Entre los controles de fórmulas figuran 31.392 expresiones de II, 25.835 de
III1/III2, y 21.117 expresiones principales más 67 finales de IV3. Son medidas
de ámbitos distintos y no se suman como unidades matemáticas únicas. IV3 tiene
696 anclas fuente y 251 marcas de página, todas localizadas. La auditoría
focalizada de prosa de I e IV4 examinó 1.785 unidades y 51.955 intervalos:
los siete candidatos de sus umbrales conservaban el contenido en la frase
adyacente; no se contabilizaron como nuevas omisiones ni traducciones.

`TRADUCCION.tsv` registra 231 unidades o fragmentos nuevos,
con 57.904 palabras según los recuentos de sus registros. Incluye ambas
capas cuando se tradujeron ambas; no es un recuento de pasajes únicos de EGA.
Las retraducciones superpuestas de texto ya existente se documentan como
cambios y trabajo de cotejo, sin inflar la cobertura nueva. Por ejemplo,
`III_TRANSLATION_WORK.tsv` contiene 1.110 operaciones y 38.909 palabras de
intervalos retraducidos que se solapan; sus verdaderos fragmentos nuevos son
35, con 405 palabras. La demostración actual de I.5.3.9 y la condición b′ de
IV.21.13.14 ya estaban traducidas: sus reubicaciones no se cuentan como nuevas.

## 2. Disposiciones de las pasadas anteriores

Se registran 4.311 identificadores únicos: 3.951 HAND
y 360 RESPELL. Todos tienen un veredicto y motivo:

| Veredicto | Entradas |
|---|---|
| already in | 3.870 |
| carried | 89 |
| does not apply to a translation | 352 |

«already in» significa que la corrección ya estaba incorporada; «does not apply
to a translation» conserva la razón específica por la que una corrección de la
fuente no exige alterar el español. Los cotejos respetan las diferencias entre
capas. Evidencia: `HECHO_REVISADO.tsv` y sus registros por ámbito.

## 3. Estándar, glosario y registro

Se aplicó la revisión `STANDARDS_20261119b` y sus decisiones, con prioridad
sobre el plan anterior. Para los silencios del estándar se usó el glosario de
115 términos del 19 de noviembre y sus decisiones de dudas. Las sustituciones
actúan en la prosa; las fórmulas conservan el TeX de la capa francesa pertinente,
con traducción de palabras en argumentos textuales y sin cambiar operadores.
La comprobación final no encontró formas residuales sustituibles de las reglas
aplicadas. Las decisiones contextuales y sus testigos están en los registros.

| Regla | Encontrados / revisados | Cambiados |
|---|---|---|
| es-foncteur | 67 | 67 |
| es-quasi | 1.700 | 1.700 |
| es-image-reciproque | 100 | 100 |
| es-limites | 29 | 29 |
| es-voisinage | 1.063 | 1.061 |
| es-stalk | 1.348 | 35 |
| es-filtrant | 172 | 36 |
| es-lisse | 1.087 | 1.087 |
| es-lissite | 32 | 32 |
| es-preesquema | 0 | 0 |
| es-iff | 0 | 0 |
| es-objet-final | 0 | 0 |
| es-construible | 121 | 121 |
| es-register-on-nous | 6.001 | 5.210 |
| es-source-abbreviations | 143 | 143 |
| es-schema-preschema-source | 314 | 133 |
| es-recouvrement | 34 | 34 |
| es-integral-closure | 6 | 6 |
| es-spectre-premier | 62 | 0 |
| es-dessin-enfant | 0 | 0 |
| es-settled-terms | 5.491 | 0 |
| es-corps-held | 2.725 | 0 |
| es-champ-held | 23 | 0 |
| es-anneau-valuation-low-confidence | 408 | 0 |

Los números «encontrados / revisados» respetan la unidad de cada regla: una
ocurrencia léxica, una cláusula editada o un evento de revisión contextual.
No todos son sitios únicos; algunas cláusulas se revisaron en varias pasadas.
`ESTANDAR_APLICADO.tsv`, `records/ESTANDAR_RULE_EVIDENCE.tsv` y
`records/ESTANDAR_APLICADO_FINAL_METHOD.md` explican cada recuento, los lugares
retenidos y su motivo. Se distinguen las 664 ocurrencias legítimas de «fibra»
y las 68 de «filtrado» de los términos que exigían «tallo» o «filtrante».

Las decisiones retenidas o de confianza baja no se impusieron: el inventario
final registra 2.725 ocurrencias de «cuerpo», 23 de «campo» y 408 de
«valoración/valuación», 3.156 en total, con sus lugares para una futura decisión
reversible. Para el registro, `on` recibe la forma impersonal y `nous` y los
imperativos autorales conservan la primera persona plural. Se mantienen
`resp.` y `cf.` donde los usa la fuente.

## 4. Notas, créditos y derechos

Se conservaron las 264 notas heredadas: 244 coinciden literalmente salvo
espacios y 20 diferencias se revisaron individualmente (14 notas autorales,
una mixta y cinco normalizaciones terminológicas editoriales). Hay 268 notas
en el inventario final, con cuatro adiciones o reubicaciones explicadas. No
quedan notas heredadas sin localizar ni cambios semánticos no autorizados
detectados. Los registros distinguen las notas de los autores de las editoriales.

Los créditos de los catorce lectores pasaron 767 controles,
con cero pendientes: 188 verificaciones de URL externas (10 URL distintas),
70 enlaces internos y 93 comprobaciones SHA-256 de módulos. Se conservan los
nombres, versiones, enlaces y alcance heredados de ryankeleti/ega y sus
contribuidores, de Tim Hosgood y de las ediciones de origen. La fidelidad de
los enlaces se cotejó con los créditos recibidos; no se comprobó su disponibilidad
actual en Internet.

La traducción se identifica como **AI-translated** y las correcciones como
**AI-produced corrections**. Se conservan los créditos anteriores de OpenAI
Codex, GPT-5.6 Sol y GPT-6.1 Sol, esfuerzo ultra, y del cotejo francés de Claude
Opus 5.5, esfuerzo max, noviembre de 2026. Esta ejecución se acredita a
**GPT-6 Astra, OpenAI, ChatGPT Pro mode**, sin inventar un nivel de esfuerzo que
el entorno no expone. La declaración de derechos española pedida figura en
el frente de cada lector. Evidencia: `records/CREDITS_FINAL_REVIEW.md`,
`records/CREDITS_FINAL_CHECKS.tsv` y `records/INHERITED_NOTE_FINAL_REVIEW.md`.

## 5. Compilación y examen visual

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

Todos los lectores se compilaron en tres pasadas. No quedan citas bibliográficas
sin resolver; el acumulativo tampoco tiene referencias sin resolver ni destinos
duplicados. Los avisos de los lectores parciales incluyen referencias a otros
volúmenes, avisos de fórmulas en marcadores PDF y avisos de fuentes; sus clases
y cantidades están detalladas en `PDF_CHECK.md`. No se afirma que haya cero avisos.

Se examinaron 103 páginas físicas distintas
de los PDF finales, con sus SHA-256, además de las páginas iniciales con
desbordamientos superiores a 10 pt y sus vecinas. La sucesión exacta que
sobresalía 17,24384 pt cabe completa tras ajustar la composición. Las únicas
cajas residuales son verticales, de 1,08224 pt, en IV3 y el acumulativo; sus
diagramas, notas y pies se examinaron sin recorte. No se observaron defectos
en las muestras. Las imágenes y todas las observaciones están en `qa/` y
`records/PDF_VISUAL_FINAL.tsv`. La revisión por muestras no equivale a mirar
todas las páginas.

## 6. Registros finales y alcance de las comprobaciones

| Registro final | Filas / entradas |
|---|---|
| CAMBIOS.tsv | 47.117 |
| TRADUCCION.tsv | 231 |
| HECHO_REVISADO.tsv | 4.311 |
| GLOSARIO_REGISTRO.tsv | 6.846 |
| ESTANDAR_APLICADO.tsv | 24 |
| CHECK_EVENTS.tsv | 12.432 |
| MAPA.tsv | 10.429 |

Distribución de `CAMBIOS.tsv`:

| Tipo de cambio | Filas |
|---|---|
| assembly | 309 |
| correction carried | 17 |
| own comparison | 35.133 |
| respelling | 16 |
| standard | 11.642 |

Distribución de `CHECK_EVENTS.tsv`:

| Tipo de evento | Filas |
|---|---|
| carried as background without fault found | 10.032 |
| computation or formal certificate | 1 |
| refuted, with refined statement IV.1.9.10-refined | 1 |
| refuted, with refined statement IV.16.8.8.proof.evaluation-refined | 1 |
| targeted proof check | 2 |
| used and rechecked in this run | 2.395 |

Los eventos de cotejo textual, notación, ensamblaje, compilación o inspección
visual no se presentan como demostraciones matemáticas. Las normalizaciones
de la taxonomía y metadatos preservan su estado anterior en
`records/MERGE_NORMALIZATION.tsv`. El único evento de cálculo o certificado
matemático de esta ejecución es el cálculo exacto de los dos contraejemplos
puntuales de `records/SOURCE_ISSUES_CERTIFICATE.json`.

`SOURCE_ISSUES.md` documenta dos dificultades conservadas en la lectura fuente:
el dominio del cuantificador de IV.1.9.10 y el factor de signo de una frase de
la demostración de IV.16.8.8. No se corrigieron silenciosamente en los lectores.
También se documenta la contradicción de una nota heredada de IV1, 0.23.2.8(ii),
sin modificarla, en `records/INHERITED_NOTE_SOURCE_CONFLICTS.md`.
El cotejo editorial no constituye una verificación independiente de toda EGA.

## 7. Organización de la entrega

- `tree/worktree/`: fuentes españolas mantenidas, con las unidades nuevas y
  las modificaciones de esta ejecución en sus convenciones de origen.
- `tree/repo/editions/`: ediciones y espejos sincronizados. La sincronización
  documenta 208 destinos únicos y 214 archivos comprobados contra manifiestos
  actuales. Los 159 archivos canónicos comprobados no se alteraron por la copia.
- `readers/`: catorce carpetas; cada una contiene un TeX autónomo, su PDF y
  `build.log`. El acumulativo está en `readers/EGA_COMPLETA_CURRENT/`.
- Tablas de raíz: mapa, cambios, traducciones, disposiciones, glosario,
  estándar y eventos; `README.md`, `PDF_CHECK.md` y `SOURCE_ISSUES.md`.
- `records/`: cotejos por ámbito, decisiones, fases históricas, hashes y
  conciliación entre registros de los puntos de control. Los estados antiguos
  «pending» o «proposed» se interpretan con su cierre posterior; no son colas
  activas. Las propuestas históricas duplicadas se excluyen del consolidado.
- `qa/`: imágenes de comprobación visual; `scripts/`: programas de trabajo.
- `OUTPUT_MANIFEST.tsv`: tamaño y SHA-256 de cada miembro entregado, salvo el
  propio manifiesto, para evitar una autorreferencia de hash imposible.

El README heredado dentro de `tree/repo/` conserva su descripción histórica,
incluidas las carencias que existían antes de este trabajo. El estado vigente
de esta entrega es el de este README y los informes finales. Los créditos y
derechos de aquel README permanecen íntegros.

Se conservan los entregables y la documentación de los puntos de control en sus
versiones vigentes. `records/CHECKPOINT_RECONCILIATION.md` explica la recuperación
de nombres históricos y la sustitución de extractos franceses de diagnóstico
por hashes y localizadores. No se incluyen archivos ZIP anteriores, adjuntos
originales, libros, escaneos ni extracciones completas de las fuentes francesas.
Los fragmentos de comparación y macros necesarios se limitan a la evidencia
editorial y al soporte de los entregables pedidos. La comprobación de privacidad
se registra en `records/FINAL_PRIVACY_SOURCE_AUDIT.md`.

## 8. Compilar y reproducir

Para compilar un lector entregado basta entrar en su carpeta y ejecutar
pdfLaTeX tres veces con una instalación estándar de TeX Live. Por ejemplo:

```bash
cd readers/EGA_I_CURRENT
pdflatex -interaction=nonstopmode -halt-on-error EGA_I_CURRENT.tex
pdflatex -interaction=nonstopmode -halt-on-error EGA_I_CURRENT.tex
pdflatex -interaction=nonstopmode -halt-on-error EGA_I_CURRENT.tex
```

Los scripts principales son:

| Script | Función |
|---|---|
| `scripts/corpus.py` y `scripts/finalize_map.py` | Índice fuente/español y cierre del mapa con evidencia |
| `scripts/assemble_readers.py` | Incorporar fuentes y preámbulos en los catorce lectores autónomos |
| `scripts/build_readers.py` | Compilar en tres pasadas y clasificar cajas y avisos |
| `scripts/render_final_pdf_samples.py` | Renderizar páginas e inventariar las muestras con hashes |
| `scripts/finalize_pdf_visual_records.py` | Consolidar observaciones visuales ya realizadas; no sustituye el examen humano o del modelo |
| `scripts/standardize.py` | Inventario y aplicación de reglas léxicas fuera de fórmulas |
| `scripts/merge_records.py` | Consolidar tablas sin duplicar registros históricos |
| `scripts/sync_edition_mirrors.py` | Sincronizar espejos y manifiestos, con `--final-readers` |
| `scripts/verify_source_issues.py` | Reproducir los dos contraejemplos puntuales con cálculo exacto |
| `scripts/finalize_reports.py` | Regenerar README y PDF_CHECK a partir de registros finales |
| `scripts/verify_final_delivery.py` | Verificar tablas, mapa, compilaciones, continuidad y, con `--zip`, CRC y manifiesto del paquete |
| `scripts/package_result.py` | Crear un ZIP nuevo y su manifiesto, sin sobrescribir entregas |

La compilación de los lectores no necesita los adjuntos. Para reejecutar el
cotejo o reconstruir desde las fuentes modulares, los programas esperan la
carpeta suministrada `source/EGA_ES_FINISH_1_FRANCES/` junto a la carpeta de
resultado, según `scripts/corpus.py`. Los originales se reutilizan desde los
adjuntos del usuario y no se redistribuyen. Los scripts de una sola aplicación
y sus diffs describen pasos históricos: no deben ejecutarse indiscriminadamente
sobre el resultado ya corregido.

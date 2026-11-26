"""Build the final Spanish delivery reports from the completed audit records."""
from pathlib import Path
import csv
import json
from collections import Counter

R = Path(__file__).resolve().parents[1]
REC = R / 'records'
ORDER = ['EGA_I_CURRENT','EGA_I_DIPLOMATIC','EGA_II_CURRENT','EGA_II_DIPLOMATIC',
         'EGA_III1_CURRENT','EGA_III1_DIPLOMATIC','EGA_III2',
         'EGA_IV1_CURRENT','EGA_IV1_DIPLOMATIC','EGA_IV2_CURRENT','EGA_IV2_DIPLOMATIC',
         'EGA_IV3','EGA_IV4','EGA_COMPLETA_CURRENT']


def rows(name):
    with (R / name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def js(name):
    return json.loads((R / name).read_text())


def n(value):
    return f'{int(value):,}'.replace(',', '.')


def table(headers, data):
    def escape(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(map(escape,headers)) + ' |',
                      '|' + '|'.join(['---']*len(headers)) + '|'] +
                     ['| ' + ' | '.join(map(escape,row)) + ' |' for row in data])


def main():
    builds = [js(f'records/BUILD_final_{name}.json') for name in ORDER]
    visual = js('records/PDF_VISUAL_FINAL_COUNTS.json')
    map_counts = js('records/MAPA_FINAL_COUNTS.json')
    manifest = rows('records/MANIFEST_VERIFICATION.tsv')
    assert all(r['sha256_match']=='True' and r['expected_bytes']==r['actual_bytes'] for r in manifest)
    counts = {name:len(rows(name+'.tsv')) for name in
              ['CAMBIOS','TRADUCCION','HECHO_REVISADO','GLOSARIO_REGISTRO','ESTANDAR_APLICADO','CHECK_EVENTS','MAPA']}
    translations = rows('TRADUCCION.tsv')
    words = sum(int(r['words']) for r in translations)
    hand = rows('HECHO_REVISADO.tsv')
    verdicts = Counter(r['verdict'] for r in hand)
    ids = {r['id'] for r in hand}
    assert len(ids) == 4311 == len(hand)
    id_counts = Counter('HAND' if i.startswith('hand:') else 'RESPELL' for i in ids)
    checks = Counter(r['type'] for r in rows('CHECK_EVENTS.tsv'))
    changes = Counter(r['kind'] for r in rows('CAMBIOS.tsv'))
    standards = rows('ESTANDAR_APLICADO.tsv')
    credits = js('records/CREDITS_FINAL_COUNTS.json')
    notes = js('records/INHERITED_NOTE_FINAL_COUNTS.json')
    mirrors = js('records/TREE_MIRROR_SYNC_COUNTS.json')
    build_rows = []
    warn_rows = []
    for b in builds:
        wc = b['warning_counts']
        build_rows.append([b['reader'], n(b['pages']), b['returncode'], len(b['warnings']),
                           len(b['overfull']), str(max((x[2] for x in b['overfull']),default=0)).replace('.',',')])
        warn_rows.append([b['reader'], wc.get('undefined reference or citation',0),
                          wc.get('PDF bookmark string',0),wc.get('pdfTeX destination or resource',0)])
        assert b['returncode']==0 and b['passes']==3
        assert max((x[2] for x in b['overfull']),default=0)<=2
    build_table = table(['Lector','Páginas físicas','Errores / salida','Avisos','Cajas desbordadas','Máximo (pt)'],build_rows)
    warn_table = table(['Lector','Referencias externas y avisos resumen','Marcadores PDF','Recursos / fuentes pdfTeX'],warn_rows)
    visual_table = table(['Lector','Páginas físicas examinadas'],
                         [[reader, ', '.join(map(str,visual['pages_by_reader'][reader]))] for reader in ORDER])
    pdf_report = f'''# Comprobación final de los PDF

Estado final: 25 de noviembre de 2026. Los catorce lectores compilaron con
pdfLaTeX en tres pasadas, con código de salida 0. Los registros de la fase
`final` corresponden a los PDF entregados. Las fases `baseline`, `interim` e
`interim_fixed` se conservan como historia y no certifican el estado final.

## Compilación y cajas

{build_table}

Doce lectores no tienen cajas desbordadas. EGA IV3 y el acumulativo tienen una
caja vertical de 1,08224 pt cada uno, por debajo del límite aproximado de 2 pt.
No quedan desbordamientos horizontales. El acumulativo contiene 1.278 páginas
físicas y una sola tabla de contenidos. La suma de páginas de los catorce PDF
es {n(sum(b['pages'] for b in builds))}; incluye las capas alternativas y vuelve
a contar los volúmenes incluidos en el acumulativo.

Los lectores son archivos TeX autónomos: sus entradas de proyecto y preámbulos
están incorporados. Solo requieren los paquetes y fuentes ordinarios de TeX Live.
No necesitan los archivos franceses para compilar. Los espejos modulares de
`tree/repo/editions/` se distinguen de estos catorce lectores; no se atribuye a
cada wrapper histórico una compilación independiente que no se haya realizado.

## Avisos restantes

{warn_table}

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

Se inspeccionaron explícitamente {n(visual['distinct_reader_pages'])} páginas
físicas distintas, con {n(visual['observation_rows'])} observaciones, en los
catorce lectores. No se observaron defectos de recorte o solapamiento en esas
muestras. Los registros guardan el SHA-256 del PDF final, la imagen examinada,
la página física, el método y la observación. Se usaron hojas de contacto y
ampliaciones de fórmulas, títulos propios y zonas con desbordamiento.

{visual_table}

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
'''
    (R / 'PDF_CHECK.md').write_text(pdf_report,encoding='utf-8')
    standard_table = table(['Regla','Encontrados / revisados','Cambiados'],
                           [[s['row'],n(s['found']),n(s['changed'])] for s in standards])
    record_table = table(['Registro final','Filas / entradas'],[[name+'.tsv',n(counts[name])] for name in counts])
    check_table = table(['Tipo de evento','Filas'],[[k,n(v)] for k,v in sorted(checks.items())])
    change_table = table(['Tipo de cambio','Filas'],[[k,n(v)] for k,v in sorted(changes.items())])
    readme = f'''# EGA en español — entrega final

**25 de noviembre de 2026.** Se completaron las traducciones pendientes, el
cotejo y ensamblaje de IV2, las disposiciones heredadas, la aplicación del
estándar y los catorce lectores pedidos. El mapa final no registra secciones
solicitadas ausentes. Los lectores compilan sin errores y satisfacen el límite
aproximado de 2 pt de desbordamiento; la revisión visual está documentada.

## 1. Cobertura y trabajo realizado

Se verificaron bytes y SHA-256 de las {n(len(manifest))} entradas de los
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

El mapa contiene {n(map_counts['source_files'])} archivos fuente por capa/parte,
{n(map_counts['source_anchors'])} anclas emparejadas y
{n(map_counts['unlabelled_whole_files'])} piezas completas sin ancla:
{n(map_counts['map_rows'])} filas, cero anclas sin correspondencia y cero filas
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

`TRADUCCION.tsv` registra {n(counts['TRADUCCION'])} unidades o fragmentos nuevos,
con {n(words)} palabras según los recuentos de sus registros. Incluye ambas
capas cuando se tradujeron ambas; no es un recuento de pasajes únicos de EGA.
Las retraducciones superpuestas de texto ya existente se documentan como
cambios y trabajo de cotejo, sin inflar la cobertura nueva. Por ejemplo,
`III_TRANSLATION_WORK.tsv` contiene 1.110 operaciones y 38.909 palabras de
intervalos retraducidos que se solapan; sus verdaderos fragmentos nuevos son
35, con 405 palabras. La demostración actual de I.5.3.9 y la condición b′ de
IV.21.13.14 ya estaban traducidas: sus reubicaciones no se cuentan como nuevas.

## 2. Disposiciones de las pasadas anteriores

Se registran {n(len(ids))} identificadores únicos: {n(id_counts['HAND'])} HAND
y {n(id_counts['RESPELL'])} RESPELL. Todos tienen un veredicto y motivo:

{table(['Veredicto','Entradas'],[[k,n(v)] for k,v in sorted(verdicts.items())])}

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

{standard_table}

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

Los créditos de los catorce lectores pasaron {n(credits['passed'])} controles,
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

{build_table}

Todos los lectores se compilaron en tres pasadas. No quedan citas bibliográficas
sin resolver; el acumulativo tampoco tiene referencias sin resolver ni destinos
duplicados. Los avisos de los lectores parciales incluyen referencias a otros
volúmenes, avisos de fórmulas en marcadores PDF y avisos de fuentes; sus clases
y cantidades están detalladas en `PDF_CHECK.md`. No se afirma que haya cero avisos.

Se examinaron {n(visual['distinct_reader_pages'])} páginas físicas distintas
de los PDF finales, con sus SHA-256, además de las páginas iniciales con
desbordamientos superiores a 10 pt y sus vecinas. La sucesión exacta que
sobresalía 17,24384 pt cabe completa tras ajustar la composición. Las únicas
cajas residuales son verticales, de 1,08224 pt, en IV3 y el acumulativo; sus
diagramas, notas y pies se examinaron sin recorte. No se observaron defectos
en las muestras. Las imágenes y todas las observaciones están en `qa/` y
`records/PDF_VISUAL_FINAL.tsv`. La revisión por muestras no equivale a mirar
todas las páginas.

## 6. Registros finales y alcance de las comprobaciones

{record_table}

Distribución de `CAMBIOS.tsv`:

{change_table}

Distribución de `CHECK_EVENTS.tsv`:

{check_table}

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
'''
    (R / 'README.md').write_text(readme,encoding='utf-8')
    summary = dict(record_counts=counts,translation_words=words,
        prior_entry_types=dict(id_counts),prior_verdicts=dict(verdicts),
        change_types=dict(changes),check_event_types=dict(checks),
        manifest_entries_verified=len(manifest),map=map_counts,
        final_readers=len(builds),reader_pages=sum(b['pages'] for b in builds),
        cumulative_pages=next(b['pages'] for b in builds if b['reader']=='EGA_COMPLETA_CURRENT'),
        final_build_errors=0,final_overfull_boxes=sum(len(b['overfull']) for b in builds),
        maximum_overflow_pt=max(x[2] for b in builds for x in b['overfull']),
        visual=visual,credits=credits,inherited_notes=notes,mirrors=mirrors)
    (REC / 'FINAL_DELIVERY_COUNTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('visual','credits','inherited_notes','mirrors')},ensure_ascii=False))


if __name__ == '__main__':
    main()

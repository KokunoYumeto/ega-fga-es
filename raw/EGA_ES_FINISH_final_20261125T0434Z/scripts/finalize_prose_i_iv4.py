"""Record the bilingual disposition of the targeted I/IV4 prose screen."""
import csv,json,collections
from corpus import RESULT,write_tsv
records=RESULT/'records'
primary=json.loads((records/'PROSE_I_IV4_CANDIDATES.json').read_text())
secondary=json.loads((records/'PROSE_I_IV4_SECONDARY_CANDIDATES.json').read_text())
assert [(r['scope'],r['edition'],r['place']) for r in primary]==[('I','current','5.1.8'),('I','diplomatic','5.1.8')]
assert [(r['scope'],r['edition'],r['place']) for r in secondary]==[('I','current','10.11.8'),('I','diplomatic','10.11.8'),('IV4','current','18.8.8'),('IV4','current','20.5.3'),('IV4','current','21.4.10')]
reasons={
 '5.1.8':'No omission. French places the non-necessity clause before the fiber-product formula; Spanish says «no es necesariamente reducido» immediately after that formula. The nilpotent-element explanation is also present.',
 '10.11.8':'No omission. Spanish names the subgroups first and then says they form a fundamental system of neighborhoods of zero; the full source condition and arbitrary-index qualification remain in the adjacent text.',
 '18.8.8':'No omission. The sufficiency of condition (iv) is placed before the citation in Spanish; necessity and faithful flatness follow the citation. All source assertions remain.',
 '20.5.3':'No omission. The justification from the definitions and reference IV.20.2.1 precede the density condition in Spanish. The local equivalence and every set occur in the surrounding sentence.',
 '21.4.10':'No substantive omission. The Spanish clause explicitly retains implications involving conditions 2° and 1°, the simplifying choice n=n_y, and the equality still to prove. The source explanatory phrasing is expressed more compactly.',
}
rows=[]
for tier,rs in [('primary',primary),('secondary',secondary)]:
 for r in rs:
  rows.append([tier,r['scope'],r['edition'],'EGA_ES_FINISH_1_FRANCES/'+r['source'],r['place'],r['source_line'],r['file'],r['target_line'],r['french_words'],r['spanish_words'],r['ratio'],'reviewed; no substantive omission',reasons[r['place']],r['french_context'],r['spanish_context']])
write_tsv(records/'PROSE_I_IV4_REVIEW.tsv',['screen','scope','edition','french_source','place','source_line','spanish_file','spanish_line','french_words','spanish_words','ratio','verdict','reason','french_context','spanish_context'],rows)
stats=list(csv.DictReader((records/'PROSE_I_IV4_SECONDARY_ALL_UNITS.tsv').open(),delimiter='\t'))
counts=collections.Counter(r['scope']+':'+r['edition'] for r in stats)
summary={'scope_units':dict(counts),'units':len(stats),'examined_intervals':sum(int(r['examined_intervals']) for r in stats),'matched_math_anchors':sum(int(r['matched_math']) for r in stats),'primary_candidates':len(primary),'secondary_candidates':len(secondary),'whole_unit_candidates':len(json.loads((records/'PROSE_I_IV4_SECONDARY_UNIT_CANDIDATES.json').read_text())),'true_substantive_omissions':0,'translation_files_changed':0,'primary_threshold':'French >=20 prose words and Spanish <50%; auxiliary French >=12 and Spanish <=3','secondary_threshold':'French >=15 prose words and Spanish <65%','whole_unit_threshold':'French >=40 prose words and Spanish <70%'}
(records/'PROSE_I_IV4_COMPLETE_COUNTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
(records/'PROSE_I_IV4_TRUE_OMISSIONS.json').write_text('[]\n')
(records/'PROSE_I_IV4_AUDIT.md').write_text('''# Auditoría focalizada de prosa: EGA I, capítulo I, y EGA IV-4

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
''')
print(json.dumps(summary,ensure_ascii=False))

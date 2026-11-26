"""Consolidate IV3 translation/source-fidelity evidence; never a proof check.

This script writes records only. It does not modify the Spanish edition.
"""
import collections
import csv
import json
import re
from corpus import RESULT, FR, canonical, write_tsv
from iv3_align import pairs, units
from iv3_core import spans
from iv3_work import DIR
from tex_tools import balanced_end, math_spans, prose_segments

REC = RESULT / 'records'
WHO = ('GPT-6 Astra; OpenAI; ChatGPT Pro; effort not separately exposed; '
       'IV3 source-fidelity run')
SOURCE = 'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'
TYPE = 'carried as background without fault found'

def read(name):
    with (REC/name).open() as f:
        return list(csv.DictReader(f, delimiter='\t'))

def norm(t):
    return re.sub(r'\s+', '', t)

def translated_formula(t):
    for a, b in [(r'\text{pour }', r'\text{para }'),
                 (r'\text{et}', r'\text{y}'),
                 (r'\hbox{et}', r'\hbox{y}')]:
        t = t.replace(a, b)
    return t

def literal_math(a, b):
    assert len(a) == len(b), ('mathematical span count', len(a), len(b))
    for x, y in zip(a, b):
        assert norm(translated_formula(x.text)) == norm(y.text), (x.text, y.text)

def notes(t):
    return [t[m.end():balanced_end(t, m.end()-1)-1]
            for m in re.finditer(r'\\footnote\{', t)]

coverage = []
summary = []
events = []
gloss = []
source_notes = []
envs = []
source_anchors = 0
source_pages = 0
numbered = 0
held_counts = collections.Counter()
TERM_PATS = [('corps', r'\bcorps\b', 'cuerpo'),
             ('champ', r'\bchamps?\b', 'campo'),
             ('anneau de valuation', r'\banneau[x]?\s+de\s+valuation\b',
              'anillo de valoración')]

for fp, q in pairs():
    ft, st = fp.read_text(), q.read_text()
    fu, su = units(ft), units(st)
    path = str(q.relative_to(RESULT))
    source_anchors += len(re.findall(r'\\(?:label|EGAReaderTarget)\{', ft))
    source_pages += len(re.findall(r'\\oldpage(?:\[[^]]*\])?\{', ft))
    for n, f in fu.items():
        if n == 'front' and 'terminal' in fp.name:
            continue
        s = su[n]
        fm, sm = spans(f.text), spans(s.text)
        literal_math(fm, sm)
        summary.append([fp.name, n, len(fm), len(sm),
                        'literal equality after source text-argument translation and TeX whitespace'])
        coverage.append([SOURCE+fp.name, n, 'current', path,
                         'translated_and_compared',
                         'Complete source-bound unit; literal core formula sequence compared; source clauses, register, references and markers reviewed. Source-fidelity only; no proof verification.'])
        if n != 'front':
            numbered += 1
            # Section 8 has its independently consolidated events.
            if not n.startswith('8.'):
                events.append(['CURRENT:IV3:'+n, '2026-11-25', WHO, TYPE,
                               'Translation/source-fidelity comparison only. Compared source clauses, literal core mathematical spans, numbering, page markers, register and references; editorial notes retained. No mathematical proof checked.'])
        if q.name == 'ega4-8.tex':
            continue
        pro = '\n'.join(x[2] for x in prose_segments(f.text))
        for term, pat, render in TERM_PATS:
            for j, m in enumerate(re.finditer(pat, pro, re.I), 1):
                held_counts[term] += 1
                witness = ('standard/DECISIONS_20261119b.tsv and '
                           'standard/DOUBT_DECISIONS_20261119.tsv: '
                           'held' if term != 'anneau de valuation' else
                           'standard/DOUBT_DECISIONS_20261119.tsv: low confidence')
                witness += ('; existing edition term retained. French witness: '+
                            SOURCE+fp.name+': '+n+': occurrence '+str(j)+': '+
                            re.sub(r'\s+', ' ', pro[max(0,m.start()-45):m.end()+75]))
                gloss.append([m[0], render, witness,
                              path+': '+n+': source occurrence '+str(j), 'yes'])
    if q.name in ['ega4-8.tex', 'ega4-11.tex']:
        fn, sn = notes(ft), notes(st)
        assert len(fn) == len(sn) == 2
        for i, (f, s) in enumerate(zip(fn, sn), 1):
            literal_math(spans(f), spans(s))
            source_notes.append(dict(
                source=SOURCE+fp.name, file=path, source_note=i,
                classification='original French footnote, translated and preserved',
                french=f, spanish=s, source_core_math=len(spans(f)),
                verdict='complete source note retained; translation comparison only, no proof verification',
                fuzzy_audit_resolution=('The Bourbaki proof note in 11.1.2 is preserved. '
                    'Voici is rendered He aquí; explicit 0_I 6.1.2 restored; '
                    'Algèbre commutative retains its publication title. '
                    'Formula/font and register corrections explain the fuzzy mismatch.'
                    if q.name=='ega4-11.tex' and i==2 else 'not a deletion')))

# The terminal introduction is prose outside the numbered-unit comparison.
fp = FR/'current/IV3/native/ega4/ega4-15-terminal-fr.tex'
q = DIR/'sections/ega4-15.tex'
assert '\\label{subsection:IV.15.7}' in q.read_text()
assert 'es independiente del resto del \\S~15' in q.read_text()
coverage.append([SOURCE+fp.name, '15.7: unnumbered introduction', 'current',
                 str(q.relative_to(RESULT)), 'translated_and_compared',
                 'Appendix heading and complete introductory sentence preserved, including II 7.3.10 and independence from the rest of section 15.'])
ft = fp.read_text()
ft = ft[ft.index('\\clearpage\n\\oldpage[IV-3]{249}'):]
q = DIR/'backmatter-es.tex'
st = q.read_text()
literal_math(math_spans(ft), math_spans(st))
coverage.append([SOURCE+fp.name, 'printed end matter, pp. 249–255', 'current',
                 str(q.relative_to(RESULT)), 'translated_and_compared',
                 'Bibliography, errata, printed contents and indexes compared; all 67 source mathematical spans literal; publication titles retained; quoted correction instructions translated; printed blank page 252 retained.'])

for q in sorted((DIR/'sections').glob('*.tex')):
    stack = []
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', q.read_text()):
        if m[1] == 'begin':
            stack.append(m[2])
        else:
            assert stack and stack.pop() == m[2], (q.name, m.group())
    assert not stack, (q.name, stack)
    envs.append([str(q.relative_to(RESULT)), 'balanced',
                 'All begin/end environments balanced; source statement/proof extents reviewed separately.'])

initial_map = REC/'IV3_INITIAL_FIDELITY_MAP.tsv'
if not initial_map.exists():
    initial_map.write_text((REC/'MAPA_iv3_fidelity.tsv').read_text())
write_tsv(REC/'MAPA_iv3_fidelity.tsv',
          ['french_file','place','edition','spanish_file','status','evidence'], coverage)
write_tsv(REC/'IV3_COMPLETE_FIDELITY.tsv',
          ['source','place','french_core_math','spanish_core_math','verdict'], summary)
write_tsv(REC/'CHECK_EVENTS_iv3_fidelity.tsv',
          ['statement_id','date','who','type','outcome'], events)
write_tsv(REC/'GLOSARIO_REGISTRO_iv3_fidelity.tsv',
          ['french_term','spanish_rendering','witness','places','reversible'], gloss)
write_tsv(REC/'IV3_ENVIRONMENT_BALANCE_FINAL.tsv', ['file','verdict','reason'], envs)
(REC/'IV3_SOURCE_NOTES_FINAL.json').write_text(json.dumps(source_notes, ensure_ascii=False, indent=2)+'\n')

# Bring the two earlier editorial events into the user's allowed taxonomy.
for name in ['CHECK_EVENTS_iv3_supplements.tsv', 'CHECK_EVENTS_standard_model.tsv']:
    rows = read(name)
    for r in rows:
        r['who'] = WHO if 'iv3' in name else WHO.replace('IV3 source-fidelity run','corpus terminology source-comparison run')
        r['type'] = TYPE
        r['outcome'] = ('Editorial source/translation comparison only; no mathematical proof verification. '
                        +r['outcome']) if not r['outcome'].startswith('Editorial source/translation') else r['outcome']
    write_tsv(REC/name, ['statement_id','date','who','type','outcome'],
              [[r[k] for k in ['statement_id','date','who','type','outcome']] for r in rows])

# The six originally detected extent differences plus the separately found 15.4.1.
extent = json.loads((REC/'IV3_ENV_EXTENT_REVIEW.json').read_text())
extent.append(dict(source='ega4-15-fr.tex', place='15.4.1', env='proposition'))
extrows=[]
for r in extent:
    fp=FR/'current/IV3/native/ega4'/r['source']
    q=DIR/'sections'/r['source'].replace('-fr','')
    f,s=units(fp.read_text())[r['place']], units(q.read_text())[r['place']]
    end='\\end{'+r['env']+'}'
    fc,sc=len(spans(f.text[:f.text.index(end)])),len(spans(s.text[:s.text.index(end)]))
    assert fc==sc,(r['place'],fc,sc)
    extrows.append([r['place'],r['env'],fc,sc,'resolved; source statement ends at the corresponding mathematical boundary'])
write_tsv(REC/'IV3_ENV_EXTENT_FINAL.tsv',
          ['place','environment','french_core_math_before_end','spanish_core_math_before_end','verdict'],extrows)
punct = json.loads((REC/'IV3_FINAL_PUNCTUATION_CANDIDATES.json').read_text())
write_tsv(REC/'IV3_PUNCTUATION_FINAL.tsv', ['source','place','formula_index','verdict'],
          [[r['source'],r['place'],r['index'],
            'Printed continuation notice restored as (Continuará.); source sentence stop retained.'
            if r['place']=='15.7.11.1' and r['index']==43 else
            'Sentence stop retained; Spanish complement/order or text wrapper accounts for the automatic candidate.']
           for r in punct])
assert r'\emph{(Continuará.)}' in (DIR/'sections/ega4-15.tex').read_text()

pages=json.loads((REC/'IV3_FINAL_PAGES_REVIEW.json').read_text())
anchors=json.loads((REC/'IV3_FINAL_ANCHORS_REVIEW.json').read_text())
assert all(r['status'] in ['same_formula_interval','present'] for r in pages)
assert all(not r['missing'] for r in anchors)
assert source_anchors==696 and source_pages==251
assert sum(r[2] for r in summary)==21117 and numbered==519
scheme=json.loads((REC/'IV3_SCHEME_REVIEW_FINAL.json').read_text())
reg9=json.loads((REC/'IV3_REGISTER_9_REBIND_REVIEW.json').read_text())
regall=json.loads((REC/'IV3_REGISTER_9_15_BROAD_VERDICTS.json').read_text())
counts=dict(
    numbered_units=numbered, core_comparison_units=len(summary),
    coverage_rows=len(coverage), core_mathematical_spans=21117,
    backmatter_mathematical_spans=len(math_spans(ft)),
    exact_core_mismatches=0, source_anchors=source_anchors, missing_source_anchors=0,
    source_pages=source_pages, missing_source_pages=0,
    page_boundary_verification={'section_8_exact_mathematical_boundaries':50,
        'sections_9_15_same_mathematical_intervals':194,'printed_backmatter_pages_present':7},
    original_source_footnotes=len(source_notes),
    math_text_arguments_reviewed=27,
    section_8_evidence='records/IV38_COMPLETE_COUNTS.json',
    root_review_register_9=dict(collections.Counter(r['status'] for r in reg9)),
    broad_register_9_15=dict(collections.Counter(r['status'] for r in regall)),
    final_observese_clauses=len(read('IV3_REGISTER_OBSERVESE_FINAL.tsv')),
    final_scheme_review=dict(collections.Counter(r['verdict'] for r in scheme)),
    final_geometric_fiber_candidates_retained=102,
    held_or_low_confidence_occurrences_9_15=dict(held_counts),
    source_proof_verification_claimed=False,
    pending_source_fidelity_blocks=0)
(REC/'IV3_COMPLETE_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')

(REC/'IV3_FIDELITY_CLOSURE.md').write_text('''# EGA IV, tercera parte: cierre del cotejo de fuente

Se cerró el cotejo editorial de §§8–15, con 519 unidades numeradas, ocho comienzos de sección, la introducción del apéndice 15.7 y los materiales finales impresos. La portada española existente se conserva; la fuente francesa del capítulo se encuentra al comienzo de §8.

Las 21.117 fórmulas principales coinciden literalmente con la fuente francesa corregida, una vez traducidos sus argumentos de texto y descontados los espacios de TeX. Los 67 segmentos matemáticos de los materiales finales coinciden también. La comparación principal distingue las fórmulas de las referencias de capítulo, los ordinales, las letras de condiciones y los añadidos editoriales; no afirma igualdad de todo el código TeX de las referencias. Los 27 argumentos text/textup/hbox se revisaron expresamente para impedir matemática duplicada dentro y fuera del argumento.

Están presentes las 696 anclas fuente por clave canónica y las 251 marcas de página. Las 50 páginas de §8 están en los mismos límites matemáticos; 194 páginas de §§9–15 están en los mismos intervalos matemáticos; las siete restantes pertenecen al material final, incluida la página en blanco 252. Se repararon ámbitos de siete enunciados y se verificó el balance de entornos de los ocho archivos de sección. Los prefijos de capítulo de las referencias dudosas se contrastaron con el francés.

Las cuatro notas originales se conservaron. La nota larga de Bourbaki en 11.1.2 es una nota original francesa, no una intervención editorial nueva. Su comienzo «Voici» se traduce «He aquí», conserva la demostración completa y su conclusión por Nakayama, restaura la referencia explícita a 0_I 6.1.2 y mantiene el título Algèbre commutative en su idioma de publicación. El aviso de similitud aproximada no indica una supresión. IV3_SOURCE_NOTES_FINAL.json conserva las parejas de texto francés y español que permiten comprobarlo. Las notas editoriales heredadas con lecturas impresas se conservaron y se distinguen de las notas originales.

El registro se cotejó con las cláusulas francesas: on se traduce impersonalmente; nous y los imperativos de los autores mantienen la primera persona plural. Tras las sustituciones se revisaron los clíticos, el tiempo verbal y la concordancia. Las 102 apariciones finales de fibra corresponden a fibras geométricas y se conservaron. La revisión de schéma/préschéma corrigió seis tipos nominales y ocho cláusulas; además restituyó «un preesquema» en el título 8.7 del índice impreso. Las decisiones held sobre corps y champ y la decisión de baja confianza sobre anneau de valuation permanecen registradas con los términos heredados. Los títulos de publicaciones conservan su idioma; las instrucciones y citas de erratas se tradujeron. Se restituyó el cierre impreso «(Continuará.)».

Este trabajo es un cotejo de traducción y de fidelidad a la fuente; no constituye una verificación de las demostraciones matemáticas. CHECK_EVENTS emplea la categoría autorizada carried as background without fault found y declara ese alcance.

Para consolidar: MAPA_iv3_fidelity.tsv, CAMBIOS_iv3_fidelity.tsv, CAMBIOS_iv3_initial_notation.tsv, TRADUCCION_iv3_supplements.tsv, GLOSARIO_REGISTRO_iv3_fidelity.tsv, CHECK_EVENTS_iv3_fidelity.tsv y CHECK_EVENTS_iv3_supplements.tsv. Los registros *_iv3_8.tsv del revisor de §8 son independientes y se conservan. IV3_FIDELITY_PATCH_LOG.json y los informes IV38_CHANGES_* son evidencia histórica; no deben contarse otra vez como cambios adicionales. Los trece pasajes completos de TRADUCCION_iv3_supplements.tsv son retraducciones completas de pasajes heredados abreviados o divergentes; sus cifras no representan únicamente palabras antes ausentes. La fila adicional de una palabra corresponde al aviso de continuación restituido.
''')
print(json.dumps(counts,ensure_ascii=False))

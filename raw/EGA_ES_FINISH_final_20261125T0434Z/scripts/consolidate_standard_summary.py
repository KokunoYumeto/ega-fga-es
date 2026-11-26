"""Summarize actual Spanish-standard passes without replaying or editing corpus.

Dry runs and unapplied proposal summaries are deliberately not inputs to counts.
Repeated real editorial passes are identified as review events, not unique sites.
"""
import collections
import csv
import json
import re
from pathlib import Path
from corpus import RESULT, write_tsv
from standardize import canonical_files, RULES, MODELS, HELD
from tex_tools import prose_segments

REC=RESULT/'records'
HEADER=['row','found','changed','places_left','reason']
RULE_ALIAS={'es-images-reciproques':'es-image-reciproque',
            'es-limite-directe':'es-limites','es-limite-inverse':'es-limites'}
counts=collections.defaultdict(lambda:dict(found=0,changed=0,parts=[]))
evidence=[]

def read(name):
    with (REC/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))

def load(name):return json.loads((REC/name).read_text())

def add(rule,found,changed,file,unit,detail=''):
    rule=RULE_ALIAS.get(rule,rule)
    assert isinstance(found,int) and isinstance(changed,int)
    assert found>=changed>=0,(rule,found,changed)
    counts[rule]['found']+=found
    counts[rule]['changed']+=changed
    part=dict(file='records/'+file,found=found,changed=changed,unit=unit,detail=detail)
    counts[rule]['parts'].append(part)
    evidence.append([rule,found,changed,unit,'records/'+file,detail])

# These three files are application journals, not their similarly named dry runs.
script_files=['CAMBIOS_standard_script.tsv',
              'CAMBIOS_standard_script_iv2_applied.tsv',
              'CAMBIOS_standard_script_final_applied.tsv']
for name in script_files:
    byrule=collections.Counter()
    for r in read(name):
        assert r['kind']=='standard'
        m=re.search(r'\b(es-[a-z-]+)\b',r['source']);assert m,r
        byrule[m[1]]+=1
    for rid,n in byrule.items():add(rid,n,n,name,'term occurrences applied')
    for rid,_,_ in RULES:counts[RULE_ALIAS.get(rid,rid)]

# Bind model occurrence decisions to completed patch IDs. Agreement edits count
# as atomic patches in evidence, never as additional changed term occurrences.
proposals=load('STANDARD_MODEL_PATCHES.json')
applied_ids=load('STANDARD_MODEL_APPLIED_IDS.json')
patches=proposals['patches']
assert set(applied_ids)==set(range(len(patches)))
assert len(applied_ids)==len(set(applied_ids))==2330
bound_ids=[]
for name in ['STANDARD_MODEL_BINDINGS_01.tsv','STANDARD_MODEL_BINDINGS_02.tsv']:
    bound_ids += [int(r['patch_id']) for r in read(name)]
assert set(bound_ids)==set(applied_ids) and len(bound_ids)==2330
applied_reviews={i for p in patches for i in p['review_ids']}
model=read('STANDARD_MODEL_VERDICTS.tsv')
assert len(model)==1401
for rid in ['es-voisinage','es-stalk','es-filtrant']:
    rs=[r for r in model if r['row']==rid]
    changed=[r for r in rs if r['verdict']=='change']
    assert all(int(r['review_id']) in applied_reviews for r in changed)
    assert all(r['verdict'] in ['change','retain'] for r in rs)
    atomic=sum(rid in p['standard_rows'] for p in patches)
    add(rid,len(rs),len(changed),'STANDARD_MODEL_VERDICTS.tsv',
        'source-reviewed term occurrences',
        str(atomic)+' atomic patches actually applied, including grammatical agreement; '
        'STANDARD_MODEL_BINDINGS_01/02 and STANDARD_MODEL_APPLIED_IDS prove completion')

# Independently owned IV2 pass and the remaining source-bound I.0 edits.
iv2=read('MODEL_TERMS_iv2.tsv')
for rid,pat in [('es-voisinage',r'^(?:entorno[s]?|vecindad(?:es)?)$'),
                ('es-stalk',r'^fibra[s]?$')]:
    rs=[r for r in iv2 if re.match(pat,r['before_term'],re.I)]
    changed=sum(r['before_term']!=r['after_term'] for r in rs)
    add(rid,len(rs),changed,'MODEL_TERMS_iv2.tsv','source-reviewed term occurrences',
        'includes already-conforming terms explicitly reviewed; no duplicate count from ESTANDAR_APLICADO_iv2')
rs=read('CAMBIOS_root_ch0_vecindad.tsv')
n=sum(len(re.findall(r'\bentornos?\b',r['before'],re.I)) for r in rs)
add('es-voisinage',n,n,'CAMBIOS_root_ch0_vecindad.tsv','term occurrences applied',
    '26 actual journal entries, independently recounted; not the earlier conversational estimate of 28')

# A second real review after source restoration. It is intentionally called a
# review-event count because some retained source locations were read twice.
final_reviews=[]
for name in ['FINAL_STANDARD_MODEL_ROOT.tsv','FINAL_STANDARD_MODEL_OTHER.tsv',
             'FINAL_STANDARD_MODEL_IV3.tsv','FINAL_STANDARD_MODEL_III.tsv']:
    rs=read(name);final_reviews.extend(rs)
    for rid in ['es-voisinage','es-stalk','es-filtrant']:
        rr=[r for r in rs if r['row']==rid]
        if not rr:continue
        changed=sum(r.get('verdict',r.get('decision')) in ['change','changed'] for r in rr)
        assert all(r.get('verdict',r.get('decision')) in ['retain','change','changed'] for r in rr)
        add(rid,len(rr),changed,name,'final source-review events',
            'real contextual rereview, not another dry-run count')
assert len(final_reviews)==736
assert len(read('CAMBIOS_standard_final_other.tsv'))==2
assert len(read('CAMBIOS_standard_final_iv3.tsv'))==0

# New standard/ledger form: use the applied component from §8 once and the final
# applied global journal once; do not add the §8 dry-run list or consolidated copy.
for name in ['IV38_CHANGES_terminology.tsv','CAMBIOS_constructible_final.tsv']:
    rs=read(name)
    assert all('constructib' in r['before'].lower() and 'construib' in r['after'].lower() for r in rs)
    add('es-construible',len(rs),len(rs),name,'term occurrences applied')

# Register has varying patch granularity. The figures below count documented
# edit/review events, not words or distinct locations; complete retranslations
# are not converted into invented substitution counts.
for name in sorted(p.name for p in REC.glob('CAMBIOS_register*.tsv')):
    rs=read(name)
    add('es-register-on-nous',len(rs),len(rs),name,'applied editorial patch rows')
for name in ['CAMBIOS_root_author_voice.tsv','CAMBIOS_root_notes_register_finish.tsv',
             'II_CHANGES_register.tsv','II_CHANGES_register2.tsv',
             'CAMBIOS_iv3_register_final_observese.tsv','CAMBIOS_root_imperative_finish.tsv']:
    rs=[r for r in read(name) if r['kind']=='standard' or name=='CAMBIOS_root_author_voice.tsv']
    add('es-register-on-nous',len(rs),len(rs),name,'applied editorial patch rows',
        'Includes four paired restorations of an author connective and its dependent relative clause (eight rows).'
        if name=='CAMBIOS_root_author_voice.tsv' else '')
for r in read('ESTANDAR_APLICADO_iv2.tsv'):
    if r['row'].startswith('es-register-'):
        add('es-register-on-nous',int(r['found']),int(r['changed']),
            'ESTANDAR_APLICADO_iv2.tsv','source-reviewed clause/edit events',r['row'])
rs=read('IV38_REGISTER_REVIEW.tsv')
add('es-register-on-nous',len(rs),sum(r['verdict']=='applied' for r in rs),
    'IV38_REGISTER_REVIEW.tsv','source-reviewed occurrence events',
    'The 118 applied component rows are already in CAMBIOS_iv3_8; do not add them again')
for name in ['IV3_REGISTER_9_REBIND_REVIEW.json','IV3_REGISTER_9_15_BROAD_VERDICTS.json']:
    rs=load(name)
    add('es-register-on-nous',len(rs),sum(r['status']=='applied' for r in rs),
        name,'source-reviewed occurrence events',
        'already-revised/retained forms are not changes in this pass')
rs=load('III_REGISTER_DECISIONS.json')
add('es-register-on-nous',len(rs),sum(r['changed'] for r in rs),
    'III_REGISTER_DECISIONS.json','source-reviewed clause events')
segments=[json.loads(s) for s in (REC/'III_SEGMENT_DECISIONS.jsonl').read_text().splitlines() if s]
for reason in sorted(set(r['reason'] for r in segments)):
    rs=[r for r in segments if r['reason']==reason]
    if reason.startswith('register-'):
        add('es-register-on-nous',len(rs),sum(r['changed'] for r in rs),
            'III_SEGMENT_DECISIONS.jsonl','source-reviewed clause/edit events',reason)
    elif reason.startswith('final concrete root QA'):
        rr=[r for r in rs if 'íntegramente' not in r['before']]
        add('es-register-on-nous',len(rr),sum(r['changed'] for r in rr),
            'III_SEGMENT_DECISIONS.jsonl','source-reviewed final QA clauses',
            'Six integral-closure terminology clauses excluded from register count')
    elif reason.startswith('recouvrement ->'):
        add('es-recouvrement',len(rs),sum(r['changed'] for r in rs),
            'III_SEGMENT_DECISIONS.jsonl','source-reviewed terminology clause edits',reason)

# Abbreviations are retained as the source prints them, unlike spelled-out
# respectivement/voir. Count applied patch rows in these dedicated journals.
rs=read('CAMBIOS_root_abbreviations.tsv')
add('es-source-abbreviations',len(rs),len(rs),'CAMBIOS_root_abbreviations.tsv',
    'applied abbreviation edit rows')
ab=load('III_ABBREVIATION_DECISIONS.json')['decisions']
ar=[r for r in ab if 'futur' in r['reason'].lower()]
if ar:add('es-register-on-nous',len(ar),len(ar),'III_ABBREVIATION_DECISIONS.json',
          'source-author tense edits','excluded from abbreviation count')
iii_standard=read('ESTANDAR_APLICADO_iii.tsv')
for r in iii_standard:
    if r['row'] in ['es-resp-III','es-cf-III']:
        add('es-source-abbreviations',int(r['found']),int(r['changed']),
            'ESTANDAR_APLICADO_iii.tsv','abbreviation occurrences applied',r['row'])
    elif r['row']=='es-integral-closure-III':
        add('es-integral-closure',int(r['found']),int(r['changed']),
            'ESTANDAR_APLICADO_iii.tsv','source-bound terminology occurrences',r['reason'])
fidelity=read('CAMBIOS_iv3_fidelity.tsv')
iv3_resp=[r for r in fidelity if r['before']=='(respectivamente, ' and '(resp.' in r['after']]
assert len(iv3_resp)==2
add('es-source-abbreviations',2,2,'CAMBIOS_iv3_fidelity.tsv','abbreviation occurrences applied',
    'only the two resp. restorations in 11.2.9.6; no other fidelity rows counted')

# The old distinction schéma/préschéma is retained literally. Clause additions
# and headings are covered by their own journals and are not invented prefix swaps.
rs=load('III_SCHEMA_DECISIONS.json')
add('es-schema-preschema-source',len(rs),len(rs),'III_SCHEMA_DECISIONS.json','nominal term corrections')
rs=read('ROOT_SCHEME_TERMS_DECISIONS.tsv')
add('es-schema-preschema-source',len(rs),sum(r['decision']=='changed' for r in rs),
    'ROOT_SCHEME_TERMS_DECISIONS.tsv','source-reviewed lexical-context events',
    'one separately repaired missing heading is not counted as a term substitution')
rs=read('OTHER_SCHEME_DECISIONS.tsv')
add('es-schema-preschema-source',len(rs),sum(r['decision']=='change' for r in rs),
    'OTHER_SCHEME_DECISIONS.tsv','source-reviewed lexical-context events')
rs=load('IV3_SCHEME_REVIEW_FINAL.json')
add('es-schema-preschema-source',len(rs),sum(r['verdict']=='corrected source scheme/prescheme distinction' for r in rs),
    'IV3_SCHEME_REVIEW_FINAL.json','source-reviewed lexical-context events',
    'eight source-clause repairs and a restored contents noun remain separately logged, not counted as prefix substitutions')

# One final read-only inventory. It does not contribute additional found/changed
# counts for mechanical or model rules. The held inventory is one final snapshot,
# rather than a sum of every historical glossary listing.
residual=collections.Counter()
held=collections.Counter()
settled=collections.Counter()
canonical_count=0
settled_patterns={
    'es-spectre-premier':r'\bespectros?\s+primos?\b',
    'es-dessin-enfant':r"\bdessins?\s+d['’]enfants?\b",
    'es-settled-terms':r'\b(?:haz|haces|prehaz|prehaces|recubrimientos?|sucesi[oó]n(?:es)?\s+exactas?|inmersi[oó]n(?:es)?|planitud|espacios?\s+anillados?|étale)\b'}
for p in canonical_files():
    canonical_count+=1
    for a,b,prose in prose_segments(p.read_text()):
        for rid,pat,_ in RULES:residual[RULE_ALIAS.get(rid,rid)]+=len(re.findall(pat,prose,re.I))
        for rid,pat in MODELS:residual[rid]+=len(re.findall(pat,prose,re.I))
        residual['es-construible']+=len(re.findall(r'\b\w*constructib\w*\b',prose,re.I))
        for term,pat in HELD:held[term]+=len(re.findall(pat,prose,re.I))
        for rid,pat in settled_patterns.items():settled[rid]+=len(re.findall(pat,prose,re.I))
assert residual['es-voisinage']==0
assert residual['es-stalk']==664 and residual['es-filtrant']==68,dict(residual)
assert all(residual[RULE_ALIAS.get(rid,rid)]==0 for rid,_,_ in RULES),dict(residual)
assert residual['es-construible']==0
for rid,n in settled.items():
    add(rid,n,0,'ESTANDAR_APLICADO_COUNTS.json','final conforming prose inventory',
        'retention of settled/new terms; no global replacement authorized or required')
for rid,term in [('es-corps-held','corps'),('es-champ-held','champ'),
                 ('es-anneau-valuation-low-confidence','anneau de valuation')]:
    add(rid,held[term],0,'GLOSARIO_REGISTRO_held_final_verify.tsv',
        'one final prose inventory',
        'held/low-confidence decision: existing cuerpo/campo/valoración/valuación retained; historical glossary scans not summed')

descriptions={
 'es-foncteur':'APPLY_PLAN Spanish: functor and related forms → funtor; prose only.',
 'es-quasi':'APPLY_PLAN Spanish and revision b: close cuasi- compounds; prose only.',
 'es-image-reciproque':'APPLY_PLAN Spanish: imagen/imágenes recíproca(s) → inversa(s).',
 'es-limites':'APPLY_PLAN Spanish: límite directo → inductivo and inverso → proyectivo; the two directions are grouped in this one plan row.',
 'es-voisinage':'APPLY_PLAN direction superseded by DECISIONS_20261119b: entorno → vecindad, with grammatical agreement. Found includes 2 IV2 vecindad forms already conforming.',
 'es-stalk':'DECISIONS and APPLY_PLAN: tallo only for a sheaf stalk; geometric/tensor fibres retain fibra. Found counts real review events across actual initial, IV2 and final contextual passes; some locations are rereviewed.',
 'es-filtrant':'DOUBT_DECISIONS addition: filtrant → filtrante; filtré retains filtrado. Found counts initial plus real final contextual review events; retained locations are rereviewed.',
 'es-lisse':'Revision b supersedes liso: suave; occurrences introduced already conforming by new translation are not counted as replacements.',
 'es-lissite':'Morphological application of suave: lisitud/lisura → suavidad.',
 'es-preesquema':'Revision-b orthography: pre-esquema → preesquema; no replaceable form found in actual script passes or final inventory.',
 'es-iff':'Revision-b orthography: si y sólo si → si y solo si; no replaceable form found in actual script passes or final inventory.',
 'es-objet-final':'DOUBT_DECISIONS addition: objeto terminal → objeto final; no replaceable form found in actual script passes or final inventory.',
 'es-construible':'DOUBT_DECISIONS and EGAIV3-ES-TERM-0004/0014: construible/construibilidad and compounds; §8 applied component and final global applied journal counted once each.',
 'es-register-on-nous':'Revision-b register: impersonal on; author nous/imperatives retain first plural. Unit is documented clause/edit/review events, not words or distinct sites. General retranslations are not assigned invented replacement counts; source-bound retained plurals remain in review journals.',
 'es-source-abbreviations':'General source-register rule: preserve resp. and cf.; full respectivement/voir remain translated in full. Unit is dedicated applied edit rows, including accompanying source-clause repairs documented in III.',
 'es-schema-preschema-source':'Settled source terms: schéma → esquema, préschéma → preesquema. Found counts reviewed lexical contexts; changed counts direct nominal corrections. Added source clauses and headings remain in fidelity journals.',
 'es-recouvrement':'Settled Spanish term recubrimiento for recouvrement; applied III source-bound clause edits. Existing conforming prose is not counted as replacement.',
 'es-integral-closure':'Source terminology: intégralement clos → integralmente cerrado, distinguished from intègre → íntegro; six explicit final III corrections.',
 'es-spectre-premier':'DOUBT_DECISIONS addition: espectro primo; final conforming phrase inventory retained.',
 'es-dessin-enfant':'DOUBT_DECISIONS addition: dessin d’enfant retained; final conforming phrase inventory.',
 'es-settled-terms':'DECISIONS settled terms remain haz, prehaz, recubrimiento, sucesión exacta, inmersión, planitud, espacio anillado, étale. Found is one final lexical inventory, not applied edits.',
 'es-corps-held':'Revision-b field decision remains held pending the specified canonical book check; existing cuerpo retained; one final inventory only.',
 'es-champ-held':'Revision-b champ decision remains held pending the specified canonical book check; existing campo retained; one final inventory only.',
 'es-anneau-valuation-low-confidence':'DOUBT_DECISIONS low-confidence valuación choice is recorded without imposing it on existing valoración; one final inventory only.',
}
order=list(descriptions)
rows=[]
for rid in order:
    d=counts[rid]
    if rid=='es-stalk':left='664 legitimate fibre uses retained; 666 final review records, with 2 later removed by source restoration in III, not changed to tallo'
    elif rid=='es-filtrant':left='68 filtré/filtered-object uses retained'
    elif rid in ['es-corps-held','es-champ-held','es-anneau-valuation-low-confidence']:
        left=str(d['found'])+' retained; GLOSARIO_REGISTRO_held_final_verify.tsv (one final snapshot)'
    elif rid in settled_patterns:left=str(d['found'])+' conforming occurrences retained'
    elif rid in ['es-register-on-nous','es-source-abbreviations','es-schema-preschema-source','es-recouvrement','es-integral-closure']:
        left='Source-conforming retained clauses and terms documented in cited review journals; no unreviewed queued replacement'
    else:left='0 replaceable residual prose forms in final canonical inventory'
    refs='; '.join(dict.fromkeys(p['file'] for p in d['parts']))
    reason=descriptions[rid]+' Evidence: '+(refs or 'actual application journals and final canonical prose inventory')
    rows.append([rid,d['found'],d['changed'],left,reason])

write_tsv(REC/'ESTANDAR_APLICADO_final.tsv',HEADER,rows)
write_tsv(REC/'ESTANDAR_RULE_EVIDENCE.tsv',
          ['rule','found','changed','count_unit','applied_or_review_record','detail'],evidence)
out=dict(canonical_files=canonical_count,counts=dict(counts),
         final_residuals=dict(residual),final_held_inventory=dict(held),
         actual_model_reviewed=1401,actual_model_changed=948,actual_model_atomic_patches=2330,
         final_model_review_events=736,final_model_remaining_lexical_candidates=732,
         important_count_convention='Actual applied or context-reviewed events, not a sum of dry runs. Final reviews may revisit initial retained locations; no unique-location total is claimed. Each CURRENT and DIPLOMATIC source occurrence is counted in its own edition. Register rows have patch/clause granularity, not word granularity.')
(REC/'ESTANDAR_APLICADO_COUNTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(REC/'ESTANDAR_APLICADO_FINAL_METHOD.md').write_text('''# Recuento final del estándar español

ESTANDAR_APLICADO_final.tsv es el único resumen que se incorpora a ESTANDAR_APLICADO.tsv. Cada fila corresponde a una regla del plan español o a una regla ampliada o conservada por la revisión b, las decisiones de duda y el registro terminológico suministrado. La dirección vieja vecindad → entorno queda sustituida por entorno → vecindad. Las decisiones held y de baja confianza mantienen los términos heredados.

Las cifras proceden de pasadas efectivamente aplicadas o de revisiones de contexto concluidas. No se suman ESTANDAR_DRY_RUN*, las tablas preapply, las propuestas ni ESTANDAR_APLICADO_model.tsv, que conserva el estado histórico anterior a la aplicación. El fichero STANDARD_MODEL_APPLIED_IDS y los dos registros BINDINGS demuestran que se aplicaron los 2.330 parches atómicos correspondientes a 948 sustituciones de término; los otros parches ajustan determinantes y concordancia. No se cuentan estos ajustes como términos adicionales.

«found» no significa siempre lugares únicos: las filas de tallo y filtrante incluyen la revisión contextual inicial y la revisión final real, con algunos lugares leídos de nuevo. Las reglas de registro cuentan actos documentados de revisión o edición de cláusulas; sus parches tienen distinta longitud. No se inventan recuentos de reemplazos a partir de traducciones nuevas o retraducciones completas. ESTANDAR_RULE_EVIDENCE.tsv explica la unidad y el registro de cada sumando. Las capas CURRENT y DIPLOMATIC tienen sus propias ocurrencias y se cuentan por separado.

La revisión final de los términos dependientes del contexto contiene 736 decisiones: 167 ROOT, 350 OTHER, 102 IV3 y 117 III. De ellas se sustituyeron dos entornos por vecindades; otras dos apariciones de fibra desaparecieron al restituir cláusulas de III, sin sustitución por tallo. Quedan 664 usos legítimos de fibra y 68 de filtrado, y ningún entorno. Esto da 732 candidatos léxicos finales conservados, no 732 incumplimientos.

Las decisiones held se cuentan a partir de un único inventario final del corpus canónico, no sumando las listas históricas de glosario. La consolidación del glosario toma GLOSARIO_REGISTRO_held_final_verify.tsv como inventario final por lugar. Los registros anteriores permanecen como evidencia histórica.

El script consolidate_standard_summary.py solo lee el corpus y escribe los registros de resumen; no cambia ninguna traducción ni verifica demostraciones matemáticas.
''')
print(json.dumps({'rows':len(rows),'model_atomic_patches':2330,'actual_mechanical_edits':sum(len(read(n)) for n in script_files),
                  'summary':[{k:v for k,v in zip(HEADER,r) if k in ['row','found','changed']} for r in rows],
                  'residuals':dict(residual)},ensure_ascii=False))

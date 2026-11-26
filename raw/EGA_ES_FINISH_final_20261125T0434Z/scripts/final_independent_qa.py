"""Independent final read-only corpus/build/credit/note validation.
Only QA reports and the authorized full BUILD_final_SUMMARY.tsv are written.
"""
from pathlib import Path
import csv,json,re,hashlib,collections
import fitz
from corpus import RESULT,SOURCE,write_tsv
from tex_tools import balanced_end

R=RESULT/'records';ORIGINAL=SOURCE/'EGA_ES_FINISH_2_ESPANOL'
def tab(name):return list(csv.DictReader((R/name).open(),delimiter='\t'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',s)
def notes(t):
 out=[]
 for m in re.finditer(r'\\footnote(?:text)?(?:\[[^]]*\])?\{',t):
  b=balanced_end(t,m.end()-1);out.append(t[m.start():b])
 return out

expected={f'EGA_{v}_{e}' for v in ['I','II','III1','IV1','IV2'] for e in ['CURRENT','DIPLOMATIC']}|{'EGA_III2','EGA_IV3','EGA_IV4','EGA_COMPLETA_CURRENT'}
pdf_evidence={r['reader']:r for r in json.loads((R/'FINAL_INDEPENDENT_PDF_EVIDENCE.json').read_text())}
assert set(pdf_evidence)==expected
actual_pdf={p.parent.name for p in (RESULT/'readers').glob('*/*.pdf')};actual_tex={p.parent.name for p in (RESULT/'readers').glob('*/*.tex')}
assert actual_pdf==expected and actual_tex==expected
builds=[];warnings=[];failures=[];aggregate_warning_types=collections.Counter()
for name in sorted(expected):
 p=R/('BUILD_final_'+name+'.json');b=json.loads(p.read_text());folder=RESULT/'readers'/name;pdf=folder/(name+'.pdf');tex=folder/(name+'.tex');log=folder/'build.log';ev=pdf_evidence[name]
 assert b['reader']==name and b['stage']=='final'
 assert pdf.is_file() and tex.is_file() and log.is_file() and pdf.stat().st_size and tex.stat().st_size
 assert sha(pdf)==ev['pdf_sha256'],name+' PDF changed during review'
 with fitz.open(pdf) as doc:pages=len(doc)
 maxpt=max((x[2] for x in b['overfull']),default=0)
 assert b['returncode']==0 and pages==b['pages']==ev['pdf_pages'] and maxpt<=2
 for x in b['overfull']:assert x[1] in ['h','v']
 specific_refs=[w for w in ev['undefined_warnings'] if 'There were undefined references' not in w]
 row={'reader':name,'tex':str(tex.relative_to(RESULT)),'pdf':str(pdf.relative_to(RESULT)),'build_log':str(log.relative_to(RESULT)),'pdf_sha256':ev['pdf_sha256'],'tex_sha256':sha(tex),'build_report_sha256':sha(p),'build_log_sha256':sha(log),'pdf_bytes':pdf.stat().st_size,'returncode':b['returncode'],'passes':b['passes'],'reported_pages':b['pages'],'actual_pages':pages,'overfull_count':len(b['overfull']),'overfull':b['overfull'],'maximum_pt':maxpt,'warning_count':len(b['warnings']),'warning_counts':b['warning_counts'],'undefined_reference_warning_count':ev['undefined_warning_count'],'specific_undefined_reference_warning_count':len(specific_refs),'undefined_citation_warning_count':ev['undefined_citation_warning_count'],'duplicate_label_destination_warning_count':ev['duplicate_label_destination_warning_count'],'visible_question_marker_count':ev['visible_question_marker_count'],'status':'pass'}
 builds.append(row);aggregate_warning_types.update(b['warning_counts'])
 if specific_refs:warnings.append({'reader':name,'kind':'standalone_external_reference_warnings','specific_count':len(specific_refs),'including_summary_count':ev['undefined_warning_count'],'detail':'Warnings remain for external hyperreferences. The PDF text scan found no [?] or ?? markers; explicit reference text remains. This is not a live-link test.'})

# Bind every recorded visual observation to the PDFs and image files now delivered.
visual=[];vrows=[]
for filename in ['PDF_VISUAL_I_II_IV1.tsv','PDF_VISUAL_III_IV34.tsv','PDF_VISUAL_ROOT.tsv']:
 rows=tab(filename)
 for i,x in enumerate(rows,1):
  assert x['reader'] in expected
  ev=pdf_evidence[x['reader']]
  assert x['pdf_sha256']==ev['pdf_sha256'] and int(x['total_pages'])==ev['pdf_pages']
  assert 1<=int(x['physical_page'])<=ev['pdf_pages']
  paths=x['image'].split(';');image_hashes=[]
  for path in paths:
   image=RESULT/path;assert image.is_file(),path;image_hashes.append(sha(image))
  if x.get('image_sha256'):assert len(paths)==1 and x['image_sha256']==image_hashes[0]
  verdict=x.get('verdict',x.get('status'))
  assert verdict=='PASS' or verdict.startswith('no_visual_issue_observed'),verdict
  vrows.append({'record':filename,'row':i,'reader':x['reader'],'physical_page':int(x['physical_page']),'pdf_sha256':x['pdf_sha256'],'images':paths,'image_sha256':image_hashes,'verdict':verdict})
 visual.append({'record':filename,'rows':len(rows),'readers':sorted({x['reader'] for x in rows}),'distinct_physical_pages':len({(x['reader'],x['physical_page']) for x in rows}),'pdf_hash_mismatches':0,'missing_images':0})
assert {x['reader'] for x in vrows}==expected

# Credits: source paragraphs and exact fields were independently checked already;
# bind all 767 checks to unchanged current fronts and original records.
cc=tab('CREDITS_FINAL_CHECKS.tsv');cr=tab('CREDITS_FINAL_REVIEW.tsv');cf=tab('CREDITS_FINAL_FINDINGS.tsv')
assert len(cc)==767 and all(x['status']=='pass' for x in cc) and len(cr)==14 and not cf
for x in cr:
 front=(RESULT/x['file']).read_text().split(r'\begin{document}',1)[1].split(r'\tableofcontents',1)[0]
 assert hashlib.sha256(front.encode()).hexdigest()==x['front_sha256']
 assert x['pending']=='0' and x['status']=='closed'
credit_counts=json.loads((R/'CREDITS_FINAL_COUNTS.json').read_text())
assert credit_counts['checks']==767 and credit_counts['pending']==0

# Independently account for every inherited original note using either unchanged
# text or an explicitly reviewed original->current pair; no similarity threshold.
audit=tab('INHERITED_NOTE_AUDIT.tsv');review=tab('INHERITED_NOTE_FINAL_REVIEW.tsv');adds=tab('INHERITED_NOTE_ADDITIONS_REVIEW.tsv')
assert len(review)==20 and all(x['status']=='closed' for x in review) and len(adds)==4
reviewmap={(x['file'],norm(x['before'])):norm(x['after']) for x in review}
original_count=current_count=exact=reviewed=0;leftovers=[];note_files=[]
for x in audit:
 p=RESULT/x['file'];q=ORIGINAL/x['file'].removeprefix('tree/')
 if not q.exists():q=Path(str(q).replace('DIPLOMATIC','CURRENT').replace('.diplomatic.tex','.tex'))
 assert q.is_file() and p.is_file()
 old=notes(q.read_text());new=notes(p.read_text());normalized=[norm(s) for s in new];used=set();exact_file=reviewed_file=0
 for s in old:
  matching=[j for j,n in enumerate(normalized) if j not in used and n==norm(s)]
  if matching:used.add(matching[0]);exact+=1;exact_file+=1;continue
  target=reviewmap.get((x['file'],norm(s)));assert target,(x['file'],'no reviewed preservation mapping')
  matching=[j for j,n in enumerate(normalized) if j not in used and n==target]
  assert len(matching)==1,(x['file'],'reviewed note absent or ambiguous')
  used.add(matching[0]);reviewed+=1;reviewed_file+=1
 original_count+=len(old);current_count+=len(new)
 for j,s in enumerate(new):
  if j not in used:leftovers.append((x['file'],norm(s)))
 note_files.append({'file':x['file'],'original_source':str(q.relative_to(SOURCE)),'original_notes':len(old),'current_notes':len(new),'unchanged':exact_file,'reviewed_pairs':reviewed_file,'current_sha256':sha(p)})
assert (original_count,current_count,exact,reviewed)==(264,268,244,20)
assert collections.Counter(leftovers)==collections.Counter((x['file'],norm(x['after'])) for x in adds)
conflicts=tab('INHERITED_NOTE_SOURCE_CONFLICTS.tsv');assert len(conflicts)==1
for x in conflicts:
 assert x['inherited_note']==x['retained_note'] and x['retained_note'] in (RESULT/x['current_file']).read_text()
assert len(leftovers)==4
notes_summary={'original_notes':original_count,'current_notes':current_count,'unchanged_ignoring_whitespace':exact,'closed_reviewed_pairs':reviewed,'unaccounted_original_notes':0,'added_or_relocated_notes_explained':len(leftovers),'known_unchanged_source_conflicts':len(conflicts),'mathematical_proof_verification':False,'files':note_files}

cumulative=next(x for x in builds if x['reader']=='EGA_COMPLETA_CURRENT')
assert cumulative['undefined_reference_warning_count']==0 and cumulative['undefined_citation_warning_count']==0 and cumulative['duplicate_label_destination_warning_count']==0 and cumulative['visible_question_marker_count']==0
warnings.append({'kind':'inherited_editorial_note_source_conflict','count':1,'place':'IV1 CURRENT 0.23.2.8(ii)','detail':'The inherited note is preserved exactly; it calls 23.2.7 nonexistent while identifying Proposition23.2.7. Supplied French CURRENT reads23.2.7 and DIPLOMATIC23.1.13. See INHERITED_NOTE_SOURCE_CONFLICTS.tsv/md; no new mathematical claim or correction.'})
summary={'readers':len(builds),'total_pdf_pages_including_layers_and_cumulative':sum(x['actual_pages'] for x in builds),'all_reader_tex_pdf_log_exist':True,'all_returncodes_zero':True,'all_page_counts_match':True,'overfull_boxes':sum(x['overfull_count'] for x in builds),'maximum_overfull_pt':max(x['maximum_pt'] for x in builds),'overfull_above_2pt':0,'undefined_citation_warnings':sum(x['undefined_citation_warning_count'] for x in builds),'undefined_reference_warnings_including_summary':sum(x['undefined_reference_warning_count'] for x in builds),'specific_undefined_reference_warnings':sum(x['specific_undefined_reference_warning_count'] for x in builds),'duplicate_label_destination_warnings':sum(x['duplicate_label_destination_warning_count'] for x in builds),'visible_question_marker_count':sum(x['visible_question_marker_count'] for x in builds),'visual_observation_rows':len(vrows),'distinct_visually_reviewed_physical_pages':len({(x['reader'],x['physical_page']) for x in vrows}),'visual_readers':len({x['reader'] for x in vrows}),'visual_pdf_hash_mismatches':0,'visual_missing_images':0,'build_warning_count':sum(x['warning_count'] for x in builds),'credit_checks':767,'credit_pending':0,'credit_front_hash_mismatches':0,'unaccounted_inherited_notes':0,'documented_inherited_note_source_conflicts':1,'source_pdf_reader_edits':0,'translation_or_build_rerun':False,'proof_verification':False,'failures':failures}
report={'summary':summary,'builds':builds,'aggregate_warning_counts':dict(aggregate_warning_types),'cumulative_references':{'reader':cumulative['reader'],'pages':cumulative['actual_pages'],'undefined_reference_warnings':0,'undefined_citation_warnings':0,'duplicate_label_destination_warnings':0,'visible_question_markers':0,'pdf_sha256':cumulative['pdf_sha256']},'visual_records':visual,'visual_observations':vrows,'credits':credit_counts,'inherited_notes':notes_summary,'warnings':warnings,'limits':['PDF text marker search is a screen, not proof of complete link correctness.','Visual observations are inherited from explicit view_image reviews and bound to exact PDF hashes; this closure does not claim a new page-by-page visual review.','External URL availability was not checked.','The 264-note account covers comparable footnote/footnotetext notes in the inherited-note audit, not every annotation of every kind.','No mathematical proof verification.']}
(R/'FINAL_INDEPENDENT_QA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Authorized restoration of the complete summary after a --only build.
write_tsv(R/'BUILD_final_SUMMARY.tsv',['reader','returncode','passes','pages','overfull_boxes','maximum_pt','warnings'],[[x['reader'],x['returncode'],x['passes'],x['actual_pages'],x['overfull_count'],x['maximum_pt'],x['warning_count']] for x in builds])

md='''# Cierre independiente de calidad

## Resultado

Se verificaron los **14 lectores finales** a partir de los 14 informes `BUILD_final_*.json`, los PDF actuales y los registros de revisión. Los 14 TeX, PDF y archivos `build.log` existen; los PDF se abren y sus **3373 páginas en total** coinciden con los recuentos de los informes. Esa suma incluye ambas capas y el acumulativo, por lo que no representa páginas de contenido único.

Los 14 códigos de salida son cero. Hay **dos cajas verticales overfull de 1,08224 pt**, una en IV3 y su repetición en el acumulativo; ninguna supera 2 pt. No se detectaron avisos de citas bibliográficas indefinidas ni de etiquetas o destinos duplicados. La extracción de texto de las 3373 páginas no contiene marcadores `??` ni citas que comiencen por `[?`.

No se reejecutaron traducciones ni compilaciones, y no se modificaron fuentes, PDF ni lectores. Se reconstruyó `BUILD_final_SUMMARY.tsv` con las 14 filas a partir de los JSON individuales; el último proceso con `--only` lo había reducido a una fila.

## Compilaciones y páginas

| Lector | Páginas PDF | Salida | Cajas overfull | Máximo pt | Avisos de referencias, incluido resumen |
|---|---:|---:|---:|---:|---:|
'''
for x in builds:md+='| '+x['reader']+' | '+str(x['actual_pages'])+' | '+str(x['returncode'])+' | '+str(x['overfull_count'])+' | '+str(x['maximum_pt'])+' | '+str(x['undefined_reference_warning_count'])+' |\n'
md+='''
## Referencias y avisos conservados

El acumulativo CURRENT tiene **1278 páginas**, cero avisos de referencias indefinidas, cero avisos de citas indefinidas y cero avisos de etiquetas o destinos duplicados. Tampoco aparecen marcadores `??` o `[?` en su texto extraído.

En los lectores independientes permanecen **81 avisos de referencias**, correspondientes a **75 advertencias concretas y seis avisos de resumen**: III1 CURRENT y DIPLOMATIC, 28 cada uno; II CURRENT, 10; II DIPLOMATIC, 6; IV3, 2; IV4, 7. Son avisos de hiperreferencias externas cuyo texto numérico se conserva. Se distinguen de las citas bibliográficas: estas últimas no generan ningún aviso de cita indefinida. La ausencia de marcadores visibles no demuestra por sí sola que todos los enlaces interactivos funcionen; no se afirma una prueba exhaustiva de navegación.

Los 537 avisos de compilación se distribuyen en 440 de cadenas de marcadores PDF, 16 de recursos o expansión de fuentes de pdfTeX y los 81 de referencias ya descritos. Permanecen en los informes originales. Los recuentos exactos por clase están en `FINAL_INDEPENDENT_QA.json`. Código de salida cero no se presenta como ausencia de avisos.

## Correspondencia con la inspección visual

Se cotejaron las tres tablas de revisión visual con los PDF actuales y sus imágenes:

| Registro | Filas | Lectores | Páginas físicas distintas |
|---|---:|---:|---:|
'''
for x in visual:md+='| '+x['record']+' | '+str(x['rows'])+' | '+str(len(x['readers']))+' | '+str(x['distinct_physical_pages'])+' |\n'
md+='''
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
'''
(R/'FINAL_INDEPENDENT_QA.md').write_text(md)
print(json.dumps(summary,ensure_ascii=False))
print('Warnings by class',json.dumps(dict(aggregate_warning_types),ensure_ascii=False))

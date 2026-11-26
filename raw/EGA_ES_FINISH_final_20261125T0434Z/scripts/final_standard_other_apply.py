"""Apply two reviewed voisinage decisions and record all 350 OTHER verdicts."""
import json,re,collections,hashlib
from pathlib import Path
from corpus import RESULT,write_tsv
from tex_tools import math_spans

rp=RESULT/'records/FINAL_STANDARD_OTHER_CONTEXTS.json'
rows=json.loads(rp.read_text())
assert len(rows)==350
verdicts=[];gloss=[];changes=[];checks=[];patches=[]
for r in rows:
 if 'selected_source' not in r:
  if r['queue_id'] in {300,453}:
   z=r['fresh_source'];p=RESULT.parent/'source'/z['file'];t=p.read_text();a=z['source_offset'];b=a+len(z['french_gap'])
   r['selected_source']={'file':z['file'],'anchor':z['unit'],'term':'celle (antécédent : fibre formelle)','source_line':z['source_line'],'context':re.sub(r'\s+',' ',t[max(0,a-180):b+180])}
   r['binding_method']='French anaphora celle; antecedent fibre formelle in the same sentence'
  else:
   assert r['queue_id'] in set(range(173,181)) and r['old_verdict']=='retain'
   r['selected_source']=r['french'][0]
   r['binding_method']='unchanged Spanish editorial note; prior French semantic witness rechecked'
 z=r['selected_source'];source=z['file']+':'+z['anchor']+(':line '+str(z['source_line']) if 'source_line' in z else '')
 assert (RESULT.parent/'source'/z['file']).is_file()
 if r['row']=='es-voisinage':
  decision='change';rendering='vecindad';reason='Voisinage topológico de un punto: vecindad; artículo femenino una.'
 elif r['row']=='es-filtrant':
  decision='retain';rendering=r['form'];reason='Módulo provisto de una filtración; la fuente dice filtré. Se conserva filtrado.'
 else:
  decision='retain';rendering=r['form']
  if re.search(r'fibr[ea]s?\s+formal',r['context'],re.I) or 'fibre formelle' in z['context'].lower() or 'fibres formelles' in z['context'].lower():reason='Fibra formal de un anillo: fibra del morfismo del espectro del completado; se conserva fibra.'
  elif 'geométrica' in r['context'].lower():reason='Fibra geométrica de un morfismo o fibrado, con extensión del cuerpo residual; se conserva fibra.'
  else:reason='Fibra de un morfismo o espacio subyacente, no tallo de un haz; se conserva fibra.'
 relation=z.get('source_relation','same source passage, bounded by aligned mathematical formulas')
 basis=('Reutiliza veredicto '+str(r['old_id'])+'; fuente y sentido cotejados sin cambio' if r['old_id'] is not None else 'Candidato ausente de la cola anterior; cotejo nuevo con fuente')
 rid='final-other-'+str(r['queue_id'])
 verdicts.append([rid,r['row'],r['file'],r['place'],r['form'],decision,reason,source,relation,r['old_id'] if r['old_id'] is not None else '',basis])
 gloss.append([z['term'],rendering,'standard/DECISIONS_20261119b.tsv; '+source+'; '+z['context']+'; '+reason,r['file']+':'+r['place']+':line '+r['line'],'yes'])
 r['decision']=decision;r['reason']=reason;r['source_witness']=source
 if decision=='change':
  p=RESULT/r['file'];t=p.read_text();a=r['offset']-3;b=r['end']+4
  assert hashlib.sha256(t.encode()).hexdigest()==r['file_sha256']
  assert re.sub(r'\s+',' ',t[a:b])=='un entorno que',(rid,t[a:b])
  new=t[a:b].replace('un','una',1).replace('entorno','vecindad');out=t[:a]+new+t[b:]
  assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(out)]
  for pat in [r'\\label\{[^}]*\}',r'\\tag\{[^}]*\}',r'\\oldpage(?:\[[^\]]*\])?\{[^}]*\}']:
   assert re.findall(pat,t)==re.findall(pat,out)
  p.write_text(out)
  changes.append([r['file'],r['place'],t[a:b],new,'standard','standard/DECISIONS_20261119b.tsv: es-voisinage; '+source])
  checks.append([r['file'],1,len(math_spans(t)),'unchanged','unchanged',hashlib.sha256(t.encode()).hexdigest(),hashlib.sha256(out.encode()).hexdigest()])
  patches.append({'file':r['file'],'review_id':rid,'offset':a,'before':t[a:b],'after':new,'source':source})

write_tsv(RESULT/'records/FINAL_STANDARD_MODEL_OTHER.tsv',['review_id','row','file','place','form','verdict','reason','french_source','source_relation','prior_review_id','review_basis'],verdicts)
write_tsv(RESULT/'records/CAMBIOS_standard_final_other.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/GLOSARIO_REGISTRO_standard_final_other.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
write_tsv(RESULT/'records/FINAL_STANDARD_OTHER_STRUCTURE.tsv',['file','atomic_edits','math_spans','math_sequence','labels_tags_pages','before_sha256','after_sha256'],checks)
write_tsv(RESULT/'records/CHECK_EVENTS_standard_final_other.tsv',['statement_id','date','who','type','outcome'],[
 ['final-standard-other','2026-11-25','IA','terminology_source_comparison','350 candidates reviewed: 344 fibers and 4 filtered modules retained; 2 topological neighborhoods changed to vecindad. 68 previous verdicts rechecked, 282 fresh comparisons; 171 French layer pairs have identical bounded passages. No mathematical proof verification.'],
 ['final-standard-other-structure','2026-11-25','script','structural_comparison','Two changed I0 files preserve ordered mathematical spans, labels, tags and original-page markers exactly.']])
rp.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(RESULT/'records/FINAL_STANDARD_OTHER_PATCHES.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reviewed':len(rows),'retained':sum(r['decision']=='retain' for r in rows),'changed':len(changes),'fresh':sum(r['old_id'] is None for r in rows),'glossary_witnesses':len(gloss),'structure_files':len(checks)}))

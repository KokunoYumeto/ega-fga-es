"""Freeze reviewed text proposals with exact preconditions; do not edit corpus."""
from pathlib import Path
import json,re,hashlib,collections
from corpus import RESULT,write_tsv
from tex_tools import math_spans

rows=json.loads((RESULT/'records/STANDARD_MODEL_PROPOSALS_DRAFT.json').read_text())
files={r['file'] for r in rows};texts={f:(RESULT/f).read_text() for f in files}
atomic=collections.defaultdict(dict)
for r in rows:
 t=texts[r['file']]
 assert hashlib.sha256(t.encode()).hexdigest()==r['file_sha256'],('File changed since binding',r['file'])
 for a,b,new in r['edits']:
  k=(a,b);d=atomic[r['file']]
  if k in d:
   assert d[k]['after']==new,('conflicting replacements',r['id'],d[k])
   d[k]['review_ids'].append(r['id'])
  else:d[k]={'start':a,'end':b,'before':t[a:b],'after':new,'review_ids':[r['id']]}

patches=[];checks=[];changes=[];snapshots={}
for f,d in sorted(atomic.items()):
 t=texts[f];es=sorted(d.values(),key=lambda e:e['start'])
 assert all(a['end']<=b['start'] for a,b in zip(es,es[1:])),('overlap',f)
 out=t
 for e in reversed(es):out=out[:e['start']]+e['after']+out[e['end']:]
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(out)],('math changed',f)
 for pat in [r'\\label\{[^}]*\}',r'\\tag\{[^}]*\}',r'\\oldpage(?:\[[^\]]*\])?\{[^}]*\}']:
  assert re.findall(pat,t)==re.findall(pat,out),('anchor changed',f,pat)
 assert not re.search(r'\b(?:de el|a el)\s+tallos?\b',out,re.I),(f,'bad contraction')
 snapshots[f]=hashlib.sha256(t.encode()).hexdigest()
 checks.append([f,len(es),len(math_spans(t)),'unchanged','unchanged','candidate_in_memory_only'])
 for e in es:
  ids=e['review_ids'];rr=[rows[i] for i in ids]
  places=sorted({r['place'] for r in rr});standards=sorted({r['row'] for r in rr})
  sources=sorted({z['file']+':'+z['anchor'] for r in rr for z in r['french']})
  p={'file':f,**e,'places':places,'standard_rows':standards,
     'prefix':t[max(0,e['start']-120):e['start']],
     'suffix':t[e['end']:min(len(t),e['end']+120)],'sources':sources}
  patches.append(p)
  changes.append([f,'; '.join(places),e['before'],e['after'],'standard_proposed',
                  'standard/DECISIONS_20261119b.tsv: '+','.join(standards)+'; '+'; '.join(sources)])

found=collections.Counter(r['row'] for r in rows)
changed=collections.Counter(r['row'] for r in rows if r['decision']=='change')
retained=found-changed
payload={'status':'proposed_not_applied','schema_version':1,
 'application_rule':'Apply in descending start order only if file SHA256 and exact before match; if file hash changed, rebind each complete prefix+before+suffix uniquely before applying. Do not infer an occurrence from before alone.',
 'reviewed_occurrences':len(rows),'proposed_occurrences':dict(changed),'retained_occurrences':dict(retained),
 'file_sha256':snapshots,'patches':patches}
(RESULT/'records/STANDARD_MODEL_PATCHES.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
write_tsv(RESULT/'records/CAMBIOS_standard_model.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/ESTANDAR_APLICADO_model.tsv',['row','found','changed','places_left','reason'],
 [[rid,found[rid],0,str(changed[rid])+' proposed',str(changed[rid])+' occurrence changes reviewed but not applied; '+str(retained[rid])+' occurrences retained after sense review'] for rid in sorted(found)])
verdicts=[]
for r in rows:
 if r['row']=='es-voisinage':reason='Topological or infinitesimal neighborhood: voisinage → vecindad; feminine agreement included.'
 elif r['row']=='es-stalk':reason='Sheaf stalk at a point: fibre → tallo; masculine agreement included.' if r['decision']=='change' else 'Fiber of a morphism, geometric/formal fiber, or tensor with a residue field: retain fibra.'
 else:reason='Directed system, set, or family: filtrant → filtrante.' if r['decision']=='change' else 'Object endowed with a filtration: filtré → filtrado; retain existing term.'
 sources='; '.join(sorted({z['file']+':'+z['anchor'] for z in r['french']}))
 relations='; '.join(sorted({z.get('source_relation','same numbered French unit') for z in r['french']}))
 verdicts.append([r['id'],r['row'],r['file'],r['place'],r['form'],r['decision'],reason,sources,relations])
write_tsv(RESULT/'records/STANDARD_MODEL_VERDICTS.tsv',['review_id','row','file','place','form','verdict','reason','french_source','source_relation'],verdicts)
write_tsv(RESULT/'records/STANDARD_MODEL_CANDIDATE_CHECKS.tsv',['file','atomic_edits','math_spans','math_sequence','labels_tags_pages','status'],checks)
write_tsv(RESULT/'records/CHECK_EVENTS_standard_model.tsv',['statement_id','date','who','type','outcome'],
 [['model-terminology-review','2026-11-25','IA','terminology_source_comparison',f'{len(rows)} occurrences reviewed; {sum(changed.values())} term changes proposed. Semantic and grammatical review only, no proof verification.'],
  ['model-terminology-candidates','2026-11-25','script','structural_comparison',f'{len(checks)} in-memory candidate files: exact ordered mathematical spans, labels, tags and original-page markers unchanged. No corpus writes performed.']])
print(json.dumps({'reviewed':len(rows),'files_with_proposals':len(checks),'atomic_patches':len(patches),'proposed':dict(changed),'retained':dict(retained)},ensure_ascii=False))

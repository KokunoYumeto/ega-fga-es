"""Record individual final fibre/stalk decisions against their French units."""
import csv,re,json,collections
from corpus import RESULT,FR,write_tsv
from iv3_align import units
from iv3_work import DIR
from tex_tools import balanced_end
queue=[r for r in csv.DictReader((RESULT/'records/ESTANDAR_MODEL_QUEUE_final_preapply.tsv').open(),delimiter='\t') if '/IV3/' in r['file']]
group=collections.defaultdict(list)
for i,r in enumerate(queue):group[r['file']].append((i,r))
out=[];details=[]
for file,rows in group.items():
 q=RESULT/file;t=q.read_text();matches=list(re.finditer(r'\bfibras?\b',t,re.I));assert len(matches)==len(rows),(file,len(matches),len(rows))
 su=units(t)
 for (i,r),m in zip(rows,matches):
  assert m.group().lower()==r['form'].lower()
  back=q.name=='backmatter-es.tex';n=next((n for n,u in su.items() if u.start<=m.start()<u.end),'front')
  section=q.stem.replace('ega4-','') if not back else '15-terminal'
  if n.startswith('15.7.'):section='15-terminal'
  fp=FR/'current/IV3/native/ega4'/f'ega4-{section}-fr.tex';ft=fp.read_text()
  if back:ft=ft[ft.index('\\clearpage\n\\oldpage[IV-3]{249}'):];fu=ft
  else:fu=units(ft)[n].text
  french=[fu[max(0,h.start()-85):h.end()+150] for h in re.finditer(r'\bfibres?\b',fu,re.I)]
  current_unit=t if back else su[n].text
  start=0 if back else su[n].start
  local=list(re.finditer(r'\bfibras?\b',current_unit,re.I))
  if len(local)==len(french):
   ordinal=next(j for j,h in enumerate(local) if start+h.start()==m.start())
   french=[french[ordinal]]
  context=t[max(0,m.start()-100):m.end()+180]
  # These 102 contexts have been read: all denote morphism fibres (including
  # generic fibres, dimension, flatness-by-fibres, and the printed indexes).
  # The two inherited editorial notes also describe a geometric fibre.
  reason='Geometric fibre of a morphism or its fibre-space properties; not a sheaf stalk. Retain fibra/fibras.'
  if back:reason='Printed index or contents entry about morphism fibres; retain fibra/fibras.'
  if 'criterio de planitud' in context.lower():reason='Flatness criterion by morphism fibres (11.3.10); retain fibras.'
  if not french:
   # The source clause may name a fibre through its inverse-image formula.
   french=[fu[:450]]
  source=str(fp.relative_to(RESULT.parent/'source'))+':'+('back matter' if back else n)
  out.append([i,r['row'],file,('back matter' if back else n),m.group(),'retain',reason,source,'French unit and geometric inverse-image meaning reviewed'])
  details.append(dict(review_id=i,file=file,place=n,source=source,spanish_context=context,french_contexts=french,verdict='retain geometric fibre'))
write_tsv(RESULT/'records/FINAL_STANDARD_MODEL_IV3.tsv',['review_id','row','file','place','form','verdict','reason','french_source','source_relation'],sorted(out))
write_tsv(RESULT/'records/CAMBIOS_standard_final_iv3.tsv',['file','place','before','after','kind','source'],[])
(RESULT/'records/FINAL_STANDARD_MODEL_IV3_CONTEXTS.json').write_text(json.dumps(sorted(details,key=lambda x:x['review_id']),ensure_ascii=False,indent=2)+'\n')
print('Reviewed',len(out),'contexts: all geometric fibres retained, zero stalk substitutions needed')

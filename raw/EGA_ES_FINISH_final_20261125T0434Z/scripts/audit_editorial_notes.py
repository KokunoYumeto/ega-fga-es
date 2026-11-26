"""Track inherited notes separately from author-text formula alignment."""
import re,json,difflib,collections,sys
from corpus import RESULT,ES,SOURCE,write_tsv
from tex_tools import balanced_end
from standardize import canonical_files
BASE=SOURCE/'EGA_ES_FINISH_2_ESPANOL'
def notes(t):
 out=[]
 for m in re.finditer(r'\\footnote(?:text)?(?:\[[^]]*\])?\{',t):
  b=balanced_end(t,m.end()-1);out.append((m.start(),b,t[m.start():b]))
 return out
rows=[];diffs=[]
for p in canonical_files():
 rel=p.relative_to(ES);q=BASE/rel
 if not q.exists() and 'DIPLOMATIC' in str(rel):
  q=BASE/str(rel).replace('DIPLOMATIC','CURRENT').replace('.diplomatic.tex','.tex')
 if not q.exists():continue
 if '--all' not in sys.argv and not any(s in str(rel) for s in ['EGA_I_ch1','PORTED_20261109/IV4']):continue
 old=notes(q.read_text());new=notes(p.read_text());used=set();exact=0;changed=0;missing=0
 for a,b,s in old:
  candidates=[i for i,x in enumerate(new) if i not in used]
  same=[i for i in candidates if re.sub(r'\s+','',new[i][2])==re.sub(r'\s+','',s)]
  if same:i=same[0];exact+=1
  elif candidates:
   i=max(candidates,key=lambda i:difflib.SequenceMatcher(None,s,new[i][2]).ratio())
   ratio=difflib.SequenceMatcher(None,s,new[i][2]).ratio()
   if ratio<.6:missing+=1;diffs.append({'file':str(p.relative_to(RESULT)),'before':s,'after':None,'ratio':ratio});continue
   changed+=1;diffs.append({'file':str(p.relative_to(RESULT)),'before':s,'after':new[i][2],'position':new[i][0],'end':new[i][1],'ratio':ratio})
  else:missing+=1;diffs.append({'file':str(p.relative_to(RESULT)),'before':s,'after':None,'ratio':0});continue
  used.add(i)
 rows.append([str(p.relative_to(RESULT)),len(old),len(new),exact,changed,missing])
write_tsv(RESULT/'records/INHERITED_NOTE_AUDIT.tsv',['file','original_notes','current_notes','verbatim_retained','modified_candidates','unmatched_original_notes'],rows)
(RESULT/'records/INHERITED_NOTE_DIFFERENCES.json').write_text(json.dumps(diffs,ensure_ascii=False,indent=2))
print('Original',sum(x[1] for x in rows),'Current',sum(x[2] for x in rows),'Exact',sum(x[3] for x in rows),'Changed',sum(x[4] for x in rows),'Missing',sum(x[5] for x in rows))
for i,r in enumerate(diffs):print(i,r['file'],round(r['ratio'],3),'BEFORE',r['before'][:200],'AFTER',(r['after'] or '')[:200])

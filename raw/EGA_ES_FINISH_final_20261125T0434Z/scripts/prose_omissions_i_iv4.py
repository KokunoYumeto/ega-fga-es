"""Read-only prose omission screen, independent of root mutation journals."""
import re,json,difflib,collections,hashlib,argparse
from corpus import RESULT,FR,write_tsv
from root_scope_pairs import pairs,scoped_units,resolve
from audit_i_ch1 import mask_notes
from tex_tools import math_spans,math_loose_key,balanced_end
ap=argparse.ArgumentParser();ap.add_argument('--secondary',action='store_true');args=ap.parse_args()
prefix='PROSE_I_IV4_SECONDARY' if args.secondary else 'PROSE_I_IV4'

def clean(t):
 t=mask_notes(t)
 for m in reversed(math_spans(t)):t=t[:m.start]+' '+t[m.end:]
 t=re.sub(r'(?<!\\)%[^\n]*',' ',t)
 # Omit structural/code arguments, retain natural-language formatting content.
 pat=re.compile(r'\\(?:label|tag|sref|eqref|eref|ref|cite|url|input|include|oldpage|EGAReaderTarget|hypertarget|hyperref|href)(?:\[[^]]*\])?\{')
 edits=[]
 for m in pat.finditer(t):
  e=balanced_end(t,m.end()-1)
  if m[0].startswith(('\\EGAReaderTarget','\\hypertarget')) and e<len(t) and t[e]=='{':e=balanced_end(t,e)
  edits.append((m.start(),e))
 for a,b in reversed(edits):t=t[:a]+' '*(b-a)+t[b:]
 t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?',' ',t)
 t=re.sub(r'\\item(?:\[[^]]*\])?',' ',t)
 t=re.sub(r'\\[A-Za-z@]+\*?',' ',t)
 t=re.sub(r'\\[^\w\s]',' ',t)
 return t
def words(t):return re.findall(r'[^\W\d_]+(?:[-’\x27][^\W\d_]+)*',clean(t),re.UNICODE)

candidates=[];unit_candidates=[];stats=[];missing=[];alignstats=[];snapshots={}
for scope,ed,fp,ft,st,p,offset,fn in pairs():
 if scope not in {'I','IV4'}:continue
 fu=scoped_units(ft,fn);su=scoped_units(st,fn);src=str(fp.relative_to(FR.parent));paircount=0;pairgaps=0
 for n,f in fu.items():
  if n not in su:missing.append([scope,ed,src,n]);continue
  s=su[n];fm=math_spans(mask_notes(f.text));sm=math_spans(mask_notes(s.text));nf=len(words(f.text));ns=len(words(s.text))
  fkeys=[math_loose_key(x.text) for x in fm];skeys=[math_loose_key(x.text) for x in sm]
  matches=[]
  for block in difflib.SequenceMatcher(None,fkeys,skeys,autojunk=False).get_matching_blocks():
   matches.extend((block.a+i,block.b+i) for i in range(block.size))
  anchors=[(-1,-1)]+matches+[(len(fm),len(sm))]
  gapcount=0
  for (i,j),(k,l) in zip(anchors,anchors[1:]):
   a=fm[i].end if i>=0 else 0;b=fm[k].start if k<len(fm) else len(f.text)
   c=sm[j].end if j>=0 else 0;d=sm[l].start if l<len(sm) else len(s.text)
   fg=f.text[a:b];sg=s.text[c:d];fw=words(fg);sw=words(sg);gapcount+=1
   # Main request thresholds, plus a modest second tier for a nearly empty gap.
   if not ((len(fw)>=15 and len(sw)<0.65*len(fw)) if args.secondary else (len(fw)>=20 and len(sw)<0.50*len(fw) or len(fw)>=12 and len(sw)<=3)):continue
   path,local=resolve(st,s.start+c,p,offset)
   endpath,endlocal=resolve(st,max(s.start+c,s.start+d-1),p,offset)
   row={'id':len(candidates),'scope':scope,'edition':ed,'source':src,'place':n,'anchor_indices':[i,k,j,l],'french_words':len(fw),'spanish_words':len(sw),'ratio':round(len(sw)/len(fw),4),'source_offset':f.start+a,'source_line':ft.count('\n',0,f.start+a)+1,'file':str(path.relative_to(RESULT)),'target_offset':local,'target_line':path.read_text().count('\n',0,local)+1,'same_file':path==endpath,'target_end':endlocal+1 if path==endpath else None,'french':fg,'spanish':sg,'french_context':f.text[max(0,a-160):min(len(f.text),b+160)],'spanish_context':s.text[max(0,c-160):min(len(s.text),d+160)],'french_clean':' '.join(fw),'spanish_clean':' '.join(sw)}
   candidates.append(row)
  if nf>=40 and ns<0.70*nf:
   path,local=resolve(st,s.start,p,offset)
   unit_candidates.append({'id':len(unit_candidates),'scope':scope,'edition':ed,'source':src,'place':n,'french_words':nf,'spanish_words':ns,'ratio':round(ns/nf,4),'file':str(path.relative_to(RESULT)),'french':f.text,'spanish':s.text})
  stats.append([scope,ed,src,n,nf,ns,round(ns/nf,4) if nf else '',len(fm),len(sm),len(matches),gapcount])
  paircount+=len(matches);pairgaps+=gapcount
 alignstats.append([scope,ed,src,len(fu),paircount,pairgaps])
 snapshots[src]=hashlib.sha256(ft.encode()).hexdigest()
for name,obj in [(prefix+'_CANDIDATES.json',candidates),(prefix+'_UNIT_CANDIDATES.json',unit_candidates),(prefix+'_SOURCE_HASHES.json',snapshots)]:
 (RESULT/'records'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
write_tsv(RESULT/('records/'+prefix+'_ALL_UNITS.tsv'),['scope','edition','source','place','french_prose_words','spanish_prose_words','ratio','french_math','spanish_math','matched_math','examined_intervals'],stats)
write_tsv(RESULT/('records/'+prefix+'_PAIR_SUMMARY.tsv'),['scope','edition','source','units','matched_math','examined_intervals'],alignstats)
write_tsv(RESULT/('records/'+prefix+'_MISSING_UNITS.tsv'),['scope','edition','source','place'],missing)
print(json.dumps({'units':len(stats),'intervals':sum(r[-1] for r in stats),'matched_math':sum(r[-2] for r in stats),'candidates':len(candidates),'unit_candidates':len(unit_candidates),'missing_units':len(missing),'candidate_scopes':dict(collections.Counter((r['scope']+':'+r['edition']) for r in candidates))}))
for r in candidates:print(r['id'],r['scope'],r['edition'],r['place'],r['french_words'],r['spanish_words'],'FR',r['french_clean'],'ES',r['spanish_clean'])
print('WHOLE UNITS',[(r['id'],r['scope'],r['edition'],r['place'],r['french_words'],r['spanish_words']) for r in unit_candidates])

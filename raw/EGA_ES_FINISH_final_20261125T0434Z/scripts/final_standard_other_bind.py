"""Bind final OTHER terminology candidates to source intervals, read-only corpus."""
import re,json,difflib,collections,hashlib,bisect
from corpus import RESULT,FR
from root_scope_pairs import pairs,scoped_units
from audit_i_ch1 import mask_notes
from tex_tools import math_spans,math_loose_key,prose_segments

path=RESULT/'records/FINAL_STANDARD_OTHER_CONTEXTS.json'
rows=json.loads(path.read_text())
byfile=collections.defaultdict(list)
for r in rows:byfile[r['file']].append(r)
for f,rr in byfile.items():
 t=(RESULT/f).read_text();hits=[]
 for a,b,s in prose_segments(t):
  for m in re.finditer(r'\b(?:fibras?|entornos?|(?:co)?filtrad[oa]s?)\b',s,re.I):
   p=a+m.start();e=a+m.end();hits.append((p,e,m[0],t[max(0,p-180):min(len(t),e+260)].replace('\n',' ')))
 for r in rr:
  hh=[h for h in hits if h[2]==r['form'] and h[3]==r['context']]
  assert len(hh)==1,(r['queue_id'],f,len(hh),'stale/ambiguous queue')
  a,b,_,_=hh[0];r['offset']=a;r['end']=b;r['file_sha256']=hashlib.sha256(t.encode()).hexdigest()

stats=collections.Counter();done=set()
for scope,edition,fp,ft,st,p,offset,fn in pairs():
 if scope in {'I','IV4'}:continue
 if p is not None:
  files={str(p.relative_to(RESULT)):(0,len(st),-offset)}
 else:
  files={}
  for m in re.finditer(r'(?m)^% BEGIN (tree/[^\n]+)\n',st):
   end=st.find('% END '+m[1],m.end());assert end>=0
   files[m[1]]=(m.end(),end,m.end())
 relevant=[]
 for f,(lo,hi,base) in files.items():
  for r in byfile.get(f,[]):
   pos=r['offset']+base
   if lo<=pos<hi and r['queue_id'] not in done:relevant.append((r,pos))
 if not relevant:continue
 su=scoped_units(st,fn);fu=scoped_units(ft,fn)
 for key,s in su.items():
  rr=[(r,pos) for r,pos in relevant if s.start<=pos<s.end]
  if not rr:continue
  if key not in fu:
   for r,pos in rr:r['binding_error']='missing source unit '+key
   continue
  f=fu[key];fm=math_spans(mask_notes(f.text));sm=math_spans(mask_notes(s.text))
  eq=[]
  for block in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in fm],[math_loose_key(x.text) for x in sm],autojunk=False).get_matching_blocks():
   eq.extend((block.a+i,block.b+i) for i in range(block.size))
  anchors=[(-1,-1)]+eq+[(len(fm),len(sm))]
  for r,pos in rr:
   pp=pos-s.start
   for (i,j),(k,l) in zip(anchors,anchors[1:]):
    c=sm[j].end if j>=0 else 0;d=sm[l].start if l<len(sm) else len(s.text)
    if not c<=pp<d:continue
    a=fm[i].end if i>=0 else 0;b=fm[k].start if k<len(fm) else len(f.text)
    src=str(fp.relative_to(FR.parent.parent));fg=f.text[a:b];sg=s.text[c:d]
    pat={'es-stalk':r'\bfibres?\b','es-filtrant':r'\bfiltr[ée]s?\b','es-voisinage':r'\bvoisinages?\b'}[r['row']]
    terms=list(re.finditer(pat,fg,re.I))
    snippets=[]
    for m in terms:
     abspos=f.start+a+m.start()
     snippets.append({'file':src,'anchor':key,'term':m[0],'context':re.sub(r'\s+',' ',ft[max(0,abspos-120):min(len(ft),f.start+a+m.end()+220)]),'source_line':ft.count('\n',0,abspos)+1,'offset':abspos})
    r['fresh_source']={'file':src,'unit':key,'edition':edition,'scope':scope,'source_offset':f.start+a,'source_line':ft.count('\n',0,f.start+a)+1,'french_gap':fg,'spanish_gap':sg,'snippets':snippets,'math_anchors':[i,k,j,l]}
    done.add(r['queue_id']);stats[scope]+=1
    break

path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
missing=[r['queue_id'] for r in rows if not r.get('fresh_source')]
no_terms=[r['queue_id'] for r in rows if r.get('fresh_source') and not r['fresh_source']['snippets']]
print(json.dumps({'bound':sum(stats.values()),'by_scope':dict(stats),'without_pair':missing,'without_french_term_in_gap':no_terms}))

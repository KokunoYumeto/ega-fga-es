"""Locate inherited source page markers between corresponding source formulas."""
import re,json,difflib,collections
from corpus import RESULT,FR,write_tsv
from audit_i_ch1 import texts,i_units,mask_notes
from audit_iv4 import pairs
from tex_tools import numbered_units,math_spans,math_loose_key
PM=re.compile(r'\\oldpage(?:\[[^\]]*\])?\{([^}]+)\}')
def audit(scope,layer,fp,ft,st,unitfn):
 fu=unitfn(ft);su=unitfn(st);si={m[1]:m for m in PM.finditer(st)};out=[]
 for fm in PM.finditer(ft):
  sm=si.get(fm[1]);n=next((n for n,u in fu.items() if u.start<=fm.start()<u.end),None)
  if sm is None:out.append({'scope':scope,'layer':layer,'source':str(fp.relative_to(FR/layer)),'page':fm[1],'status':'missing','fr_context':ft[max(0,fm.start()-140):fm.end()+140]});continue
  sn=next((n for n,u in su.items() if u.start<=sm.start()<u.end),None)
  if n is None or n not in su:continue
  f,s=fu[n],su[n];ff=math_spans(mask_notes(f.text));ss=math_spans(mask_notes(s.text));pairs=[]
  for bl in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_matching_blocks():
   pairs.extend((bl.a+i,bl.b+i) for i in range(bl.size))
  pre=[(a,b) for a,b in pairs if f.start+ff[a].end<=fm.start()];post=[(a,b) for a,b in pairs if f.start+ff[a].start>=fm.end()]
  lo=s.start+(ss[pre[-1][1]].end if pre else 0);hi=s.start+(ss[post[0][1]].start if post else len(s.text));ok=lo<=sm.start()<=hi
  out.append({'scope':scope,'layer':layer,'source':str(fp.relative_to(FR/layer)),'page':fm[1],'unit':n,'es_unit':sn,'status':'same_formula_interval' if ok else 'review','fr_context':ft[max(0,fm.start()-120):fm.end()+140],'es_context':st[max(0,sm.start()-120):sm.end()+140],'expected_es_interval':st[lo:hi],'lo':lo,'hi':hi})
 return out
rows=[]
for ed in ['current','diplomatic']:
 p,st=texts(ed.upper())
 for fp in sorted((FR/ed/'BASE/native/ega1').glob('ega1-*-fr.tex')):rows+=audit('I',ed,fp,fp.read_text(),st,i_units)
for fp,ft,st in pairs():rows+=audit('IV4','current',fp,ft,st,numbered_units)
(RESULT/'records/ROOT_PAGE_POSITION_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
write_tsv(RESULT/'records/ROOT_PAGE_POSITION_AUDIT.tsv',['scope','edition','source','page','unit','status'],[[r['scope'],r['layer'],r['source'],r['page'],r.get('unit','prelude'),r['status']] for r in rows])
print(len(rows),collections.Counter(r['status'] for r in rows))
for i,r in enumerate(rows):
 if r['status']!='same_formula_interval' and r['layer']=='current':print(i,r['scope'],r['page'],r.get('unit'),r.get('es_unit'),'FR',re.sub(r'\s+',' ',r['fr_context']),'ES',re.sub(r'\s+',' ',r.get('es_context','')),'TARGET',re.sub(r'\s+',' ',r.get('expected_es_interval',''))[:360])

"""Read-only source-bound final audit for IV3."""
import re,json,difflib,collections
from iv3_align import pairs,units,key
from iv3_core import spans
from corpus import RESULT,canonical,FR
from iv3_work import DIR
from tex_tools import math_spans,balanced_end
from audit_i_ch1 import mask_notes
PM=re.compile(r'\\oldpage(?:\[[^\]]*\])?\{([^}]+)\}')
AM=re.compile(r'\\(?:label|EGAReaderTarget)\{([^}]+)\}(?:\{([^}]+)\})?')
RM=re.compile(r'\\sref(?:\[([^]]*)\])?\{([^}]+)\}')
TP=re.compile(r'\\(text|textup|textnormal|textrm|textbf|mbox|hbox)\{')
pages=[];anchors=[];refs=[];textargs=[]
for fp,q in pairs():
 if q.name=='ega4-8.tex':continue
 ft=fp.read_text();st=q.read_text();fu=units(ft);su=units(st)
 if 'terminal' in fp.name:st+='\n'+(DIR/'backmatter-es.tex').read_text()
 # Reader aliases permit canonical -fr/-es marker variants, but require every key.
 fa=[canonical(m[2] if m.group().startswith('\\EGAReaderTarget') else m[1]) for m in AM.finditer(ft)]
 sa=[canonical(m[2] if m.group().startswith('\\EGAReaderTarget') else m[1]) for m in AM.finditer(st)]
 anchors.append(dict(source=fp.name,source_count=len(fa),spanish_count=len(sa),missing=list((collections.Counter(fa)-collections.Counter(sa)).elements())))
 si={m[1]:m for m in PM.finditer(st)}
 for fm in PM.finditer(ft):
  sm=si.get(fm[1]);n=next((n for n,u in fu.items() if u.start<=fm.start()<u.end),None)
  row=dict(source=fp.name,page=fm[1],place=n,status='present',fr_context=ft[max(0,fm.start()-120):fm.end()+140])
  if sm is None:row['status']='missing'
  elif n in su:
   f,s=fu[n],su[n];ff=spans(f.text);ss=spans(s.text);links=[]
   for bl in difflib.SequenceMatcher(None,[key(x.text) for x in ff],[key(x.text) for x in ss],autojunk=False).get_matching_blocks():links.extend((bl.a+i,bl.b+i) for i in range(bl.size))
   pre=[(a,b) for a,b in links if f.start+ff[a].end<=fm.start()];post=[(a,b) for a,b in links if f.start+ff[a].start>=fm.end()]
   lo=s.start+(ss[pre[-1][1]].end if pre else 0);hi=s.start+(ss[post[0][1]].start if post else len(s.text))
   row.update(status='same_formula_interval' if lo<=sm.start()<=hi else 'review',lo=lo,hi=hi,expected=st[lo:hi])
  if sm:row['es_context']=st[max(0,sm.start()-120):sm.end()+140]
  pages.append(row)
 for n,f in fu.items():
  if n not in su or (n=='front' and 'terminal' in fp.name):continue
  s=su[n];ff=spans(f.text);ss=spans(s.text)
  for bl in difflib.SequenceMatcher(None,[key(x.text) for x in ff],[key(x.text) for x in ss],autojunk=False).get_matching_blocks():
   for i in range(bl.size):
    a,b=ff[bl.a+i],ss[bl.b+i]
    if TP.search(a.text) or TP.search(b.text):
     def args(t):
      return [(m[1],t[m.end():balanced_end(t,m.end()-1)-1]) for m in TP.finditer(t)]
     textargs.append(dict(source=fp.name,file=str(q.relative_to(RESULT)),place=n,fr=a.text,es=b.text,fr_args=args(a.text),es_args=args(b.text)))
  fm=mask_notes(f.text)
  fm=re.sub(r'\\(?:label|EGAReaderTarget|tag)\{[^}]+\}(?:\{[^}]+\})?',lambda m:' '*len(m.group()),fm)
  for m in RM.finditer(mask_notes(s.text)):
   raw=m[2];k=canonical(raw);num=re.sub(r'^.*?(?:I{1,3}|IV|0)\.', '',k)
   if not re.fullmatch(r'\d+(?:\.\d+)+',num):continue
   hits=list(re.finditer(r'(?<![\d.])'+re.escape(num)+r'(?![\d.])',fm))
   chapter=k.split('.')[0];contexts=[fm[max(0,h.start()-70):h.end()+40] for h in hits]
   refs.append(dict(source=fp.name,file=str(q.relative_to(RESULT)),place=n,macro=m.group(),target=k,number=num,chapter=chapter,source_hits=len(hits),fr_contexts=contexts,es_context=s.text[max(0,m.start()-90):m.end()+70]))
for name,rows in [('PAGES',pages),('ANCHORS',anchors),('REFERENCES',refs),('MATH_TEXT',textargs)]:
 (RESULT/f'records/IV3_FINAL_{name}_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('pages',collections.Counter(r['status'] for r in pages),'anchors',anchors,'math text',len(textargs),'references',len(refs))
for i,r in enumerate(pages):
 if r['status'] not in ['same_formula_interval','present']:print('PAGE',i,r)
print('EXTERNAL REFERENCE CANDIDATES')
for i,r in enumerate(refs):
 if r['chapter']=='IV' or r['chapter']=='0':continue
 explicit=[re.search(r'\\(?:textbf|mathbf)\s*(?:\{'+r['chapter']+r'\}|'+r['chapter']+r'(?![IV]))',c) for c in r['fr_contexts']]
 if any(explicit):continue
 print(i,r)

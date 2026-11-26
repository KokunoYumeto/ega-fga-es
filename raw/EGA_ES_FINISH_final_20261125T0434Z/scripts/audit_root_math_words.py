"""Inventory source/Spanish text-bearing formulas, including embedded math in text."""
import re,json,collections
from corpus import FR,RESULT
from audit_i_ch1 import texts,i_units,mask_notes
from audit_iv4 import pairs as v4pairs
from tex_tools import numbered_units,math_spans,math_loose_key,balanced_end
pairs=[]
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);su=i_units(t)
 for fp in (FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex'):
  for n,u in i_units(fp.read_text()).items():pairs.append((layer,str(p.relative_to(RESULT)),n,u.text,su[n].text))
for fp,ft,st in v4pairs():
 fu=numbered_units(ft);su=numbered_units(st)
 for n,u in fu.items():pairs.append(('IV4',fp.name,n,u.text,su[n].text))
rows=[]
for layer,p,n,ft,st in pairs:
 ff=math_spans(mask_notes(ft));ss=math_spans(mask_notes(st));index=collections.defaultdict(list)
 for s in ss:index[math_loose_key(s.text)].append(s)
 for f in ff:
  c=index[math_loose_key(f.text)]
  if not c:continue
  s=c.pop(0);fa=[];sa=[]
  for text,arr in [(f.text,fa),(s.text,sa)]:
   for m in re.finditer(r'\\(text|textup|textnormal|textrm|mbox|hbox)\s*\{',text):
    b=balanced_end(text,m.end()-1);arr.append(text[m.end():b-1])
  if fa or sa:rows.append({'layer':layer,'file':p,'place':n,'fr':fa,'es':sa,'fr_formula':f.text,'es_formula':s.text})
(RESULT/'records/ROOT_MATH_TEXT_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('text bearing formulas',len(rows))
for i,r in enumerate(rows):
 if r['layer']=='DIPLOMATIC':continue
 print(i,r['layer'],r['place'],r['fr'],'=>',r['es'])

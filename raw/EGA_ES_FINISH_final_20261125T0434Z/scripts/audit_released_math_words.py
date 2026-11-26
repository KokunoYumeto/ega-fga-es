"""Strong source-text-argument inventory for the released translated scopes."""
import re,json,collections
from corpus import FR,ES,RESULT
from audit_i_ch1 import mask_notes
from tex_tools import numbered_units,math_spans,math_loose_key,balanced_end
pairs=[]
for layer in ['CURRENT','DIPLOMATIC']:
 d=ES/f'worktree/es/{layer}/EGA_I_ch0'
 files=sorted(d.glob('ega0_i_*.tex'),key=lambda p:[int(x) for x in re.findall(r'\d+',p.stem)])
 st='\n'.join(p.read_text() for p in files);pairs.append(('I0',layer,FR/layer.lower()/'BASE/native/ega1/ega0-1-fr.tex',st))
 for f in (FR/layer.lower()/'IV1/native/ega4').glob('ega0-*-fr.tex'):
  p=ES/f'worktree/es/PORTED_20261109/IV1_{layer}/ega4'/f.name.replace('-fr.tex','-es.tex');pairs.append(('IV1_0',layer,f,p.read_text()))
 for scope,src,orderfile in [('IV1_1','IV1/native/ega4/ega4-1-fr.tex','IV1_CH4_INPUT_ORDER.json'),('IV2','IV2/native/ega4/ega4-2-fr.tex','IV2_INPUT_ORDER.json')]:
  order=json.load(open(RESULT/'records'/orderfile));order=order if isinstance(order,list) else order[layer]
  st='\n'.join((RESULT/x).read_text() for x in order);pairs.append((scope,layer,FR/layer.lower()/src,st))
rows=[];unmatched=[]
for scope,layer,f,st in pairs:
 ft=f.read_text();fu=numbered_units(ft);su=numbered_units(st)
 for n,u in fu.items():
  if n not in su:continue
  ff=math_spans(mask_notes(u.text));ss=math_spans(mask_notes(su[n].text));index=collections.defaultdict(list)
  for s in ss:index[math_loose_key(s.text)].append(s)
  for fspan in ff:
   c=index[math_loose_key(fspan.text)]
   if not c:
    if re.search(r'\\(?:text|textup|textnormal|textrm|mbox|hbox)\s*\{',fspan.text):unmatched.append([scope,layer,n,fspan.text])
    continue
   s=c.pop(0);fa=[];sa=[]
   for text,arr in [(fspan.text,fa),(s.text,sa)]:
    for m in re.finditer(r'\\(text|textup|textnormal|textrm|mbox|hbox)\s*\{',text):
     b=balanced_end(text,m.end()-1);arr.append(text[m.end():b-1])
   if fa or sa:rows.append({'scope':scope,'layer':layer,'source':str(f.relative_to(FR/layer.lower())),'place':n,'fr':fa,'es':sa,'fr_formula':fspan.text,'es_formula':s.text})
(RESULT/'records/RELEASED_MATH_TEXT_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(RESULT/'records/RELEASED_MATH_TEXT_UNMATCHED.json').write_text(json.dumps(unmatched,ensure_ascii=False,indent=2))
print('text-bearing matched',len(rows),'unmatched',len(unmatched))
for i,r in enumerate(rows):
 if r['layer']=='CURRENT':print(i,r['scope'],r['place'],r['fr'],'=>',r['es'])
for x in unmatched:print('UNMATCHED',x)

"""Generate source-bounded clauses for every remaining first-plural form."""
import re,json,collections
from corpus import RESULT
from iv3_align import pairs,units
import register_review as rr
from register_root_other import IMP
from register_forms import BASE
rr.PAT=re.compile(r'\b(?:nos\s+)?[^\W\d_]{2,}mos\b',re.I)
IGNORE={'mismos','últimos','extremos','primos','ramos','máximos','mínimos','supremos','ínfimos','logaritmos','algoritmos','ritmos','óptimos'}
rows=[]
for fp,q in pairs():
 if q.name=='ega4-8.tex':continue
 ft=fp.read_text();st=q.read_text();su=units(st)
 for n,f in units(ft).items():
  if n=='front' and 'terminal' in fp.name:continue
  if n not in su:continue
  u=su[n]
  for a,b,word,fc,sc in rr.contexts(f.text,u.text):
   w=word.lower()
   if w.endswith('morfismos') or w in IGNORE:continue
   pure=bool(re.search(r'\bon\b',fc,re.I) and not re.search(IMP,fc,re.I) and len(fc)<800)
   rows.append({'id':len(rows),'file':str(q.relative_to(RESULT)),'source':fp.name,'place':n,'before':word,'position':u.start+a,'end':u.start+b,'fr':fc,'es':sc,'prefix':u.text[max(0,a-100):a],'suffix':u.text[b:min(len(u.text),b+150)],'pure_on':pure,'suggested':BASE.get(w) if pure else None})
(RESULT/'records/IV3_REGISTER_9_15_BROAD_REVIEW.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),dict(collections.Counter((x['source'],x['pure_on']) for x in rows)))
print('Pure forms',dict(collections.Counter(x['before'].lower() for x in rows if x['pure_on'])))
for x in rows:
 if x['pure_on']:
  print(x['id'],x['place'],x['before'],'FR',re.sub(r'\s+',' ',x['fr'])[:310],'ES',re.sub(r'\s+',' ',x['es'])[:230])


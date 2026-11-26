"""Mixed and imperative register clauses read individually after source-on pass."""
import json,re,collections
from corpus import RESULT,write_tsv
from audit_i_ch1 import i_units
from tex_tools import numbered_units,math_spans
R=json.loads((RESULT.parent/'tmp/register_review.json').read_text())
M={3:'Notemos',8:'Demostremos',13:'Ahora bien,',14:'Ahora bien,',15:'apliquemos',17:'pongamos',19:'denotémoslo',33:'pongamos',38:'Notemos',39:'Supongamos',40:'Observemos',41:'supongamos',42:'supongamos',44:'consideremos',45:'Ahora bien,',46:'',47:'Demostremos',48:'es necesario',50:'consideremos',51:'Supongamos',52:'mostremos',53:'consideremos',69:'probemos',72:'demostremos',73:'se considera',75:'Demostremos',76:'se pone',78:'denotemos',82:'demostremos',85:'definamos',91:'mostremos',186:'Notemos',192:'Notemos',196:'Notemos',201:'se puede',212:'se puede',213:'se puede',215:'se puede',218:'',222:'se puede',237:'denotando',238:'poniendo',242:'Notemos',243:'Consideremos',245:'Notemos',247:'se puede',248:'Notemos',249:'Notemos',252:'Notemos',256:'Notemos',257:'se puede',272:'Notemos'}
keys={(R[i]['scope'],R[i]['place'],R[i]['before'],R[i]['fr']):(i,n) for i,n in M.items()}
cache={};edits=collections.defaultdict(list);rows=[]
for r in R:
 key=(r['scope'],r['place'],r['before'],r['fr'])
 if key not in keys:continue
 idx,new=keys[key];p=RESULT/r['file']
 if p not in cache:
  t=p.read_text();cache[p]=(t,i_units(t) if r['scope']=='I' else numbered_units(t))
 t,units=cache[p];u=units[r['place']];a=r['unit_position'];b=r['unit_end'];assert u.text[a:b]==r['before']
 if idx in [13,14,45,46]:
  q=re.match(r'\s+que\s+',u.text[b:]);assert q;b+=q.end();new+=(' ' if new else '')
 if idx==19:
  cm=re.search(r'lo\s+$',u.text[:a]);assert cm;a=cm.start()
 if idx==218:
  cm=re.search(r'que\s+$',u.text[:a]);assert cm;a=cm.start()
  q=re.match(r'\s+',u.text[b:]);b+=q.end() if q else 0
 if idx==69:
  cm=re.search(r',\s+por\s+lo\s+que\s+$',u.text[:a]);assert cm;a=cm.start();new='; probemos'
 edits[p].append((u.start+a,u.start+b,new));rows.append([r['file'],r['place'],u.text[a:b],new,'standard','STANDARDS_20261119b.md register; '+r['source']+': '+r['place']+'; mixed/imperative source clause individually compared'])
for p,ee in edits.items():
 t=cache[p][0];original=t
 for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(original)]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_register_I_IV4_manual.tsv',['file','place','before','after','kind','source'],rows)
print('Manual register edits',len(rows))

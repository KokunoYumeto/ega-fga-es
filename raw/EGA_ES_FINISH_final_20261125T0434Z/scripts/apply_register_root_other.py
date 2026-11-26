"""Apply reviewed chapter-zero register choices, preserving all formula spans."""
import re,json,collections
from corpus import RESULT,write_tsv
from tex_tools import math_spans
R=json.loads((RESULT/'records/REGISTER_ROOT_OTHER_REVIEW.json').read_text())
manual={20:'se identificarán',39:'Se definen',84:'observemos',88:'Notemos',96:'notemos',101:'Se puede',131:'Se denotarán',140:'notemos',153:'Se dice',165:'se puede',172:'se tiene',175:'se consideran',188:'Se observará',199:'se puede'}
keys={(R[i]['scope'],R[i]['place'],R[i]['before'].lower(),R[i]['fr']):v for i,v in manual.items()}
edits=collections.defaultdict(list);logs=[]
for i,r in enumerate(R):
 new=keys.get((r['scope'],r['place'],r['before'].lower(),r['fr']),r['after'])
 r['after']=new;r['decision']='source impersonal or author imperative corrected' if new else 'explicit author nous/imperative retained'
 if not new:continue
 p=RESULT/r['file'];t=p.read_text();a=r['position'];b=r['end'];assert t[a:b]==r['before'],i
 if r['before'][0].isupper():new=new[0].upper()+new[1:]
 cm=re.search(r'\b(lo|la|los|las)\s+$',t[:a])
 if cm:a=cm.start();new=re.sub(r'^[Ss]e ',lambda m:m[0]+cm[1]+' ',new)
 edits[p].append((a,b,new));logs.append([r['file'],r['place'],t[a:b],new,'standard','STANDARDS_20261119b.md register; '+r['source']+': '+r['place']+' ('+r['layer']+')'])
 if r['before'].lower() in ['podemos','podremos','debemos']:
  tail=t[b:b+240];stop=re.search(r'[.!?;]\s',tail)
  if stop:tail=tail[:stop.start()]
  rm=re.search(r'\b(reducir|limitar|restringir|referir|remitir|contentar|servir|valer|atener)nos\b',tail)
  if rm:
   edits[p].append((b+rm.start(),b+rm.end(),rm[1]));logs.append([r['file'],r['place'],rm[0],rm[1],'standard','STANDARDS_20261119b.md register; clitic concordance'])
for p,ee in edits.items():
 t=p.read_text();old=t
 for i,(a,b,new) in enumerate(sorted(set(ee),reverse=True)):
  t=t[:a]+new+t[b:]
 assert [x.text for x in math_spans(t)]==[x.text for x in math_spans(old)]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_register_root_other.tsv',['file','place','before','after','kind','source'],logs)
(RESULT/'records/REGISTER_ROOT_OTHER_REVIEW.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('register edits',len(logs),'files',len(edits))

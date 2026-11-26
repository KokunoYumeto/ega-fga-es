"""Review wider Spanish first-plural forms against source-bound French clauses."""
import re,json,collections,contextlib
from corpus import RESULT,write_tsv
from audit_i_ch1 import i_units
from tex_tools import numbered_units,math_spans
from register_root_other import IMP
import register_review as rr
# Re-index after restored source anchors, retaining the same prose candidate order.
rr.PAT=re.compile(r'\b(?:nos\s+)?[^\W\d_]{2,}mos\b',re.I)
with open(RESULT.parent/'tmp/register_broad_refresh.txt','w') as f,contextlib.redirect_stdout(f):rr.main()
R=json.loads((RESULT.parent/'tmp/register_review.json').read_text())
(RESULT/'records/REGISTER_BROAD_I_IV4_REVIEW.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
BASE={'recuperamos':'se recupera','observemos':'se observará','hemos':'se ha','supongamos':'se supone','hablemos':'se hable','dotamos':'se dota','asociamos':'se asocia','sustituimos':'se sustituye','habíamos':'se había','señalemos':'se observará','quedamos':'se reduce','denotemos':'se denota','pongamos':'se pone','recordemos':'se recuerda','estamos':'se está','construimos':'se construye','comenzamos':'se comienza','acabamos':'se acaba','convenimos':'se conviene','respondemos':'se responde','formamos':'se forma','seguimos':'se sigue','seguiremos':'se sigue','comenzaremos':'se comenzará','tomemos':'se toma','consideremos':'se considera','formemos':'se forma','habremos':'se habrá','localizamos':'se localiza','vimos':'se ha visto','razonamos':'se razona','responderemos':'se responderá','fijamos':'se dejan fijos','vamos':'se va'}
IGNORE={'mismos','últimos','extremos','primos','ramos','máximos','mínimos','supremos','ínfimos','logaritmos','algoritmos'}
# Source clauses reviewed explicitly; these contain another author imperative.
EXCLUDE={('I_IV4',2025),('OTHER',498),('OTHER',1032)}
OVERRIDES={('I_IV4',45):'se han',('I_IV4',620):'Se suponen',('I_IV4',1658):'se forman',('I_IV4',2125):'se denotan',('I_IV4',2128):'se denotan',('I_IV4',2454):'se acaban',('I_IV4',2471):'se acaban',('OTHER',889):'Se suponen',('OTHER',911):'Se consideran'}
edits=collections.defaultdict(list);logs=[];reviews=[]
for scope,rows in [('I_IV4',R),('OTHER',json.loads((RESULT/'records/REGISTER_BROAD_OTHER_REVIEW.json').read_text()))]:
 manualkeys={(rows[i]['scope'],rows[i]['place'],rows[i]['before'].lower(),rows[i]['fr']):v for (sc,i),v in OVERRIDES.items() if sc==scope}
 exkeys={(rows[i]['scope'],rows[i]['place'],rows[i]['before'].lower(),rows[i]['fr']) for sc,i in EXCLUDE if sc==scope}
 for i,r in enumerate(rows):
  w=r['before'].lower();key=(r['scope'],r['place'],w,r['fr']);new=None
  if w.endswith('morfismos') or w in IGNORE:continue
  pure=re.search(r'\bon\b',r['fr'],re.I) and not re.search(IMP,r['fr'],re.I) and len(r['fr'])<800
  if pure and key not in exkeys:
   new=manualkeys.get(key,BASE.get(w));assert new is not None,(scope,i,w)
  reviews.append([scope,str(i),r['file'],r['place'],r['before'],new or '',re.sub(r'\s+',' ',r['fr'])])
  if not new:continue
  p=RESULT/r['file'];t=p.read_text()
  if scope=='I_IV4':
   u=(i_units(t) if r['scope']=='I' else numbered_units(t))[r['place']];a=u.start+r['unit_position'];b=u.start+r['unit_end']
  else:a=r['position'];b=r['end']
  assert t[a:b]==r['before'],(scope,i)
  if w=='quedamos':
   m=re.match(r'((?:\s+así|,\s+por\s+tanto,)?\s+)reducidos\b',t[b:]);assert m,(scope,i,t[b:b+60]);b+=m.end();extra=m[1].strip();new='se reduce'+(' '+extra if extra else '')
  if w=='fijamos' and t[b:b+2]==' $':pass
  if r['before'][0].isupper():new=new[0].upper()+new[1:]
  edits[p].append((a,b,new));logs.append([r['file'],r['place'],t[a:b],new,'standard','STANDARDS_20261119b.md register; '+r['source']+' '+r['place']+' '+r['layer']])
for p,ee in edits.items():
 t=p.read_text();old=t;ee=sorted(set(ee),reverse=True)
 for j,(a,b,new) in enumerate(ee):
  assert not j or b<=ee[j-1][0]
  t=t[:a]+new+t[b:]
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(old)]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_register_broad_root.tsv',['file','place','before','after','kind','source'],logs)
write_tsv(RESULT/'records/REGISTER_BROAD_REVIEW.tsv',['scope','id','file','place','before','after','french_context'],reviews)
print('broad register edits',len(logs),'reviewed verbal candidates',len(reviews))

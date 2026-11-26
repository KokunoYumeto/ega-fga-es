"""Locate French author plurals whose aligned Spanish clause has no first plural."""
import re,json,collections
from corpus import RESULT,FR
from root_scope_pairs import pairs,scoped_units,resolve
import register_review as rr
rr.PAT=re.compile(r'\b(?:nous|supposons|montrons|prouvons|démontrons|considérons|prenons|posons|notons|remarquons|rappelons|choisissons|utilisons|appliquons|définissons|désignons|écrivons|distinguons|cherchons|raisonnons|représentons|observons|voyons|examinons|traitons|admettons|appelons|gardons|reprenons|partons)\b',re.I)
IGNORE={'mismos','últimos','extremos','primos','ramos','máximos','mínimos','supremos','ínfimos','logaritmos','algoritmos'}
R=[]
for scope,ed,fp,ft,st,p,offset,fn in pairs():
 fu=scoped_units(ft,fn);su=scoped_units(st,fn)
 for n,f in fu.items():
  if n not in su:continue
  s=su[n]
  for a,b,w,sc,fc in rr.contexts(s.text,f.text):
   verbs=[x for x in re.findall(r'\b[^\W\d_]+mos\b',sc,re.I) if x.lower() not in IGNORE and not x.lower().endswith('morfismos')]
   if verbs or re.search(r'\bnuestro[s]?\b|\bnuestra[s]?\b|\bnosotros\b|\bnos\b',sc,re.I):continue
   R.append({'scope':scope,'edition':ed,'source':str(fp.relative_to(FR/ed)),'place':n,'french_word':w,'fr':fc,'es':sc,'french_position':a})
(RESULT/'records/ROOT_AUTHOR_VOICE_REVIEW.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('voice candidates',len(R),collections.Counter(r['scope'] for r in R))
for i,r in enumerate(R):
 if r['edition']=='current':print(i,r['scope'],r['place'],'FR',re.sub(r'\s+',' ',r['fr'])[:330],'ES',re.sub(r'\s+',' ',r['es'])[:500])

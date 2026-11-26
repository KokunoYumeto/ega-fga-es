"""Apply individually reviewed French/Spanish register clauses in IV3 §§9–15.

The review data retain source witnesses. Formula arrays are invariant here.
This is a language/source comparison, not verification of mathematical proofs.
"""
import collections,json,re
from corpus import RESULT
from register_forms import BASE
from iv3_work import apply_edits
from tex_tools import math_spans

P=RESULT/'records/IV3_REGISTER_9_15_BROAD_REVIEW.json'
R=RESULT/'records/IV3_REGISTER_9_15_BROAD_VERDICTS.json'
EXTRA={'hemos':'se ha','vimos':'se ha visto','supongamos':'se supone',
 'quedamos':'se reduce','pongamos':'se pone','consideremos':'se considera',
 'tomemos':'se toma','procedamos':'se procede','procedemos':'se procede',
 'acabamos':'se acaba','estamos':'se está','recuperamos':'se recupera',
 'estudiamos':'se estudia','daremos':'se dará','definamos':'se define',
 'recordemos':'se recuerda','nos limitaremos':'se limitará',
 'examinamos':'se examina','nos proponemos':'se propone',
 'distinguimos':'se distinguen','sustituimos':'se sustituyen',
 'exigimos':'se debe tener','observemos':'se observa',
 'tendríamos':'se deduciría'}
OVERRIDE={9:'se deduciría',26:'Se deducen',118:'se debe tener',
 163:'se consideran',164:'Se tomará entonces',166:'se pondrá',177:'Se pone entonces',
 220:'se tiene',247:'Se consideran',268:'Si se pone',353:'se señalará',
 440:'se señala',527:'Se tomará en efecto',528:'Se define',529:'Se dará',548:'se aplicará',
 624:'Se estudian',698:'se tienen',713:'se considera',751:'se limitará',
 787:'se examinan',789:'se estudian',791:'Se estudia',842:'se dará',869:'se está',
 896:'si se considera',985:'se distinguen',998:'se sustituyen',
 1057:'Se propone',1059:'se darán',1060:'Se verá',
 # Mixed source clauses: only the words corresponding to French on change.
 21:'se puede',99:'se sabe',112:'se examinan',113:'se recupera',114:'se establece',
 158:'se puede',273:'Utilicemos',483:'se puede',562:'se puede',574:'Se puede',
 701:'se puede',742:'se ve',871:'se esté',889:'Se señalará',946:'se ha',
 # Elliptic/continued clauses and neutral French soit; source witnesses reviewed.
 73:'sea',134:'Sean',171:'se puede',204:'Sea',205:'sea',301:'Sean',320:'sea',
 341:'suponer',384:'se considera',385:'se puede',493:'sean',512:'Sean',546:'Sea',
 570:'sea',588:'sean',617:'sea',633:'Sean',656:'sean',690:'se puede',767:'se puede',
 891:'suponer',905:'hay que',960:'sea',971:'se sigue',1004:'introduzcamos',
 1030:'se sigue',1038:'Procedamos',1039:'sea'}
for i in [412,416,438,582,611,626,852,882,897,923,930,933]:OVERRIDE[i]='se señalará'
RETAIN={505:'Envisageons is an explicit author imperative',506:'Passons is an explicit author imperative'}
PHRASES={
 57:('quedamos así reducidos','se reduce entonces'),
 70:('Lo hemos','Se lo ha'),
 119:('quedamos así reducidos','se ve que se reduce'),
 143:('podemos suponer que',r'\emph{se puede suponer que se ha tomado}'),
 183:('que acabamos de describir','como antes'),
 246:('Consideremos primero','Se consideran por una parte'),
 342:('podemos puede suponer','se puede suponer'),
 712:('Comencemos con','Se parte de'),
 761:('Estamos, pues, efectivamente reducidos','Se reduce, pues, efectivamente'),
 780:('Estamos, pues, reducidos','Se reduce, pues,'),
 782:('Disponemos ahora del','Ahora bien, se tiene el'),
 803:('Supongamos satisfechas','Se suponen satisfechas'),
 808:('Supongamos satisfechas','Se suponen satisfechas'),
 811:('Supongamos satisfechas','Se suponen satisfechas'),
 904:('quedamos reducidos','se ve que se reduce'),
 914:('nos hemos situado','se sitúa'),
 916:('nos hemos situado','se sitúa'),
 917:('nos hemos situado','se está situado'),
 1012:('acabamos de ver más arriba','se ha visto antes'),
 213:('; supongamos que',', tal que'),
 375:('Pongamos ahora','Pero sean'),
 533:('denotemos por','sea'),
 705:('Supongamos','Suponiendo'),
 934:('que damos a continuación','siguiente'),
}

def phrase_span(t,x,phrase):
 pattern=r'\s+'.join(map(re.escape,re.split(r'\s+',phrase)))
 hits=[m for m in re.finditer(pattern,t) if m.start()<=x['position']<m.end()]
 assert len(hits)==1,(x['id'],phrase,len(hits),t[x['position']-70:x['end']+100])
 return hits[0].span()

def run(apply=False):
 rows=json.loads(P.read_text()); edits=collections.defaultdict(list); verdicts=[]
 texts={x['file']:(RESULT/x['file']).read_text() for x in rows}
 for x in rows:
  i=x['id'];w=x['before'];lo=w.lower();t=texts[x['file']];a=x['position'];b=x['end']
  assert t[a:b]==w,(i,'stale register position')
  after=None;reason='French explicit author plural or imperative retained after context review'
  if x['pure_on'] and i not in RETAIN:
   after=BASE.get(lo,EXTRA.get(lo,OVERRIDE.get(i,PHRASES.get(i,(None,None))[1])));assert after is not None,(i,lo)
   reason='French on clause rendered impersonally after individual source review'
  if i in OVERRIDE:
   after=OVERRIDE[i];reason='Individually reviewed source syntax, tense, or number'
  if i in PHRASES:
   old,after=PHRASES[i];a,b=phrase_span(t,x,old)
   reason='Individually reviewed complete clause, with agreement and clitics'
  elif after is not None and lo=='quedamos':
   m=re.match(r'(\s+(?:así|por tanto|entonces))?\s+reducidos\b',t[b:]);assert m,(i,t[b:b+70])
   b+=m.end();after+=''+(m.group(1) or '')
  if after is not None:
   if t[a:a+1].isupper():after=after[0].upper()+after[1:]
   # Spanish object clitics precede the auxiliary, but follow impersonal se.
   if after.lower().startswith('se '):
    m=re.search(r'\b(lo|la|los|las)\s+$',t[max(0,a-12):a],re.I)
    if m:
     aa=max(0,a-12)+m.start();cl=t[aa:a].strip().lower()
     after=('Se ' if t[aa:aa+1].isupper() else 'se ')+cl+' '+after[3:]
     a=aa
   edits[x['file']].append((a,b,after,x['place'],x['source']))
  verdicts.append(dict(x,status=('applied' if apply else 'ready') if after is not None else 'retained author register',
    reason=RETAIN.get(i,reason),actual_before=t[a:b],actual_after=after))
 # Validate all files before writing the first one.
 final={}
 for file,ee in edits.items():
  before=texts[file];out=before;last=len(before)+1
  for a,b,v,place,src in sorted(ee,reverse=True):
   assert b<=last,(file,place,a,b,last);last=a;out=out[:a]+v+out[b:]
  assert [s.text for s in math_spans(before)]==[s.text for s in math_spans(out)],(file,'math array changed')
  final[file]=out
 if apply:
  # Section 15 spans two source files. Keep the true witness per atomic edit.
  from iv3_work import JOURNAL,save_rows
  oldrows=json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
  for file,ee in edits.items():
   (RESULT/file).write_text(final[file])
   for a,b,v,place,src in sorted(ee,reverse=True):
    oldrows.append({'file':file,'place':place,'before':texts[file][a:b],'after':v,'kind':'own comparison',
       'source':'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'+src+': '+place})
  save_rows(oldrows)
 R.write_text(json.dumps(verdicts,ensure_ascii=False,indent=2)+'\n')
 print(dict(collections.Counter(x['status'] for x in verdicts)))
 print('Math arrays invariant for',len(edits),'files;',sum(map(len,edits.values())),'edits')

if __name__=='__main__':
 import sys
 run('--apply' in sys.argv)

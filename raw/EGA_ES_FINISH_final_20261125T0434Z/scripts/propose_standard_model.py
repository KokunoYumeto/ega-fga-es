"""Reviewed model-pass terminology proposals; this script never edits corpus files."""
from pathlib import Path
import json,re,collections,bisect,sys,csv,hashlib
from corpus import RESULT,write_tsv
from tex_tools import prose_segments,math_spans

ROWS=json.loads((RESULT/'records/STANDARD_MODEL_BOUND.json').read_text())
STALKS={320,396,328,404,334,410,335,411,339,414,344,419,345,420,
478,556,484,562,485,563,486,564,493,571,685,716,920,
1268,1269,1277,1302,1320,1324,1332,1390}
DIRECTED={8,130,9,131,10,132,11,133,12,134,702,896,897,898,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,919,921,923,927,928,929}
FEM={'un':'una','el':'la','los':'las','unos':'unas','al':'a la','del':'de la',
     'todo':'toda','todos':'todas','este':'esta','estos':'estas','ese':'esa','esos':'esas',
     'aquel':'aquella','aquellos':'aquellas','otro':'otra','otros':'otras','algún':'alguna',
     'ningún':'ninguna','cierto':'cierta','ciertos':'ciertas','dicho':'dicha','dichos':'dichas',
     'buen':'buena','buenos':'buenas'}
ADJS='abierto cerrado retrocompacto cuasicompacto compacto noetheriano pequeño arbitrario conexo isomorfo ádico dado fijo elegido contenido requerido buscado único mismo respectivo nuevo afino tal'.split()
for w in ADJS:
 if w.endswith('o'): FEM[w]=w[:-1]+'a';FEM[w+'s']=w[:-1]+'as'
MASC={'la':'el','las':'los','una':'un','unas':'unos','cuya':'cuyo','cuyas':'cuyos','toda':'todo','todas':'todos','misma':'mismo','mismas':'mismos','esta':'este','estas':'estos','esa':'ese','esas':'esos','aquella':'aquel','aquellas':'aquellos'}
for w in 'nula isomorfa identificada canónica igual'.split():
 if w.endswith('a'):MASC[w]=w[:-1]+'o';MASC[w+'s']=w[:-1]+'os'
NEUTRAL={'afín','afines','formal','formales','principal','principales','irreducible','irreducibles','suficientemente','arbitrariamente','muy','más','menos','y','o','no','cada','cualquier','cualesquiera'}
SKIP={'suficientemente','arbitrariamente','muy','tal'}
FMT=re.compile(r'\\(?:emph|textup|textbf|textrm|textit|mathrm|upshape|rm|it|bf|mdseries|normalfont)\b\s*\{?')
def gap_allowed(s):
 s=FMT.sub('',s)
 return not s.strip(' \t\r\n{}~') and '\n\n' not in s

def case(new,old):return new[0].upper()+new[1:] if old[0].isupper() else new
files={r['file'] for r in ROWS};texts={f:(RESULT/f).read_text() for f in files}
file_tokens={}
for f,t in texts.items():
 mask=[' ']*len(t)
 for a,b,p in prose_segments(t): mask[a:b]=p
 masked=''.join(mask)
 masked=re.sub(r'\\[A-Za-z@]+',lambda m:' '*len(m.group()),masked)
 toks=list(re.finditer(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+',masked))
 file_tokens[f]=(toks,[m.start() for m in toks])

proposals=[]
for r in ROWS:
 f=r['file'];t=texts[f];a=r['start'];b=r['end'];old=t[a:b]
 assert old.lower()==r['form'].lower(),(r['id'],old,r['form'])
 edits=[]
 def add(a,b,new):
  if new!=t[a:b]:edits.append([a,b,new])
 if r['row']=='es-filtrant':
  change=r['id'] in DIRECTED
  if change:add(a,b,case('filtrante'+('s' if old.endswith('s') else ''),old))
 elif r['row']=='es-stalk':
  change=r['id'] in STALKS
  if change:add(a,b,case('tallo'+('s' if old.endswith('s') else ''),old))
 else:
  change=True;add(a,b,case('vecindad'+('es' if old.endswith('s') else ''),old))
 if change and r['row'] in ('es-voisinage','es-stalk'):
  toks,starts=file_tokens[f];i=bisect.bisect_left(starts,a)
  assert toks[i].start()==a
  mapping=FEM if r['row']=='es-voisinage' else MASC
  prev=a
  for j in range(i-1,max(-1,i-8),-1):
   m=toks[j];w=m.group().lower()
   if not gap_allowed(t[m.end():prev]):break
   if w in mapping:
    if r['row']=='es-stalk' and w=='la' and j>0 and toks[j-1].group().lower() in ('de','a') and t[toks[j-1].end():m.start()].isspace():
     prep=toks[j-1];add(prep.start(),m.end(),case('del' if prep.group().lower()=='de' else 'al',prep.group()))
    else:add(m.start(),m.end(),case(mapping[w],m.group()))
   elif w not in SKIP:break
   prev=m.start()
  prev=b
  for j in range(i+1,min(len(toks),i+10)):
   m=toks[j];w=m.group().lower()
   if not gap_allowed(t[prev:m.start()]):break
   if w in mapping and w not in {'un','el','los','unos','al','del','todo','todos','este','estos','ese','esos','aquel','aquellos','otro','otros','algún','ningún','cierto','ciertos','dicho','dichos','la','las','una','unas','cuya','cuyas'}:
    add(m.start(),m.end(),case(mapping[w],m.group()))
   elif w not in NEUTRAL:break
   prev=m.end()
 proposals.append({**r,'decision':'change' if change else 'retain','edits':edits})

# Explicit grammatical corrections follow a contextual reading. Values are
# literal source text and its replacement, resolved near the reviewed noun.
MANUAL={}
manual_path=RESULT/'records/STANDARD_MODEL_MANUAL.json'
if manual_path.exists():MANUAL=json.loads(manual_path.read_text())
for r in proposals:
 t=texts[r['file']]
 for correction in MANUAL.get(str(r['id']),[]):
  bef,aft=correction[:2];mode=correction[2] if len(correction)>2 else 'unique'
  lo=max(0,r['start']-450);hi=min(len(t),r['end']+650)
  hits=[m.start() for m in re.finditer(re.escape(bef),t[lo:hi])]
  if mode=='after':hits=[h for h in hits if lo+h>=r['end']];hits=hits[:1]
  if mode=='before':hits=[h for h in hits if lo+h+len(bef)<=r['start']];hits=hits[-1:]
  if len(hits)!=1:raise ValueError((r['id'],bef,len(hits)))
  a=lo+hits[0];b=a+len(bef)
  # Replace auto edits inside the explicit span; explicit changes carry the
  # full noun agreement where a larger phrase was necessary.
  r['edits']=[e for e in r['edits'] if e[1]<=a or e[0]>=b]
  r['edits'].append([a,b,aft])

(RESULT/'records/STANDARD_MODEL_PROPOSALS_DRAFT.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(proposals),'changes':dict(collections.Counter(r['row'] for r in proposals if r['decision']=='change')),'retained':dict(collections.Counter(r['row'] for r in proposals if r['decision']=='retain')),'manual':len(MANUAL)}))

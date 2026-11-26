import json,collections,re,sys
from pathlib import Path
from tex_tools import math_spans
xs=json.load(open('result/records/STANDARD_MODEL_PROPOSALS_DRAFT.json'));gs=collections.defaultdict(list)
for x in xs:
 if x['row']==sys.argv[1]:gs[x['context']].append(x)
def compact(s):
 return re.sub(r'\s+',' ',s)
for i,g in list(enumerate(gs.values()))[int(sys.argv[2]):int(sys.argv[3])]:
 r=g[0];t=(Path('result')/r['file']).read_text();a=r['start'];b=r['end'];lo=max(0,a-65);hi=min(len(t),b+220)
 c=t[lo:hi]
 for aa,bb,n in sorted(r['edits'],reverse=True):
  if lo<=aa and bb<=hi:c=c[:aa-lo]+n+c[bb-lo:]
 print(f"{i} / {','.join(str(x['id']) for x in g)} / {r['place']} E: {compact(c)}")
 fs=r['french'];
 if fs:
  # Show only one short excerpt per occurrence. Full aligned evidence remains
  # available in the JSON, including all occurrences in the source statement.
  z=fs[0];fc=z['context'];m=re.search((r'voisinages?' if sys.argv[1]=='es-voisinage' else r'fibr[ée]s?|filtr[a-zéè]+'),fc,re.I)
  print(' F: '+compact(fc[max(0,m.start()-10):m.end()+75]))
 else:print(' F: [separate source lookup needed]')

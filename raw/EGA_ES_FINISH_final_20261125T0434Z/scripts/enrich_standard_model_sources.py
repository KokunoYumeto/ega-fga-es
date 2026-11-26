"""Record separately located frontmatter, index and editorial-note witnesses."""
from pathlib import Path
import json,re,bisect
from corpus import RESULT,FR,labels

p=RESULT/'records/STANDARD_MODEL_REVIEW_CONTEXTS.json'
rows=json.loads(p.read_text())
def at_line(ids,rel,line,anchor,relation='direct source passage'):
 for i in ids:
  edition='diplomatic' if 'DIPLOMATIC' in rows[i]['file'] else 'current'
  q=FR/edition/rel
  if not q.exists():q=FR/'current'/rel
  lines=q.read_text().splitlines()
  ctx=' '.join(lines[max(0,line-2):line+3])
  rows[i]['french']=[{'file':str(q.relative_to(FR.parent.parent)),'anchor':anchor,'term':rows[i]['row'],'context':ctx,'source_relation':relation,'source_line':line}]

at_line([73,195],'BASE/native/ega3/ega3-1-fr.tex',11556,'III.4.4.2','French identifies f^{-1}(y) as an algebraic prescheme; Spanish supplies the noun fibra')
for i,line in zip(range(265,274),[3553,3716,3721,3722,3799,3800,3815,3879,3879]):
 at_line([i],'BASE/native/ega3/ega3-7-fr.tex',line,'III2 errata/addenda')
at_line([348,423],'BASE/native/ega2/ega2-indexes-and-contents-fr.tex',271,'II index:4.2.6')
at_line([349,424,437,515],'BASE/native/ega2/ega2-errata-addenda-fr.tex',56,'Errata:0.5.2.7')
at_line([509,510,511,512,513,514,587,588],'BASE/native/ega1/intro-fr.tex',98,'I introduction')
for i,line in zip(range(669,683),[231,327,327,328,354,356,362,363,377,378,379,382,382,383]):
 at_line([i],'IV3/native/ega4/ega4-15-terminal-fr.tex',line,'IV3 index/contents')
at_line([722],'IV3/native/ega4/ega4-12-fr.tex',3,'section:IV.12')
at_line([827],'IV3/native/ega4/ega4-15-fr.tex',3,'section:IV.15')
at_line([1093],'IV4/native/ega4/ega4-17-fr.tex',749,'subsection:IV.17.8')
at_line([1153],'IV4/native/ega4/ega4-18-fr.tex',1232,'subsection:IV.18.9')
at_line([1251],'IV4/native/ega4/ega4-18-fr.tex',2899,'subsection:IV.19.6')
for i,line in [(1387,43),(1388,66),(1389,77)]:
 at_line([i],'IV4/native/ega4/ega4-backmatter-contents-fr.tex',line,'IV4 contents')

def unit(ids,rel,key,relation):
 for i in ids:
  edition='diplomatic' if 'DIPLOMATIC' in rows[i]['file'] else 'current'
  q=FR/edition/rel;t=q.read_text();ll=labels(t)
  hit=[x for x in ll if x[0]==key]
  assert hit,(rel,key)
  a=hit[0][2];ends=[m.start() for m in re.finditer(r'\\begin\{[^{}]+\}\[[0-9]',t) if m.start()>a]
  b=ends[0] if ends else min(len(t),a+3000)
  ctx=t[a:b]
  term={'es-voisinage':r'voisinages?','es-stalk':r'fibres?','es-filtrant':r'filtr[a-zé]+'}[rows[i]['row']]
  m=re.search(term,ctx,re.I)
  if m:ctx=ctx[max(0,m.start()-120):m.end()+260]
  else:ctx=ctx[:700]
  rows[i]['french']=[{'file':str(q.relative_to(FR.parent.parent)),'anchor':key,'term':m.group() if m else 'semantic source passage','context':re.sub(r'\s+',' ',ctx),'source_relation':relation}]

unit([508,586],'BASE/native/ega1/ega1-3-fr.tex','I.3.6.3','Index entry for the fiber of a morphism; definition is the source witness')
note_map={425:'II.3.8.5',426:'II.4.2.7',427:'II.4.2.7',428:'II.5.2.1',429:'II.6.1.7',430:'II.6.1.7',431:'II.8.3.9',432:'II.8.3.9',433:'II.8.10.3',434:'II.8.10.3',435:'II.8.10.3',436:'II.8.10.3'}
for i,key in note_map.items():
 unit([i],'BASE/native/ega2/ega2-1-fr.tex',key,'Spanish editorial note; sense compared with the cited French unit, not a translated sentence')
unit([738],'IV3/native/ega4/ega4-12-fr.tex','IV.12.2.3','Spanish editorial footnote about the scheme fiber; French construction is the source witness')
assert all(r['french'] for r in rows),[r['id'] for r in rows if not r['french']]
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'without_source_witness':0}))

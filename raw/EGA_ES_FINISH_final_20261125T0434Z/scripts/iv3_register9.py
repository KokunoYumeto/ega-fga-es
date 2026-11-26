"""Apply root-reviewed section 9 register proposals with unit/context rebinding."""
import json,re,difflib,collections
from corpus import RESULT,write_tsv
from iv3_align import units
from iv3_work import apply_edits,DIR
from tex_tools import math_spans
PROPOSALS=RESULT/'records/IV3_REGISTER_89_PROPOSALS.json'
REPORT=RESULT/'records/IV3_REGISTER_9_REBIND_REVIEW.json'
def norm(t):return re.sub(r'\s+',' ',t)
def run(apply=False):
 q=DIR/'sections/ega4-9.tex';original=q.read_text();out=original
 rows=[]
 for index,p in enumerate(json.loads(PROPOSALS.read_text())):
  if not p['place'].startswith('9.'):continue
  u=units(out).get(p['place'])
  row=dict(p,index=index)
  if u is None:row.update(status='unit missing');rows.append(row);continue
  if p['after'] is None:
   row.update(status='retained author plural' if p['before'] in u.text else 'rewritten by complete source translation')
   rows.append(row);continue
  old=p['before'];hits=list(re.finditer(r'(?<!\w)'+re.escape(old)+r'(?!\w)',u.text))
  scored=[]
  for hit in hits:
   pref=u.text[max(0,hit.start()-len(p['prefix'])-50):hit.start()]
   suff=u.text[hit.end():hit.end()+len(p['suffix'])+50]
   a=norm(p['prefix'])[-75:];b=norm(p['suffix'])[:110]
   aa=norm(pref)[-len(a):];bb=norm(suff)[:len(b)]
   sc=(difflib.SequenceMatcher(None,a,aa,autojunk=False).ratio()+difflib.SequenceMatcher(None,b,bb,autojunk=False).ratio())/2
   if pref.endswith(p['prefix']) and suff.startswith(p['suffix']):sc=1.0
   scored.append((sc,hit))
  scored.sort(key=lambda x:-x[0])
  if not scored:
   row.update(status='already revised by source comparison');rows.append(row);continue
  best,h=scored[0]
  if best<0.48 or (len(scored)>1 and best<0.85 and best-scored[1][0]<0.12):
   row.update(status='needs re-review',score=best,current_context=u.text[max(0,h.start()-140):h.end()+180]);rows.append(row);continue
  a=u.start+h.start();b=u.start+h.end();after=p['after'];before=out[a:b]
  if old.lower()=='podemos':
   tail=out[b:b+100];boundary=re.search(r'[$.;]|\bque\b',tail)
   if boundary:tail=tail[:boundary.start()]
   reflexive=re.search(r'\b([a-záéíóúñ]+r)nos\b',tail)
   if reflexive:
    b+=reflexive.end()
    before=out[a:b]
    after+=tail[:reflexive.start()]+reflexive.group(1)
  row.update(status='applied' if apply else 'ready',score=best,actual_before=before,actual_after=after,current_context=out[max(u.start,a-110):b+170])
  if apply:
   apply_edits(q,[(a,b,after,p['place'])],'ega4-9-fr.tex')
   out=q.read_text()
  else:out=out[:a]+after+out[b:]
  rows.append(row)
 assert [s.text for s in math_spans(original)]==[s.text for s in math_spans(out)],'Register changed math'
 REPORT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 print(dict(collections.Counter(x['status'] for x in rows)))
if __name__=='__main__':
 import sys
 run('--apply' in sys.argv)


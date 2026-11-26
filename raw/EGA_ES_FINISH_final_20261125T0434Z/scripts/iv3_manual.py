"""Exact, unit-scoped source comparisons reviewed by the translating agent."""
import re,json
from iv3_work import DIR,FR,JOURNAL,apply_edits
from iv3_align import units

def patch(n,old,new,all=False):
 rows=json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
 if any(r['place']==n and re.sub(r'\s+',' ',r['before'])==re.sub(r'\s+',' ',old) and r['after']==new for r in rows):return
 k=n.split('.')[0];q=DIR/f'sections/ega4-{k}.tex';t=q.read_text();u=units(t)[n]
 hits=list(re.finditer(re.escape(old),u.text))
 if not hits:
  hits=list(re.finditer(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',old)),u.text))
 assert hits and (len(hits)==1 or all),(n,len(hits),old[:110])
 source=f'ega4-{k}-fr.tex' if not n.startswith('15.7.') else 'ega4-15-terminal-fr.tex'
 apply_edits(q,[(u.start+m.start(),u.start+m.end(),new,n) for m in hits],source)

def whole(n,new):
 k=n.split('.')[0];q=DIR/f'sections/ega4-{k}.tex';t=q.read_text();u=units(t)[n]
 if u.text==new:return
 source=f'ega4-{k}-fr.tex' if not n.startswith('15.7.') else 'ega4-15-terminal-fr.tex'
 apply_edits(q,[(u.start,u.end,new,n)],source)

def source_unit(n):
 k=n.split('.')[0];name=f'ega4-{k}-fr.tex'
 if n.startswith('15.7.'):name='ega4-15-terminal-fr.tex'
 return units((FR/'current/IV3/native/ega4'/name).read_text())[n].text

"""Rebind the stable semantic review queue to the current source text."""
from pathlib import Path
import collections,json,re,hashlib
from corpus import RESULT
from tex_tools import prose_segments
from standardize import MODELS

rows=json.loads((RESULT/'records/STANDARD_MODEL_REVIEW_CONTEXTS.json').read_text())
groups=collections.defaultdict(list)
for r in rows:groups[(r['file'],r['row'])].append(r)
patterns=dict(MODELS)
texts={f:(RESULT/f).read_text() for f,_ in groups}
for (f,rid),rs in groups.items():
    t=texts[f];hits=[]
    for a,b,p in prose_segments(t):
        hits.extend((a+m.start(),a+m.end(),m.group()) for m in re.finditer(patterns[rid],p,re.I))
    assert len(hits)==len(rs),(f,rid,len(hits),len(rs))
    for r,(a,b,form) in zip(rs,hits):
        assert form.lower()==r['form'].lower(),(r['id'],form,r['form'])
        r.update(start=a,end=b,raw_context=t[max(0,a-120):min(len(t),b+200)],current_line=t.count('\n',0,a)+1,
                 file_sha256=hashlib.sha256(t.encode()).hexdigest())
(RESULT/'records/STANDARD_MODEL_BOUND.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'bound_rows':len(rows),'files':len(texts)}))

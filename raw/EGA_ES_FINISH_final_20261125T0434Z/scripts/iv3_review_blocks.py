"""Apply explicitly reviewed comparison blocks; never select automatically."""
import json,re,collections
from pathlib import Path
from corpus import RESULT,FR
from tex_tools import math_spans
from iv3_work import apply_edits
def reviewed(ids,translations=None):
 blocks=json.loads((RESULT/'records/IV3_CORE_BLOCKS.json').read_text())
 translations=translations or {}
 grouped=collections.defaultdict(list)
 for i in ids:
  b=next(x for x in blocks if x['id']==i)
  q=RESULT/b['target'];st=q.read_text()
  fp=FR/'current/IV3/native/ega4'/b['source'];ft=fp.read_text()
  fa,fb=b['f_range'];sa,sb=b['s_range']
  before=st[sa:sb];after=ft[fa:fb]
  if i in translations:after=translations[i]
  else:
   assert before and after,(i,'Use manual clause translation for insertion/deletion')
   tail=0;prose=[]
   for z in math_spans(after):
    prose.append(after[tail:z.start]);tail=z.end
   prose.append(after[tail:])
   assert all(re.fullmatch(r'[\s,;:.~]*(?:(?:et|ou)[\s,;:.~]*)?',p) for p in prose),(i,'Source prose requires translation',prose)
   after=re.sub(r'\bet\b','y',after);after=re.sub(r'\bou\b','o',after)
  after=re.sub(r'\\label\{([^{}]+)-fr\}',r'\\label{\1}',after)
  # Preserve target outer sentence punctuation when restoring an inline span.
  if after.endswith('$') and before.endswith(r'\]'):
   m=re.search(r'([.,;:!?])\s*\\\]$',before)
   if m and not re.match(r'\s*[.,;:!?]',st[sb:]):after+=m.group(1)
  grouped[(q,b['source'])].append((sa,sb,after,b['place']))
 for (q,source),edits in grouped.items():apply_edits(q,edits,source)
 print('Reviewed source blocks applied:',len(ids))

def reviewed_math(ids):
 """Restore individually inspected, one-to-one mathematical spans only."""
 blocks=json.loads((RESULT/'records/IV3_CORE_BLOCKS.json').read_text())
 grouped=collections.defaultdict(list)
 for i in ids:
  b=next(x for x in blocks if x['id']==i)
  assert not b['place'].startswith('8.'), 'Section 8 belongs to another agent'
  q=RESULT/b['target'];st=q.read_text()
  ft=(FR/'current/IV3/native/ega4'/b['source']).read_text()
  fa,fb=b['f_range'];sa,sb=b['s_range']
  fs=math_spans(ft[fa:fb]);ss=math_spans(st[sa:sb])
  assert len(fs)==len(ss) and fs,(i,len(fs),len(ss))
  for f,s in zip(fs,ss):
   after=re.sub(r'\\label\{([^{}]+)-fr\}',r'\\label{\1}',f.text)
   if after==s.text:continue
   assert not re.search(r'\\(?:text|hbox|mbox)\s*\{',after),(i,'Translate text arguments explicitly')
   grouped[(q,b['source'])].append((sa+s.start,sa+s.end,after,b['place']))
 for (q,source),edits in grouped.items():apply_edits(q,edits,source)
 print('Reviewed mathematical blocks applied:',len(ids))


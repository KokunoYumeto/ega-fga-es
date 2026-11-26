"""Restore citation/item math boundaries found by the IV3 source comparison."""
import re,collections
from iv3_work import DIR,FR,apply_edits
from tex_tools import math_spans,numbered_units,math_loose_key,prose_segments

counts=collections.Counter()
for q in sorted((DIR/'sections').glob('*.tex')):
 fp=FR/'current/IV3/native/ega4'/q.name.replace('.tex','-fr.tex')
 if not fp.exists():continue
 ft=fp.read_text();fu=numbered_units(ft);t=q.read_text();su=numbered_units(t);edits=[]
 for num,u in su.items():
  if num not in fu:continue
  f=fu[num].text;fm=math_spans(f);fkeys={math_loose_key(s.text) for s in fm}
  for s in math_spans(u.text):
   z=s.text;new=None
   if math_loose_key(z) in fkeys:continue
   m=re.fullmatch(r'\$([a-zA-Z])([\x27]*)\)\$',z)
   if m:
    letter,primes=m.groups()
    # The corresponding French unit must use this prose condition label.
    needle=letter+('$'+primes+'$' if primes else '')+')'
    if needle in f:
     new=r'\emph{'+needle+'}';counts['condition_label_math_boundary']+=1
   elif re.fullmatch(r'\$\([^$]*\d+\.\d+[^$]*\)\$',z):
    ref=re.search(r'\d+\.\d+(?:\.\d+)*',z).group()
    if ref not in f:continue
    body=z[2:-2]
    before=body[:body.index(ref)]
    # First handle references whose chapter marker remains mathematical.
    if re.search(r'\\(?:mathbf|textbf|mathrm)',before) or re.search(r'\b(?:T|M),',before):
     candidates=[]
     for fs in fm:
      if ref in f[fs.end:fs.end+80] and re.fullmatch(r'\$[^$=<>+()]+\$',fs.text):
       if re.search(r'\\(?:mathbf|mathrm|textbf)|\bT\b',fs.text):candidates.append(fs.text)
     if not candidates:continue
     chapter=candidates[0];tail=body[body.index(ref):]
     tail=re.sub(r'\\text\{([^{}]*)\}',r'\1',tail)
     tail=re.sub(r'\\mathrm\{([ivxlcdm]+)\}',r'\textup{\1}',tail)
     new='('+chapter+', '+tail+')'
    else:
     body=re.sub(r'\\text\{([^{}]*)\}',r'\1',body)
     body=re.sub(r'\\mathrm\{([ivxlcdm]+)\}',r'\textup{\1}',body)
     new='('+body+')'
    if new is not None:counts['citation_math_boundary']+=1
   if new is not None:edits.append((u.start+s.start,u.start+s.end,new,num))
  # A-/B-module notation occasionally lost its math delimiter in the old text.
  for a,b,prose in prose_segments(u.text):
   for m in re.finditer(r'(?<![A-Za-z\\$])([AB])-(?:álgebra|módulo)',prose):
    letter=m.group(1)
    if '$'+letter+'$' in f:
     start=u.start+a+m.start();edits.append((start,start+1,'$'+letter+'$',num));counts['plain_variable_math_boundary']+=1
 if edits:apply_edits(q,edits,fp.name)
print(dict(counts))

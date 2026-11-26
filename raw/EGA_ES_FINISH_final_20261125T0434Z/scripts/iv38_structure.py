from iv38_patchlib import *
p=Patches('structure')
p.replace('8.10.5.1',r'basta considerar el caso en que $f$ es cuasiproyectivo.', 'basta\n'+r'\oldpage[IV-3]{41}'+'\n'+r'considerar el caso en que $f$ es cuasiproyectivo.')
p.replace('8.12.9',r'\oldpage[IV-3]{48}','')
p.save()

ft=FP.read_text();st=SP.read_text();edits=[];canon=lambda k:re.sub(r'-(?:fr|es)$','',k)
markers={canon(m[1]):m[0] for m in re.finditer(r'\\label\{([^}]+)\}',ft)}
for m in re.finditer(r'\\EGAReaderTarget\{[^}]+\}\{([^}]+)\}',ft):markers[canon(m[1])]=m[0]
for m in re.finditer(r'\\label\{([^}]+)\}',st):
 k=canon(m[1]);assert k in markers,('extra label',k)
 if m[0]!=markers[k]:edits.append((m.start(),m.end(),markers[k],k,'Literal French label or EGAReaderTarget restored, retaining the reader alias convention.'))
apply(edits,'anchors')

TRANS={'-Alg.':'-Alg.','-Mod.':'-Mod.','pour ':'para ','-alg.':'-alg.','et':'y','-':'-'}
ft=FP.read_text();st=SP.read_text();edits=[];audit=[]
pat=re.compile(r'\\(text|textup|textnormal|textrm|textbf|mbox|hbox)\{')
for n,f in units(ft).items():
 s=units(st)[n];fm=core_spans(f.text);sm=core_spans(s.text);assert len(fm)==len(sm)
 for i,(a,b) in enumerate(zip(fm,sm)):
  inner=[]
  for m in pat.finditer(a.text):
   end=balanced_end(a.text,m.end()-1);word=a.text[m.end():end-1];assert word in TRANS,word
   inner.append((m.end(),end-1,TRANS[word]));audit.append([n,i,m.group(1),word,TRANS[word],'Source text argument read; translated without moving or duplicating math.'])
  if not inner:continue
  new=a.text
  for x,y,z in reversed(inner):new=new[:x]+z+new[y:]
  if new!=b.text:edits.append((s.start+b.start,s.start+b.end,new,n,'French mathematical text argument translated at its literal source boundary; operator names preserved.'))
apply(edits,'math_text')
write('IV38_MATH_TEXT_VERIFIED.tsv',['place','formula','command','french','spanish','verdict'],audit)
print('math text arguments reviewed',len(audit))

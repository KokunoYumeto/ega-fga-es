from iv38_tools import *
from iv3_core import classification
from collections import Counter
ft=FP.read_text();st=SP.read_text();fu=units(ft);su=units(st)
FIRST=re.compile(r'\b(?:[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+mos|[Nn]os|[Nn]uest(?:r[oa]s?))\b')
preg=[];punct=[];short=[];pages=[];refs=[];neg=[];allblocks=[]
def words(z):
 z=re.sub(r'\\(?:sref|eqref|eref|ref|label|tag)(?:\[[^]]*\])?\{[^}]*\}','',z)
 z=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?','',z)
 z=re.sub(r'\\[A-Za-z]+','',z)
 return re.findall(r'[^\W\d_]+',z)
def refnums(z):
 marks=list(core_spans(z))
 for m in reversed(marks):z=z[:m.start]+' '*(m.end-m.start)+z[m.end:]
 for p in [r'\\label\{[^}]*\}',r'\\EGAReaderTarget\{[^}]*\}\{[^}]*\}',r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?',r'\\oldpage(?:\[[^]]*\])?\{[^}]*\}',r'\\tag\{[^}]*\}']:
  z=re.sub(p,lambda m:' '*len(m[0]),z)
 return list(re.finditer(r'(?<![0-9])\d+(?:\.\d+){1,4}(?![0-9])',z))
for un,f in fu.items():
 s=su[un];fm=core_spans(f.text);sm=core_spans(s.text);assert len(fm)==len(sm),(un,len(fm),len(sm))
 fb=[(0,0)]+[(m.start,m.end) for m in fm]+[(len(f.text),len(f.text))];sb=[(0,0)]+[(m.start,m.end) for m in sm]+[(len(s.text),len(s.text))]
 for i in range(len(fb)-1):
  fs,fe=fb[i][1],fb[i+1][0];ss,se=sb[i][1],sb[i+1][0];fg=f.text[fs:fe];sg=s.text[ss:se]
  clean=re.sub(r'(?<!\\)%[^\n]*','',sg)
  common=[un,i,fg,sg,f.text[max(0,fs-120):min(len(f.text),fe+120)],s.text[max(0,ss-120):min(len(s.text),se+120)]]
  if FIRST.search(clean):preg.append(common)
  if i and fm[i-1].text.startswith('$') and re.match(r'\s*[.;:]\s',fg) and not re.match(r'\s*[,.;:!?)]',sg):punct.append(common)
  fw,sw=words(fg),words(sg)
  if len(fw)>=7 and len(sw)<0.58*len(fw):short.append([len(fw),len(sw)]+common)
  if re.search(r'\b(?:n[e’\x27]|pas|non|aucun|ni|sauf|sauf|inversement|nécessaire)\b',fg,re.I) and len(fw)>=4 and not re.search(r'\b(?:no|ni|ning[uú]n\w*|salvo|excepto|inversa|rec[ií]proc\w*|necesari\w*|basta|suficiente)\b',sg,re.I):neg.append(common)
 for lang,u,ms in [('fr',f,fm),('es',s,sm)]:
  for m in re.finditer(r'\\oldpage\[([^]]*)\]\{([^}]+)\}',u.text):pages.append([lang,un,m[1],m[2],sum(x.end<=m.start() for x in ms),u.text[max(0,m.start()-90):m.end()+90]])
 ff=refnums(f.text);sr=refnums(s.text)
 for op,a,b,c,d in difflib.SequenceMatcher(None,[x[0] for x in ff],[x[0].removeprefix('0.') for x in sr],autojunk=False).get_opcodes():
  if op!='equal':refs.append([un,op,'|'.join(x[0] for x in ff[a:b]),'|'.join(x[0] for x in sr[c:d]),f.text[max(0,ff[a].start()-120):ff[b-1].end()+120] if a<b else '',s.text[max(0,sr[c].start()-120):sr[d-1].end()+120] if c<d else ''])
 # Review noncore reference / ordinal / condition math separately.
 fn=math_spans(f.text);sn=math_spans(s.text)
 for op,a,b,c,d in difflib.SequenceMatcher(None,[key(x.text) for x in fn],[key(x.text) for x in sn],autojunk=False).get_opcodes():
  if op!='equal':allblocks.append([un,op,' | '.join(x.text for x in fn[a:b]),' | '.join(x.text for x in sn[c:d])])
write('IV38_REGISTER_CANDIDATES.tsv',['place','gap','french','spanish','french_context','spanish_context'],preg)
write('IV38_PUNCTUATION_CANDIDATES.tsv',['place','gap','french','spanish','french_context','spanish_context'],punct)
write('IV38_SHORT_CANDIDATES.tsv',['french_words','spanish_words','place','gap','french','spanish','french_context','spanish_context'],short)
write('IV38_NEGATIVE_CANDIDATES.tsv',['place','gap','french','spanish','french_context','spanish_context'],neg)
write('IV38_PAGES_AUDIT.tsv',['language','place','part','page','core_before','context'],pages)
write('IV38_REFERENCE_CANDIDATES.tsv',['place','kind','french_refs','spanish_refs','french_context','spanish_context'],refs)
write('IV38_ALL_MATH_BLOCKS.tsv',['place','kind','french_math','spanish_math'],allblocks)
print('register',len(preg),'punctuation',len(punct),'short',len(short),'negative',len(neg),'references',len(refs),'all math blocks',len(allblocks))

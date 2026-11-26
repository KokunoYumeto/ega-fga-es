"""Candidate audit of references, sentence punctuation, and authorial voice.

Candidates require bilingual reading; this script never mutates a translation.
"""
from ii_tools import *
import collections
REF=re.compile(r'\\(?:sref(?:\[[^\]]*\])?|eref|ref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]')
FIRST=re.compile(r'\b(?:[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+mos|[Nn]os|[Nn]uest(?:r[oa]s?))\b')
refrows=[];preg=[];punct=[];variants=[];french=[]
for ed in ['current','diplomatic']:
 for part,ps in parts(espath(ed).read_text()).items():
  fu=units(frpath(ed,part).read_text());su=units(ps.text)
  for un,f in fu.items():
   if un not in su:continue
   s=su[un];ff=list(REF.finditer(f.text));sr=list(REF.finditer(s.text));fk=[x.group(1) or x.group(2) for x in ff];sk=[x.group(1) or x.group(2) for x in sr]
   for typ,a,b,c,d in difflib.SequenceMatcher(None,fk,sk,autojunk=False).get_opcodes():
    if typ!='equal':refrows.append([ed,part,un,typ,' | '.join(fk[a:b]),' | '.join(sk[c:d]),f.text[max(0,ff[a].start()-100):ff[b-1].end()+180] if a<b else '',s.text[max(0,sr[c].start()-100):sr[d-1].end()+180] if c<d else ''])
   fm=math_spans(f.text);sm=math_spans(s.text)
   if len(fm)!=len(sm):continue
   fb=[(0,0)]+[(m.start,m.end) for m in fm]+[(len(f.text),len(f.text))];sb=[(0,0)]+[(m.start,m.end) for m in sm]+[(len(s.text),len(s.text))]
   for i in range(len(fb)-1):
    fs,fe=fb[i][1],fb[i+1][0];ss,se=sb[i][1],sb[i+1][0];fg=f.text[fs:fe];sg=s.text[ss:se]
    clean=re.sub(r'(?<!\\)%[^\n]*','',sg)
    if FIRST.search(clean):
     preg.append([ed,part,un,i,fg,sg,f.text[max(0,fs-160):min(len(f.text),fe+160)],s.text[max(0,ss-160):min(len(s.text),se+160)]])
    if i and fm[i-1].text.startswith('$') and re.match(r'\s*[.;:]\s',fg) and not re.match(r'\s*[,.;:!?)]',sg):
     punct.append([ed,part,un,i,fg,sg,f.text[max(0,fs-90):min(len(f.text),fe+120)],s.text[max(0,ss-90):min(len(s.text),se+120)]])
   for m in sm:
    if re.search(r'\\(?:text|textup|textnormal|mbox|hbox)\{[^}]*\b(?:et|ou|pour|sur|dans|avec|si|alors|degré|rang|pente|sinon)\b',m.text):french.append([ed,part,un,m.text])
write('II_REFERENCE_PENDING_NOW.tsv',['edition','part','unit','kind','fr_keys','es_keys','french_context','spanish_context'],refrows)
write('II_REGISTER_CANDIDATES.tsv',['edition','part','unit','gap','french','spanish','french_context','spanish_context'],preg)
write('II_PUNCTUATION_CANDIDATES.tsv',['edition','part','unit','gap','french','spanish','french_context','spanish_context'],punct)
write('II_FRENCH_MATH_CANDIDATES.tsv',['edition','part','unit','formula'],french)
print('references',len(refrows),'register',len(preg),'punctuation',len(punct),'French math text',len(french))
print('register per part',collections.Counter(x[1] for x in preg));print('punctuation per part',collections.Counter(x[1] for x in punct))
print('reference discrepancies by part',collections.Counter(x[1] for x in refrows))

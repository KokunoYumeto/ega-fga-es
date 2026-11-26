from ii_tools import *
import bisect,collections
mp=re.compile(r'\\(?:label|oldpage|EGAReaderTarget|tag)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?')
def norm(x):return x.replace('-fr','').replace('-es','')
rows=[]
for ed in ['current','diplomatic']:
 t=espath(ed).read_text()
 for part,sp in parts(t).items():
  f=frpath(ed,part).read_text();s=sp.text;fm=mp.findall(f);sm=mp.findall(s);seq=difflib.SequenceMatcher(None,[norm(x) for x in fm],[norm(x) for x in sm],autojunk=False)
  for op,a,b,c,d in seq.get_opcodes():
   if op!='equal':rows.append([ed,part,'marker sequence',op,' | '.join(fm[a:b]),' | '.join(sm[c:d])])
  fs=math_spans(f);ss=math_spans(s)
  if len(fs)!=len(ss):print('MATH unequal',ed,part,len(fs),len(ss))
  for m in re.finditer(r'\\oldpage\[II\]\{([^}]+)\}',f):
   smatch=list(re.finditer(re.escape(m.group()),s));i=bisect.bisect_right([x.end for x in fs],m.start())
   if len(smatch)!=1:rows.append([ed,part,'page '+m[1],'count',str(len(smatch)),m[0]]);continue
   z=smatch[0];j=bisect.bisect_right([x.end for x in ss],z.start())
   if i!=j:
    lo=ss[i-1].end if i else 0;hi=ss[i].start if i<len(ss) else len(s)
    rows.append([ed,part,'page '+m[1],str(i)+':'+str(j),re.sub(r'\s+',' ',f[max(0,m.start()-130):m.end()+130]),re.sub(r'\s+',' ',s[lo:hi])])
write('II_ATTRIBUTES_PENDING.tsv',['edition','part','place','kind','french','spanish_gap'],rows)
print('pending attributes',len(rows),collections.Counter(x[2].split()[0] for x in rows))
for row in rows:
 if row[0]=='current':print(row)

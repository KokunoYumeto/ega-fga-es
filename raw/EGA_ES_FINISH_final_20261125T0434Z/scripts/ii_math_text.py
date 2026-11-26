"""Translate source text arguments, preserving their exact math boundaries.

Do not transplant inherited Spanish arguments: some contain duplicated formulas.
"""
from ii_tools import *
TRANS={'pour tout ':'para todo ','où ':'donde ',' pour ':' para ','et':'y','(ouvert de $P_k$)':'(abierto de $P_k$)','(ouvert de $P$)':'(abierto de $P$)',"(ouverts de $X'$)":"(abiertos de $X'$)",'pour ':'para ','quels que soient ':'cualesquiera que sean ','avec':'con','où':'donde'}
pat=re.compile(r'\\(text|textup|textnormal|textrm|textbf|mbox|hbox)\{')
rows=[];audit=[]
for ed in ['current','diplomatic']:
 path=espath(ed);t=path.read_text();edits=[]
 for part,ps in parts(t).items():
  su=units(ps.text)
  for unit,f in units(frpath(ed,part).read_text()).items():
   s=su[unit];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm)
   for i,(a,b) in enumerate(zip(fm,sm)):
    inner=[]
    for m in pat.finditer(a.text):
     end=balanced_end(a.text,m.end()-1);word=a.text[m.end():end-1];assert word in TRANS,word
     inner.append((m.end(),end-1,TRANS[word]));audit.append([ed,part,unit,i,m.group(1),word,TRANS[word],'Source argument translated; all embedded and adjacent math retained literally.'])
    if not inner:continue
    new=apply_edits(a.text,inner)
    if re.sub(r'\s+','',new)!=re.sub(r'\s+','',b.text):
     edits.append((ps.start+s.start+b.start,ps.start+s.start+b.end,new));rows.append([str(path.relative_to(ROOT)),part+':'+unit+': formula '+str(i),b.text,new,'own comparison',source_note(ed,part,unit)+'; translated the exact French text argument; removed inherited duplicated math/English words.'])
 path.write_text(apply_edits(t,edits))
write('II_CHANGES_math_text.tsv',HEADER,rows)
write('II_MATH_TEXT_VERIFIED.tsv',['edition','part','unit','formula','command','french','spanish','verdict'],audit)
print('text arguments verified',len(audit),'formulas corrected',len(rows))

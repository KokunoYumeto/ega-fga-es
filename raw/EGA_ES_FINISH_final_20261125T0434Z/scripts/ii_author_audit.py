from ii_tools import *
AUTH=re.compile(r'\b(?:nous|notre|nos|supposons|posons|montrons|démontrons|prouvons|considérons|prenons|reprenons|rappelons|notons|voyons|revenons|désignons|écrivons|conservons|définissons|interprétons|recouvrons|commençons|terminons|partons|faisons|indiquons|adoptons|appelons|donnons|passons|gardons|remarquons|observons|explicitons|couvrons|formons)\b',re.I)
ES=re.compile(r'\b(?:[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+mos|[Nn]os|[Nn]uest(?:r[oa]s?))\b')
nouns={'morfismos','homomorfismos','isomorfismos','primos','dihomomorfismos','endomorfismos','diisomorfismos','automorfismos','mismos','monomorfismos','extremos'}
rows=[]
for ed in ['current','diplomatic']:
 for part,ps in parts(espath(ed).read_text()).items():
  su=units(ps.text)
  for unit,f in units(frpath(ed,part).read_text()).items():
   s=su[unit];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm)
   fb=[(0,0)]+[(m.start,m.end) for m in fm]+[(len(f.text),len(f.text))];sb=[(0,0)]+[(m.start,m.end) for m in sm]+[(len(s.text),len(s.text))]
   for i in range(len(fb)-1):
    fg=f.text[fb[i][1]:fb[i+1][0]];sg=s.text[sb[i][1]:sb[i+1][0]]
    if AUTH.search(fg) and not any(m.group().lower() not in nouns for m in ES.finditer(sg)):
     rows.append([ed,part,unit,i,fg,sg,f.text[max(0,fb[i][1]-100):min(len(f.text),fb[i+1][0]+100)],s.text[max(0,sb[i][1]-100):min(len(s.text),sb[i+1][0]+100)]])
write('II_AUTHORIAL_CANDIDATES.tsv',['edition','part','unit','gap','french','spanish','french_context','spanish_context'],rows)
print('authorial candidates',len(rows))
for i,x in enumerate(rows):
 if x[0]=='current':print(i,x[2],x[3],'FR',re.sub(r'\s+',' ',x[4]),'| ES',re.sub(r'\s+',' ',x[5]))

from iv38_tools import *
class Patches:
 def __init__(self,name):self.name=name;self.text=SP.read_text();self.rows=[];self.missed=[]
 def replace(self,unit,old,new,count=1,why='Read the French and Spanish clause; restore source wording, mathematical partition and order.'):
  u=units(self.text)[unit];pat=re.compile(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',old.strip())),re.S);notes=note_ranges(u.text);ms=[m for m in pat.finditer(u.text) if not any(a<=m.start()<b for a,b in notes)]
  if (count is not None and len(ms)!=count) or not ms:self.missed.append([unit,len(ms),old]);return
  for m in reversed(ms):
   a=u.start+m.start();b=u.start+m.end();self.rows.append([str(SP.relative_to(ROOT)),unit,self.text[a:b],new,'own comparison',SOURCE+': '+unit+'; '+why]);self.text=self.text[:a]+new+self.text[b:]
 def literal(self,i):
  r=json.loads((ROOT/'records/IV38_BLOCKS.json').read_text())[i];fs=math_spans(r['french_math']);ss=math_spans(r['spanish_math']);assert len(fs)==len(ss)
  for f,s in zip(fs,ss):self.replace(r['place'],s.text,f.text,count=None,why='Restored the literal source mathematical expression after bilingual block review; editorial footnotes excluded.')
 def save(self):
  SP.write_text(self.text);write('IV38_CHANGES_'+self.name+'.tsv',HEADER,self.rows);write('IV38_MISSED_'+self.name+'.tsv',['place','matches','before'],self.missed);print(self.name,'changes',len(self.rows),'missed',len(self.missed));print(self.missed)

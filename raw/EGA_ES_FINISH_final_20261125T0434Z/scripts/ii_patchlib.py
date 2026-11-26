from ii_tools import *
class Patches:
 def __init__(self,name):
  self.name=name;self.text={ed:espath(ed).read_text() for ed in ['current','diplomatic']};self.rows=[];self.missed=[]
 def replace(self,unit,old,new,part='main',editions=('current','diplomatic'),count=1,note='Read French and Spanish clause together; restored the source formula/prose boundary and order.'):
  pat=re.compile(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',old.strip())),re.S)
  for ed in editions:
   t=self.text[ed];p=parts(t)[part];u=units(p.text)[unit];ms=list(pat.finditer(u.text))
   if len(ms)!=count:
    self.missed.append([ed,part,unit,len(ms),old]);continue
   edits=[]
   for m in ms:
    edits.append((p.start+u.start+m.start(),p.start+u.start+m.end(),new));self.rows.append([str(espath(ed).relative_to(ROOT)),part+':'+unit,m.group(0),new,'own comparison',source_note(ed,part,unit)+'; '+note])
   self.text[ed]=apply_edits(t,edits)
 def gap(self,i,new,**kwargs):
  row=read('II_PENDING_pass1.tsv')[i];assert row['edition']=='current';self.replace(row['unit'],row['spanish'],new,part=row['part'],**kwargs)
 def regex(self,unit,pattern,new,part='main',editions=('current','diplomatic'),note='Read the entire source and Spanish clause; translated the supplied source reading.'):
  for ed in editions:
   u=units(parts(self.text[ed])[part].text)[unit].text;ms=list(re.finditer(pattern,u,re.S))
   if len(ms)!=1:self.missed.append([ed,part,unit,len(ms),pattern]);continue
   self.replace(unit,ms[0].group(0),new,part=part,editions=(ed,),note=note)
 def save(self):
  for ed,t in self.text.items():espath(ed).write_text(t)
  write('II_CHANGES_'+self.name+'.tsv',HEADER,self.rows)
  write('II_MISSED_'+self.name+'.tsv',['edition','part','unit','matches','old'],self.missed)
  print(self.name,'changes',len(self.rows),'missed',len(self.missed))
  for x in self.missed:print(x)

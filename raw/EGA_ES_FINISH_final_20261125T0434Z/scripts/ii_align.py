"""Source-literal alignment after separately partitioning the II monolith."""
from ii_tools import *
import argparse
P=argparse.ArgumentParser();P.add_argument('--apply',action='store_true');P.add_argument('--suffix',default='');a=P.parse_args()
changes=[];pending=[];stats=[]
for ed in ['current','diplomatic']:
 p=espath(ed);t=p.read_text();edits=[]
 for part,sp in parts(t).items():
  ft=frpath(ed,part).read_text();fu=units(ft);su=units(sp.text)
  for num,f in fu.items():
   if num not in su:pending.append([ed,part,num,'unit missing','','',f.text[:300],'']);continue
   s=su[num];fs=math_spans(f.text);ss=math_spans(s.text)
   seq=difflib.SequenceMatcher(None,[key(x.text) for x in fs],[key(x.text) for x in ss],autojunk=False)
   exact=0
   for op,fa,fb,sa,sb in seq.get_opcodes():
    if op=='equal' or (op=='replace' and fb-fa==sb-sa):
     for fm,sm in zip(fs[fa:fb],ss[sa:sb]):
      z=retain_translated_text(fm.text,sm.text)
      if z is None:
       pending.append([ed,part,num,'text',str(fs.index(fm)),str(ss.index(sm)),fm.text,sm.text]);continue
      punct=''
      if sm.kind!='inline' and fm.kind=='inline':
       ff=f.text[fm.end:];sf=s.text[sm.end:]
       if ff and ff[0] in '.,;:' and not sf.lstrip().startswith(ff[0]):punct=ff[0]
      z+=punct
      if z!=sm.text:
       edits.append((sp.start+s.start+sm.start,sp.start+s.start+sm.end,z));changes.append([str(p.relative_to(ROOT)),part+':'+num,sm.text,z,'own comparison',source_note(ed,part,num)+'; source TeX restored in corresponding formula; no proof claim.'])
      exact+=1
    else:
     ff=f.text[fs[fa].start:fs[fb-1].end] if fb>fa else ''
     sf=s.text[ss[sa].start:ss[sb-1].end] if sb>sa else ''
     pending.append([ed,part,num,op,str(fa)+':'+str(fb),str(sa)+':'+str(sb),ff,sf])
   stats.append([ed,part,num,len(fs),len(ss),exact])
 if a.apply:p.write_text(apply_edits(t,edits))
write('II_CHANGES_math'+a.suffix+'.tsv',HEADER,changes)
write('II_PENDING'+a.suffix+'.tsv',['edition','part','unit','kind','f_indices','s_indices','french','spanish'],pending)
write('II_STATS'+a.suffix+'.tsv',['edition','part','unit','fr_math','es_math','aligned'],stats)
print('changes',len(changes),'pending',len(pending),'aligned',sum(int(x[-1]) for x in stats),'totalFR',sum(int(x[-3]) for x in stats))

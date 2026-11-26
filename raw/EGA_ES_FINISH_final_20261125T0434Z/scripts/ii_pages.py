"""Place page markers at their translated source clauses after exact math alignment."""
from ii_tools import *
import bisect
rows=[]
points={'45':'cuando','51':'','54':'','55':'donde','61':'siguientes','62':r'\emph{afín}','63':'y que','64':'canónicamente','65':'el haz','71':'finito','113':'cuyo','114':'de ','116':'de los','118':'','120':'','125':'morfismo','127':'elementos','131':'el núcleo','134':'','135':'','137':''}
for ed in ['current','diplomatic']:
 p=espath(ed);t=p.read_text()
 def edit(a,b,new,place):
  global t
  old=t[a:b];t=t[:a]+new+t[b:];rows.append([str(p.relative_to(ROOT)),place,old,new,'own comparison',source_note(ed,'main',place)+'; source page position in the corresponding translated clause.'])
 for page,anchor in [('10',r'\begin{proposition}[1.4.3]'),('12',r'\begin{proposition}[1.4.11]'),('59',r'\subsection{Condiciones de finitud}')]:
  marker=r'\oldpage[II]{'+page+'}';a=t.index(marker);edit(a,a+len(marker),'','page '+page+' remove prior position');a=t.index(anchor);edit(a,a,marker+'\n','page '+page+' source position')
 for page,anchor in points.items():
  sp=parts(t)['main'];s=sp.text;f=frpath(ed,'main').read_text();marker=r'\oldpage[II]{'+page+'}';fi=f.index(marker);sm=s.index(marker);fs=math_spans(f);ss=math_spans(s);assert len(fs)==len(ss)
  idx=bisect.bisect_right([x.end for x in fs],fi);a=sp.start+sm
  oldcontext=t[a-60:a+len(marker)+60]
  t=t[:a]+t[a+len(marker):];sp=parts(t)['main'];s=sp.text;ss=math_spans(s);lo=ss[idx-1].end if idx else 0;hi=ss[idx].start if idx<len(ss) else len(s);gap=s[lo:hi]
  if page=='71':
   assert gap=='-módulo coherente ',repr(gap);newgap='-módulo coherente de tipo finito ';a=sp.start+lo;edit(a,sp.start+hi,newgap,'3.8.5 source phrase de type fini');s=parts(t)['main'].text;gap=newgap
  if anchor:
   assert gap.count(anchor)==1,(ed,page,repr(gap),anchor);pos=sp.start+lo+gap.index(anchor)
  else:pos=sp.start+lo+len(gap.rstrip()) if gap.strip() else sp.start+lo
  insert=('%' if page=='125' else '')+'\n'+marker+'\n';t=t[:pos]+insert+t[pos:]
  rows.append([str(p.relative_to(ROOT)),'page '+page,oldcontext,t[pos-60:pos+len(insert)+60],'own comparison',source_note(ed,'main','printed page '+page)+'; placement read in both languages.'])
 marker=r'\oldpage[II]{206}';a=t.index(marker);edit(a,a+len(marker),'','extra page 206 removed')
 marker=r'\oldpage[II]{205}';a=t.index(marker);edit(a,a+len(marker),'','bibliography page 205 remove prior position');sp=parts(t)['bibliography'];a=sp.start+len(r'\clearpage');edit(a,a,'\n'+marker,'bibliography page 205 source position')
 p.write_text(t)
write('II_CHANGES_pages.tsv',HEADER,rows)
print('page/phrase restorations',len(rows))

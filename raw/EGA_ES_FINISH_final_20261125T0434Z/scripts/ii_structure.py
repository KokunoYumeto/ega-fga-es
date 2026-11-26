from ii_tools import *
rows=[]
for ed in ['current','diplomatic']:
 p=espath(ed);t=p.read_text();before=t
 for num,env in [('3.4.7','remarks'),('3.7.9','remarks'),('5.5.4','remark'),('7.4.19','remarks')]:
  old=r'\begin{'+env+'}['+num+']';a=t.index(old);b=t.index(r'\end{'+env+'}',a)+len(r'\end{'+env+'}')
  chunk=t[a:b]
  if num in ['3.4.7','5.5.4']:
   new=chunk.replace(old,r'\par\medskip\noindent\textit{Observaciones ('+num+r'). ---\ }',1).replace(r'\end{'+env+'}','',1)
  else:new=chunk.replace(old,r'\begin{namedtheorem}['+num+']{Observaciones}',1).replace(r'\end{'+env+'}',r'\end{namedtheorem}',1)
  t=t[:a]+new+t[b:]
  rows.append([str(p.relative_to(ROOT)),num,chunk,new,'own comparison',source_note(ed,'main',num)+'; restored the source form of the numbered remarks.'])
 p.write_text(t)
write('II_CHANGES_structure.tsv',HEADER,rows)
print('structural changes',len(rows))

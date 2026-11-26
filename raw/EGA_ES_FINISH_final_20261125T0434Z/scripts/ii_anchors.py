from ii_tools import *
rows=[]
for ed in ['current','diplomatic']:
 p=espath(ed);t=p.read_text()
 def change(old,new,place,source):
  global t
  assert t.count(old)==1,(ed,place,t.count(old),old);t=t.replace(old,new);rows.append([str(p.relative_to(ROOT)),place,old,new,'own comparison',source])
 change(r'\section*{Sumario}',r'''% EGA II SOURCE FRONT MATTER
\oldpage[II]{5}
\phantomsection
\label{chapter:II-fr}
\begin{center}
{\large CAPÍTULO II\par}
\vspace{1.5em}
{\Large\bfseries ESTUDIO GLOBAL ELEMENTAL\par}
{\Large\bfseries DE ALGUNAS CLASES DE MORFISMOS\par}
\vspace{1.8em}
\end{center}
\section*{Sumario}''','source chapter heading',source_note(ed,'front','chapter:II-fr'))
 # Page 5 precedes the chapter heading, not the introduction paragraph.
 old=r'\oldpage[II]{5}'+'\nLas diversas';change(old,'Las diversas','front page 5',source_note(ed,'front','page 5'))
 for lab in ['II.1.3','II.8.1']:change(r'\label{'+lab+'}','',lab,source_note(ed,'main',lab)+'; extra inherited alias absent from source.')
 change(r'\label{subsection:II.5.4}',r'\label{subsection:II.5.4}'+'\n'+r'\label{II.5.4-fr}','II.5.4',source_note(ed,'main','II.5.4-fr'))
 allfr='\n'.join(frpath(ed,part).read_text() for part in NAMES)
 keys={k.removesuffix('-fr'):k for k in re.findall(r'\\label\{([^}]+)\}|\\hyperref\[([^\]]+)\]',allfr) for k in k if k}
 aliases={f'subsection:II.{s}':f'II.{s}' for s in ['1.5','1.6','1.7','4.6']}
 aliases.update({'II.1.3':'subsection:II.1.3','II.8.1':'subsection:II.8.1'})
 for k in ['8.4.4.2','8.4.4.3','8.5.1.2','8.5.1.3','8.5.3.2']:aliases['eq:2.'+k]='II.'+k
 for k in re.findall(r'\\label\{(ega2:addendum:[^}]+)-fr\}',allfr):aliases[k.replace('ega2:addendum:','')]=k
 start=parts(t)['front'].start;body=t[start:];edits=[]
 pat=re.compile(r'\\(?:label|ref|sref|eref)(?:\[[^\]]*\])?\{([^}]+)\}|\\hyperref\[([^\]]+)\]')
 for m in pat.finditer(body):
  n=1 if m[1] else 2;old=m[n];base=old.removesuffix('-fr').removesuffix('-es');base=aliases.get(base,base);new=keys.get(base)
  if new and old!=new:
   edits.append((start+m.start(n),start+m.end(n),new));rows.append([str(p.relative_to(ROOT)),base,old,new,'standard',source_note(ed,'main',base)+'; source label/reference key restored.'])
 t=apply_edits(t,edits)
 # Keep source spellings printable in the independent native monolith.
 old=r'\newcommand{\EGARefNumber}[1]{\EGARefNumberAux#1\@nil}'
 new=r'\newcommand{\EGARefNumber}[1]{\begingroup\StrSubstitute{#1}{-fr}{}[\egarefkey]\StrSubstitute{\egarefkey}{-es}{}[\egarefkey]\StrBehind{\egarefkey}{.}\endgroup}'
 change(old,new,'reference display macro','Assembly: strip language suffix from printed reference number while linking exact source key.')
 p.write_text(t)
write('II_CHANGES_anchors.tsv',HEADER,rows)
print('anchor changes',len(rows))

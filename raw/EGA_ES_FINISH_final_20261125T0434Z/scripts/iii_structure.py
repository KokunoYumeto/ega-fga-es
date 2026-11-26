#!/usr/bin/env python3
"""Source-checked restoration of prose environment boundaries."""
from iii_bridge_patch import *
from tex_tools import is_escaped

def update(edition,part,fn):
 f=source(edition,part).read_text();e,b=aggregate(edition,part);fs={k:f[a:z] for k,a,z in sections(f)};ed=[]
 for k,a,z in sections(e):
  old=e[a:z];new=fn(k,old,fs[k])
  if new!=old:
   if not any(q[0]<=a and z<=q[1] for q in b):
    for tag,x,y,c,d in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
     if tag!='equal':ed.append((a+x,a+y,new[c:d],k,old[x:y]))
   else:ed.append((a,z,new,k,old))
 if ed:apply_edits(edition,part,ed,b)
 print('structure',edition,part,len(ed))

def repair(k,t,f):
 if k=='6.10.3':t=re.sub(r'\\begin\{env\}\[6\.10\.3\.1\]','',t)
 # These inherited proof wrappers introduced headings/QED marks absent in source.
 if r'\begin{proof}' not in f and r'\begin{proof}' in t:t=t.replace(r'\begin{proof}','').replace(r'\end{proof}','')
 # Formula-only numbered env wrappers were added by the inherited translation.
 sourceenv=set(re.findall(r'\\begin\{env\}\[([^]]+)\]',f))
 edits=[]
 for m in re.finditer(r'\\begin\{env\}\[([^]]+)\]',t):
  if m[1] in sourceenv or re.fullmatch(r'\d+\.\d+\.\d+',m[1]):continue
  close=t.find(r'\end{env}',m.end());assert close>=0,(k,m[1])
  edits.extend([(m.start(),m.end(),''),(close,close+len(r'\end{env}'),'')])
 for a,z,new in sorted(edits,reverse=True):t=t[:a]+new+t[z:]
 # Outer environment title follows supplied source.
 fm=re.match(r'\\begin\{(\w+)\}\[([^]]+)\](?:\{([^}]+)\})?',f)
 em=re.match(r'\\begin\{(\w+)\}\[([^]]+)\](?:\{([^}]+)\})?',t)
 if fm and em and fm[1]!=em[1] and k not in ['6.5.7','6.5.10','6.5.12','4.3.11','4.4.12']:
  name={'Corollaire':'Corolario','Lemme':'Lema','Remarques':'Observaciones','Remarque':'Observación'}.get(fm[3],fm[3])
  beg='\\begin{'+fm[1]+'}['+fm[2]+']'+('{'+name+'}' if name else '')
  t=beg+t[em.end():]
  oldend='\\end{'+em[1]+'}';newend='\\end{'+fm[1]+'}'
  if oldend in t:t=t.replace(oldend,newend,1)
  t=re.sub(r'\n\\emph\{(?:Observaciones|Observación|Escolio)\.\}\n','\n',t,count=1)
 if k=='11.1.1':
  t=t.replace('  Definimos entonces,',r'\end{enumerate}'+'\n\nSe definen entonces,')
  t=t.replace('  Definimos entonces',r'\end{enumerate}'+'\n\nSe definen entonces')
 if k=='11.3.1' and r'\begin{enumerate}' not in f:t=t.replace(r'\end{enumerate}','')
 if k=='11.5.2':
  t=t.replace(r'\end{enumerate}'+'\nEntonces:','Entonces:')
  t=t.replace(r'\end{enumerate}'+'\nComponiendo','Componiendo')
  t=t.replace(r'para $i\leq0$.',r'para $i\leq0$);')
  t=t.replace('Es inmediato que todo ','Es inmediato que ')
 if k=='1.1.3':t=t.replace('$A$-isomorfismo}',r'$A$-\emph{isomorfismo}')
 if k=='1.2.1':t=t.replace(r'\begin{enumerate}',r'\begin{itemize}').replace(r'\end{enumerate}',r'\end{itemize}')
 if k=='5.3.5':t=t.replace(r'\end{env}','')
 if k=='5.4.2':t=t.replace(r'\end{env}',r'\end{scholium}')
 if k=='6.4.2':t=t.replace(r'\end{lemma}',r'\end{namedtheorem}')
 if k=='6.6.7':t=t.replace(r'\end{env}','')
 if k=='6.10.3':t=re.sub(r'\\begin\{env\}\[6\.10\.3\.1\]','',t)
 if k in ['6.7.8','6.7.9','6.9.7']:
  t=t.replace(r'\begin{enumerate}','').replace(r'\end{enumerate}','')
  t=re.sub(r'\\item\[\{(\$.*?\$)\}\]',r'\1',t)
  t=re.sub(r'\\item\[(\$.*?\$)\]',r'\1',t)
 if k=='7.6.4':
  t=t.replace(r'\textnormal{(i)}',r'\begin{enumerate}'+'\n'+r'\item[(i)]',1).replace(r'\textnormal{(ii)}',r'\item[(ii)]',1)
  t=t.replace(r'\end{remarks}',r'\end{enumerate}'+'\n'+r'\end{remarks}')
 if k=='7.6.9':
  t=t.replace(r'\textnormal{(ii)}',r'\item[(ii)]').replace(r'\end{proof}',r'\end{enumerate}'+'\n'+r'\end{proof}')
 return t
if __name__=='__main__':
 for ed,part in [('current','6'),('current','7')]:update(ed,part,repair)

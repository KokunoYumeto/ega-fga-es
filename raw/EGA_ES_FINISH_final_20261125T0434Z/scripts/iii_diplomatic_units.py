#!/usr/bin/env python3
"""Reviewed III1 printed prose/reference variants for complete restored units."""
from iii_bridge_patch import *

def renumber(t,cut):return re.sub(r'§(\d+)§',lambda m:'§'+str(int(m[1])-(int(m[1])>cut))+'§',t)
def run():
 c,cb=aggregate('current','1');d,db=aggregate('diplomatic','1');f=source('diplomatic','1').read_text()
 cs={k:(a,b) for k,a,b in sections(c)};ds={k:(a,b) for k,a,b in sections(d)};fs={k:(a,b) for k,a,b in sections(f)}
 patches={
 '11.8.1': [('y §29§ en caso contrario, donde §30§ es la sucesión de los §31§ ordenados \\emph{en orden creciente}', 'y la sucesión §30§ de los §31§ ordenados \\emph{en orden creciente} en caso contrario')],
 '2.3.4':[(r'(\hyperref[III.2.3.1-fr]{2.3.1}). El hecho',r'(\hyperref[III.2.3.2-fr]{2.3.2}). El hecho')],
 '2.4.1':[('finalmente que se tiene\n§89§',r'finalmente que se \textbf{tiene}'+'\n§89§')],
 '2.5.3':[('la prop. (2.5.2), resulta','la prop. (2.5.1), resulta')],
 '3.1.2':[('§11§ de soporte §12§ tal que','§11§ tal que')],
 '4.1.7':[('definido como en (4.1.7.8)','definido como en (4.7.1.8)')],
 '4.2.1':[('(G, II, 4.9.1). En el caso general','(G, II, 4 9.1). En el caso general')],
 '4.6.7':[(r'(\textbf{II}, 6.1.1 y \textbf{I}, 4.2.4)',r'(\textbf{II}, 6.1.1 y I, 4.2.4)'),(r'(\textbf{II}, 5.4.3); si se',r'(II, 5.4.3); si se')],
 '4.6.8':[(r'(\textbf{I}, 10.9.1 y 10.14.2)',r'(I, 10.9.1 y 10.14.2)')],
 '4.7.1': [('§43§ definido por el Ideal',r'§43§ definido \textbf{por} el Ideal'),(r'(\textbf{II}, 4.6.11); reemplazando',r'(\textbf{I}I, 4.6.11); reemplazando')],
 '5.3.4':[]
 }
 ed=[];logs=[]
 for k,pp in patches.items():
  a,b=cs[k];t=masked(c[a:b]);fa,fb=fs[k];ea,eb=ds[k]
  for old,new in pp:
   assert t.count(old)==1,(k,old);t=t.replace(old,new)
  if k=='11.8.1':t=renumber(t,29)
  if k=='3.1.2':t=renumber(t,12)
  new=expand(t,f[fa:fb]);ed.append((ea,eb,new,k,d[ea:eb]));logs.append(dict(edition='diplomatic',part='1',place=k,source_sha256=hashlib.sha256(f[fa:fb].encode()).hexdigest(),before=d[ea:eb],after=new,kind='complete printed unit; reviewed French prose variants retained; no mathematical proof'))
 apply_edits('diplomatic','1',ed,db)
 with (ROOT/'records/III_BRIDGE_TRANSLATIONS.jsonl').open('a') as o:
  for x in logs:o.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('diplomatic complete variants',len(ed))
if __name__=='__main__':run()

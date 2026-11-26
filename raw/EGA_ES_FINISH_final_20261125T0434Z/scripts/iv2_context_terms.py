#!/usr/bin/env python3
"""Apply the individually reviewed IV-2 voisinage contexts and log all fiber decisions."""
from pathlib import Path
import re,csv,difflib,json
import audit_iv2_alignment as a
import reconcile_iv2 as r
ROOT=a.ROOT

def outside(t,func):
 out=[];p=0
 for m in a.MATH.finditer(t):out.extend([func(t[p:m.start()]),m[0]]);p=m.end()
 out.append(func(t[p:]));return ''.join(out)

def phrase(s):
 s=re.sub(r'\bentornos\b','vecindades',s,flags=re.I);s=re.sub(r'\bentorno\b','vecindad',s,flags=re.I)
 for x,y in [('un','una'),('el','la'),('todo','toda'),('ese','esa'),('este','esta'),('del','de la'),('al','a la'),('algún','alguna'),('ningún','ninguna')]:
  s=re.sub(r'\b'+x+r'(\s+)vecindad\b',lambda m:y+m[1]+'vecindad',s)
 s=re.sub(r'\buno de estos(\s+)vecindades',r'una de estas\1vecindades',s)
 s=re.sub(r'(vecindad\s+)abierto\b',r'\1abierta',s)
 s=re.sub(r'(vecindades\s+)abiertos\b',r'\1abiertas',s)
 s=re.sub(r'(vecindad\s+afín\s+suficientemente\s+)pequeño\b',r'\1pequeña',s)
 s=re.sub(r'(vecindad\s+más\s+)pequeño\b',r'\1pequeña',s)
 s=re.sub(r'(vecindad\s+abierta\s+no\s+)vacío\b',r'\1vacía',s)
 s=re.sub(r'(vecindad\s+abierta\s+)íntegro\b',r'\1íntegra',s)
 s=re.sub(r'(vecindad\s+abierta\s+)isomorfo\b',r'\1isomorfa',s)
 s=re.sub(r'(vecindad\s+\()relativo\b',r'\1relativa',s)
 return s

def main():
 modelrows=[];total=0;adjchanges=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  f,e,b,paired,gaps=a.compare(layer);assert not gaps
  for lo,hi,file in b:
   path=ROOT/file;old=path.read_text();n=len(re.findall(r'\bentornos?\b',a.MATH.sub('',old),re.I))
   if not n:continue
   new=outside(old,phrase)
   # Individually reviewed relative clauses whose antecedent is the newly feminine vecindad.
   pat=r'(vecindad\s+abierta[^;]{0,140}?\bque es (?:\\emph\{)?(?:geométricamente\s+)?(?:puntualmente\s+)?)(reducido|íntegro)\b'
   def rel(m):
    adjchanges.append([file,m[0],m[1]+{'reducido':'reducida','íntegro':'íntegra'}[m[2]]]);return adjchanges[-1][2]
   new=re.sub(pat,rel,new)
   # Affine-neighborhood comparisons in 5.8.3, and the immediately following size adjective in 4.6.13.
   if '5.8.1_5.8.4' in file or '5.8.3' in file:
    new=re.sub(r'(vecindad\s+abierta[^;.]{0,100}?\b)isomorfo\b',r'\1isomorfa',new)
   if '4.6.11_4.6.14' in file or '4.6.12_4.6.14' in file:
    new=new.replace('tomando $U$ suficientemente pequeño','tomando $U$ suficientemente pequeña')
   assert [m[0] for m in a.MATH.finditer(old)]==[m[0] for m in a.MATH.finditer(new)]
   assert not re.search(r'\bentornos?\b',a.MATH.sub('',new),re.I)
   path.write_text(new);total+=n
   r.log('CAMBIOS',[file,'reviewed voisinage contexts',old,new,'standard','standard/STANDARDS_20261119b.md Spanish; supplied French IV2 voisinage occurrences, context and gender reviewed'])
  assert not re.search(r'\bentornos?\b',a.MATH.sub('',a.aggregate(layer)[0]),re.I)
 print('voisinage replacements',total)
 for q in adjchanges:print('AGREEMENT',q[0],repr(q[1]),'=>',repr(q[2]))
if __name__=='__main__':main()

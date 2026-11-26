import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_segment_decisions import *
from iii_structure import update
apply_decisions({
'1:11.4.5:1':' los límites inductivos filtrantes existen y son exactos. Si ',
'1:11.9.1:82':'\n(donde la flecha de la izquierda es la restricción de ',
'1:11.9.1:115':' (',
'1:11.9.1:116':') es el morfismo deducido de ',
'1:13.7.2:6':' compatibles\n'+r'\oldpage[0\textsubscript{III}]{76}'+'\ncon las filtraciones, y que hacen de\n',
'1:13.7.5:17':r' satisface (ML), se deduce de (\hyperref[0.13.3.1-fr]{13.3.1}) un isomorfismo canónico'+'\n'+r'\hypertarget{canon-legacy.0-III.13.7.5.proof-comparison}{}'+'\n',
'1:2.3.1:52':' (',
'1:4.3.10:7':' (',
'1:4.3.12:11':' normal (y ',
'1:4.4.2:14':r' es un conjunto finito (\textbf{II}, 6.1.7), y se ve que \emph{b)} implica \emph{c)}. Finalmente, como ',
'1:4.4.4:1':' es reducido (resp. irreducible y ',
'1:5.2.6:27':' (definido sobre el abierto ',
'1:4.6.3:22':'\nes inyectivo (resp. sobreyectivo),\n'+r'\oldpage[III]{142}'+'\n',
'6:6.5.11:10':r'-Módulos\textup{)} cuasicoherentes; se tiene entonces un isomorfismo canónico funtorial'+'\n',
'6:6.5.15:7':' (',
'7:7.3.7:25':' en (7.3.3).\n'+r'\end{proof}'+'\n\n'+r'\oldpage[III]{184}'+'\n\n',
'7:7.7.6:10':'\n'+r'\textup{(de donde un isomorfismo de funtores}'+'\n',
'7:7.7.6:14':r' es exacto por la izquierda. Basta entonces aplicar la equivalencia de (7.7.5, \emph{b)}) y (7.7.5, \emph{b',
'7:7.7.6:15':')}) para ',
'7:7.8.4:15':'\n(donde se trata de longitudes de ',
'7:7.8.4:38':r'-módulo plano (7.3.3, \emph{f)}), luego libre (\textbf{0}, 10.1.3), puesto que se trata de un ',
'7:7.8.10:14':' (donde ',
'7:7.8.10:15':') sea espectro de un álgebra separable sobre ',
'7:7.8.10:17':'); resultará entonces de (7.8.7, (ii)) que la hipótesis hecha sobre el punto ',
},name='source-punctuation-and-page-boundaries')
for ed in ['current','diplomatic']:
 def fn(k,t,f):
  t=t.replace(r'\oldpage[0\textsubscript{III-1}]',r'\oldpage[0\textsubscript{III}]')
  for loc,token in [('12.1.1',r'\oldpage[0\textsubscript{III}]{49}'),('2.1.1',r'\oldpage[III]{95}'),('2.1.7',r'\oldpage[III]{98}')]:
   if k==loc:t=t.replace(token,'')
  if k=='4.3.10' and ed=='diplomatic':
   q=r'\oldpage[III]{134}';start=t.find(q)
   if start>=0:t=t[:start+len(q)]+t[start+len(q):].replace(q,'')
  for loc,token in [('1.1.2',r'\oldpage[III]{83}'),('4.4.5',r'\oldpage[III]{137}')]:
   if k==loc and token not in t:t=t.rstrip()+'\n\n'+token+'\n\n'
  return t
 update(ed,'1',fn)
update('current','7',lambda k,t,f:t.replace('% La página impresa 216 está en blanco.\n\\clearpage\n','% La página impresa 216 está en blanco.\n\\clearpage\n\\oldpage[III]{216}\n'))

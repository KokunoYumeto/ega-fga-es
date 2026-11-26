#!/usr/bin/env python3
"""Carry Spanish clause punctuation from the November 15 respell review, outside formulas."""
import reconcile_iv2 as r
P=[
(213,'ega4-2_2.1.8_through_2.1.14_ES','2.1.14',r'$x\in X$ y por',r'$x\in X$, y por'),
(217,'ega4-2_4.1.1_4.1.2_ES','4.1.2.1',r'n\textsuperscript{o}~1, th.~1) existe',r'n\textsuperscript{o}~1, th.~1), existe'),
(218,'ega4-2_4.1.1_4.1.2_ES','4.1.2.1',r"Cuando $n'\geqslant n$ se tendrá",r"Cuando $n'\geqslant n$, se tendrá"),
(241,'ega4-2_5.4.1_ES','5.4.1',r'$0\leq i\leq n-1$ existe una',r'$0\leq i\leq n-1$, existe una'),
(246,'ega4-2_5.11.4_5.11.7_ES','5.11.5','(5.11.1) que $\\operatorname{codim}','(5.11.1), que $\\operatorname{codim}'),
(249,'ega4-2_5.12.5_5.12.7_ES','5.12.5','se tiene, por (5.12.1)\n','se tiene, por (5.12.1),\n'),
(260,'ega4-2_6.11.8_6.11.9_ES','6.11.8',r'$x\in V\cap W$ se tiene',r'$x\in V\cap W$, se tiene'),
(266,'ega4-2_6.7.5_ES','6.7.5','resulta de (4.6.1) que\ncuando','resulta de (4.6.1) que,\ncuando'),
]
if __name__=='__main__':
 for layer in ['CURRENT','DIPLOMATIC']:
  for row,name,place,old,new in P:
   file='tree/worktree/es/'+layer+'/EGA_IV2/'+name+('.tex' if layer=='CURRENT' else '.diplomatic.tex')
   r.change(file,place,old,new,'respelling','EGA_ES_FINISH_4_HECHO/done/RESPELL_CORRECTIONS_20261115.jsonl:'+str(row)+'; source clause checked in French IV.'+place)

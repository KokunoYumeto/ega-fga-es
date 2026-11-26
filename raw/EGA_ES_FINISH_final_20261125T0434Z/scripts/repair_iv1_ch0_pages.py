#!/usr/bin/env python3
"""Restore original page markers to their corresponding translated clauses.
Math gaps are paired by the already verified whole-file formula sequence.
Each nontrivial insertion point below was read against the French clause.
"""
from pathlib import Path
import re,csv,bisect
from tex_tools import math_spans,retain_translated_text
r=Path(__file__).resolve().parents[1];root=r.parent/'source/EGA_ES_FINISH_1_FRANCES/fr';changes=[];texts={}
pat=re.compile(r'\\oldpage\[[^\]]+\]\{([^}]+)\}')
anchors=re.compile(r'\\(?:label|tag|EGAReaderTarget)\{[^}]+\}(?:\{[^}]+\})?')
# The insertion occurs just before the named literal within its math gap;
# empty literal means the beginning of that gap. Special homogeneous word
# split at p.139 mirrors the French printed-page split.
points={
 ('15','14'):r'\begin{env}[15.1.5]',('15','15'):'en',('15','20'):r'\begin{corollary}[15.1.20]',('15','22'):r'\begin{proposition}[15.2.5]',
 ('16','23'):r'\begin{env}[16.1.3]',('16','25'):r'\begin{proposition}[16.1.8]',('16','26'):r'\begin{lemma}[16.2.2.1]',
 ('19','69'):r'\section{',('19','75'):r'\item[\textup{a)}]',('19','80'):'',('19','81'):r'\item[\textup{(ii)}]',('19','82'):'el álgebra',('19','83'):'',('19','89'):'una',('19','90'):r'\subsection{',('19','91'):'',('19','92'):'formalmente',('19','93'):r'\begin{env}[19.5.4.3]',('19','95'):'homomorfismo sobreyectivo',('19','106'):'',
 ('20','117'):r'\subsection{',('20','119'):r'\subsection{',('20','128'):r'\subsection{',('20','129'):'',('20','134'):r'\item[\rm(iv)]',('20','139'):'morfismo característico',('20','153'):'metrizable',
 ('21','156'):'',('21','162'):'',('21','163'):r'\begin{proof}',('21','172'):'',('21','176'):'que',
 ('22','184'):'invertible',('22','186'):'mismo',('23','221'):'finita'
}
for ed in ['current','diplomatic']:
 for fp in sorted((root/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
  p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed.upper())/'ega4'/fp.name.replace('-fr.tex','-es.tex');fr=fp.read_text();es=p.read_text();n=fp.name.removeprefix('ega0-').removesuffix('-fr.tex');fs=math_spans(fr);ss=math_spans(es)
  assert len(fs)==len(ss),(ed,n,len(fs),len(ss))
  assert all(re.sub(r'\s+','',retain_translated_text(f.text,s.text) or f.text)==re.sub(r'\s+','',s.text) for f,s in zip(fs,ss)),(ed,n)
  source_pages={m.group(1) for m in pat.finditer(fr)}
  for m in reversed(list(pat.finditer(es))):
   if m.group(1) not in source_pages:
    assert n=='15' and m.group(1)=='12'
    changes.append([str(p.relative_to(r)),'oldpage 12',m.group(),'','own comparison','Extra marker absent from supplied French ega0-15-fr.tex; page12 is already marked in §14'])
    es=es[:m.start()]+es[m.end():]
  for fm in pat.finditer(fr):
   old=[m for m in pat.finditer(es) if m.group(1)==fm.group(1)];assert len(old)==1;sm=old[0];ss=math_spans(es)
   i=bisect.bisect_right([x.end for x in fs],fm.start());j=bisect.bisect_right([x.end for x in ss],sm.start())
   fa=anchors.findall(fr[:fm.start()]);sa=anchors.findall(es[:sm.start()])
   if i==j and (fa[-1] if fa else '')==(sa[-1] if sa else ''):continue
   key=(n,fm.group(1));assert key in points,(ed,key)
   oldcontext=es[max(0,sm.start()-80):sm.end()+80];marker=sm.group();es=es[:sm.start()]+es[sm.end():];ss=math_spans(es)
   lo=ss[i-1].end if i else 0;hi=ss[i].start if i<len(ss) else len(es);gap=es[lo:hi];anchor=points[key]
   if anchor:
    assert gap.count(anchor)==1,(ed,key,repr(gap),anchor)
    pos=lo+gap.index(anchor)
   else:pos=lo
   insert='\n'+marker+'\n'
   if key==('20','139'):insert='%\n'+marker+'\n'
   es=es[:pos]+insert+es[pos:];newcontext=es[max(0,pos-80):pos+len(insert)+80]
   changes.append([str(p.relative_to(r)),'oldpage '+fm.group(1),oldcontext,newcontext,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/IV1/native/ega4/'+fp.name+': marker restored within corresponding translated clause'])
  texts[p]=es
for p,t in texts.items():p.write_text(t)
with (r/'records/IV1_CH0_CHANGES_pages.tsv').open('w') as f:w=csv.writer(f,delimiter='\t');w.writerow(['file','place','before','after','kind','source']);w.writerows(changes)
print('Page-marker restorations:',len(changes))

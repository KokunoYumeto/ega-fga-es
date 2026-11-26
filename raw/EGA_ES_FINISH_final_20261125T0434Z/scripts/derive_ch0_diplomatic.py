#!/usr/bin/env python3
"""Derive diplomatic Spanish variants from the supplied French layer deltas.
No source text is bundled. Supply --source-root for the unpacked input archive.
"""
import runpy,re,csv,sys
from pathlib import Path
v=runpy.run_path(str(Path(__file__).with_name('verify_ch0_translation.py')))
out=v['out'];a=v['a'];keys=v['keys'];names=v['filenames'];mathre=v['mathre'];maths=v['maths'];marks=v['marks']
fr=v['fr'];starts=v['starts'];dipname='EGA_ES_FINISH_1_FRANCES/fr/diplomatic/BASE/native/ega1/ega0-1-fr.tex';dfr=(a.source_root/dipname).read_text()
ds=[]
for key in keys:
 pos=re.search(r'\\begin\{[^}]+\}\['+re.escape(key)+r'\]',dfr).start()
 if key!='4.4.3':
  h=list(re.finditer(r'\\(?:subsection|section)\{',dfr[:pos]))[-1].start()
  if key in ['5.1.1','7.1.1']:h=list(re.finditer(r'\\section\{',dfr[:pos]))[-1].start()
  pos=h
 ds.append(pos)
ds.append(len(dfr))
manual={
 'ega0_i_5_1.tex': [('suma directa finita de','suma directa de')],
 'ega0_i_5_4.tex': [('$f^*(\\mathcal{L})$, restringido a la categoría de los $\\mathcal{O}_X$-Módulos invertibles,','$f^*(\\mathcal{L})$ en la categoría de los $\\mathcal{O}_X$-Módulos libres')],
 'ega0_i_7_6.tex': [('lo que, por el corolario (7.2.8), termina de demostrar la proposición\n    (7.6.11).','lo que termina de demostrar la proposición\n    (7.2.8).')],
 'ega0_i_7_7.tex': [('$w:(B\\otimes_A C)^\\wedge\\to D$ tal que','$w:(B\\otimes_A C)^\\wedge\\to D$ y uno solo tal que')]
}
variants=[];audit=[]
for i,name in enumerate(names):
 p=out/'tree/worktree/es/CURRENT/EGA_I_ch0'/name
 if not p.exists():continue
 es=p.read_text();fc=fr[starts[i]:starts[i+1]];fd=dfr[ds[i]:ds[i+1]]
 cm=list(mathre.finditer(fc));dm=list(mathre.finditer(fd));em=list(mathre.finditer(es))
 assert len(cm)==len(dm)==len(em),(name,len(cm),len(dm),len(em))
 for c,d,e in reversed(list(zip(cm,dm,em))):
  if re.sub(r'\s+','',c.group())!=re.sub(r'\s+','',d.group()):
   es=es[:e.start()]+d.group()+es[e.end():]
   units=list(re.finditer(r'\\begin\{[^}]+\}\[([\d.]+)\]',fc[:c.start()]))
   key=units[-1].group(1) if units else keys[i]
   variants.append([name,'0.'+key,'math',c.group(),d.group()])
 for before,after in manual.get(name,[]):
  assert es.count(before)==1,(name,before,es.count(before))
  es=es.replace(before,after)
  variants.append([name,keys[i],'prose',before,after])
 target=out/'tree/worktree/es/DIPLOMATIC/EGA_I_ch0'/name;target.write_text(es)
 assert maths(es)==maths(fd),name
 assert marks(es)==marks(fd),name
 audit.append([str(target.relative_to(out)),len(dm),len(em),True,True])
# Earlier units absent from the diplomatic working tree have identical French
# prose except the three local readings recorded below. Current-only source
# notes are intentionally not copied into the diplomatic edition.
orig=a.source_root/'EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch0'
existing_added=[]
for p in sorted(orig.glob('ega0_i_*.tex')):
 target=out/'tree/worktree/es/DIPLOMATIC/EGA_I_ch0'/p.name
 if (a.source_root/'EGA_ES_FINISH_2_ESPANOL/worktree/es/DIPLOMATIC/EGA_I_ch0'/p.name).exists():continue
 es=(out/'tree/worktree/es/CURRENT/EGA_I_ch0'/p.name).read_text()
 if p.name=='ega0_i_1_6_7.tex':
  before='$M=M_n$';after='$M=M_{\\imath}$';assert es.count(before)==1;es=es.replace(before,after)
  variants.append([p.name,'0.1.6.1','math',before,after])
 if p.name=='ega0_i_2_1_5_8.tex':
  before='$Z\\cap f^{-1}(y)$ de $f^{-1}(y)$, siendo los puntos genéricos';after='$Z\\cap f^{-1}(Y)$ de $f^{-1}(y)$, siendo los puntos genéricos';assert es.count(before)==1;es=es.replace(before,after)
  variants.append([p.name,'0.2.1.8','math',before,after])
 # French inter-section is only a word-break artifact; Spanish intersección stays.
 target.write_text(es);existing_added.append(str(target.relative_to(out)))
with (out/'records/DIPLOMATIC_VARIANTS_ch0.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['file','place','kind','current','diplomatic']);w.writerows(variants)
with (out/'records/FORMULA_AUDIT_ch0_diplomatic_new.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['file','french_math_spans','spanish_math_spans','math_equal_ignoring_whitespace_and_text_words','markers_equal']);w.writerows(audit)
with (out/'records/DIPLOMATIC_ASSEMBLY_ch0.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['file','action','source']);w.writerows([[x,'assembled missing diplomatic unit from existing Spanish; French layer deltas applied','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch0/'+Path(x).name] for x in existing_added])
print('New diplomatic files:',len(audit),'variant rows:',len(variants),'earlier units added:',len(existing_added))

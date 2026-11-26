#!/usr/bin/env python3
"""Audit translated EGA I chapter 0 math, labels and original page markers.
Run with --source-root pointing to the unpacked user-provided archive.
This checks transcription fidelity, not the truth of mathematical statements.
"""
import argparse,csv,re,difflib
from pathlib import Path
P=argparse.ArgumentParser();P.add_argument('--source-root',type=Path,required=True);P.add_argument('--write-progress-records',action='store_true');a=P.parse_args()
out=Path(__file__).resolve().parents[1]
srcname='EGA_ES_FINISH_1_FRANCES/fr/current/BASE/native/ega1/ega0-1-fr.tex'
fr=(a.source_root/srcname).read_text()
keys=['4.4.3','5.1.1','5.2.1','5.3.1','5.4.1','5.5.1','6.0','6.1.1','6.2.1','6.3.1','6.4.1','6.5.1','6.6.1','6.7.1','7.1.1','7.2.1','7.3.1','7.4.1','7.5.1','7.6.1','7.7.1','7.8.1']
filenames=['ega0_i_4_4_3_8.tex']+['ega0_i_'+'.'.join(k.split('.')[:2]).replace('.','_')+'.tex' for k in keys[1:]]
starts=[]
for k in keys:
 m=re.search(r'\\begin\{[^}]+\}\['+re.escape(k)+r'\]',fr)
 pos=m.start()
 if k!='4.4.3':
  prev=fr[:pos]; h=list(re.finditer(r'\\(?:subsection|section)\{',prev))[-1].start()
  if k in ['5.1.1','7.1.1']:h=list(re.finditer(r'\\section\{',prev))[-1].start()
  pos=h
 starts.append(pos)
starts.append(len(fr))
mathre=re.compile(r'\\\[.*?\\\]|(?<!\\)\$.*?(?<!\\)\$',re.S)
def maths(t):
 return [re.sub(r'\s+','',re.sub(r'\\text\{[^{}]*\}',r'\\text{WORDS}',m)) for m in mathre.findall(t)]
def marks(t):return re.findall(r'\\(?:label|oldpage|EGAReaderTarget|tag)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?',t)
checks=[];tr=[];events=[]
for i,(k,name) in enumerate(zip(keys,filenames)):
 p=out/'tree/worktree/es/CURRENT/EGA_I_ch0'/name
 if not p.exists():continue
 es=p.read_text();s=fr[starts[i]:starts[i+1]]
 fm,em=maths(s),maths(es);mm=marks(s)==marks(es)
 checks.append([str(p.relative_to(out)),len(fm),len(em),fm==em,mm])
 if fm!=em:
  print('MATH MISMATCH',name)
  for line in list(difflib.unified_diff(fm,em))[:25]:print(line)
 if not mm:print('MARKER MISMATCH',name)
 words=len(re.findall(r'[A-Za-zÀ-ÿ]+',re.sub(r'\\[A-Za-z]+',' ',mathre.sub(' ',es))))
 ids=re.findall(r'\\begin\{[^}]+\}\[([\d.]+)\]',s)
 tr.append([str(p.relative_to(out)),srcname,ids[0]+'–'+ids[-1],words])
 for id in ids:events.append(['0.'+id,'2026-11-25','GPT-6 Astra; effort inherited, not separately reported; ch0 translation run','carried as background without fault found','Translated from supplied corrected French; no proof verification claimed. TeX fidelity audited separately.'])
def write(name,head,rows):
 with (out/'records'/name).open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
write('FORMULA_AUDIT_ch0.tsv',['file','french_math_spans','spanish_math_spans','math_equal_ignoring_whitespace_and_text_words','markers_equal'],checks)
if a.write_progress_records:write('TRADUCCION_ch0.tsv',['file','french_source','range','words'],tr)
if a.write_progress_records:write('CHECK_EVENTS_ch0.tsv',['statement_id','date','who','type','outcome'],events)
print('Audited',len(checks),'translated files;',sum(int(r[3] and r[4]) for r in checks),'passed;',len(events),'numbered statements carried.')

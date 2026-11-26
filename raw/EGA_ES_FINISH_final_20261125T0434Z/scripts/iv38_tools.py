"""Isolated IV3 section-8 source-fidelity work; no shared IV3 journal writes."""
from pathlib import Path
import re,csv,json,difflib
from tex_tools import math_spans,balanced_end,retain_translated_text
from iv3_align import units,key
from iv3_core import spans as core_spans,note_ranges
ROOT=Path(__file__).resolve().parents[1]
FP=ROOT.parent/'source/EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/ega4-8-fr.tex'
SP=ROOT/'tree/worktree/es/PORTED_20261109/IV3/sections/ega4-8.tex'
SOURCE='EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/ega4-8-fr.tex'
HEADER=['file','place','before','after','kind','source']
def write(name,header,rows):
 with (ROOT/'records'/name).open('w',encoding='utf-8',newline='') as f:w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
def read(name):return list(csv.DictReader((ROOT/'records'/name).open(),delimiter='\t'))
def apply(edits,name,kind='own comparison'):
 t=SP.read_text();rows=[];last=len(t)+1
 for a,b,new,place,why in sorted(edits,reverse=True):
  assert b<=last,('overlap',a,b,last);last=a
  old=t[a:b]
  if old==new:continue
  t=t[:a]+new+t[b:];rows.append([str(SP.relative_to(ROOT)),place,old,new,kind,SOURCE+': '+place+'; '+why])
 SP.write_text(t);write('IV38_CHANGES_'+name+'.tsv',HEADER,rows);print(name,'changes',len(rows))
 return rows
def patch(unit,old,new,name,expected=1):
 t=SP.read_text();u=units(t)[unit];pat=re.compile(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',old.strip())),re.S);ms=list(pat.finditer(u.text));assert len(ms)==expected,(unit,len(ms),old)
 return apply([(u.start+m.start(),u.start+m.end(),new,unit,'Bilingual clause comparison; source wording/formula order restored.') for m in ms],name)

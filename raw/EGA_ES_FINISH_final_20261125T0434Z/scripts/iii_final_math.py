#!/usr/bin/env python3
from iii_bridge_patch import *
from tex_tools import is_escaped

def run():
 report=[];counts={}
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,paired,gaps=compare(ed,part);assert not gaps,(ed,part,len(gaps));edits=[];ng=0
  for q in paired:
   new=translate_math(q['f'])
   if new!=q['e']:edits.append((q['estart'],q['eend'],new,q['place'],q['e']))
   for m in re.finditer(r'\\(?:text|textup|mbox|hbox)\{',q['f']):
    z=balanced_end(q['f'],m.end()-1);raw=q['f'][m.end():z-1]
    if re.search('[A-Za-zÀ-ÿ]{2}',raw):
     ng+=1;report.append(dict(edition=ed,part=part,place=q['place'],source_argument=raw,translated_formula=new,verdict='explicit translated prose; all nested mathematical content taken from source' if raw in __import__('iii_restore_local_math').TEXT else 'mathematical hbox content retained literally'))
  if edits:apply_edits(ed,part,edits,b)
  counts[ed+'_'+part]=dict(source_formulas=len(paired),changes=len(edits),text_and_hbox_groups=ng)
 (ROOT/'records/III_MATH_TEXT_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(counts)
if __name__=='__main__':run()

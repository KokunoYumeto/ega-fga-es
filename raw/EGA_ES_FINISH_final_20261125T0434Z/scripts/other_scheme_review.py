"""Read-only source-bounded schéma/préschéma comparison in OTHER scopes."""
import re,json,difflib,collections,argparse
from corpus import RESULT,FR,write_tsv
from root_scope_pairs import pairs,scoped_units,resolve
from audit_i_ch1 import mask_notes
from tex_tools import math_spans,math_loose_key

FP=re.compile(r'\b(?:sous-)?(?:pré)?schémas?\b',re.I)
SP=re.compile(r'\b(?:sub-?)?(?:pre-?)?esquemas?\b',re.I)
def typ(t,fr=False):
 t=t.lower();return ('sub' if t.startswith('sous-' if fr else 'sub') else '')+('pre' if ('pré' if fr else 'pre') in t else '')+'esquema'
def mask(t):
 t=mask_notes(t);out=list(t)
 for m in re.finditer(r'(?<!\\)%[^\n]*',t):out[m.start():m.end()]=' '*(m.end()-m.start())
 # Exclude publication titles in a bibliography while retaining following indexes.
 for m in re.finditer(r'\\section\*?\{BIBLIO(?:GRAPHIE|GRAFÍA)',t,re.I):
  nxt=re.search(r'\\section\*?\{',t[m.end():]);end=m.end()+nxt.start() if nxt else len(t)
  out[m.start():end]=' '*(end-m.start())
 return ''.join(out)
def run(tag='initial'):
 rows=[];summaries=[];matching=0;terms=0;gaps=0;unmatched=[]
 for scope,ed,fp,ft,st,p,off,fn in pairs():
  if scope in {'I','IV4'}:continue
  fu=scoped_units(ft,fn);su=scoped_units(st,fn);src=str(fp.relative_to(FR.parent.parent));pterms=0;pgaps=0;pmatch=0
  for n,f in fu.items():
   if n not in su:unmatched.append([scope,ed,src,n]);continue
   s=su[n];ftext=mask(f.text);stext=mask(s.text);ff=math_spans(ftext);ss=math_spans(stext);links=[]
   for bl in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_matching_blocks():
    links.extend((bl.a+i,bl.b+i) for i in range(bl.size))
   anchors=[(-1,-1)]+links+[(len(ff),len(ss))]
   for (fa,sa),(fb,sb) in zip(anchors,anchors[1:]):
    a=ff[fa].end if fa>=0 else 0;b=ff[fb].start if fb<len(ff) else len(ftext)
    c=ss[sa].end if sa>=0 else 0;d=ss[sb].start if sb<len(ss) else len(stext)
    fc=ftext[a:b];ec=stext[c:d]
    # Unmatched formula bodies remain excluded from lexical comparison.
    for q in reversed(math_spans(fc)):fc=fc[:q.start]+' '*(q.end-q.start)+fc[q.end:]
    for q in reversed(math_spans(ec)):ec=ec[:q.start]+' '*(q.end-q.start)+ec[q.end:]
    fm=list(FP.finditer(fc));sm=list(SP.finditer(ec));terms+=len(fm);pterms+=len(fm);gaps+=1;pgaps+=1
    if not fm and not sm:continue
    at=[typ(m[0],True) for m in fm];bt=[typ(m[0]) for m in sm]
    if at==bt:matching+=1;pmatch+=1;continue
    out={'id':len(rows),'scope':scope,'edition':ed,'source':src,'place':n,'source_line':ft.count('\n',0,f.start+a)+1,'source_offset':f.start+a,'french':fc,'spanish':ec,'source_terms':[m[0] for m in fm],'target_terms':[m[0] for m in sm],'source_types':at,'target_types':bt,'spanish_matches':[],'aligned_neighbors_only':fb==fa+1 and sb==sa+1,'math_anchors':[fa,fb,sa,sb]}
    for m in sm:
     q,pos=resolve(st,s.start+c+m.start(),p,off)
     out['spanish_matches'].append({'file':str(q.relative_to(RESULT)),'start':pos,'end':pos+len(m[0]),'word':m[0],'line':q.read_text().count('\n',0,pos)+1})
    out['class']='homogeneous same count' if len(fm)==len(sm) and len(set(at))==1 else 'mixed same count' if len(fm)==len(sm) else 'count difference'
    rows.append(out)
  summaries.append([scope,ed,src,len(fu),pgaps,pterms,pmatch])
 base=RESULT/'records'
 (base/f'OTHER_SCHEME_REVIEW_{tag}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 write_tsv(base/f'OTHER_SCHEME_COVERAGE_{tag}.tsv',['scope','edition','source','units','intervals','source_terms','matching_term_intervals'],summaries)
 write_tsv(base/f'OTHER_SCHEME_MISSING_UNITS_{tag}.tsv',['scope','edition','source','unit'],unmatched)
 counts={'terms':terms,'intervals':gaps,'matching':matching,'discrepancy_intervals':len(rows),'classes':dict(collections.Counter(r['class'] for r in rows)),'scopes':dict(collections.Counter(r['scope'] for r in rows)),'unmatched_source_units':len(unmatched)}
 (base/f'OTHER_SCHEME_COUNTS_{tag}.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n');print(json.dumps(counts))
 for r in rows:
  if r['edition']=='current':print(r['id'],r['scope'],r['place'],r['class'],r['source_terms'],r['target_terms'],'FR',re.sub(r'\s+',' ',r['french'])[:200],'ES',re.sub(r'\s+',' ',r['spanish'])[:200])
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='initial');args=ap.parse_args();run(args.tag)

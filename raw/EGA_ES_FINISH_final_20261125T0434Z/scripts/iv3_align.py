"""IV3 formula alignment including free-standing numbered source statements."""
from pathlib import Path
import re,sys,json,collections,difflib,argparse,bisect
from corpus import RESULT,FR,write_tsv,canonical
from tex_tools import Span,numbered_units,math_spans,math_loose_key,retain_translated_text,balanced_end
from iv3_work import DIR,apply_edits

def key(t):
 # The one hbox conjunction is translated prose, not a mathematical variable.
 t=t.replace(r'\hbox{y}',r'\hbox{et}')
 t=t.replace('\\\\',' ')
 for a,b in [(r'\setminus',r'\setmin'),(r'\rightarrow',r'\to'),(r'\mapsto',r'\leadsto'),(r'\dots',r'\ldots'),(r'\tfrac',r'\frac'),(r'\dfrac',r'\frac'),(r'\mathbb',r'\mathbf')]:
  t=re.sub(re.escape(a)+r'(?![A-Za-z])',lambda m:b,t)
 # Font wrappers, including multiletter abbreviations, are comparison-only.
 # Preserve the literal French wrapper when applying an aligned formula.
 fp=re.compile(r'\\(?:mathbf|mathrm|mathcal|mathscr|mathfrak|boldsymbol)\s*\{')
 while True:
  m=fp.search(t)
  if not m:break
  e=balanced_end(t,m.end()-1);content=t[m.end():e-1]
  if content in {'Spec','Spf','Proj','Hom','Ext','Tor','Ker','Coker','Im','Supp','Ass','Ann','rg','gr','codim','id','Der','Diff','Tr'}:content=r'\operatorname{'+content+'}'
  t=t[:m.start()]+' '+content+' '+t[e:]
 t=re.sub(r'\\(?:mathbf|mathrm|mathcal|mathscr|mathfrak|boldsymbol)\s+([A-Za-z0-9])',r' \1 ',t)
 t=re.sub(r'\\(?:mathbf|mathrm|mathcal|mathscr|mathfrak|boldsymbol)\s*\{([0-9])\}',r'\1',t)
 t=re.sub(r'\\(?:mathbf|mathrm|mathcal|mathscr|mathfrak|boldsymbol)\s+([0-9])',r'\1',t)
 t=re.sub(r'\\bar\s*\{\s*([A-Za-z])\s*\}',r'\\overline{\1}',t)
 t=re.sub(r'\\bar\s+([A-Za-z])',r'\\overline{\1}',t)
 # TeX accepts either order for adjacent subscript/superscript arguments.
 def arg_end(t,i):
  while i<len(t) and t[i].isspace():i+=1
  if i>=len(t):return i
  if t[i]=='{':return balanced_end(t,i)
  if t[i]=='\\':
   m=re.match(r'\\(?:[A-Za-z]+|.)',t[i:]);return i+len(m.group())
  return i+1
 edits=[]
 for m in re.finditer(r'\^',t):
  e=arg_end(t,m.end());j=e
  while j<len(t) and t[j].isspace():j+=1
  if j<len(t) and t[j]=='_':
   end=arg_end(t,j+1);edits.append((m.start(),end,t[j:end]+t[e:j]+t[m.start():e]))
 for a,b,new in reversed(edits):t=t[:a]+new+t[b:]
 k=math_loose_key(t).replace(r'\operatorname','')
 k=re.sub(r'\\(dim|prof|depth|deg|tr|rank|long|card|Spec|Spf|Proj|Hom|Ext|Tor|Ker|Coker|Im|Supp|Ass|Ann|rg|gr|codim|id|Der|Diff|Tr)(?![A-Za-z])',r'\1',k)
 return k

def units(t):
 existing=numbered_units(t);starts={n:s.start for n,s in existing.items()};mm=math_spans(t);ms=[s.start for s in mm]
 def inside_math(a):
  j=bisect.bisect_right(ms,a)-1
  return j>=0 and a<mm[j].end
 pattern=r'\\(?:label\{(IV\.[^}]+)\}|EGAReaderTarget\{[^}]+\}\{(IV\.[^}]+)\})'
 for m in re.finditer(pattern,t):
  raw=m.group(1) or m.group(2);k=canonical(raw)
  if not re.fullmatch(r'IV\.\d+\.\d+\.\d+(?:\.\d+)*',k) or inside_math(m.start()):continue
  n=k[3:]
  if n not in starts:starts[n]=m.start()
 # Printed backmatter is translated in a separate Spanish file.
 cutoff=t.find('\\clearpage\n\\oldpage[IV-3]{249}')
 if cutoff<0:cutoff=len(t)
 ordered=sorted((a,n) for n,a in starts.items() if a<cutoff)
 out={}
 for j,(a,n) in enumerate(ordered):
  b=ordered[j+1][0] if j+1<len(ordered) else cutoff
  out[n]=Span(a,b,t[a:b],existing[n].kind if n in existing else 'labelled_statement')
 if ordered:out['front']=Span(0,ordered[0][0],t[:ordered[0][0]],'front')
 return out

def pairs():
 for fp in sorted((FR/'current/IV3/native/ega4').glob('ega4-*-fr.tex')):
  q=DIR/'sections'/fp.name.replace('-terminal','').replace('-fr.tex','.tex')
  if q.exists():yield fp,q

def run(apply=False):
 from iv3_core import spans as core_spans
 report=[];summary=[];dry=[];blocks=[];serial=0;changed=0
 for fp,q in pairs():
  ft=fp.read_text();st=q.read_text();fu=units(ft);su=units(st);edits=[]
  for n,fs in fu.items():
   if n=='front' and '-terminal-' in fp.name:continue
   if n not in su:
    report.append([fp.name,n,'missing_unit',str(q.relative_to(RESULT)),'','']);continue
   ss=su[n];ff=core_spans(fs.text);sf=core_spans(ss.text);fk=[key(s.text) for s in ff];sk=[key(s.text) for s in sf]
   aligned=0;delta=0
   for op,a,b,c,d in difflib.SequenceMatcher(None,fk,sk,autojunk=False).get_opcodes():
    if op=='equal':
     for i,j in zip(range(a,b),range(c,d)):
      aligned+=1
      if ff[i].text!=sf[j].text:
       new=retain_translated_text(ff[i].text,sf[j].text)
       if new is not None and r'\hbox{y}' in sf[j].text:
        new=new.replace(r'\hbox{et}',r'\hbox{y}')
       if new is not None and new!=sf[j].text:
        if new.startswith('$') and not new.startswith('$$') and not sf[j].text.startswith('$'):
         fm=re.match(r'\s*([.,;:!?])',fs.text[ff[i].end:]);sm=re.match(r'\s*([.,;:!?])',ss.text[sf[j].end:])
         if fm and not sm and re.search(r'[.,;:!?]\s*(?:\\\]|\\end\{[^}]+\})$',sf[j].text):new+=fm.group(1)
        edits.append((ss.start+sf[j].start,ss.start+sf[j].end,new,n));delta+=1
        dry.append([str(q.relative_to(RESULT)),n,sf[j].text,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'+fp.name+': '+n])
    else:
     fmath=' | '.join(x.text for x in ff[a:b]);smath=' | '.join(x.text for x in sf[c:d]);report.append([fp.name,n,op,str(q.relative_to(RESULT)),fmath,smath])
     fa=ff[a].start if a<len(ff) else len(fs.text);fb=ff[b-1].end if b>a else fa
     sa=sf[c].start if c<len(sf) else len(ss.text);sb=sf[d-1].end if d>c else sa
     blocks.append({'id':serial,'source':fp.name,'target':str(q.relative_to(RESULT)),'place':n,'kind':op,'f_range':[fs.start+fa,fs.start+fb],'s_range':[ss.start+sa,ss.start+sb],
      'french_math':fmath,'spanish_math':smath,'french_context':fs.text[max(0,fa-180):min(len(fs.text),fb+220)],'spanish_context':ss.text[max(0,sa-180):min(len(ss.text),sb+220)]});serial+=1
   summary.append([fp.name,n,len(ff),len(sf),aligned,delta])
  if apply and edits:apply_edits(q,edits,fp.name)
  changed+=len(edits)
 write_tsv(RESULT/'records/IV3_NOTATION_UNMATCHED.tsv',['source','place','kind','target','french_math','spanish_math'],report)
 write_tsv(RESULT/'records/IV3_NOTATION_SUMMARY.tsv',['source','place','french_formulas','spanish_formulas','aligned','changes'],summary)
 write_tsv(RESULT/'records/IV3_NOTATION_DRY_RUN.tsv',['file','place','before','after','kind','source'],dry)
 (RESULT/'records/IV3_ALIGNMENT_BLOCKS.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'apply':apply,'units':len(summary),'formulas':sum(x[2] for x in summary),'aligned':sum(x[4] for x in summary),'changes':changed,'unmatched':len(report)}))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');run(ap.parse_args().apply)

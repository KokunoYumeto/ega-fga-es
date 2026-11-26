#!/usr/bin/env python3
"""Whole-reader III source alignment, including prose crossing input-file boundaries."""
from pathlib import Path
import re,json,collections,difflib,argparse
from corpus import RESULT,FR
from tex_tools import math_spans,numbered_units,ENV_RE,retain_translated_text,balanced_end
ROOT=RESULT

def script_token(s,i):
 if i>=len(s):return '',i
 if s[i]=='{':j=balanced_end(s,i);return s[i:j],j
 if s[i]=='\\':
  m=re.match(r'\\[A-Za-z]+|\\.',s[i:]);j=i+len(m[0]);return s[i:j],j
 return s[i],i+1

def canonical_scripts(s):
 out=[];i=0
 while i<len(s):
  if s[i] in '^_':
   a=s[i];x,j=script_token(s,i+1)
   if j<len(s) and s[j] in '^_' and s[j]!=a:
    b=s[j];y,k=script_token(s,j+1);q={a:x,b:y};out.append('_'+q['_']+'^'+q['^']);i=k;continue
  out.append(s[i]);i+=1
 return ''.join(out)

def weak(s):
 s=re.sub(r'\\(?:label|tag)\{[^}]*\}','',s)
 s=re.sub(r'\\(?:begin|end)\{[^}]*\}','',s)
 s=s.strip('$').removeprefix('\\[').removesuffix('\\]').removeprefix('\\(').removesuffix('\\)')
 s=re.sub(r'\\(?:text|textup|mbox)\{(?:[^{}]|\{[^{}]*\})*\}',r'\\TEXT',s)
 s=s.replace(r'\xrightarrow{\sim}','ISO').replace(r'\overset{\sim}{\longrightarrow}','ISO')
 alias={'neq':r'\ne','Set':'Ens','C':'C','CHom':'Hom','kres':'k','shHom':'Hom','shExt':'Ext','shTor':'Tor','shDer':'Der','shDiff':'Diff','shProj':'Proj','HH':'H','RR':'R','LL':'L','red':'red','op':'^0','simto':'ISO','isoto':'ISO','simeq':'ISO','cong':'ISO','leqslant':r'\leq','le':r'\leq','geqslant':r'\geq','ge':r'\geq','longrightarrow':r'\to','rightarrow':r'\to','longleftarrow':r'\leftarrow','from':r'\leftarrow','widehat':r'\hat','widetilde':r'\tilde','setmin':'-','setminus':'-','vphi':r'\varphi','emp':r'\varnothing','cdots':r'\ldots','longmapsto':r'\leadsto','mapsto':r'\leadsto','implies':r'\Rightarrow','bigoplus':r'\oplus','subseteq':r'\subset','supseteq':r'\supset','varinjlim':r'\lim','varprojlim':r'\lim'}
 for x,y in alias.items():s=re.sub(r'\\'+x+r'(?![A-Za-z])',lambda m:y,s)
 s=re.sub(r'\\(?:operatorname|mathrm|mathcal|mathscr|mathfrak|mathbf|boldsymbol|mathit|mathbb|cat|bb|sh|bm)(?![A-Za-z])','',s)
 s=s.replace('rank','rang').replace('length','long')
 for op in ['Spec','Spf','Proj','Hom','Ext','Tor','Ker','Coker','Im','Supp','Ass','Ann','rg','gr','codim','id','Der','Diff','Tr','dim','det','lim','inf','sup','deg','long','rang','length','lg','coker','ker','im','End','Aut','Sym']:
  s=re.sub(r'\\'+op+r'(?![A-Za-z])',lambda m:op,s)
 s=re.sub(r'\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big|bigg|Bigg|quad|qquad|enspace|thinspace|medspace)(?![A-Za-z])','',s)
 s=re.sub(r'\\(?:hspace|vspace)\*?\{[^}]*\}','',s)
 s=re.sub(r'\\(?:mathop|nolimits|limits|hbox|tiny|scriptstyle)(?![A-Za-z])','',s)
 s=re.sub(r'@(?:C|R)=[\d.]+pt','',s)
 s=re.sub(r'\\[,;! ]','',s);s=s.replace('\\\\','');s=re.sub(r'\s','',s)
 s=canonical_scripts(s)
 s=re.sub(r'[{}~&()]','',s)
 s=re.sub(r'(\\ar\[[^]]+\][_^])-',r'\1',s)
 s=s.replace(r'\prime',"'").replace(r'\circ','0')
 primes=s.count("'");s=s.replace("'",'')
 return s.strip('.,;:')+'PRIMES'+str(primes)

def aggregate(edition,part):
 chunks=[]
 if part=='1':
  folder=ROOT/f'tree/repo/editions/III1_{edition.upper()}'
  reader=folder/f'EGA_III1_ES_{edition.upper()}_READER.tex';t=reader.read_text()
  lo=t.find(r'\clearpage',t.find(r'\maketitle'));hi=t.index(r'\input{ega0/ega0-8}')
  chunks.append((reader,lo,hi))
  for i in range(8,14):p=folder/f'ega0/ega0-{i}.tex';chunks.append((p,0,len(p.read_text())))
  lo=t.index(r'\input{ega0/ega0-13}')+len(r'\input{ega0/ega0-13}');hi=t.index(r'\input{ega3/ega3-1}')
  chunks.append((reader,lo,hi))
  for i in range(1,6):p=folder/f'ega3/ega3-{i}.tex';chunks.append((p,0,len(p.read_text())))
 else:
  folder=ROOT/'tree/repo/editions/III2/units'
  for i in range(1,11 if part=='6' else 10):p=folder/f'III.{part}.{i}.es.tex';chunks.append((p,0,len(p.read_text())))
  if part=='7':p=folder/'III.backmatter.es.tex';chunks.append((p,0,len(p.read_text())))
 text=[];bounds=[];pos=0
 for p,lo,hi in chunks:
  t=p.read_text()[lo:hi];text.append(t);bounds.append((pos,pos+len(t),str(p.relative_to(ROOT)),lo));pos+=len(t)+1
 return '\n'.join(text),bounds

def source(edition,part):return FR/edition/f'BASE/native/ega3/ega3-{part}-fr.tex'
def sections(t):
 marks=[]
 for m in re.finditer(r'\\begin\{(?:env|definition|proposition|theorem|corollary|lemma|remark|remarks|example|examples|scholium|notation|namedtheorem)\}\[([^\]]+)\]',t):
  k=m[1].strip().rstrip('.')
  if re.fullmatch(r'\d+\.\d+\.\d+(?:\s*(?:bis|ter))?',k):marks.append((m.start(),k))
 for m in re.finditer(r'\\par\\medskip\\noindent\\textbf\{(\d+(?:\.\d+)+)\.\}',t):marks.append((m.start(),m[1]))
 marks.sort();return [('opening',0,marks[0][0])]+[(k,lo,marks[i+1][0] if i+1<len(marks) else len(t)) for i,(lo,k) in enumerate(marks)]
def compare(edition='current',part='1'):
 f=source(edition,part).read_text();e,bounds=aggregate(edition,part);fs=sections(f);es=sections(e)
 if [q[0] for q in fs]!=[q[0] for q in es]:raise ValueError(('unit order',edition,part,[x[0] for x in fs if x[0] not in {q[0] for q in es}],[x[0] for x in es if x[0] not in {q[0] for q in fs}]))
 paired=[];gaps=[]
 for (place,lo,hi),(_,x,y) in zip(fs,es):
  fm=math_spans(f[lo:hi]);em=math_spans(e[x:y]);aa=[weak(q.text) for q in fm];bb=[weak(q.text) for q in em]
  for tag,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
   if tag=='equal':
    for u,v in zip(fm[i:j],em[k:l]):paired.append(dict(place=place,fstart=lo+u.start,fend=lo+u.end,estart=x+v.start,eend=x+v.end,f=u.text,e=v.text))
   else:gaps.append(dict(place=place,tag=tag,f=[z.text for z in fm[i:j]],e=[z.text for z in em[k:l]],fpos=[(lo+z.start,lo+z.end) for z in fm[i:j]],epos=[(x+z.start,x+z.end) for z in em[k:l]]))
 return f,e,bounds,paired,gaps

def apply_edits(edition,part,edits,bounds):
 byfile=collections.defaultdict(list)
 for lo,hi,new,place,old in edits:
  p=next((q for q in bounds if q[0]<=lo and hi<=q[1]),None);assert p,('cross input',lo,hi)
  off,_,file,native=p;byfile[file].append((native+lo-off,native+hi-off,new,place,old))
 import csv
 log=ROOT/'records/III_CHANGES_math_aligned.tsv'
 if not log.exists():log.write_text('file\tplace\tbefore\tafter\tkind\tsource\n')
 with log.open('a') as out:
  wr=csv.writer(out,delimiter='\t')
  for file,items in byfile.items():
   p=ROOT/file;t=p.read_text();last=len(t)+1
   for lo,hi,new,place,old in sorted(items,reverse=True):
    assert hi<=last and t[lo:hi]==old,(file,place,'preimage/overlap');t=t[:lo]+new+t[hi:];last=lo
    wr.writerow([file,place,old,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+edition+'/BASE/native/ega3/ega3-'+part+'-fr.tex: '+place+'; source/translation/notation comparison at cited place'])
   p.write_text(t)
 return len(edits)

def run(apply=False):
 result={}
 for edition,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(edition,part);ed=[];untranslated=[]
  for q in p:
   new=retain_translated_text(q['f'],q['e'])
   if new is None:untranslated.append(q);continue
   if new!=q['e']:
    if new.startswith('$') and not new.startswith('$$') and not q['e'].startswith('$'):
     mark=re.match(r'\s*([,.;:!?])',f[q['fend']:]);already=re.match(r'\s*([,.;:!?])',e[q['eend']:])
     if mark and not already and re.search(r'[.,;:!?]\s*(?:\\\]|\\end\{[^}]+\})$',q['e']):new+=mark[1]
    ed.append((q['estart'],q['eend'],new,q['place'],q['e']))
  key=edition+'_'+part;result[key]=dict(formulas=len(math_spans(f)),spanish_formulas=len(math_spans(e)),paired=len(p),gaps=len(g),changes=len(ed),text_review=len(untranslated))
  (ROOT/'records'/('III_GAPS_'+key+'.json')).write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
  (ROOT/'records'/('III_TEXT_REVIEW_'+key+'.json')).write_text(json.dumps(untranslated,ensure_ascii=False,indent=2)+'\n')
  if apply:apply_edits(edition,part,ed,b)
 print(json.dumps(result,ensure_ascii=False));return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args();run(args.apply)

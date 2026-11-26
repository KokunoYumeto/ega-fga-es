"""Compare mathematical content while classifying reference and editorial markup."""
import re,json,difflib,collections,argparse
from corpus import RESULT,FR,write_tsv
from tex_tools import math_spans,balanced_end
from iv3_align import pairs,units,key
from iv3_work import apply_edits

def note_ranges(t):
 out=[]
 for m in re.finditer(r'\\footnote\{',t):
  e=balanced_end(t,m.end()-1);body=t[m.end():e-1]
  if body.startswith(('La fuente impresa','El texto impreso','El francés impreso','El original impreso')):out.append((m.start(),e))
 return out

def classification(s,t,notes):
 if any(a<=s.start<b for a,b in notes):return 'editorial_note'
 if s.start and t[s.start-1:s.start]=='\\' and s.text.startswith(r'\['):return 'layout_spacing'
 if re.search(r'\\sref\[$',t[:s.start]):return 'chapter_reference'
 z=s.text
 if z==r'$^{\mathrm{er}}$':return 'ordinal_marker'
 if re.fullmatch(r'\$[A-Za-z][\x27]*\)\$',z) or re.fullmatch(r"\$'+\$",z):return 'condition_label'
 if re.fullmatch(r'\$(?:[0-9]+)?\^(?:\\circ|\\mathrm\{(?:os|er)\}|\*)\$',z):return 'ordinal_marker'
 if re.fullmatch(r'\$\([^$]*\d+\.\d+[^$]*\)\$',z):return 'reference'
 body=re.sub(r'\\[A-Za-z]+','',z);body=re.sub(r'[\s{}_$]','',body)
 if re.fullmatch(r'0?[IV]{1,3}|0|IV',body):
  following=t[s.end:s.end+100]
  if re.match(r'\s*[,;~]+\s*(?:\\(?:hyperref|sref)[^}]*|[0-9]+\.[0-9]+)',following):return 'chapter_reference'
 return 'core'

def spans(t):
 notes=note_ranges(t);return [s for s in math_spans(t) if classification(s,t,notes)=='core']

def join_key(zs):
 parts=[];primes=0
 for z in zs:
  k=key(z);m=re.search(r'PRIMES(\d+)$',k)
  if m:primes+=int(m.group(1));k=k[:m.start()]
  k=re.sub(r'\\(?:begin|end)(?:gathered|aligned|gather|align)','',k)
  k=re.sub(r'[,;]','',k)
  parts.append(k)
 return ''.join(parts)+'PRIMES'+str(primes)

def pure_gaps(t,ss):
 for a,b in zip(ss,ss[1:]):
  gap=t[a.end:b.start]
  if not re.fullmatch(r'[\s,;:.~]*(?:(?:et|y|e|ou|o)[\s,;:.~]*)?',gap):return False
 return True

def run(apply=False):
 rows=[];allblocks=[];summaries=[];serial=0;edits_count=0;classified=collections.Counter();group_candidates=[]
 for fp,q in pairs():
  ft=fp.read_text();st=q.read_text();fu=units(ft);su=units(st);edits=[]
  for n,f in fu.items():
   if n=='front' and '-terminal-' in fp.name:continue
   if n not in su:continue
   s=su[n]
   for z in math_spans(f.text):classified['source:'+classification(z,f.text,[])]+=1
   ns=note_ranges(s.text)
   for z in math_spans(s.text):classified['spanish:'+classification(z,s.text,ns)]+=1
   ff=spans(f.text);ss=spans(s.text);fk=[key(z.text) for z in ff];sk=[key(z.text) for z in ss];aligned=0
   for op,a,b,c,d in difflib.SequenceMatcher(None,fk,sk,autojunk=False).get_opcodes():
    if op=='equal':aligned+=b-a;continue
    fs=ff[a:b];ts=ss[c:d]
    if op=='replace' and fs and ts and (len(fs)>1 or len(ts)>1) and pure_gaps(f.text,fs) and pure_gaps(s.text,ts) and join_key([z.text for z in fs])==join_key([z.text for z in ts]):
     after=fs[0].text
     for left,right in zip(fs,fs[1:]):
      gap=f.text[left.end:right.start]
      gap=re.sub(r'\bet\b','y',gap);gap=re.sub(r'\bou\b','o',gap)
      after+=gap+right.text
     # Keep Spanish sentence punctuation when an old display consumed it.
     punct=re.search(r'([.,;:!?])\s*(?:\\\]|\\end\{[^}]+\})$',ts[-1].text)
     following=s.text[ts[-1].end:]
     if after.endswith('$') and punct and not re.match(r'\s*[.,;:!?]',following):after+=punct.group(1)
     start=s.start+ts[0].start;end=s.start+ts[-1].end
     group_candidates.append([str(q.relative_to(RESULT)),n,st[start:end],after,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'+fp.name+': '+n+'; regrouped literal formulas'])
     edits.append((start,end,after,n));continue
    fm=' | '.join(z.text for z in fs);sm=' | '.join(z.text for z in ts)
    fa=ff[a].start if a<len(ff) else len(f.text);fb=ff[b-1].end if b>a else fa
    sa=ss[c].start if c<len(ss) else len(s.text);sb=ss[d-1].end if d>c else sa
    block={'id':serial,'source':fp.name,'target':str(q.relative_to(RESULT)),'place':n,'kind':op,'f_range':[f.start+fa,f.start+fb],'s_range':[s.start+sa,s.start+sb],
       'french_math':fm,'spanish_math':sm,'french_context':f.text[max(0,fa-180):min(len(f.text),fb+220)],'spanish_context':s.text[max(0,sa-180):min(len(s.text),sb+220)]}
    allblocks.append(block);rows.append([serial,fp.name,n,op,fm,sm]);serial+=1
   summaries.append([fp.name,n,len(ff),len(ss),aligned])
  if apply and edits:apply_edits(q,edits,fp.name)
  edits_count+=len(edits)
 (RESULT/'records/IV3_CORE_BLOCKS.json').write_text(json.dumps(allblocks,ensure_ascii=False,indent=2)+'\n')
 write_tsv(RESULT/'records/IV3_CORE_UNMATCHED.tsv',['id','source','place','kind','french_math','spanish_math'],rows)
 write_tsv(RESULT/'records/IV3_CORE_SUMMARY.tsv',['source','place','french_math','spanish_math','aligned'],summaries)
 write_tsv(RESULT/'records/IV3_GROUP_CANDIDATES.tsv',['file','place','before','after','kind','source'],group_candidates)
 print(json.dumps({'apply':apply,'units':len(summaries),'core_source_math':sum(x[2] for x in summaries),'aligned':sum(x[4] for x in summaries),'unmatched_blocks':len(rows),'regrouped':edits_count,'classified':dict(classified)}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');run(ap.parse_args().apply)


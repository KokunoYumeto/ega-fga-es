"""Conservative TeX span utilities; no expansion or mathematical inference."""
import re, difflib
from dataclasses import dataclass

@dataclass
class Span:
    start: int
    end: int
    text: str
    kind: str

MATH_ENVS = {'equation','equation*','align','align*','gather','gather*',
             'multline','multline*','displaymath','math','eqnarray','eqnarray*'}

def is_escaped(t,i):
    n=0;i-=1
    while i>=0 and t[i]=='\\':n+=1;i-=1
    return n%2==1

def balanced_end(t,start,op='{',cl='}'):
    depth=0
    for i in range(start,len(t)):
        if is_escaped(t,i):continue
        if t[i]==op:depth+=1
        if t[i]==cl:
            depth-=1
            if depth==0:return i+1
    return len(t)

def math_spans(t):
    spans=[];i=0
    while i<len(t):
        if t[i]=='%' and not is_escaped(t,i):
            j=t.find('\n',i);i=len(t) if j<0 else j+1;continue
        start=i;closing=None;kind=None
        if t[i]=='$' and not is_escaped(t,i):
            closing='$$' if t.startswith('$$',i) else '$';i+=len(closing);kind='display' if closing=='$$' else 'inline'
        elif t.startswith('\\[',i) and not is_escaped(t,i):closing='\\]';i+=2;kind='display'
        elif t.startswith('\\(',i) and not is_escaped(t,i):closing='\\)';i+=2;kind='inline'
        elif t.startswith('\\begin{',i) and not is_escaped(t,i):
            m=re.match(r'\\begin\{([^}]+)\}',t[i:])
            if m and m.group(1) in MATH_ENVS:
                closing='\\end{'+m.group(1)+'}';i+=len(m.group(0));kind=m.group(1)
        if closing:
            j=t.find(closing,i)
            while j>=0 and closing.startswith('$') and is_escaped(t,j):j=t.find(closing,j+1)
            end=len(t) if j<0 else j+len(closing)
            spans.append(Span(start,end,t[start:end],kind));i=end
        else:i+=1
    return spans

def prose_segments(t):
    masks=[(s.start,s.end) for s in math_spans(t)]
    for m in re.finditer(r'(?<!\\)%[^\n]*',t):masks.append(m.span())
    for m in re.finditer(r'\\(?:label|ref|sref|eref|url|href|cite|input|include|bibliography|bibliographystyle|hypertarget|EGAReaderTarget)\*?(?:\[[^\]]*\])?\{',t):
        end=balanced_end(t,m.end()-1);masks.append((m.start(),end))
    masks.sort();end=0
    for a,b in masks:
        if a>end:yield end,a,t[end:a]
        end=max(end,b)
    if end<len(t):yield end,len(t),t[end:]

ENV_RE=re.compile(r'\\begin\{(env|definition|proposition|theorem|corollary|lemma|remark|remarks|example|examples|scholium|notation)\}\[([^\]]+)\]')

def numbered_units(t):
    matches=list(ENV_RE.finditer(t));out={}
    for n,m in enumerate(matches):
        num=m.group(2).strip().rstrip('.')
        if re.fullmatch(r'\d+(?:\.\d+)+(?:\s*(?:bis|ter))?',num):
            end=matches[n+1].start() if n+1<len(matches) else len(t)
            out[num]=Span(m.start(),end,t[m.start():end],m.group(1))
    return out

def math_key(t):
    """Comparison spelling only. Distinct alphabets remain distinguishable."""
    t=re.sub(r'%[^\n]*','',t)
    t=re.sub(r'\\(?:label|tag)\{[^}]*\}','',t)
    t=re.sub(r'\\(?:begin|end)\{[^}]*\}','',t)
    t=t.replace('\\[','').replace('\\]','').replace('\\(','').replace('\\)','').strip('$')
    t=re.sub(r'\\(?:text|textup|mbox)\{[^}]*\}',r'\\TEXT{}',t)
    repl={'\\sh':'\\mathcal','\\bb':'\\mathbf','\\vphi':'\\varphi',
          '\\emp':'\\varnothing','\\leqslant':'\\leq','\\geqslant':'\\geq',
          '\\setmin':'-','\\longrightarrow':'\\to','\\longleftarrow':'\\from',
          '\\widehat':'\\hat','\\widetilde':'\\tilde', '\\simto':'\\xrightarrow{\\sim}'}
    for a,b in repl.items():t=re.sub(re.escape(a)+r'(?![A-Za-z])',lambda m:b,t)
    for op in ['Spec','Spf','Proj','Hom','Ext','Tor','Ker','Coker','Im','Supp','Ass','Ann','rg','gr','codim','id','Der','Diff','Tr']:
        t=re.sub(r'\\'+op+r'(?![A-Za-z])',lambda m:'\\operatorname{'+op+'}',t)
    for op in ['HH','RR','LL','red']:
        t=re.sub(r'\\'+op+r'(?![A-Za-z])',lambda m:'\\mathrm{'+{'HH':'H','RR':'R','LL':'L','red':'red'}[op]+'}',t)
    # A braced and unbraced one-token command argument is the same TeX input.
    t=re.sub(r'\\(mathcal|mathscr|mathbf|boldsymbol|mathfrak|mathrm|tilde|hat)\s*\{([A-Za-z])\}',r'\\\1\2',t)
    t=re.sub(r'\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big|bigg|Bigg)(?![A-Za-z])','',t)
    t=re.sub(r'\\[,;! ]','',t)
    return re.sub(r'\s+','',t).replace('&','').strip('.,;:~')

def math_loose_key(t):
    # Comparison-only aliases used by inherited Spanish preambles.
    for name,expanded in [('shHom',r'\mathcal{H}om'),('shExt',r'\mathcal{E}xt'),('shTor',r'\mathcal{T}or'),('shDer',r'\mathcal{D}er'),('shDiff',r'\mathcal{D}iff'),('shProj',r'\mathcal{P}roj'),('shGr',r'\mathcal{G}r')]:
        t=re.sub(r'\\'+name+r'(?![A-Za-z])',lambda m:expanded,t)
    t=t.replace(r'\kres','k').replace(r'\acute{e}','e')
    t=re.sub(r'\\(?:xrightarrow\{\\sim\}|isoto|cong|simeq)(?![A-Za-z])', 'ISO',t)
    t=math_key(t)
    t=t.replace('\\rad','\\mathfrakr').replace('\\nilrad','\\mathfrakN')
    t=t.replace('\\not\\in','\\notin').replace('{}','')
    t=re.sub(r'([_^])\{([A-Za-z0-9])\}',r'\1\2',t)
    t=re.sub(r'\\(?:mathrm|mathcal|mathscr|mathfrak|mathbf|boldsymbol)([A-Za-z])',r'\1',t)
    for a,b in [('\\kres','k'),('\\C','C'),('\\Set','\\mathit{Ens}'),('\\CHom','\\operatorname{Hom}'),('\\op','^{\\circ}'),('\\setminus','-'),('\\cdots','\\ldots'),('\\mapsto','\\leadsto'),('\\subseteq','\\subset')]:
        t=re.sub(re.escape(a)+r'(?![A-Za-z])',lambda m:b,t)
    # In alignment only, remove braces, spacing controls and row separators.
    # The output always uses the unmodified source literal, never this key.
    t=re.sub(r'\\(?:quad|qquad|enspace|thinspace|medspace)(?![A-Za-z])','',t)
    t=t.replace('\\\\','')
    t=re.sub(r'[{}~]','',t)
    t=re.sub(r'(\\ar\[[^]]+\][_^])-',r'\1',t)
    # The two TeX spellings theta'_i and theta_i' put the prime on theta.
    primes=t.count("'");t=t.replace("'",'')
    return t+'PRIMES'+str(primes)

def retain_translated_text(fr,es):
    """Use source math, retaining Spanish words inside matching text commands."""
    pattern=re.compile(r'\\(text|textup|mbox)\{')
    fmatches=list(pattern.finditer(fr));ematches=list(pattern.finditer(es))
    if len(fmatches)!=len(ematches):return None if fmatches else fr
    replacements=[]
    for fm,em in zip(fmatches,ematches):
        fe=balanced_end(fr,fm.end()-1);ee=balanced_end(es,em.end()-1)
        fs=fr[fm.end():fe-1];ss=es[em.end():ee-1]
        if re.search('[A-Za-zÀ-ÿ]{2}',fs) and not re.search(r'\\(?:math|operator|ref|hyperref)',fs):
            replacements.append((fm.end(),fe-1,ss))
    for a,b,new in reversed(replacements):fr=fr[:a]+new+fr[b:]
    return fr

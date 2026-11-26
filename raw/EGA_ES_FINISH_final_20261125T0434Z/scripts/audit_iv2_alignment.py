#!/usr/bin/env python3
"""Compare IV-2 math and structural streams, keeping source data outside deliverables."""
from pathlib import Path
import re, json, difflib, csv, collections, argparse
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'
FR=SOURCE/'EGA_ES_FINISH_1_FRANCES/fr'
ES=ROOT/'tree/worktree/es'
ORDER=json.loads((SOURCE/'EGA_ES_FINISH_4_HECHO/done/codex_session/ES_IV2_CURRENT_ORDERED_READER_V2.json').read_text())['input_order']
ANCHOR=re.compile(r'\\begin\{(?:env|definition|proposition|theorem|corollary|example|examples|remark|remarks|scholium|lemma)\}\[([\d.]+)[^\]]*\]')
MATH=re.compile(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\\begin\{(equation\*?|align\*?|gather\*?|displaymath|eqnarray\*?)\}[\s\S]*?\\end\{\1\}')

def weak(s):
    s=re.sub(r'\\(?:label|tag)\{[^}]*\}', '', s)
    s=re.sub(r'\\(?:begin|end)\{(?:equation\*?|align\*?|gather\*?|displaymath|eqnarray\*?)\}', '', s)
    s=s.strip('$').removeprefix('\\[').removesuffix('\\]').removeprefix('\\(').removesuffix('\\)')
    # Loose normalization used only to locate corresponding formulas; source literal wins on write.
    for name in ['mathcal','mathscr','sh']:
        s=re.sub(r'\\'+name+r'\b',r'\\FONT',s)
    for name in ['mathfrak','mathbf','boldsymbol','mathrm']:
        s=re.sub(r'\\'+name+r'\b','',s)
    s=re.sub(r'\\operatorname\{([^}]+)\}',lambda m:'\\'+m[1],s)
    s=re.sub(r'\\text\{(?:[^{}]|\{[^{}]*\})*\}',r'\\TEXT',s)
    s=re.sub(r'\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big|bigg|Bigg)\b','',s)
    for a,b in [('widehat','hat'),('widetilde','tilde'),('leqslant','leq'),('geqslant','geq'),('setmin','-'),('setminus','-'),('longrightarrow','to'),('longleftarrow','leftarrow'),('cdots','ldots'),('subseteq','subset'),('supseteq','supset'),('mapsto','leadsto'),('kres','k'),('vphi','varphi'),('emp','varnothing')]:
        s=re.sub(r'\\'+a+r'\b',lambda m:(b if b=='-' else '\\'+b),s)
    s=re.sub(r'\\(?:,|;|!|quad|qquad|enspace|thinspace|medspace)\b?', '', s) if False else s
    s=re.sub(r'\\[,;!]|\\(?:quad|qquad|enspace|thinspace|medspace)\b','',s)
    s=re.sub(r'[\s{}~&]','',s)
    s=s.replace('\\\\','')
    return s

def aggregate(layer='CURRENT',fallback=False):
    texts=[]; bounds=[]; pos=0
    for name in ORDER:
        actual=name if layer=='CURRENT' else name.replace('.tex','.diplomatic.tex')
        p=ES/layer/'EGA_IV2'/actual
        if not p.exists() and fallback: p=ES/'CURRENT/EGA_IV2'/name
        t=p.read_text();texts.append(t);bounds.append((pos,pos+len(t),str(p.relative_to(ROOT))))
        pos+=len(t)+1
    return '\n'.join(texts),bounds

def owner(pos,bounds):
    return next((f for a,b,f in bounds if a<=pos<=b),'unknown')

def sections(t):
    anchors=list(ANCHOR.finditer(t));r=[('opening',0,anchors[0].start())]
    for i,m in enumerate(anchors):r.append((m[1],m.start(),anchors[i+1].start() if i+1<len(anchors) else len(t)))
    return r

def compare(layer='CURRENT',fallback=False):
    f=(FR/layer.lower()/'IV2/native/ega4/ega4-2-fr.tex').read_text();e,bounds=aggregate(layer,fallback)
    fs=sections(f);es=sections(e)
    assert [s[0] for s in fs]==[s[0] for s in es], 'Statement sequence differs'
    paired=[];gaps=[]
    for (place,a,b),(_,x,y) in zip(fs,es):
        fm=list(MATH.finditer(f,a,b));em=list(MATH.finditer(e,x,y))
        aa=[weak(m[0]) for m in fm];bb=[weak(m[0]) for m in em]
        for tag,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
            if tag=='equal':
                for u,v in zip(fm[i:j],em[k:l]):
                    paired.append({'place':place,'fstart':u.start(),'fend':u.end(),'estart':v.start(),'eend':v.end(),'f':u[0],'e':v[0],'file':owner(v.start(),bounds)})
            else:
                gaps.append({'place':place,'tag':tag,'fcount':j-i,'ecount':l-k,'f':[m[0] for m in fm[i:j]],'e':[m[0] for m in em[k:l]],'fpos':[(m.start(),m.end()) for m in fm[i:j]],'epos':[(m.start(),m.end()) for m in em[k:l]],'file':owner(em[k].start() if k<len(em) else x,bounds)})
    return f,e,bounds,paired,gaps

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--layer',default='CURRENT');p.add_argument('--fallback',action='store_true');a=p.parse_args()
    f,e,b,paired,gaps=compare(a.layer,a.fallback)
    tmp=ROOT.parent/'tmp/iv2';tmp.mkdir(parents=True,exist_ok=True)
    (tmp/('gaps_'+a.layer+'.json')).write_text(json.dumps(gaps,ensure_ascii=False,indent=2))
    print('Compared',a.layer,'source math',len(list(MATH.finditer(f))),'Spanish math',len(list(MATH.finditer(e))),'paired',len(paired),'diff literal',sum(x['f']!=x['e'] for x in paired),'gap blocks',len(gaps))
    for i,g in enumerate(gaps):
        print(i,g['place'],g['tag'],g['fcount'],g['ecount'],g['file'])
        print(' FR',repr(g['f'])[:600]);print(' ES',repr(g['e'])[:600])

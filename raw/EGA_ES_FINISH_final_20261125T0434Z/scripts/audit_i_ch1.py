"""I chapter I: main-text formula audit excluding separately retained notes."""
import re,json,difflib
from corpus import FR,RESULT,ES,write_tsv
from tex_tools import numbered_units,math_spans,math_loose_key,Span,balanced_end
from audit_iv4 import mask_footnotes

def i_units(t):
    existing=numbered_units(t)
    starts=[(v.start,k,v.kind) for k,v in existing.items()]
    for m in re.finditer(r'\\phantomsection\s*\\label\{I\.(\d+\.\d+\.\d+)(?:-fr)?\}',t):
        if m[1] not in existing:starts.append((m.start(),m[1],'free paragraph'))
    for m in re.finditer(r'\\section\{[^}]+\}\s*\\label\{section:I\.(\d+)(?:-fr)?\}',t):
        starts.append((m.start(),'intro:'+m[1],'section prelude'))
    starts.sort();out={}
    for i,(a,n,k) in enumerate(starts):
        b=starts[i+1][0] if i+1<len(starts) else len(t)
        out[n]=Span(a,b,t[a:b],k)
    return out

def mask_notes(t):
    t=mask_footnotes(t);out=list(t)
    for m in re.finditer(r'\\footnotetext(?:\[[^]]*\])?\{',t):
        end=balanced_end(t,m.end()-1);out[m.start():end]=' '*(end-m.start())
    # Optional short headings repeat formulas solely for the table of contents.
    for m in re.finditer(r'\\(?:subsection|section)\[',t):
        end=balanced_end(t,m.end()-1,'[',']');out[m.end()-1:end]=' '*(end-m.end()+1)
    return ''.join(out)

def texts(layer):
    p=ES/f'worktree/es/{layer}/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex'
    t=p.read_text()
    # The inherited indexes follow the mathematical chapter.
    markers=[m.start() for m in re.finditer(r'\\(?:section|chapter)\*\{(?:Índice|Indice|Notas)',t)]
    end=min((x for x in markers if x>t.find(r'\label{I.10.15.7')),default=len(t))
    return p,t[:end]
def main():
    gaps=[];stats=[];missing=[]
    for layer in ['CURRENT','DIPLOMATIC']:
        p,t=texts(layer);su=i_units(t)
        for fp in sorted((FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex')):
            for num,fu in i_units(fp.read_text()).items():
                if num not in su:missing.append([layer,fp.name,num]);continue
                eu=su[num];ff=math_spans(mask_notes(fu.text));ss=math_spans(mask_notes(eu.text));aligned=0
                for op,a,b,c,d in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_opcodes():
                    if op=='equal':aligned+=b-a
                    else:gaps.append({'layer':layer,'source':str(fp.relative_to(FR/layer.lower())),'place':num,'op':op,'fr':[x.text for x in ff[a:b]],'es':[x.text for x in ss[c:d]],'fpos':[(x.start,x.end) for x in ff[a:b]],'epos':[(x.start,x.end) for x in ss[c:d]],'fr_context':fu.text[max(0,ff[a].start-130):min(len(fu.text),ff[b-1].end+200)] if a<b else '', 'es_context':eu.text[max(0,ss[c].start-130):min(len(eu.text),ss[d-1].end+200)] if c<d else ''})
                stats.append([layer,fp.name,num,len(ff),len(ss),aligned])
    tmp=RESULT.parent/'tmp/i';tmp.mkdir(exist_ok=True)
    (tmp/'gaps.json').write_text(json.dumps(gaps,ensure_ascii=False,indent=2))
    write_tsv(RESULT/'records/I_CH1_ALIGNMENT_SUMMARY.tsv',['edition','source','unit','french_math','spanish_math_excluding_editorial_notes','aligned'],stats)
    write_tsv(RESULT/'records/I_CH1_MISSING_UNITS.tsv',['edition','source','unit'],missing)
    print(json.dumps({'units':len(stats),'missing':missing,'french_math':sum(x[3] for x in stats),'aligned':sum(x[5] for x in stats),'gaps':len(gaps)}))
    for i,g in enumerate(gaps):
        if g['layer']=='CURRENT':print(i,g['place'],g['op'],len(g['fr']),len(g['es']),str(g['fr'])[:180],str(g['es'])[:180])
if __name__=='__main__':main()

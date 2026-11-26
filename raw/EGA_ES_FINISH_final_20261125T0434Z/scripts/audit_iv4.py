"""IV4 comparison across component boundaries and optional editorial notes."""
import re,json,csv,difflib,collections
from corpus import FR,RESULT,ES,write_tsv
from tex_tools import numbered_units,math_spans,math_loose_key,balanced_end
from assemble_readers import flatten_text

PROJECT=ES/'worktree/es/PORTED_20261109/IV4'
FILES=['16','17','18','20','21a','21b','21c','errata-addenda-list3']
def mask_footnotes(t):
    out=list(t)
    for m in re.finditer(r'\\footnote(?:\[[^]]*\])?\{',t):
        end=balanced_end(t,m.end()-1)
        out[m.start():end]=' '*(end-m.start())
    return ''.join(out)
def pairs():
    for n in FILES:
        fp=FR/'current/IV4/native/ega4'/f'ega4-{n}-fr.tex'
        names=[f'ega4-{n}-es.tex']+(['ega4-19-es.tex'] if n=='18' else [])
        st='\n'.join(flatten_text((PROJECT/'ega4'/name).read_text(),PROJECT) for name in names)
        yield fp,fp.read_text(),st
def main():
    gaps=[];stats=[];missing=[]
    for fp,ft,st in pairs():
        fu=numbered_units(ft);su=numbered_units(st)
        for num,f in fu.items():
            if num not in su:missing.append([fp.name,num]);continue
            s=su[num]
            ff=math_spans(mask_footnotes(f.text));ss=math_spans(mask_footnotes(s.text))
            aligned=0
            for op,a,b,c,d in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_opcodes():
                if op=='equal':aligned+=b-a
                else:gaps.append({'source':str(fp.relative_to(FR/'current')),'place':num,'op':op,'fr':[x.text for x in ff[a:b]],'es':[x.text for x in ss[c:d]],'fr_context':f.text[max(0,ff[a].start-100):min(len(f.text),ff[b-1].end+150)] if a<b else '', 'es_context':s.text[max(0,ss[c].start-100):min(len(s.text),ss[d-1].end+150)] if c<d else ''})
            stats.append([fp.name,num,len(ff),len(ss),aligned])
    out=RESULT.parent/'tmp/iv4';out.mkdir(exist_ok=True)
    (out/'gaps.json').write_text(json.dumps(gaps,ensure_ascii=False,indent=2))
    write_tsv(RESULT/'records/IV4_ALIGNMENT_SUMMARY.tsv',['source','unit','french_math','spanish_math_excluding_editorial_notes','aligned'],stats)
    write_tsv(RESULT/'records/IV4_MISSING_UNITS.tsv',['source','unit'],missing)
    print(json.dumps({'units':len(stats),'missing':missing,'french_math':sum(x[2] for x in stats),'aligned':sum(x[4] for x in stats),'gaps':len(gaps)}))
    for i,g in enumerate(gaps):print(i,g['place'],g['op'],len(g['fr']),len(g['es']),str(g['fr'])[:160],str(g['es'])[:160])
if __name__=='__main__':main()

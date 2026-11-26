"""Construct the EGA I diplomatic chapter from its current Spanish base.

Only source math-span deltas with established ordered correspondences are
transferred automatically. Prose differences are emitted for model review.
"""
import re, json, difflib, collections, shutil
from corpus import RESULT, FR, ES, write_tsv
from tex_tools import numbered_units, math_spans, math_key

def masked(t):
    for s in reversed(math_spans(t)):t=t[:s.start]+'<MATH>'+t[s.end:]
    return t

def main():
    curp=ES/'worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex'
    dipp=ES/'worktree/es/DIPLOMATIC/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex'
    text=curp.read_text();units=numbered_units(text);changes=[];edits=[];pending=[];events=[]
    for f in sorted((FR/'current/BASE/native/ega1').glob('ega1-*-fr.tex')):
        ft=f.read_text();dt=(FR/'diplomatic'/f.relative_to(FR/'current')).read_text()
        fu=numbered_units(ft);du=numbered_units(dt)
        for num,fs in fu.items():
            if num not in du or fs.text==du[num].text:continue
            ds=du[num]
            if num not in units:pending.append([f.name,num,'missing_span','',fs.text,ds.text]);continue
            ss=units[num];ff=math_spans(fs.text);df=math_spans(ds.text);sf=math_spans(ss.text)
            # Current French to Spanish, preserving order even when notes add formulas.
            fmap={}
            sm=difflib.SequenceMatcher(None,[math_key(s.text) for s in ff],[math_key(s.text) for s in sf],autojunk=False)
            for op,a,b,c,d in sm.get_opcodes():
                if op=='equal':fmap.update(zip(range(a,b),range(c,d)))
            delta=difflib.SequenceMatcher(None,[s.text for s in ff],[s.text for s in df],autojunk=False)
            resolved=0
            for op,a,b,c,d in delta.get_opcodes():
                if op=='equal':continue
                if op=='replace' and b-a==d-c and all(i in fmap for i in range(a,b)):
                    for i,j in zip(range(a,b),range(c,d)):
                        sspan=sf[fmap[i]];new=df[j].text
                        edits.append((ss.start+sspan.start,ss.start+sspan.end,new))
                        changes.append([str(dipp.relative_to(RESULT)),num,sspan.text,new,'assembly',f'EGA_ES_FINISH_1_FRANCES/fr/diplomatic/BASE/native/ega1/{f.name}: {num}'])
                        resolved+=1
                else:
                    pending.append([f.name,num,'math_delta',op,' | '.join(s.text for s in ff[a:b]),' | '.join(s.text for s in df[c:d])])
            fm=masked(fs.text);dm=masked(ds.text)
            if re.sub(r'\s+',' ',fm)!=re.sub(r'\s+',' ',dm):
                diff='\n'.join(difflib.unified_diff(fm.splitlines(),dm.splitlines(),n=1))
                pending.append([f.name,num,'prose_delta',diff,fs.text,ds.text])
            events.append([f'I.{num}:diplomatic','2026-11-25','GPT-6 Astra; effort not separately exposed; EGA_ES_FINISH','carried as background without fault found',f'Compared French editorial layers and transferred {resolved} aligned formula variants; no proof verification. Prose deltas tracked separately.'])
    for a,b,new in sorted(set(edits),reverse=True):text=text[:a]+new+text[b:]
    dipp.parent.mkdir(parents=True,exist_ok=True);dipp.write_text(text)
    write_tsv(RESULT/'records/CAMBIOS_i_diplomatic.tsv',['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/'records/I_DIPLOMATIC_PENDING.tsv',['source','place','kind','detail','current','diplomatic'],pending)
    write_tsv(RESULT/'records/CHECK_EVENTS_i_diplomatic.tsv',['statement_id','date','who','type','outcome'],events)
    print(json.dumps({'formula_variants':len(changes),'pending':len(pending),'prose_units':sum(r[2]=='prose_delta' for r in pending)}))

if __name__=='__main__':main()

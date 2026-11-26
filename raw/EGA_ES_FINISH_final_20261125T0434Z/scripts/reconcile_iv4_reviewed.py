"""Literal formula differences reviewed side by side in the IV4 audit.

This pass carries the supplied French readings, including printed mathematical
readings that an inherited Spanish note may discuss. It is not a proof check.
"""
import csv,re,difflib,collections,json
from corpus import RESULT,FR,write_tsv
from tex_tools import numbered_units,math_spans,math_loose_key,retain_translated_text

IDS={0,2,3,4,9,10,16,17,21,22,27,29,33,34,39,40,41,42,43,44,55,56,57,58,59,60,61,62,65,66,67,68,70,76,77,78,79,84,85,86,87,88,89,111,112,113,114,117,126,127,129,130,131,155,156,165,169,170,174}
def main():
    rows=list(csv.DictReader((RESULT/'records/NOTATION_UNMATCHED_IV4_.tsv').open(),delimiter='\t'))
    chosen=[r for i,r in enumerate(rows) if i in IDS]
    groups=collections.defaultdict(list)
    for r in chosen:groups[(r['source'],r['place'],r['target'])].append(r)
    edits=collections.defaultdict(list);changes=[];done=0
    for (source,num,target),rr in groups.items():
        fp=FR/'current'/source;tp=RESULT/target;fu=numbered_units(fp.read_text())[num];su=numbered_units(tp.read_text())[num]
        ff=math_spans(fu.text);ss=math_spans(su.text)
        for op,fa,fb,sa,sb in difflib.SequenceMatcher(None,[math_loose_key(s.text) for s in ff],[math_loose_key(s.text) for s in ss],autojunk=False).get_opcodes():
            fseq=' | '.join(s.text for s in ff[fa:fb]);sseq=' | '.join(s.text for s in ss[sa:sb])
            if op!='replace' or not any(r['french_math']==fseq and r['spanish_math']==sseq for r in rr):continue
            assert fb-fa==sb-sa;done+=1
            for f,s in zip(ff[fa:fb],ss[sa:sb]):
                new=retain_translated_text(f.text,s.text)
                if new is None:raise ValueError('Text-command translation needs a separate review')
                after=re.match(r'\s*([.,;:!?])',fu.text[f.end:]);oldafter=re.match(r'\s*([.,;:!?])',su.text[s.end:])
                if f.kind=='inline' and s.kind!='inline' and after and not oldafter:new+=after[1]
                edits[tp].append((su.start+s.start,su.start+s.end,new))
                changes.append([target,num,s.text,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/'+source+': '+num+'; reviewed formula literal'])
    for p,ee in edits.items():
        t=p.read_text()
        for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
        p.write_text(t)
    write_tsv(RESULT/'records/CAMBIOS_iv4_reviewed_literals.tsv',['file','place','before','after','kind','source'],changes)
    print(json.dumps({'reviewed_blocks':done,'formula_changes':len(changes)}))
if __name__=='__main__':main()

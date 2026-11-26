"""Restore source math spelling only for individually aligned formula spans.

The alignment is within the same numbered paragraph. Equal loose keys identify
typographic correspondences; unmatched spans are reported, never guessed.
"""
import re, csv, json, difflib, argparse, collections
from corpus import RESULT, FR, route, source_files, write_tsv
from tex_tools import numbered_units, math_spans, math_loose_key, retain_translated_text

def main(apply=False, only=None):
    changes=[];unmatched=[];summaries=[];edits=collections.defaultdict(list)
    for edition in ('current','diplomatic'):
        for fp in source_files(edition):
            rel=str(fp.relative_to(FR/edition))
            if only and only not in rel:continue
            if 'ega0-1-fr.tex' in rel or rel.startswith('IV2/') or (rel.startswith('IV1/') and fp.name=='ega4-1-fr.tex'):continue
            ft=fp.read_text();fu=numbered_units(ft)
            targets=route(rel,edition);tu=collections.defaultdict(list)
            for tp in targets:
                if tp.exists():
                    for num,u in numbered_units(tp.read_text()).items():tu[num].append((tp,u))
            for num,funit in fu.items():
                if len(tu[num])!=1:
                    unmatched.append([edition,rel,num,'unit_candidates',len(tu[num]),'','']);continue
                tp,sunit=tu[num][0]
                ff=math_spans(funit.text);sf=math_spans(sunit.text)
                fk=[math_loose_key(s.text) for s in ff];sk=[math_loose_key(s.text) for s in sf]
                sm=difflib.SequenceMatcher(None,fk,sk,autojunk=False)
                paired=0;changed=0
                for op,fa,fb,sa,sb in sm.get_opcodes():
                    if op=='equal':
                        for fi,si in zip(range(fa,fb),range(sa,sb)):
                            fspan,sspan=ff[fi],sf[si];paired+=1
                            if fspan.text!=sspan.text:
                                new=retain_translated_text(fspan.text,sspan.text)
                                if new is None:
                                    unmatched.append([edition,rel,num,'text_command',str(tp.relative_to(RESULT)),fspan.text,sspan.text]);continue
                                if new==sspan.text:continue
                                # A legacy display may contain sentence punctuation that
                                # the source places after the restored inline formula.
                                if fspan.text.startswith('$') and not fspan.text.startswith('$$') and not sspan.text.startswith('$'):
                                    fm=re.match(r'\s*([.,;:!?])',funit.text[fspan.end:])
                                    smp=re.match(r'\s*([.,;:!?])',sunit.text[sspan.end:])
                                    if fm and not smp and re.search(r'[.,;:!?]\s*(?:\\\]|\\end\{[^}]+\})$',sspan.text):
                                        new+=fm.group(1)
                                a=sunit.start+sspan.start;b=sunit.start+sspan.end
                                edits[tp].append((a,b,new));changed+=1
                                changes.append([str(tp.relative_to(RESULT)),num,sspan.text,new,'own comparison',f'EGA_ES_FINISH_1_FRANCES/fr/{edition}/{rel}: {num}; formula correspondence'])
                    else:
                        fs=' | '.join(s.text for s in ff[fa:fb]);ss=' | '.join(s.text for s in sf[sa:sb])
                        unmatched.append([edition,rel,num,op,str(tp.relative_to(RESULT)),fs,ss])
                summaries.append([edition,rel,num,len(ff),len(sf),paired,changed])
    suffix='_'+only.replace('/','_').replace('.','_') if only else ''
    write_tsv(RESULT/f'records/NOTATION_DRY_RUN{suffix}.tsv',['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/f'records/NOTATION_UNMATCHED{suffix}.tsv',['edition','source','place','kind','target','french_math','spanish_math'],unmatched)
    write_tsv(RESULT/f'records/NOTATION_SUMMARY{suffix}.tsv',['edition','source','place','french_formulas','spanish_formulas','aligned','changes'],summaries)
    if apply:
        for p,ee in edits.items():
            text=p.read_text();last=len(text)+1
            for a,b,new in sorted(set(ee),reverse=True):
                if b>last:raise ValueError('Overlapping edits '+str(p.relative_to(RESULT)))
                text=text[:a]+new+text[b:];last=a
            p.write_text(text)
        write_tsv(RESULT/f'records/CAMBIOS_notation{suffix}.tsv',['file','place','before','after','kind','source'],changes)
    print(json.dumps({'apply':apply,'units':len(summaries),'formulas':sum(r[3] for r in summaries),'aligned':sum(r[5] for r in summaries),'changes':len(changes),'unmatched_blocks':len(unmatched)},ensure_ascii=False))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');ap.add_argument('--only');args=ap.parse_args();main(args.apply,args.only)

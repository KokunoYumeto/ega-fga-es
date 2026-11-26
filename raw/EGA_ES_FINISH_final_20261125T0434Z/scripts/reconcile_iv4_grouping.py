"""Restore the reviewed French formula boundaries and their Spanish connectors."""
import csv,re,difflib,collections,json
from corpus import RESULT,FR,write_tsv
from tex_tools import numbered_units,math_spans,math_loose_key,prose_segments

REVIEWED={'16.4.8.3','17.4.4','17.12.8','17.13.5','18.6.6','18.6.8','18.10.16','18.11.10','18.11.12.1','19.9.8','21.8.5','21.10.18','21.13.6','21.13.9','21.14.1','21.14.3','3.1.10.2','6.2.4','8.12.12','21.4.9','21.4.13'}
PHRASES=[("et d'autre part",'y por otra parte'),("l'injection canonique",'la inyección canónica'),('somme des degrés séparables des','suma de los grados separables de los'),('est localement noethérien','es localmente noetheriano'),("d'où",'de donde'),('donc','por tanto'),('où','donde'),('avec','con'),('et','y'),('sur','en')]
def translate_connectors(t):
    edits=[]
    for a,b,p in prose_segments(t):
        new=p
        for fr,es in PHRASES:new=re.sub(r'(?<![A-Za-zÀ-ÿ])'+re.escape(fr)+r'(?![A-Za-zÀ-ÿ])',es,new)
        edits.append((a,b,new))
    for a,b,new in reversed(edits):t=t[:a]+new+t[b:]
    return t

def main():
    rows=list(csv.DictReader((RESULT/'records/NOTATION_UNMATCHED_IV4_.tsv').open(),delimiter='\t'))
    keys=sorted({(r['source'],r['place'],r['target']) for r in rows if r['place'] in REVIEWED})
    edits=collections.defaultdict(list);changes=[]
    for source,num,target in keys:
        fu=numbered_units((FR/'current'/source).read_text())[num];tp=RESULT/target;su=numbered_units(tp.read_text())[num]
        ff=math_spans(fu.text);ss=math_spans(su.text)
        for op,fa,fb,sa,sb in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_opcodes():
            if op!='replace' or fb-fa<=1 or sb-sa!=1:continue
            a=ss[sa].start;b=ss[sa].end;fe=ff[fb-1].end
            fragment=fu.text[ff[fa].start:fe]
            balance=len(re.findall(r'(?<!\\)\{',fragment))-len(re.findall(r'(?<!\\)\}',fragment))
            while balance>0:
                c=fu.text[fe];fragment+=c;fe+=1
                if c=='{':balance+=1
                elif c=='}':balance-=1
            new=translate_connectors(fragment)
            if num=='21.13.6':
                tail=' la inyección canónica'
                assert su.text.startswith(tail,b);b+=len(tail)
            if num=='21.4.13':new='de '+new
            following=su.text[b:]
            fp=re.match(r'\s*([.,;:!?])',fu.text[fe:])
            sp=re.match(r'\s*([.,;:!?])',following)
            if fp and not sp:new+=fp[1]
            if ss[sa].kind=='inline' and ff[fb-1].kind!='inline' and sp and not fp:
                b+=sp.end()
                new+=' '
            old=su.text[a:b]
            edits[tp].append((su.start+a,su.start+b,new))
            changes.append([target,num,old,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/'+source+': '+num+'; reviewed grouping and connective prose'])
    for p,ee in edits.items():
        t=p.read_text()
        for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
        p.write_text(t)
    write_tsv(RESULT/'records/CAMBIOS_iv4_grouping.tsv',['file','place','before','after','kind','source'],changes)
    print(json.dumps({'reviewed_groups':len(changes)}))
if __name__=='__main__':main()

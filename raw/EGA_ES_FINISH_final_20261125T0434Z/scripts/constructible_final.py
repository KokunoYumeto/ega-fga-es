"""Apply the witnessed Spanish construible family outside math and bibliography."""
import re,argparse,collections,csv
from corpus import RESULT,write_tsv
from standardize import canonical_files,place_for
from tex_tools import prose_segments,math_spans

ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
rows=[];gl=[];dry=[];total=collections.Counter()
for p in canonical_files():
    t=p.read_text();edits=[];bibliography=[]
    for m in re.finditer(r'\\begin\{thebibliography\}[\s\S]*?\\end\{thebibliography\}',t):bibliography.append(m.span())
    if 'bibliograph' in p.name.lower():continue
    for a,b,prose in prose_segments(t):
        for m in re.finditer(r'\b(?:cuasi|pro|ind)?constructib(?:les?|ilidad(?:es)?)\b',prose,re.I):
            start=a+m.start();end=a+m.end()
            if any(x<=start<y for x,y in bibliography):continue
            old=m[0];new=re.sub('construct','constru',old,flags=re.I)
            if old[0].isupper():new=new[0].upper()+new[1:]
            f=str(p.relative_to(RESULT));place=place_for(t,start)
            edits.append((start,end,new));total[old]+=1
            witness='EGA_ES_FINISH_3_ESTANDAR/glossary/TERMINOLOGY_DECISIONS.tsv:EGAIV3-ES-TERM-0004,0014; Zalamea p.18 and morphological extension for cuasi-'
            dry.append([f,place,t.count('\n',0,start)+1,old,new,t[max(0,start-80):end+100].replace('\n',' ')])
            rows.append([f,place,old,new,'standard',witness]);gl.append([old,new,witness,f+':'+place,'yes'])
    out=t
    for a,b,new in sorted(edits,reverse=True):out=out[:a]+new+out[b:]
    assert [x.text for x in math_spans(t)]==[x.text for x in math_spans(out)],str(p)
    if args.apply:p.write_text(out)
def accumulated(name,header,new):
    p=RESULT/'records'/name
    previous=list(csv.reader(p.open(),delimiter='\t'))[1:] if p.exists() else []
    seen={tuple(x) for x in previous};combined=previous+[x for x in new if tuple(map(str,x)) not in seen]
    write_tsv(p,header,combined)
accumulated('CONSTRUCTIBLE_FINAL_DRY_RUN.tsv',['file','place','line','before','after','context'],dry)
if args.apply:
    accumulated('CAMBIOS_constructible_final.tsv',['file','place','before','after','kind','source'],rows)
    accumulated('GLOSARIO_REGISTRO_constructible_final.tsv',['french_term','spanish_rendering','witness','places','reversible'],gl)
print('apply',args.apply,'occurrences',len(dry),'forms',dict(total))

"""Close source-read Obsérvese residues: on -> se, Notons -> Observemos."""
import json,re,collections
from corpus import RESULT,FR,write_tsv
from tex_tools import math_spans
rows=json.loads((RESULT/'records/ROOT_IMPERATIVE_REVIEW.json').read_text())
edits=collections.defaultdict(list);changes=[];decisions=[]
for r in rows:
    old=r['before']
    if r['scope']=='I':
        src='BASE/native/ega1/chapter1-frontmatter-fr.tex'
        assert 'Notons cependant' in (FR/r['edition']/src).read_text()
        new='Observemos';witness='Notons cependant'
    else:
        src=r['source']
        if re.search(r'\bon\s+observe\b',r['fr'],re.I):new='se observa';witness='on observe'
        else:
            assert re.search(r'\bon\s+notera\b',r['fr'],re.I),r
            new='se observará';witness='on notera'
        if old[0].isupper():new=new[0].upper()+new[1:]
    edits[r['file']].append((r['position'],r['end'],old,new))
    source=f'EGA_ES_FINISH_1_FRANCES/fr/{r["edition"]}/{src}:{r["place"]}; {witness}; STANDARDS_20261119b register'
    changes.append([r['file'],r['place'],old,new,'standard',source])
    decisions.append([r['file'],r['place'],old,new,witness,'read against source'])
f='tree/worktree/es/PORTED_20261109/IV4/ega4/ega4-21c-es/components/03_21_14.tex'
t=(RESULT/f).read_text();old='Obsérvese también que, gracias a esta reducción';new='Observemos también que, gracias a esta reducción'
m=list(re.finditer(r'\s+'.join(re.escape(x) for x in old.split()),t));assert len(m)==1
old=m[0][0];new=old.replace('Obsérvese','Observemos',1)
ft=(FR/'current/IV4/native/ega4/ega4-21c-fr.tex').read_text();assert re.search(r'Notons\s+aussi que, grâce à cette réduction',ft)
pos=t.index(old);edits[f].append((pos,pos+len(old),old,new))
changes.append([f,'IV.21.14.4 author footnote',old,new,'standard','EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-21c-fr.tex:21.14.4; Notons aussi; author first plural'])
decisions.append([f,'IV.21.14.4 author footnote',old,new,'Notons aussi','read against source; note retained in full'])
for f,ee in edits.items():
    p=RESULT/f;t=p.read_text();out=t
    for a,b,old,new in sorted(ee,reverse=True):
        assert out[a:b]==old,(f,a,out[a:b],old)
        out=out[:a]+new+out[b:]
    assert [x.text for x in math_spans(t)]==[x.text for x in math_spans(out)],f
    p.write_text(out)
write_tsv(RESULT/'records/CAMBIOS_root_imperative_finish.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/ROOT_IMPERATIVE_FINAL.tsv',['file','place','before','after','french_form','decision'],decisions)
print('source-read register corrections',len(changes))

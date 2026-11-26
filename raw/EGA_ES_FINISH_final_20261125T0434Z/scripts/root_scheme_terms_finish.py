"""Apply the five source-read scheme/prescheme corrections and close the noun audit.

This is a one-shot, exact-position patch against ROOT_SCHEME_TERMS_REVIEW.json.
It changes prose only and asserts byte-identical ordered mathematical spans.
"""
import collections,json,re
from corpus import RESULT,write_tsv
from tex_tools import math_spans

review=json.loads((RESULT/'records/ROOT_SCHEME_TERMS_REVIEW.json').read_text())
counts=json.loads((RESULT/'records/ROOT_SCHEME_TERMS_COUNT_REVIEW.json').read_text())
patches=collections.defaultdict(list);changes=[];decisions=[]
for i,r in enumerate(review):
    assert len(r['fr_types'])==len(r['spanish_terms'])==1
    z=r['spanish_terms'][0];old=z['word'];plural=old.endswith('s')
    new=('preesquema' if r['fr_types'][0] else 'esquema')+('s' if plural else '')
    patches[z['file']].append((z['position'],z['end'],old,new))
    witness=f"EGA_ES_FINISH_1_FRANCES/fr/{r['edition']}/{r['source']}:{r['place']}"
    changes.append([z['file'],r['place'],old,new,'own comparison',witness])
    decisions.append([f'same-{i}',r['scope'],r['edition'],r['place'],'changed',f'French nominal distinction restored: {old} → {new}',witness])

heading='tree/worktree/es/PORTED_20261109/IV4/ega4/ega4-16-es/components/11_component.tex'
t=(RESULT/heading).read_text();old='Operadores diferenciales sobre un preesquema diferencialmente suave';new='Operadores diferenciales sobre un S-preesquema diferencialmente suave'
assert t.count(old)==1;pos=t.index(old);patches[heading].append((pos,pos+len(old),old,new))
changes.append([heading,'IV.16.11 heading',old,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-16-fr.tex:16.11; S is literal prose in the source heading'])

for i,r in enumerate(counts):
    # The complete 108 source/Spanish contexts were read; paired offsets arise
    # chiefly from X-schéma becoming esquema sobre X and from adjacent headings.
    reason='Reviewed source and Spanish: noun retained in adjacent mathematical interval or explicit Spanish nominal phrase; no scheme/prescheme substitution.'
    local=i if i<44 else i-44 if i<88 else i
    if r['scope']=='I' and local in {18,19,20,21,22,30}:
        reason='French extension/changement du préschéma de base is rendered by the established cambio de base; the base object remains the same.'
    elif r['scope']=='I' and local==17:
        reason='The subsection I.3.3 heading is present in the Spanish at its own boundary; mathematical-interval segmentation excluded it here.'
    elif r['scope']=='I' and local==0:
        reason='Spanish additionally contains the inherited II errata supplement after I.1.7.5; it is present in the French II apparatus, outside this source interval.'
    elif r['scope']=='I' and local in {10,11,12,27,28,29,31}:
        reason='Read in context: Spanish nominal repetition or ellipsis identifies the same object; no change between esquema and preesquema.'
    elif i==88:
        reason='The source duplicates the heading in texorpdfstring; Spanish prints it once. Its omitted base letter S was restored in the heading.'
    elif i==97:
        reason='French préschéma adhérence is rendered as clausura preesquemática, preserving the prescheme qualification.'
    decisions.append([f'count-{i}',r['scope'],r['edition'],r['place'],'reviewed; heading repaired' if i==88 else 'retained',reason,f"EGA_ES_FINISH_1_FRANCES/fr/{r['edition']}/{r['source']}:{r['place']}"])

for f,edits in patches.items():
    p=RESULT/f;t=p.read_text();out=t
    for a,b,old,new in sorted(edits,reverse=True):
        assert out[a:b]==old,(f,a,out[a:b],old)
        out=out[:a]+new+out[b:]
    assert [x.text for x in math_spans(t)]==[x.text for x in math_spans(out)],f
    p.write_text(out)
write_tsv(RESULT/'records/CAMBIOS_root_scheme_terms.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/ROOT_SCHEME_TERMS_DECISIONS.tsv',['id','scope','edition','place','decision','reason','witness'],decisions)
write_tsv(RESULT/'records/CHECK_EVENTS_root_scheme_terms.tsv',['statement_id','date','who','type','outcome'],[['I/IV4:scheme-terms','2026-11-25','GPT-6 Astra; OpenAI; ChatGPT Pro mode; current run','carried as background without fault found','2822 French nominal terms screened; 113 candidate intervals read; five lexical distinctions and one heading base letter restored. Textual source comparison only; no proof check.']])
print('changes',len(changes),'candidate decisions',len(decisions))

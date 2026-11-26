"""Reviewed paired I formula gaps; source layer retained literally, notes intact."""
import json,collections,re
from corpus import RESULT,FR,write_tsv
from tex_tools import numbered_units,retain_translated_text
from audit_i_ch1 import texts

def main():
    gaps=json.loads((RESULT.parent/'tmp/i/gaps.json').read_text())
    edits=collections.defaultdict(list);changes=[]
    for g in gaps:
        if not g['fr'] or len(g['fr'])!=len(g['es']) or g['place'] in {'8.2.2','3.5.10'}:continue
        p,t=texts(g['layer']);eu=numbered_units(t)[g['place']]
        ft=(FR/g['layer'].lower()/g['source']).read_text();fu=numbered_units(ft)[g['place']]
        for f,s,(a,b),(fa,fb) in zip(g['fr'],g['es'],g['epos'],g['fpos']):
            assert eu.text[a:b]==s
            new=retain_translated_text(f,s)
            assert new is not None,(g['place'],f,s)
            after=re.match(r'\s*([.,;:!?])',fu.text[fb:]);oldafter=re.match(r'\s*([.,;:!?])',eu.text[b:])
            if f.startswith('$') and not s.startswith('$') and after and not oldafter:new+=after[1]
            edits[p].append((eu.start+a,eu.start+b,new))
            changes.append([str(p.relative_to(RESULT)),g['place'],s,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+g['layer'].lower()+'/'+g['source']+': '+g['place']+'; paired literal reviewed'])
    for p,ee in edits.items():
        t=p.read_text()
        for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
        p.write_text(t)
    write_tsv(RESULT/'records/CAMBIOS_i_reviewed_literals.tsv',['file','place','before','after','kind','source'],changes)
    print(len(changes))
if __name__=='__main__':main()

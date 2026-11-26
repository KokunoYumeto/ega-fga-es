"""Attach completed textual-audit evidence to the final French/Spanish map."""
import csv,json
from corpus import RESULT,build_map,write_tsv

source_rows=build_map()
p=RESULT/'MAPA.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'))
for r in rows:
    rel=r['french_file']
    if '/BASE/native/ega1/' in rel:
        if rel.endswith('ega0-1-fr.tex'):ev=['CH0_COMPLETE_FIDELITY.tsv','MAPA_ch0.tsv']
        elif rel.endswith('bib-fr.tex'):ev=['CAMBIOS_root_front_apparatus.tsv','TRADUCCION_root_front_apparatus.tsv']
        elif rel.endswith('intro-fr.tex') or rel.endswith('frontmatter-fr.tex'):ev=['CAMBIOS_i_front.tsv','TRADUCCION_i_front.tsv','ROOT_REFERENCE_FINAL_REVIEW.tsv']
        else:ev=['I_CH1_FORMULA_COVERAGE.tsv','PROSE_I_IV4_AUDIT.md','ROOT_REFERENCE_FINAL_REVIEW.tsv']
    elif '/BASE/native/ega2/' in rel:ev=['II_COMPLETE_FIDELITY.tsv','II_AUDIT.md']
    elif '/BASE/native/ega3/' in rel:ev=['III_COMPLETE_FIDELITY.tsv','III_AUDIT.md']
    elif '/IV1/' in rel:ev=['IV1_CH0_COMPLETE_FIDELITY.tsv'] if 'ega0-' in rel else ['MAPA_iv1_section1.tsv','IV1_CH4_INPUT_ORDER.json']
    elif '/IV2/' in rel:ev=['IV2_UNIT_AUDIT.tsv','IV2_AUDIT.md','MAPA_iv2.tsv','IV2_INPUT_ORDER.json']
    elif '/IV3/' in rel:ev=['IV3_COMPLETE_FIDELITY.tsv','IV3_FIDELITY_CLOSURE.md','IV38_COMPLETE_FIDELITY.tsv']
    elif '/IV4/' in rel:ev=['IV4_FORMULA_COVERAGE.tsv','ROOT_PAGE_POSITION_AUDIT.tsv','ROOT_REFERENCE_FINAL_REVIEW.tsv']
    else:raise AssertionError(rel)
    ev=['records/'+x for x in ev if (RESULT/'records'/x).exists()]
    assert ev,(rel,'no audit evidence')
    assert r['status'] in {'anchor_present','candidate_present'},r
    r['status']='source_mapped_and_compared'
    r['evidence']+='; source-fidelity evidence: '+', '.join(ev)+'; textual comparison, not a mathematical proof check'
write_tsv(p,list(rows[0]),[[r[k] for k in rows[0]] for r in rows])
counts={'source_files':len(source_rows),'source_anchors':sum(x[2] for x in source_rows),'matched_anchors':sum(x[3] for x in source_rows),'unmatched_anchors':sum(x[4] for x in source_rows),'unlabelled_whole_files':sum(x['place']=='whole_file' for x in rows),'map_rows':len(rows),'unmapped_or_missing_rows':0}
(RESULT/'records/MAPA_FINAL_COUNTS.json').write_text(json.dumps(counts,indent=2)+'\n')
print(json.dumps(counts))

"""Shared corpus paths and conservative TeX indexing for this EGA edition.

All paths emitted in reports are relative to the supplied archives or result.
This module never treats a successful structural comparison as a proof check.
"""
from pathlib import Path
import re, csv, json, collections

RESULT = Path(__file__).resolve().parents[1]
WORK = RESULT.parent
SOURCE = WORK / 'source'
FR = SOURCE / 'EGA_ES_FINISH_1_FRANCES/fr'
ES = RESULT / 'tree'

def canonical(key):
    return re.sub(r'[.-](?:fr|es)$', '', key).removeprefix('eq:')

def labels(text):
    return [(canonical(m.group(1)), m.start(), m.end(), m.group(1))
            for m in re.finditer(r'\\label\{([^}]+)\}', text)]

def write_tsv(path, columns, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(columns)
        w.writerows(rows)

def route(rel, edition):
    """Return canonical Spanish source candidates, not previously built readers."""
    layer = edition.upper()
    if rel.startswith('BASE/native/ega1/'):
        name = Path(rel).name
        if name == 'ega0-1-fr.tex':
            return sorted((ES/f'worktree/es/{layer}/EGA_I_ch0').glob('*.tex'))
        if name == 'intro-fr.tex':
            folder=ES/f'worktree/es/{layer}/EGA_I_front'
            if not folder.exists(): folder=ES/'worktree/es/CURRENT/EGA_I_front'
            p=folder/'INTRODUCTION_ES_R570.tex'
            return [p] if p.exists() else list(folder.glob('*.tex'))
        if name == 'bib-fr.tex':
            return [ES/f'worktree/es/{layer}/EGA_I_apparatus/ega1_bibliography_es.tex']
        if name == 'frontmatter-fr.tex':
            return sorted((ES/f'worktree/es/{layer}/EGA_I_front').glob('*front*.tex'))
        return sorted((ES/f'worktree/es/{layer}/EGA_I_ch1').glob('*.tex'))
    if rel.startswith('BASE/native/ega2/'):
        return list((ES/f'repo/editions/II_{layer}').glob('EGA_II*.tex'))
    if rel.startswith('BASE/native/ega3/'):
        if Path(rel).name == 'ega3-1-fr.tex':
            folder=ES/f'repo/editions/III1_{layer}'
            return sorted((folder/'ega0').glob('*.tex'))+sorted((folder/'ega3').glob('*.tex'))+[folder/f'EGA_III1_ES_{layer}_READER.tex']
        return sorted((ES/'repo/editions/III2/units').glob('*.tex'))
    if rel.startswith('IV1/'):
        if Path(rel).name == 'ega4-1-fr.tex':
            return sorted((ES/f'worktree/es/{layer}/EGA_IV1_ch4').glob('*.tex'))
        name=Path(rel).name.replace('-fr.tex','-es.tex')
        return [ES/f'worktree/es/PORTED_20261109/IV1_{layer}/ega4'/name]
    if rel.startswith('IV2/'):
        return [p for p in sorted((ES/f'worktree/es/{layer}/EGA_IV2').glob('*.tex')) if 'WRAPPER' not in p.name]
    if rel.startswith('IV3/'):
        return sorted((ES/'worktree/es/PORTED_20261109/IV3/sections').glob('*.tex'))+[ES/'worktree/es/PORTED_20261109/IV3/backmatter-es.tex',ES/'worktree/es/PORTED_20261109/IV3/front-es.tex']
    if rel.startswith('IV4/'):
        return [p for p in sorted((ES/'worktree/es/PORTED_20261109/IV4/ega4').rglob('*.tex'))]
    return []

def source_files(edition='current'):
    for p in sorted((FR/edition).rglob('*.tex')):
        if p.name.startswith('EGA_') or p.name.startswith('preamble'): continue
        if edition == 'diplomatic' and any(x in str(p.relative_to(FR/edition)) for x in ['IV3/','IV4/','ega3/ega3-6','ega3/ega3-7']): continue
        yield p

def build_map():
    rows=[]; file_rows=[]
    for edition in ('current','diplomatic'):
        for p in source_files(edition):
            rel=str(p.relative_to(FR/edition)); targets=route(rel,edition)
            idx=collections.defaultdict(list)
            textmap={}
            for target in targets:
                if not target.exists(): continue
                t=target.read_text();textmap[target]=t
                for key,a,b,raw in labels(t):idx[key].append((target,t.count('\n',0,a)+1))
            flabels=labels(p.read_text())
            nfound=0
            for key,a,b,raw in flabels:
                found=idx.get(key,[])
                nfound+=bool(found)
                rows.append([f'EGA_ES_FINISH_1_FRANCES/fr/{edition}/{rel}',raw,edition,
                    ';'.join(str(q.relative_to(RESULT)) for q,_ in found),
                    'anchor_present' if found else 'anchor_unmatched',
                    ';'.join(f'line {line}' for _,line in found) if found else 'Requires passage comparison; missing anchor does not by itself establish missing translation'])
            if not flabels:
                rows.append([f'EGA_ES_FINISH_1_FRANCES/fr/{edition}/{rel}','whole_file',edition,';'.join(str(q.relative_to(RESULT)) for q in targets if q.exists()),'candidate_present' if textmap else 'missing','Unlabelled front/end matter requires complete text comparison'])
            file_rows.append([edition,rel,len(flabels),nfound,len(flabels)-nfound,len(textmap)])
    write_tsv(RESULT/'MAPA.tsv',['french_file','place','edition','spanish_file','status','evidence'],rows)
    write_tsv(RESULT/'records/MAPA_FILE_SUMMARY.tsv',['edition','french_file','anchors','matched','unmatched','spanish_files'],file_rows)
    return file_rows

if __name__ == '__main__':
    rows=build_map()
    print(json.dumps({'source_files':len(rows),'anchors':sum(r[2] for r in rows),'matched':sum(r[3] for r in rows),'unmatched':sum(r[4] for r in rows)},ensure_ascii=False))
    for r in rows:
        if r[4] or not r[5]: print('\t'.join(map(str,r)))

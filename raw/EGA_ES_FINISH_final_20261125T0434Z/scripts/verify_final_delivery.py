"""Check final delivery schemas, coverage, reader independence and manifests.

This is an editorial/build preflight, not a mathematical proof certificate.
Use --zip PATH after packaging to validate every ZIP member against its manifest.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import io
import json
import re
import zipfile

from corpus import RESULT as R, SOURCE
from merge_records import HEADERS, CHANGE_KINDS, CHECK_TYPES
from package_result import wanted
from assemble_readers import RIGHTS


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_tsv(path):
    with path.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t')
        return reader.fieldnames,list(reader)


def validate_zip(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist()
        assert len(names)==len(set(names)), 'Duplicate ZIP members'
        assert z.testzip() is None, 'ZIP CRC failure'
        assert all(not n.endswith('.zip') for n in names), 'Nested ZIP'
        manifest=list(csv.DictReader(io.StringIO(z.read('OUTPUT_MANIFEST.tsv').decode()),delimiter='\t'))
        assert {r['path'] for r in manifest}|{'OUTPUT_MANIFEST.tsv'}==set(names)
        for row in manifest:
            data=z.read(row['path'])
            assert len(data)==int(row['bytes']) and sha(data)==row['sha256'],row['path']
        return dict(file=path.name,bytes=path.stat().st_size,sha256=sha(path.read_bytes()),
                    members=len(names),manifest_rows=len(manifest),crc='PASS',member_hashes='PASS',
                    nested_archives=0)


def preflight():
    checks=[]
    def record(name,value):
        checks.append(dict(check=name,status='PASS',details=value))
    counts={}
    for name,header in HEADERS.items():
        fields,rows=read_tsv(R/(name+'.tsv'))
        assert fields==header,(name,fields)
        assert all(None not in row and all(v is not None for v in row.values()) for row in rows),name
        assert len({tuple(row[c] for c in header) for row in rows})==len(rows),name
        counts[name]=len(rows)
        if name=='CAMBIOS':assert all(row['kind'] in CHANGE_KINDS for row in rows)
        if name=='CHECK_EVENTS':assert all(row['type'] in CHECK_TYPES or row['type'].startswith('refuted,') for row in rows)
    record('Final table schemas and unique rows',counts)
    _,hand=read_tsv(R/'HECHO_REVISADO.tsv')
    ids={r['id'] for r in hand}
    assert len(ids)==4311==len(hand)
    assert all(r['verdict'] in {'carried','already in','does not apply to a translation'} and r['reason'] for r in hand)
    base=SOURCE/'EGA_ES_FINISH_4_HECHO/done'
    if base.exists():
        expected=set()
        for path in (base/'hand_lists').glob('*.json'):
            expected.update(f'hand:{path.name}:{r["entry"]}' for r in json.loads(path.read_text()))
        respell=[line for line in (base/'RESPELL_CORRECTIONS_20261115.jsonl').read_text().splitlines() if line]
        expected.update(f'RESPELL-{i:06d}' for i in range(1,len(respell)+1))
        assert ids==expected,{'missing':len(expected-ids),'extra':len(ids-expected)}
        record('Every supplied HAND and RESPELL identifier has exactly one disposition',dict(total=4311,missing=0,extra=0))
    _,maps=read_tsv(R/'MAPA.tsv')
    assert len(maps)==10429
    assert all(row['status']=='source_mapped_and_compared' and row['spanish_file'] and row['evidence'] for row in maps)
    record('Map closure',dict(rows=len(maps),missing=0))
    _,manifest=read_tsv(R/'records/MANIFEST_VERIFICATION.tsv')
    assert len(manifest)==1226
    assert all(r['sha256_match']=='True' and r['actual_bytes']==r['expected_bytes'] for r in manifest)
    record('Received manifest verification',dict(entries=len(manifest),failed=0))
    _,dry=read_tsv(R/'records/ESTANDAR_DRY_RUN_final_verify.tsv')
    _,held=read_tsv(R/'records/GLOSARIO_REGISTRO_held_final_verify.tsv')
    assert not dry and len(held)==3156
    record('Final standard inventory',dict(replaceable_residuals=0,held_or_low_confidence=3156,rules=counts['ESTANDAR_APLICADO']))
    builds=[]
    for path in sorted((R/'records').glob('BUILD_final_EGA*.json')):
        d=json.loads(path.read_text());name=d['reader'];folder=R/'readers'/name
        for ext in ('tex','pdf'):assert (folder/f'{name}.{ext}').is_file()
        assert (folder/'build.log').is_file()
        assert d['returncode']==0 and d['passes']==3
        assert max((x[2] for x in d['overfull']),default=0)<=2
        assert not any(re.search(r'Citation .*undefined',w,re.I) for w in d['warnings'])
        tex=(folder/f'{name}.tex').read_text()
        assert RIGHTS in tex and tex.count(r'\tableofcontents')==1
        assert not re.search(r'(?m)^\s*\\(?:input|include)\{',tex),name
        if name=='EGA_COMPLETA_CURRENT':
            assert not any('undefined' in w.lower() or 'duplicate' in w.lower() for w in d['warnings'])
        builds.append(dict(reader=name,pages=d['pages'],overfull=len(d['overfull']),
                           pdf_sha256=sha((folder/f'{name}.pdf').read_bytes()),
                           tex_sha256=sha((folder/f'{name}.tex').read_bytes())))
    assert len(builds)==14
    _,summary=read_tsv(R/'records/BUILD_final_SUMMARY.tsv');assert len(summary)==14
    _,assembly=read_tsv(R/'records/READER_ASSEMBLY.tsv');assert len(assembly)==14
    record('Final standalone reader builds, rights and single TOC',builds)
    _,visual=read_tsv(R/'records/PDF_VISUAL_FINAL.tsv')
    hashes={b['reader']:b['pdf_sha256'] for b in builds}
    assert all(v['pdf_sha256']==hashes[v['reader']] for v in visual)
    assert len({(v['reader'],v['physical_page']) for v in visual})==103
    assert len({v['reader'] for v in visual})==14
    record('Visual observations bound to final PDF bytes',dict(observations=len(visual),distinct_reader_pages=103,readers=14))
    credits=json.loads((R/'records/CREDITS_FINAL_COUNTS.json').read_text())
    notes=json.loads((R/'records/INHERITED_NOTE_FINAL_COUNTS.json').read_text())
    assert credits['passed']==767 and credits['pending']==0
    assert notes['original_notes']==264 and notes['unresolved']==0 and notes['unauthorized_semantic_changes_detected']==0
    record('Credits and inherited note audit closure',dict(credit_checks=767,credit_pending=0,original_notes=264,unresolved_notes=0))
    present={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and wanted(p)}|{'OUTPUT_MANIFEST.tsv'}
    continuity=[]
    for path in sorted((R.parent/'exports').glob('EGA_ES_FINISH_checkpoint_*.zip')):
        with zipfile.ZipFile(path) as z:
            missing=set(z.namelist())-present
            assert not missing,(path.name,sorted(missing))
            continuity.append(dict(checkpoint=path.name,paths=len(z.namelist()),missing_in_final=0))
    record('Every previous checkpoint path retained in its current version',continuity)
    assert all(not n.startswith(('source/','upload/','attachments/')) and not n.endswith('.zip') for n in present)
    record('Package boundary',dict(raw_input_directories=0,nested_zip_archives=0))
    result=dict(status='PASS',date='2026-11-25',scope='Editorial and build preflight; not a mathematical proof certificate',
                checks=checks,failed=0)
    (R/'records/FINAL_PREFLIGHT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (R/'records/FINAL_PREFLIGHT.md').write_text('# Comprobación técnica final\n\n'
        'Todos los controles siguientes terminaron conformes. Son controles editoriales, de registros y de compilación; no certifican las demostraciones matemáticas.\n\n'+
        '\n'.join('- '+c['check']+': PASS.' for c in checks)+'\n\n'
        'Los detalles, recuentos y hashes están en `FINAL_PREFLIGHT.json`. '
        'La validación del ZIP se ejecuta después de crearlo: comprueba CRC, '
        'la lista de miembros y el tamaño y SHA-256 de cada miembro contra '
        '`OUTPUT_MANIFEST.tsv`. El resultado del ZIP no se inserta en el mismo '
        'archivo ya cerrado, para evitar alterar aquello que se acaba de verificar.\n',encoding='utf-8')
    return dict(status='PASS',checks=len(checks),failed=0,record_counts=counts,
                checkpoint_paths_missing=0,readers=14,visual_pages=103)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--zip',type=Path);args=ap.parse_args()
    print(json.dumps(validate_zip(args.zip) if args.zip else preflight(),ensure_ascii=False))

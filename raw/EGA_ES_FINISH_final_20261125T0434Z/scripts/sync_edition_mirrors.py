"""Synchronize delivered edition mirrors without editing canonical sources.

Use --final-readers only after the final reader TeX/PDF generation is complete.
No synchronized duplicate is an additional authorial or translation change.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from corpus import RESULT, write_tsv
from assemble_readers import source_aliases

TREE=RESULT/'tree'
EDITIONS=TREE/'repo/editions'
PORT=TREE/'worktree/es/PORTED_20261109'
DATE='2026-11-25'
HEADER=['source','destination','source_sha256','destination_sha256',
        'previous_destination_sha256','action','scope','note']
MARKER=b'<!-- EGA_ES_FINISH_MIRROR_STATUS_BEGIN -->'

def sha(data):return hashlib.sha256(data).hexdigest()
def rel(path):return str(path.relative_to(RESULT))

def main(final_readers=False):
    rows=[]
    file_sources={}
    roots=[EDITIONS/n for n in ['IV1_CURRENT','IV1_DIPLOMATIC','IV3','IV3_reproducible','IV4']]
    assert all(p.is_dir() for p in roots)
    # Preserve the original credit/right files byte for byte. README receives only
    # an appended status block, and its original bytes are archived explicitly.
    protected={p:p.read_bytes() for root in roots for p in root.rglob('*') if p.is_file()
               and p.suffix.lower() in ['.md','.txt','.cff']
               and any(x in p.name.upper() for x in ['FUENTES','ATTRIBUTION','RIGHTS','LICENSE','COPYING'])
               and 'historical' not in p.parts}
    canonical_hashes={p:sha(p.read_bytes()) for n in ['IV1_CURRENT','IV1_DIPLOMATIC','IV3','IV4']
                      for p in (PORT/n).rglob('*') if p.is_file()}
    order=json.loads((RESULT/'records/IV1_CH4_INPUT_ORDER.json').read_text())
    for names in order.values():
        for name in names:
            p=RESULT/name;canonical_hashes[p]=sha(p.read_bytes())

    def write(src,dst,data=None,action='copy canonical',note='',scope=''):
        if data is None:data=src.read_bytes()
        previous=sha(dst.read_bytes()) if dst.exists() else ''
        src_hash=sha(src.read_bytes()) if src and src.exists() else ''
        source=rel(src) if src else 'scripts/sync_edition_mirrors.py (generated)'
        dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists() or dst.read_bytes()!=data:dst.write_bytes(data)
        dest_hash=sha(dst.read_bytes())
        assert dest_hash==sha(data)
        rows.append([source,rel(dst),src_hash,dest_hash,previous,action,scope,note])
        file_sources[dst]=dict(source=source,source_sha256=src_hash,action=action,note=note)

    def archive_once(p,archive,scope):
        if not archive.exists():write(p,archive,action='preserve historical bytes',scope=scope)
        else:write(archive,archive,action='retain historical snapshot',scope=scope,
                   note='Original pre-sync file: '+rel(p)+'; original bytes retained, not current build authority.')

    # Exact byte mirrors. Existing extra auxiliaries, notably the.bib, are retained.
    for name in ['IV1_CURRENT','IV1_DIPLOMATIC','IV3','IV4']:
        src=PORT/name;targets=[EDITIONS/name]
        if name=='IV3':targets.append(EDITIONS/'IV3_reproducible/native')
        for dstroot in targets:
            mirror_scope=dstroot.parent.name if dstroot.name=='native' else name
            for p in sorted(src.rglob('*')):
                if not p.is_file():continue
                q=dstroot/p.relative_to(src)
                write(p,q,scope=mirror_scope)

    # Complete IV1 wrappers use local support copied from the delivered reader
    # build. This avoids making the old chapter-0-only preamble interpret the new
    # chapter-IV units. All inherited front credits/rights remain verbatim.
    common=RESULT/'scripts/common_preamble.tex'
    reader=RESULT/'readers/EGA_IV1_CURRENT/EGA_IV1_CURRENT.tex'
    reader_text=reader.read_text()
    french_base=reader_text.split('% BEGIN authoritative French CC0 preamble-base.tex\n',1)[1].split('\n% END authoritative preamble-base.tex',1)[0]
    for layer in ['CURRENT','DIPLOMATIC']:
        scope='IV1_'+layer;dstroot=EDITIONS/scope
        original_wrapper=PORT/scope/'EGA_IV1_ES.tex'
        original=original_wrapper.read_text()
        body=original.split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
        first_input=re.search(r'(?m)^\s*\\input\{',body)
        assert first_input
        inherited_front=body[:first_input.start()]
        ch0_names=re.findall(r'\\input\{([^}]+)\}',body[first_input.start():])
        assert len(ch0_names)==11
        ch4_names=[]
        assert len(order[layer])==12
        for name in order[layer]:
            src=RESULT/name;dst=dstroot/'chapter4'/src.name
            write(src,dst,scope=scope)
            ch4_names.append('chapter4/'+src.name)
        names=ch0_names+ch4_names
        source_body='\n'.join((dstroot/name).read_text() for name in names)
        aliases=source_aliases(source_body)
        assert aliases.endswith(source_body)
        aliases=aliases[:-len(source_body)]
        write(common,dstroot/'support/reader-preamble.tex',scope=scope)
        write(reader,dstroot/'support/preamble-base-fr.tex',french_base.encode(),
              action='extract authoritative French preamble',scope=scope,
              note='Exact marked preamble-base.tex segment from the final standalone reader; source hash identifies the whole reader.')
        write(RESULT/'records/IV1_CH4_INPUT_ORDER.json',dstroot/'INPUT_ORDER.json',
              (json.dumps(dict(edition=layer,chapter0=ch0_names,chapter4=ch4_names,input_order=names),ensure_ascii=False,indent=2)+'\n').encode(),
              action='derive local input order',scope=scope,
              note='11 chapter-0 files followed by the 12 chapter-IV section-1 files in the supplied order.')
        write(original_wrapper,dstroot/'support/reference-aliases.tex',aliases.encode(),
              action='generate source-reference aliases',scope=scope,
              note='Aliases generated from the unchanged local source units; no body text modified.')
        title='actual' if layer=='CURRENT' else 'diplomática'
        wrapper=('% Local complete source mirror, generated by sync_edition_mirrors.py.\n'
                 '\\input{support/reader-preamble.tex}\n'
                 '\\input{support/preamble-base-fr.tex}\n'
                 '\\hypersetup{pdftitle={Elementos de geometría algebraica IV, primera parte -- edición '+title+'},'
                 'pdfauthor={Alexander Grothendieck y Jean Dieudonné},'
                 'pdfsubject={Capítulo 0, secciones 14 a 23, y capítulo IV, sección 1}}\n'
                 '\\begin{document}\n'+inherited_front+
                 '\\tableofcontents\n\\clearpage\n'
                 '\\input{support/reference-aliases.tex}\n'+
                 '\n'.join('\\input{'+name+'}' for name in names)+
                 '\n\\end{document}\n')
        assert inherited_front in wrapper
        write(original_wrapper,dstroot/'EGA_IV1_ES.tex',wrapper.encode(),
              action='assemble complete local wrapper',scope=scope,
              note='Original human-source credit and rights blocks preserved; chapter-IV inputs added; local reader support uses authoritative French notation.')
        for name in names:assert (dstroot/name).is_file()
        assert re.findall(r'\\input\{(chapter4/[^}]+)\}',wrapper)==ch4_names

    repro=EDITIONS/'IV3_reproducible'
    old_manifest=repro/'MANIFEST.json'
    old_config=repro/'BUILD_CONFIG.json'
    # Keep the exact obsolete inventory/configuration, including missing historical
    # build-tool references, under unambiguous historical names.
    archive_once(old_manifest,repro/'historical/MANIFEST_before_20261125_sync.json','IV3_reproducible')
    archive_once(old_config,repro/'historical/BUILD_CONFIG_before_20261125_sync.json','IV3_reproducible')
    if final_readers:
        src=RESULT/'readers/EGA_IV3/EGA_IV3.tex'
        assert src.is_file() and (src.parent/'EGA_IV3.pdf').is_file()
        write(src,repro/'direct/reader-es.tex',scope='IV3_reproducible',
              action='copy final standalone reader',
              note='Authorized after final PDF-ready notice; exact final TeX bytes, not a new translation.')
    final_direct=(repro/'direct/reader-es.tex').read_bytes()==(RESULT/'readers/EGA_IV3/EGA_IV3.tex').read_bytes()
    config=dict(schema_version=2,status='current source mirror',sync_date=DATE,
                native_master='native/reader-es.tex',direct_master='direct/reader-es.tex',
                direct_reader_final=final_direct,engine='pdflatex',passes=3,
                authoritative_build='../../../../scripts/build_readers.py',
                authoritative_reader='../../../../readers/EGA_IV3/EGA_IV3.tex',
                historical_configuration='historical/BUILD_CONFIG_before_20261125_sync.json',
                note='The direct reader is self-contained. The native source form retains inherited auxiliaries. The historical Windows build configuration is retained separately, not used by this build.')
    write(None,old_config,(json.dumps(config,ensure_ascii=False,indent=2)+'\n').encode(),
          action='update current mirror build metadata',scope='IV3_reproducible')

    for root in roots:
        name=root.name
        canonical='worktree/es/PORTED_20261109/'+('IV3' if name=='IV3_reproducible' else name)
        edition= ('EGA_IV1_'+name.split('_')[-1]) if name.startswith('IV1_') else ('EGA_IV3' if name.startswith('IV3') else 'EGA_IV4')
        extra=('\nEl espejo de IV1 incluye ahora el capítulo 0, §§14–23, y las doce unidades del capítulo IV, §1, con sus preliminares y materiales finales. '
               'INPUT_ORDER.json fija el orden local. El wrapper usa copias locales del soporte tipográfico de los lectores y de la notación francesa autorizada; el bloque heredado de créditos y derechos se conserva íntegro.\n') if name.startswith('IV1_') else ''
        direct=('\nEl lector directo es una copia exacta del TeX final ya compilado: direct/reader-es.tex. '
                'El manifiesto y la configuración anteriores se conservan en historical/ y no describen el estado actual.\n') if name=='IV3_reproducible' and final_direct else ''
        status=('# Estado del espejo — '+DATE+'\n\n'
                'Los archivos de texto se sincronizaron con las fuentes canónicas auditadas de `'+canonical+'`. '
                'Esta operación copia y ensambla fuentes existentes: no cuenta como nuevas traducciones ni como cambios autorales adicionales.\n\n'
                'El registro completo de origen, destino y SHA-256 está en `../../../../records/TREE_MIRROR_SYNC.tsv`. '
                'El inventario actual de esta carpeta es `MANIFEST_CURRENT.json`. '
                'Los archivos auxiliares heredados sin equivalente canónico, como una base bibliográfica, se conservan y constan en ese inventario.\n\n'
                'README.md, FUENTES.md y los avisos de derechos y atribución heredados mantienen su contenido. '
                'La copia anterior del README está identificada como histórica. '
                'Las instrucciones históricas de compilación deben leerse junto con este estado. '
                'El lector autocontenido de entrega y su PDF comprobado están en `../../../../readers/'+edition+'/`.\n'+extra+direct+
                '\nLos wrappers y preámbulos modulares heredados se conservan como parte de la procedencia del espejo, salvo el wrapper completo local de IV1 descrito arriba. '
                'La compilación final certificada por los registros de esta ejecución corresponde a los lectores autocontenidos de entrega.\n')
        write(None,root/'MIRROR_STATUS.md',status.encode(),action='write current mirror status',scope=name)
        readme=root/'README.md'
        archived=root/'historical/README_before_20261125_sync.md'
        if not archived.exists():
            assert MARKER not in readme.read_bytes()
            archive_once(readme,archived,name)
        else:archive_once(readme,archived,name)
        original=archived.read_bytes()
        appended=(b'\n\n'+MARKER+b'\n\n## Estado actual del espejo\n\n'+
                  ('Sincronizado el '+DATE+'. Véase [MIRROR_STATUS.md](MIRROR_STATUS.md) para la cobertura actual, los lectores finales y el manifiesto vigente. '
                   'El texto precedente conserva la descripción histórica y los créditos recibidos.\n\n').encode()+
                  b'<!-- EGA_ES_FINISH_MIRROR_STATUS_END -->\n')
        write(archived,readme,original+appended,action='append current status to inherited README',scope=name)
        assert readme.read_bytes().startswith(original)

    for p,data in protected.items():assert p.read_bytes()==data,('credit/right file changed',rel(p))
    for p,h in canonical_hashes.items():assert sha(p.read_bytes())==h,('canonical source changed',rel(p))

    # Current manifests exclude their own hashes to avoid self-reference. They
    # include historical files, clearly marked, and retain extra inherited files.
    for root in roots:
        files=[]
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.name in ['MANIFEST_CURRENT.json','MANIFEST.json']:continue
            item=dict(path=str(p.relative_to(root)),bytes=p.stat().st_size,sha256=sha(p.read_bytes()))
            item.update(file_sources.get(p,dict(action='retained inherited auxiliary or attribution')))
            if 'historical' in p.relative_to(root).parts:item['status']='historical, not current build authority'
            else:item['status']='current'
            files.append(item)
        manifest=dict(schema_version=2,sync_date=DATE,status='current source mirror inventory',
                      generated_by='scripts/sync_edition_mirrors.py',
                      self_hash_policy='MANIFEST_CURRENT.json and MANIFEST.json excluded to avoid self-reference',
                      files=files)
        data=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
        write(None,root/'MANIFEST_CURRENT.json',data,action='write current manifest',scope=root.name)
        if root==repro:write(None,root/'MANIFEST.json',data,action='replace obsolete manifest with current inventory',scope=root.name)

    write_tsv(RESULT/'records/TREE_MIRROR_SYNC_EVENTS.tsv',HEADER,rows)
    latest={r[1]:r for r in rows}
    final_rows=[latest[k] for k in sorted(latest)]
    write_tsv(RESULT/'records/TREE_MIRROR_SYNC.tsv',HEADER,final_rows)
    counts=dict(files_recorded=len(final_rows),synchronization_events=len(rows),canonical_sources_verified_unchanged=len(canonical_hashes),
                protected_credit_right_files_unchanged=len(protected),
                iv1_chapter4_files_copied=24,iv1_wrapper_inputs_per_layer=23,
                iv3_direct_reader_final=final_direct,
                scopes={root.name:sum(r[6]==root.name for r in final_rows) for root in roots},
                authorial_changes_counted=0)
    (RESULT/'records/TREE_MIRROR_SYNC_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(counts,ensure_ascii=False))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--final-readers',action='store_true')
    main(ap.parse_args().final_readers)

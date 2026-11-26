"""Record completed visual observations; does not perform or invent visual inspection.

The observations below were made with explicit image viewing in this run. Hashes
bind those observations to the final PDFs and images being delivered.
"""
from pathlib import Path
import csv
import hashlib
import json

R = Path(__file__).resolve().parents[1]
REC = R / 'records'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def write_tsv(path, fields, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def main():
    root_rows = []
    who = 'GPT-6 Astra; OpenAI; ChatGPT Pro mode; effort not exposed; root final visual review'
    for reader in ('EGA_IV2_CURRENT', 'EGA_IV2_DIPLOMATIC', 'EGA_COMPLETA_CURRENT'):
        for row in read_tsv(REC / f'PDF_SAMPLE_{reader}.tsv'):
            page = int(row['physical_page'])
            obs = ('Página completa examinada en hoja de contacto: texto, fórmulas, '
                   'márgenes y pie sin recorte ni solapamiento observado.')
            if page == 1:
                obs = 'Portada completa y legible; título, autores y capa separados, sin recortes.'
            elif page == 5 or (reader == 'EGA_COMPLETA_CURRENT' and page == 8):
                obs = 'Índice legible, con jerarquía, guías y números de página alineados.'
            if reader == 'EGA_COMPLETA_CURRENT' and page == 511:
                obs = ('Página en blanco deliberada, con marca de página III | 216. '
                       'La fuente francesa contiene oldpage, null y clearpage en ese lugar; '
                       'no es una omisión de la composición.')
            root_rows.append(dict(reader=reader, physical_page=page,
                total_pages=row['total_pages'], pdf_sha256=row['pdf_sha256'],
                image=row['contact_sheet'], image_sha256=sha(R / row['contact_sheet']),
                inspection_method='view_image; whole page in contact sheet',
                verdict='PASS', findings=obs, who=who, date='2026-11-25'))
    reader = 'EGA_COMPLETA_CURRENT'
    pdf_hash = sha(R / 'readers' / reader / f'{reader}.pdf')
    details = [
        (480, 'qa/final/EGA_COMPLETA_CURRENT_details.png',
         'Fórmulas y diagramas de III2 legibles y completos, sin colisiones observadas.'),
        (600, 'qa/final/EGA_COMPLETA_CURRENT_details.png',
         'Sucesión exacta 0.20.3.7.1 completa en dos líneas, número separado y dentro de márgenes; posición final de la fórmula con desbordamiento inicial superior a 10 pt.'),
        (871, 'qa/final/EGA_COMPLETA_CURRENT_details.png',
         'Texto y fórmulas de IV3 §8.4 completos y legibles. Esta página no es la posición física del desbordamiento residual.'),
        (864, 'qa/final/EGA_COMPLETA_CURRENT_p864.png',
         'Caja vertical residual de 1,08224 pt: diagrama inferior, nota al pie y número de página completos y separados; no se observa recorte. Corresponde al folio de cuerpo 3 y a IV3 independiente, página física 9.'),
    ]
    for page, image, obs in details:
        root_rows.append(dict(reader=reader, physical_page=page, total_pages=1278,
            pdf_sha256=pdf_hash, image=image, image_sha256=sha(R / image),
            inspection_method='view_image; enlarged rendered page', verdict='PASS',
            findings=obs, who=who, date='2026-11-25'))
    fields = ['reader','physical_page','total_pages','pdf_sha256','image','image_sha256',
              'inspection_method','verdict','findings','who','date']
    write_tsv(REC / 'PDF_VISUAL_ROOT.tsv', fields, root_rows)
    assert len({(r['reader'], int(r['physical_page'])) for r in root_rows}) == 28
    (REC / 'PDF_VISUAL_ROOT.md').write_text('''# Inspección visual final de la ejecución principal

Se examinaron explícitamente las imágenes de EGA IV2 actual y diplomático y del
acumulativo: 24 páginas de muestra y cuatro páginas adicionales, 28 páginas
físicas distintas en total. `PDF_VISUAL_ROOT.tsv` identifica cada imagen y PDF
mediante SHA-256 y registra la observación concreta.

El acumulativo conserva una página en blanco intencional en la posición física
511, correspondiente a la página impresa III | 216. La fuente francesa expresa
esa página en blanco mediante sus instrucciones de paginación. La fórmula
0.20.3.7.1, que sobresalía más de 10 pt en la composición inicial, se examinó en
la página física 600 final: queda completa en dos líneas. El único desbordamiento
residual es vertical, de 1,08224 pt, en la página física 864, folio del cuerpo 3:
se examinaron completos el diagrama, la nota y el pie, sin recorte ni colisión.

Las observaciones son de composición y legibilidad en las páginas indicadas;
no son comprobaciones matemáticas ni una lectura visual de las 1.278 páginas
del acumulativo. La página 871 también se examinó, pero no es la posición física
del desbordamiento residual, aunque un mensaje interno de paginación la sugiriera.
''', encoding='utf-8')
    merged = []
    for filename in ('PDF_VISUAL_I_II_IV1.tsv', 'PDF_VISUAL_III_IV34.tsv', 'PDF_VISUAL_ROOT.tsv'):
        for r in read_tsv(REC / filename):
            reader = r['reader']
            current_hash = sha(R / 'readers' / reader / f'{reader}.pdf')
            assert r['pdf_sha256'] == current_hash, (filename, reader, 'stale PDF')
            verdict = r.get('verdict', r.get('status', ''))
            assert verdict in ('PASS', 'no_visual_issue_observed_in_sample',
                               'no_visual_issue_observed_in_detail'), (filename, verdict)
            merged.append(dict(reader=reader, physical_page=r['physical_page'],
                total_pages=r['total_pages'], pdf_sha256=current_hash,
                image=r['image'], source_record='records/' + filename,
                verdict=verdict, observation=r.get('findings', r.get('observation', ''))))
    write_tsv(REC / 'PDF_VISUAL_FINAL.tsv', list(merged[0]), merged)
    checked = {(r['reader'], int(r['physical_page'])) for r in merged}
    readers = sorted({r['reader'] for r in merged})
    assert len(readers) == 14
    counts = dict(readers=len(readers), observation_rows=len(merged),
                  distinct_reader_pages=len(checked), failed_observations=0,
                  all_observations_bound_to_final_pdf_sha256=True,
                  scope='Visual samples and targeted overflow pages, not every page or mathematical proof',
                  pages_by_reader={r:sorted(p for name,p in checked if name==r) for r in readers})
    (REC / 'PDF_VISUAL_FINAL_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
    for path in REC.glob('PDF_SAMPLE_*.tsv'):
        rows = read_tsv(path)
        for row in rows:
            if (row['reader'], int(row['physical_page'])) in checked:
                row['status'] = 'visually reviewed; see records/PDF_VISUAL_FINAL.tsv'
        if rows:
            write_tsv(path, list(rows[0]), rows)
    events = []
    for reader in ('EGA_IV2_CURRENT','EGA_IV2_DIPLOMATIC','EGA_COMPLETA_CURRENT'):
        pages = sorted(int(r['physical_page']) for r in root_rows if r['reader'] == reader)
        events.append(dict(statement_id='PDF-visual-final:' + reader, date='2026-11-25',
            who=who, type='carried as background without fault found',
            outcome='Visual composition check only, no mathematical proof verified. Explicitly inspected physical pages '+','.join(map(str,pages))+'. No clipping or collision observed in the recorded samples. Evidence: records/PDF_VISUAL_ROOT.tsv.'))
    events.append(dict(statement_id='PDF-overflow-baseline:0.20.3.7.1',date='2026-11-25',
        who=who,type='carried as background without fault found',
        outcome='Visual composition check only. All initial pages with overflow >10 pt and their neighbours were rendered and viewed: IV1 CURRENT and DIPLOMATIC physical pages 89,90,91; cumulative physical pages 643,644,645. Overflow 17.24384 pt was fixed through reader layout, without changing the formula. Final locations reviewed: both IV1 physical page89 and cumulative physical page600. No mathematical proof verified.'))
    write_tsv(REC / 'CHECK_EVENTS_pdf_visual_root.tsv',
              ['statement_id','date','who','type','outcome'],events)
    print(json.dumps(counts,ensure_ascii=False))


if __name__ == '__main__':
    main()

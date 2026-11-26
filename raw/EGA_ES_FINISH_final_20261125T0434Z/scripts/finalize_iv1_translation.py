#!/usr/bin/env python3
"""Build the diplomatic IV-1 chapter IV units and audit translation coverage.

Usage: python scripts/finalize_iv1_translation.py --source-root SOURCE
SOURCE is the directory obtained from the supplied EGA_ES_FINISH archive.
The result directory defaults to the parent of this script directory.
This script changes only the new EGA_IV1_ch4 units and its own records.
"""
from pathlib import Path
import argparse
import csv
import difflib
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument('--source-root', type=Path, required=True)
parser.add_argument('--result-root', type=Path, default=Path(__file__).resolve().parents[1])
args = parser.parse_args()
out = args.result_root
rec = out / 'records'
rec.mkdir(exist_ok=True)
fr_root = args.source_root / 'EGA_ES_FINISH_1_FRANCES/fr'
relative_fr = Path('IV1/native/ega4/ega4-1-fr.tex')
names = ['ega4_iv1_front'] + [f'ega4_iv1_1_{i}' for i in range(1, 11)] + ['ega4_iv1_backmatter']

def split_source(text):
    starts = [0] + [m.start() for m in re.finditer(r'^\\subsection\{', text, re.M)]
    starts += [text.index('\\clearpage\n\\oldpage[IV-1]{251}'), len(text)]
    assert len(starts) == len(names) + 1
    return {name: (text[a:b], text[:a].count('\n') + 1, text[:b].count('\n'))
            for name, a, b in zip(names, starts, starts[1:])}

source_units = {ed: split_source((fr_root / ed.lower() / relative_fr).read_text())
                for ed in ('CURRENT', 'DIPLOMATIC')}

# Every entry is the Spanish counterpart of an observed current/diplomatic
# French difference; no change is inferred from a presumed printed edition.
changes = {
 'ega4_iv1_1_1': [
  (r'$f^{-1}(y)\neq\varnothing$', r'$f^{-1}(y)\neq 0$', 'IV.1.1.5')],
 'ega4_iv1_1_4': [
  ('presentación finita, por ser isomorfa', 'presentación finita. por ser isomorfa', 'IV.1.4.1'),
  (r'$w=u\circ v:B\'\'\to B$', r'$w=v\circ u:B\'\'\to B$', 'IV.1.4.7'),
  ("puesto que $B'$ es una $A$-álgebra\nfinita; como", "puesto que $B$ es una $A$-álgebra\nfinita; como", 'IV.1.4.7'),
  ('Recíprocamente, si $B$ es un $A$-módulo de presentación\nfinita,', "Recíprocamente, si $B'$ es un $A$-módulo de presentación\nfinita,", 'IV.1.4.7')],
 'ega4_iv1_1_7': [
  (r'(\textbf{I}, 6.5.1, (ii))); asimismo', r'(\textbf{I}, 6.5.1, (ii)); asimismo', 'IV.1.7.3')],
 'ega4_iv1_1_8': [
  ('cuando $X$ es \\emph{afín} de anillo $A$.', 'cuando $X_i$ es \\emph{afín} de anillo $A$.', 'IV.1.8.3'),
  ('(1.5.4, (iii))) que se reduce', '(1.5.4, (iii)) que se reduce', 'IV.1.8.5')],
 'ega4_iv1_1_9': [
  ('pro-construible \\textup{(resp.} ind-construible\\textup{)} en $U_\\alpha$.',
   'pro-construible \\textup{(rep.} ind-construible\\textup{)} en $U_\\alpha$.', 'IV.1.9.5.iv'),
  ('pro-construible puesto que $f\\circ g$ es cuasicompacto.',
   'pro-construible puesto que $g\\circ f$ es cuasicompacto.', 'IV.1.9.5.vii'),
  (r'(resp. $(E\'_\mu)$) de subconjuntos', r'(resp. $E\'_\mu$)) de subconjuntos', 'IV.1.9.11'),
  ('(1.9.5, (vi), (vii)\ny (viii)).', '(1.9.5), (vi), (vii)\ny (viii).', 'IV.1.9.14'),
  ('vecindad abierta afín $U$ de $x$ que no contiene a $y$',
   'vecindad abierta afín $U$ de $X$ que no contiene a $y$', 'IV.1.9.15.ii')],
 'ega4_iv1_backmatter': [
  (r'$\dim_c(X)$, $\dim(X)$', r'$\operatorname{dimc}(X)$, $\dim(X)$', 'IV1.notation.dimc'),
  ('($E$ $B$-álgebra topológica): \\textbf{0}, 20.7.10.\\par',
   '($E$ $B$-álgebra topológica): \\textbf{0}, 20.7.10,\\par', 'IV1.notation.chiE'),
  (r'$A$-álgebra de Cohen:', r'$\mathbf{A}$-álgebra de Cohen:', 'IV1.terminology.Cohen')]
}
# Raw-string apostrophes above use a backslash solely for Python quoting.
for key in changes:
    changes[key] = [(a.replace("\\'", "'"), b.replace("\\'", "'"), p)
                    for a, b, p in changes[key]]

delta_rows = []
for name in names:
    current = out / f'tree/worktree/es/CURRENT/EGA_IV1_ch4/{name}.tex'
    diplomatic = out / f'tree/worktree/es/DIPLOMATIC/EGA_IV1_ch4/{name}.tex'
    text = current.read_text()
    for before, after, place in changes.get(name, []):
        if text.count(before) != 1:
            raise ValueError(f'{name}: expected one counterpart at {place}, found {text.count(before)}')
        text = text.replace(before, after, 1)
        delta_rows.append([name + '.tex', place, before, after,
                           f'EGA_ES_FINISH_1_FRANCES/fr/diplomatic/{relative_fr.as_posix()}'])
    diplomatic.parent.mkdir(exist_ok=True, parents=True)
    diplomatic.write_text(text)

math_pattern = re.compile(r'(?<!\\)\$(?:\\.|[^$])*?\$|\\\[.*?\\\]', re.S)
def math_spans(text):
    return [re.sub(r'\s+', '', m.group()) for m in math_pattern.finditer(text)]

def prose_words(text):
    text = math_pattern.sub(' ', text)
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    text = re.sub(r'\\(?:label|tag|setmanualcurrentlabel|oldpage)(?:\[[^\n]*?\])?\{[^}]*\}', ' ', text)
    text = re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?', ' ', text)
    text = re.sub(r'\\[A-Za-z]+', ' ', text)
    return len(re.findall(r"[^\W\d_]+(?:['’-][^\W\d_]+)*", text, re.U))

def write_tsv(filename, columns, rows):
    with (rec / filename).open('w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(columns)
        w.writerows(rows)

translation_rows, map_rows, audit_rows, event_rows, glossary_rows = [], [], [], [], []
who = 'GPT-6 Astra; OpenAI; ChatGPT Pro mode; effort not exposed; run translate_iv1_section1'
for edition in ('CURRENT', 'DIPLOMATIC'):
    for name in names:
        path = Path(f'tree/worktree/es/{edition}/EGA_IV1_ch4/{name}.tex')
        es = (out / path).read_text()
        fr, start, end = source_units[edition][name]
        fs, ts = math_spans(fr), math_spans(es)
        checks = {'math_spans': fs == ts}
        for kind, pattern in [
            ('labels', r'\\label\{[^}]*\}'),
            ('page_markers', r'\\oldpage(?:\[[^\n]*?\])?\{[0-9]+\}'),
            ('tags', r'\\tag\{[^}]*\}'),
            ('environments', r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?'),
            ('reader_targets', r'\\EGAReaderTarget\{[^}]*\}\{[^}]*\}')]:
            checks[kind] = re.findall(pattern, fr) == re.findall(pattern, es)
        if not all(checks.values()):
            for line in difflib.unified_diff(fs, ts):
                print(line)
            raise ValueError(f'{path.as_posix()}: {checks}')
        french_path = f'EGA_ES_FINISH_1_FRANCES/fr/{edition.lower()}/{relative_fr.as_posix()}'
        units = re.findall(r'\\begin\{(?:env|definition|proposition|theorem|lemma|corollary|remark|examples)\}\[([^]]+)\]', fr)
        place = f'IV.{units[0]}–IV.{units[-1]}' if units else ('chapter IV front matter' if name.endswith('front') else 'IV1 bibliography and indexes and contents')
        translation_rows.append([path.as_posix(), french_path, f'lines {start}–{end}; {place}', prose_words(es)])
        map_rows.append([french_path, place, edition, path.as_posix(), 'translated; source-fidelity audit passed',
                         f'All {len(fs)} math spans, labels, tags, environments and original page markers match corresponding French layer.'])
        audit_rows.append([edition, path.as_posix(), len(fs), len(ts), len(units), len(re.findall(r'\\oldpage', fr)),
                           prose_words(fr), prose_words(es), 'PASS; exact math modulo whitespace, labels/tags/pages/environments/targets in order'])
        event_rows.append([f'IV1.translation-fidelity.{name}.{edition}', '2026-11-25', who,
                           'computation or formal certificate',
                           f'Textual computation only: {len(fs)} math spans and structural markers match; no mathematical proof certified.'])
        for unit in units:
            statement = 'IV.' + unit
            if statement == 'IV.1.9.10':
                event_rows.append([statement, '2026-11-25', who, 'targeted proof check',
                                   'Counterexample to supplied quantifier x∈X: X=Spec(F₂), E=∅; proposed refined statement IV.1.9.10-refined, x∈E. Source reading preserved; see SOURCE_ISSUES_iv1.md.'])
            else:
                event_rows.append([statement, '2026-11-25', who, 'carried as background without fault found',
                                   f'Translated from {edition.lower()} French; statement/proof carried as background; no proof verification claimed.'])
        for match in re.finditer(r'\bcuerpos?\b', es, re.I):
            line = es[:match.start()].count('\n') + 1
            glossary_rows.append(['corps', match.group(), 'STANDARDS_20261119b.md Spanish block: held; inherited cuerpo retained',
                                  f'{path.as_posix()}:line {line}', 'yes'])

choices = [
 ('générisation', 'generalización', 'worktree/es/CURRENT/EGA_I_ch0/ega0_i_2_1_1_4.tex, 0.2.1.2', 'IV.1.10.1–IV.1.10.4', 'yes'),
 ('rare', 'raro', 'repo/editions/III1_CURRENT/ega0/ega0-9.tex, 0.9.2.3', 'IV.1.8.5', 'yes'),
 ('augmentation', 'aumentación', 'repo/editions/IV1_CURRENT/ega4/ega0-18-es.tex, 0.18.1.4', 'IV.1.4.3.1; IV1 indexes', 'no'),
 ('unibranche', 'unirrama', 'repo/editions/IV1_CURRENT/ega4/ega0-23-es.tex, 0.23.1.7', 'IV1 terminology index', 'no'),
 ('pro-constructible; ind-constructible', 'pro-construible; ind-construible', 'repo/editions/IV3/sections/ega4-9.tex: inherited pro/ind-construibilidad; construible in glossary and III1 §0.9', 'IV.1.9; IV.1.10; IV1 indexes', 'yes'),
 ('de présentation finie', 'de presentación finita', 'GLOSARIO_es_20261119/GLOSSARY_es.tsv, decided row', 'IV.1; chapter front matter; IV1 indexes', 'no'),
 ('lissité', 'suavidad', 'STANDARDS_20261119b.md lisse=suave; corresponding noun by derivation', 'IV1 printed contents 19.4,19.5,21.2,22,22.1', 'yes')
]
glossary_rows += [list(row) for row in choices]

write_tsv('TRADUCCION_iv1_section1.tsv', ['file','french_source','range','words'], translation_rows)
write_tsv('MAPA_iv1_section1.tsv', ['french_file','place','edition','spanish_file','status','evidence'], map_rows)
write_tsv('CAMBIOS_iv1_section1.tsv', ['file','place','before','after','kind','source'], [])
write_tsv('CHECK_EVENTS_iv1_section1.tsv', ['statement_id','date','who','type','outcome'], event_rows)
write_tsv('GLOSARIO_REGISTRO_iv1_section1.tsv', ['french_term','spanish_rendering','witness','places','reversible'], glossary_rows)
write_tsv('IV1_DIPLOMATIC_DIFFERENCES.tsv', ['file','place','current_es','diplomatic_es','source'], delta_rows)
write_tsv('IV1_SOURCE_FIDELITY.tsv', ['edition','file','french_math_spans','spanish_math_spans','numbered_units','page_markers','french_prose_words','spanish_prose_words','status'], audit_rows)
(rec / 'IV1_CH4_INPUT_ORDER.json').write_text(json.dumps(
    {edition: [f'tree/worktree/es/{edition}/EGA_IV1_ch4/{name}.tex' for name in names]
     for edition in ('CURRENT','DIPLOMATIC')}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'units_per_edition': len(names), 'distinct_diplomatic_changes': len(delta_rows),
                  'math_spans_per_edition': sum(r[2] for r in audit_rows if r[0]=='CURRENT'),
                  'translated_prose_words_current': sum(r[7] for r in audit_rows if r[0]=='CURRENT'),
                  'numbered_units': sum(r[4] for r in audit_rows if r[0]=='CURRENT'),
                  'audit': 'PASS'}, ensure_ascii=False))

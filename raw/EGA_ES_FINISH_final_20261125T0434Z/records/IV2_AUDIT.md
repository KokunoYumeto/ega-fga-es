# IV.2: source comparison and assembly

## Delivered text and order

Both editions contain **342 ordered content inputs**. The earlier CURRENT count of 343 included its wrapper, which is not a content input. `IV2_INPUT_ORDER.json` gives the complete sequence for both editions, including the opening, bibliography continuation, notation index, terminology index, and original printed contents. The sequence follows the French source. The 150 absent DIPLOMATIC inputs were assembled from the inherited Spanish current text and reconciled with the printed French; copied Spanish is recorded as assembly, not counted as a new translation.

`MAPA_iv2.tsv` was written before any IV.2 edit and subsequently updated. It now has 1,984 rows: numbered environments, headings, and every input unit in both layers. `IV2_UNIT_AUDIT.tsv` has 684 rows, one for each input in each edition. No missing numbered environment or unmatched source formula remains. Source line ranges in the unit audit identify the first and last matched formulas, not mechanically inferred paragraph boundaries.

## Exhaustive structural comparisons

| Check | CURRENT | DIPLOMATIC |
|---|---:|---:|
| Ordered content inputs | 342 | 342 |
| Numbered environments | 582 | 582 |
| Source mathematical spans | 18,865 | 18,851 |
| Unmatched mathematical spans | 0 | 0 |
| Labels and stable targets, in source order | 740 | 740 |
| Printed-page markers, in source order | 227 | 227 |
| Formula tags, in source order | 119 | 119 |

Mathematical spans retain the literal TeX of the corresponding French layer. Six prose groups inside `text{}` are translated within five formulas per edition; those are the only literal text differences in the formula comparison. Loose comparison keys were used only to locate corresponding formulas. They were not written into the edition and are not mathematical equivalence certificates.

Counts of `emph`, `textup`, and `footnote` agree with French in every numbered segment. Additional formatting in inherited editorial notes is retained. The source's printed errors remain in the diplomatic layer. The current and diplomatic French differ in 142 line-diff blocks; formula differences and 33 language/reference/format patches were reconciled, together with the already-correct printed readings in the inherited diplomatic text.

The comparison found and repaired omitted mathematical mentions in 2.1.2 and 6.14.4, incorrect formula indices or primes, a reversed source/target description in 4.8.4, and an unmarked expansion in 4.6.15. Previously untranslated `et` in the formula at 3.3.3 was translated. The nine entries in `TRADUCCION_iv2.tsv` count only newly rendered fragments (51 lexical words), not entire inherited files.

## Register and terminology

The primary register pass read all source-aligned candidates and corrected **456 prose spans per edition** where French `on` had become Spanish first-person plural. A follow-up corrected 28 mixed clauses, pronouns, or imperative forms per edition, preserving French `nous` and the authors' imperatives. The long source period in proof III of 6.14.1 was restored. Earlier targeted corrections at 7.2.10 and 7.3.16 are separately logged.

All **156** occurrences of `entorno/entornos` were compared with French `voisinage` and changed to `vecindad/vecindades`, with determiner and adjective agreement. Two pre-existing correct occurrences of `vecindad` were retained. All **262** occurrences of `fibra/fibras` denote morphism fibers, formal fibers, or their headings/index entries; none denotes a sheaf stalk. The 420 individual decisions are in `MODEL_TERMS_iv2.tsv`.

The held `corps/champ` decision and the low-confidence `anneau de valuation` decision were not applied. Each existing occurrence of the affected Spanish terms is recorded in `GLOSARIO_REGISTRO_iv2.tsv`. The root task owns the remaining unambiguous whole-corpus terminology script.

## Earlier corrections

`HECHO_REVISADO_iv2.tsv` covers **2,674 HAND entries**: 1,922 CURRENT and 752 DIPLOMATIC. All 80 previously pending diplomatic entries were carried. Earlier admitted dispositions remain distinguished from new work. Twenty-seven older French replacement snippets have evolved in the supplied release; their reasons explicitly identify the latest source as controlling.

The same record covers all **71 IV.2 RESPELL rows** using global JSONL identifiers. Nine rows are carried; eight Spanish punctuation repairs are propagated to both editions. For the other 62 rows, the literal intermediate rollback would restore older notation or punctuation incompatible with the later standard or supplied source. Their required manual source comparison is recorded, and each reason explains why the literal rollback was not reinstated.

## Scope of the checks

The work includes exhaustive unit order, formula, marker, and specified typography comparisons; source-aligned linguistic review; all earlier-row dispositions; and targeted reading where differences required a decision. It does **not** claim an independent re-proof of EGA's statements. `CHECK_EVENTS_iv2.tsv` keeps editorial/source checks distinct from mathematical proof verification. The formula stream tests establish literal source identity, not the truth of the mathematics.

Reader composition, compilation, and PDF inspection belong to the root task. The inherited optional proof title in the continuation of 7.3.16 is retained and requires the reader's proof environment to accept an optional argument.

## Scripts

- `audit_iv2_alignment.py`: source/Spanish formula and unit correspondence.
- `reconcile_iv2.py`: literal formula and structural restoration, with change records.
- `iv2_layer_patches.py`: printed-layer wording and reference variants.
- `iv2_typography_patches.py`: individually reviewed typography and early register corrections.
- `iv2_register_patches.py` and its JSON data: reviewed register edits with revision digests.
- `iv2_register_tail.py`: mixed clauses and remaining pronouns.
- `iv2_respell_prose.py`: Spanish clause punctuation from the earlier respell review.
- `iv2_context_terms.py`: reviewed neighborhood terminology.
- `finish_iv2_records.py`, followed by `update_iv2_term_records.py`: coverage and reconciliation records.

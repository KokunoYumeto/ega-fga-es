# EGA III: source fidelity, translation and editorial records

## Delivered scope

This audit covers III part 1 in CURRENT and DIPLOMATIC, including its continuation of chapter 0, chapter III opening, and sections 1–5. It also covers the supplied CURRENT text of III part 2, sections 6–7 and its back matter. No independent diplomatic III part 2 source was supplied for this scope. The Spanish files remain in their inherited `repo/editions` layout.

The source comparison is exhaustive for ordered mathematical spans, canonical source targets, printed-page markers, formula tags, and numbered environments. The source prose was read where alignment, omissions, register, terminology, or inherited differences required a decision. These are translation and source-fidelity checks. They do not establish the mathematical truth of EGA's statements or independently verify their proofs.

| Source stream | Logical units | Numbered environments | Mathematical spans | Canonical targets | Printed pages | Formula tags |
|---|---:|---:|---:|---:|---:|---:|
| III1 CURRENT | 353 | 379 | 10,335 | 668 | 163 | 227 |
| III1 DIPLOMATIC | 352 | 378 | 10,289 | 667 | 163 | 227 |
| III2 section 6 | 86 | 85 | 2,318 | 78 | 39 | 73 |
| III2 section 7 and back matter | 86 | 92 | 2,893 | 95 | 48 | 69 |
| **Total** | **877** | **934** | **25,835** | **1,508** | **413** | **596** |

There are no unmatched mathematical spans or missing canonical targets in these streams. The complete target, printed-page and formula-tag sequences match the corresponding French edition in order. Every logical unit has the source's environment counters and brace balance. `III_COMPLETE_FIDELITY.tsv` records all 877 logical units and source line ranges; `MAPA_iii.tsv` has 2,445 target, statement and front-matter rows.

The mathematical comparison ultimately uses literal source TeX after explicitly translating words in `text`, `textup`, `mbox` and `hbox`. Loose keys were used to locate corresponding material, never as output notation or as proofs of equivalence. All 68 source text/hbox groups were checked, including nested mathematics; the final literal comparison requires no further edits. The comparison counts include the short inline spans that were initially obscured by a TeX line-break spacing option in the III2 heading.

## Source passages and structure restored

The work restored the chapter 0 convention note explaining references to the earlier chapter 0, the chapter III contents entries for sections 6 and 7, two omitted introductory sentences, the continuation notice and relevant printed blank-page boundaries. III2 again begins with its source chapter III continuation title. Missing canonical labels were added beside inherited Spanish aliases, including the nested labels near III.1.1 and III.7.3.5.

Mathematical and prose restorations include the separate CURRENT paragraph 0.11.4.4; omitted equalities and intermediate mentions in 0.12.3.4 and 0.13.2; source hypotheses and spectral-sequence clauses in 0.11; the generic-point paragraph of III.4.3.10; the exactness conditions in III.7.1.3; and smaller source clauses identified in the translation inventory. The old indirect expansion of III.7.6.11 was brought into the actual reading order. Duplicate material from III.7.9.11 was removed from III.7.9.12. Extra proof or formula-environment wrappers were reconciled with the source rather than used to manufacture additional numbered statements.

CURRENT and DIPLOMATIC were compared separately. Identical French prose intervals can share a translation; differing printed intervals received separate decisions. This preserves, among other differences, the CURRENT epsilon-permutation passage in 0.11.8.1 and the printed variants in III.4.3 and the chapter 0 material. The printed implication direction in III.7.5.6 was restored as supplied. That record is a source-reading decision, not a mathematical endorsement or an unrecorded correction to the source.

`TRADUCCION_iii.tsv` identifies 35 newly supplied fragments, counted as 405 Spanish lexical words. Formulas, repeated inherited prose and rearrangements are excluded from that new-coverage count. The separate `III_TRANSLATION_WORK.tsv` records all 1,110 source bridge and complete-unit translation operations, including revisions of inherited Spanish. Its 38,909 operation words can include passages revisited in later operations and must not be presented as distinct new corpus coverage. The complete before/after history is retained in the change and decision records.

## Register and terms

The initial register pass has 448 decisions, of which 374 changed the Spanish. Follow-ups contain 198 impersonal/imperative and clause decisions, 129 author-voice decisions, and 16 final imperative corrections. French `on` remains impersonal; authorial `nous` and imperatives retain first-person plural. In the final concrete findings, `on notera` and `on observera` became `se observará`, `soient` became `sean`, and `Faisons` became `Hagamos, en efecto`. These counts refer to successive editorial acts; they are not counts of disjoint locations.

The schema pass corrected 120 occurrences in 106 aligned prose intervals, retaining singular/plural and the distinctions `schéma/préschéma` and `sous-schéma/sous-préschéma`. Different-cardinality intervals were read and repaired in their full source context. The final source-term stream has no residual mismatch at scope release. Other full-unit retranslations also restore the source terms but are not added to the 120 occurrence count.

All 57 final `fibra/fibras` candidates refer to morphism, geometric, or formal fibers and were retained. All 60 final `filtrado/filtrados` candidates refer to objects endowed with filtrations and were retained. None of these 117 candidates requires `tallo` or `filtrante`. Their individual source-context verdicts are in `FINAL_STANDARD_MODEL_III.tsv`.

The remaining 34 instances of `cubrimiento/cubrimientos` in III2 were compared with aligned French `recouvrement/recouvrements` and changed to the settled term `recubrimiento/recubrimientos`. Fifty-two expanded instances of source `resp.` were restored to the abbreviation; source `respectivement` remains `respectivamente`. Four missing `cf.` occurrences were restored. Six uses of `íntegramente cerrado` were corrected to `integralmente cerrado`, keeping `intégralement clos` distinct from `intègre`, rendered `íntegro`.

The held `corps/champ` and low-confidence `anneau de valuation` decisions were not applied. The glossary register identifies all 91 source `corps` occurrences and 14 source occurrences of `anneau de valuation`; there are no source `champ` occurrences in these prose streams. The inherited terms remain, including noun phrases placed before their formulas in Spanish. The root task owns the final whole-corpus `construible` and other global standard passes.

## Notes and provenance

Source author notes were retained. `Sans doute` in the chapter III opening note is rendered `probablemente`. The inherited CURRENT translator aside, `\emph{[Trad.] Estos cuatro últimos capítulos nunca se publicaron.}`, was restored exactly. It was absent from the inherited DIPLOMATIC opening and was not newly added there.

`CAMBIOS_iii.tsv` consolidates 5,210 local changes. The root's earlier generic III notation restoration is recorded separately and is not duplicated in that count. The two local intermediate logs are named `III_CHANGES_math_aligned.tsv` and `III_CHANGES_manual.tsv`, avoiding a second inclusion by the global `CAMBIOS_*.tsv` merger. The historical mathematical-log description was broadened to source/translation/notation comparison because that helper was also used for prose edits.

`CHECK_EVENTS_iii.tsv` has 1,064 events. Inherited numbered statements are carried as background after editorial comparison. String-equality certificates are explicitly about TeX streams, and terminology/register events are explicitly editorial. No event claims an independent proof check. `GLOSARIO_REGISTRO_iii.tsv` has 1,479 reversible decisions and witnesses; `ESTANDAR_APLICADO_iii.tsv` separates the standard counts and their limitations.

Raw French context diagnostics are excluded from the deliverable tree. Source coordinates and hashes remain in the records, with the Spanish before/after changes. No raw French source files are repackaged here.

## Scripts and remaining ownership

`audit_iii_alignment.py`, `iii_restore_local_math.py`, `iii_final_math.py`, `iii_final_markers.py` and `finish_iii_records.py` provide the source comparison and record generation. The bridge, register, schema, segment, abbreviation and final-term scripts record the editorial decisions. Historical Spanish translation templates are retained under `scripts/iii_replay` as audit material; they are state-dependent editing steps and must not be blindly rerun on the completed text.

The source files were released to the root task after the final concrete corrections. Reader composition, cross-volume reference resolution, compilation, PDF inspection and global packaging remain with the root task. This report gives source-fidelity results and does not substitute for that build or visual QA.

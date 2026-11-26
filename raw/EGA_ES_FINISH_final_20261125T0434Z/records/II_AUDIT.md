# EGA II: source-fidelity and register audit

Both native Spanish editions were compared against the corresponding supplied
French layer, including front matter, main chapter, bibliography, indexes and
contents, and the complete errata/addenda list.

The final audit compares every formula literally after translating only the
text arguments in the French formula itself. It does not transplant inherited
Spanish text arguments. This stronger test covers 31,392 math spans and all
50 text/hbox/mbox-type arguments; it found and corrected 26 formulas containing
duplicated embedded mathematical conditions, untranslated English words, or a
French connective. Labels and page/tag sequences agree with the French.

The 1,106 original unmatched alignment records have individual resolved
dispositions in `II_UNMATCHED_REVIEW.tsv`. The main body has no unmatched
source-reference keys. Twenty front/errata audit rows retain inherited Spanish
hyperlinks around references printed without hyperlinks in the French; their
displayed reference numbers follow the source and this tree convention is
documented in `II_REFERENCE_FINAL_REVIEW.tsv`.

Source-bounded register comparison restored impersonal constructions for
French “on” and first-person authorial constructions for “nous” and actual
French imperatives. Mixed clauses were reviewed separately. Thirty-one
punctuation candidates were read in context; their stops follow Spanish
complements or closing emphasis and were not missing. Forty-four units with
French current/diplomatic prose differences were reviewed. Source mathematical,
reference, hypothesis and emphasis distinctions were retained; French-only
grammar or capitalization differences do not require an artificial Spanish
mistranslation.

Missing short prose was restored, including the chapter heading, the declaration
of the endomorphism in 6.4.8, finite-type qualifications in 1.4.5 and across page
71, and the universal element qualification in errata 1.8.1. Existing passages
were also retranslated where source comparison required it, notably the current
readings of 5.6.3, 7.1.4, and the local-finiteness quantifiers in 8.3.9. These are
source translations, including any mathematical difficulty in the supplied
reading, not mathematical emendations.

Quoted correction phrases in the errata are Spanish. Bibliographic publication
titles retain their publication language. Existing edition notes, bibliography
additions and credits remain. Held or low-confidence terminology was retained
and its 356 French occurrences were logged.

Merge only the consolidated `MAPA_ii.tsv`, `CAMBIOS_ii.tsv`,
`TRADUCCION_ii.tsv`, `GLOSARIO_REGISTRO_ii.tsv`, and `CHECK_EVENTS_ii.tsv` into
the root tables. Component `II_CHANGES_*.tsv` files are historical stages and
must not be counted again. Earlier root notation change files remain intact.

Run `python scripts/finalize_ii_records.py` from the delivered result tree with
the original supplied archive extracted in the sibling `source/` directory.
This script writes the final counts and asserts the source unit, formula,
label, and page/tag comparisons. No event in this audit is a proof verification.

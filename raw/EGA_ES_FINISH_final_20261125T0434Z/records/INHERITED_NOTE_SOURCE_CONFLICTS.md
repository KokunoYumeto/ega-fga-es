# Conflicto de una nota editorial heredada con sus testigos

## Resultado y disposición

En IV1 CURRENT, 0.23.2.8(ii), se conserva **literalmente** la siguiente nota editorial del español suministrado:

> Lectura diplomática: la fuente remite a la inexistente 23.2.7; el resultado utilizado es la Proposición 23.2.7.

La nota ya figuraba así tanto en `worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-23-es.tex` como en `repo/editions/IV1_CURRENT/ega4/ega0-23-es.tex` del ZIP español original. No es una modificación introducida por esta ejecución. No se ha cambiado la nota ni ninguna de las fuentes como resultado de este hallazgo.

## Testigos y conflicto

| Testigo | Referencia en 0.23.2.8(ii) |
|---|---|
| Francés CURRENT suministrado | (23.2.7) |
| Francés DIPLOMATIC suministrado | (23.1.13) |
| Nota editorial española heredada | Afirma que la referencia diplomática es la inexistente 23.2.7 y que el resultado utilizado es la Proposición 23.2.7. |

La nota presenta una contradicción interna entre «inexistente 23.2.7» y «Proposición 23.2.7», y su descripción de la lectura diplomática no corresponde al testigo francés diplomático suministrado, que dice (23.1.13). Se registra esta discordancia textual sin evaluar qué resultado demuestra la afirmación matemática.

Se mantiene la nota editorial íntegra por la instrucción de preservación de las notas heredadas. El riesgo es que su afirmación histórica sobre la referencia diplomática induzca a error. El registro deja explícito su origen y las dos lecturas francesas, y distingue este conflicto heredado de cualquier cambio de la ejecución actual.

`INHERITED_NOTE_SOURCE_CONFLICTS.tsv` conserva la nota antes/después y los dos pasajes franceses exactos con su ubicación. Este caso está entre las 244 notas conservadas salvo espacios, no entre los 20 avisos de diferencias cerrados en `INHERITED_NOTE_FINAL_REVIEW.tsv`. No se afirma comprobación de ninguna demostración.

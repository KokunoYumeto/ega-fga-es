# Las correcciones del EGA francés en la edición española (5–9 de noviembre de 2026): registros

Del 1 al 5 de noviembre de 2026 la transcripción francesa de EGA ([ega-fr](https://github.com/KokunoYumeto/ega-fr))
se comprobó página por página con los escaneos de Numdam de los volúmenes impresos; sus registros están en ega-fr,
`raw/scan_check_20261101/`. Esta carpeta contiene los registros del traslado de esas correcciones a las dos ediciones
españolas de este repositorio (la diplomática y la corregida). El método completo está en `METHODOLOGY.md` (§ 4).

## Cómo

- **5 de noviembre, por script** (`port_fixes_to_lang.py`; registros `PORT_ES_CURRENT_LOG.jsonl`,
  `PORT_ES_DIPLOMATIC_LOG.jsonl`): la edición española conserva los marcadores de página impresa y las macros del
  francés, de modo que cada corrección se localiza en la misma página. Ediciones corregidas: 3.528 aplicadas y 2.105 ya
  correctas; ediciones diplomáticas: 1.229 aplicadas y 792 ya correctas. Las correcciones de erratas del impreso
  decididas después (`apply_recheck_es.py`) y la compilación de cada edición (`compile_es.py`,
  `rebuild_es_readers.py`) completan el paso. Los elementos que el script no pudo situar quedaron en
  `PORT_ES_*_HAND.json`.
- **9 de noviembre, por modelo** (`sol_port_es_20261109/`): GPT-6.1 Sol (OpenAI, API, esfuerzo máximo, nivel flex)
  decidió esos elementos por lotes (`batches_*`, `prompt*`, respuestas `answer_*.md`, decisiones `decisions_*.json`);
  cada respuesta se auditó por script (`AUDIT_*.md`) antes de aplicarse (`apply.py`). Los elementos que quedaron:
  `PORT_ES_*_SOL_LEFT.json` y una segunda ronda (`decisions_second_*.json`).

## Dónde están las correcciones

Commits 5971923, d82cf84 y ec9dd92 (5 de noviembre), d570398 y 92d1cb1 (9 de noviembre).

## Pendiente

En la segunda ronda quedaron 106 elementos sin decidir ("unclear": 73 de la edición corregida y 33 de la
diplomática). El paquete autónomo `editions/IV3_reproducible` se había separado de `editions/IV3` antes del 5 de
noviembre y no recibió las correcciones de ese día; el 9 de noviembre recibió cambios en cinco archivos.

No se incluyen imágenes ni PDF. Las rutas locales están reescritas (`user`).

## Derechos

Los derechos sobre la obra original pertenecen a su autor o a sus representantes o herederos. En la medida en que
tengamos derechos sobre la traducción, las correcciones, los registros y la composición producidos por IA, quedan
dedicados al dominio público bajo [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.es). Esta edición
se publica con fines educativos y sin ánimo de lucro, y no reclamamos derechos que no tengamos. Si usted tiene
derechos sobre esta obra y se opone a su publicación aquí, abra una incidencia en GitHub y la retiraremos.

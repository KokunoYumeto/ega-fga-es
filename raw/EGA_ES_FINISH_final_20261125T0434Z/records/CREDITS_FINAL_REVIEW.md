# Revisión final de créditos y derechos de los lectores

## Resultado

Los **14 lectores ensamblados** conservan los créditos exigidos en sus frentes: **767 comprobaciones conformes, cero pendientes**. Se compararon los archivos TeX con los registros originales suministrados, independientemente del texto del ensamblador. No se modificó ningún archivo del corpus ni del ensamblador durante esta auditoría.

La declaración de derechos pedida por el usuario está presente **literalmente** en los 14 frentes. Los créditos identifican la traducción como «AI-translated» y las correcciones como «AI-produced corrections». No aparece «AI-assisted» en esos frentes. Se conservan tanto los créditos humanos heredados como los de los modelos anteriores y de esta ejecución.

## Qué se cotejó

Se conservaron las secciones «Cómo se hizo» y «Fuentes y créditos» del README original, y el ATTRIBUTION original completo. El cotejo de párrafos ignora el marcado Markdown/TeX, los espacios y la puntuación de formato; las identidades de versiones, los SHA-256 de módulos y los destinos de enlace se verifican literalmente, deshaciendo únicamente el escape TeX de caracteres. Los créditos se cotejaron con los originales, no con una copia modificada del árbol de salida.

Los ocho nombres humanos conservados son Mateo Carmona, Tim Holzschuh, Tim Hosgood, Ryan Keleti, Thiago Solovera & Nery, Wayne Yang, Steve Hnizdur y Jon Sterling. También permanecen la autoría de Grothendieck y la colaboración de Dieudonné. Las atribuciones delimitan el trabajo inglés heredado: III-1, capítulo 0 §§8–10 y parte de §11, y capítulo III §§1 y 3; IV-1, capítulo 0 §14; IV-4, §16 y los comienzos de §§17 y 20. La declaración específica de EGA II sobre su referencia inglesa se conserva en sus dos lectores y en el acumulativo. No se atribuye a los colaboradores humanos la traducción española de IA ni se presenta la atribución como permiso o aval.

Se mantienen las versiones inglesas `3d7afe28c99d1887ccdb85acf2ca1afd93fb1971` de ryankeleti/ega y `9976dd5f8e2ddcb388f0a07f3aa334f120d1019f` de la traducción FGA de Tim Hosgood, sus enlaces y las cautelas originales sobre la identificación de la versión FGA. El texto conserva los créditos anteriores de OpenAI Codex, GPT-5.6 Sol y GPT-6.1 Sol, esfuerzo Ultra; GPT-6 Astra, esfuerzo Ultra; y el crédito de composición de EGA I por Claude Opus 5.5, esfuerzo high. Este último se distingue del cotejo francés por Claude Opus 5.5, esfuerzo max, noviembre de 2026. La ejecución actual se atribuye a GPT-6 Astra, OpenAI, ChatGPT Pro mode.

Además, se incorporan y cotejan los FUENTES específicos de II, III-1, III-2, IV-1, IV-3 e IV-4 en sus lectores correspondientes y, conjuntamente, en el lector acumulativo. Los FUENTES originales CURRENT y DIPLOMATIC de II, III-1 e IV-1 son idénticos entre sí. Se comprobaron 93 apariciones de identidades SHA-256 de módulos. Los registros de notas matemáticas separadas y la copia IV3_reproducible no definen lectores adicionales de esta entrega; se consultaron para delimitar el alcance de los créditos, sin atribuirles contenido que no se ensambla en estos lectores.

Se verificaron 188 apariciones de enlaces externos, correspondientes a 10 URL originales distintas, por identidad con las fuentes. No se comprobó su disponibilidad en Internet. Los 70 enlaces relativos del paquete resuelven a archivos entregados. El control de privacidad no detectó correos electrónicos ni rutas locales absolutas en los frentes.

## Hallazgos resueltos durante la revisión

Se comunicaron dos clases de hallazgo al agente que mantiene el ensamblador. Primero, faltaban las dos entradas bibliográficas originales EGA/FGA del README y sus enlaces NUMDAM; el nuevo ensamblaje conserva toda la sección «Fuentes y créditos». Segundo, los cuatro enlaces heredados `editions/.../FUENTES.md` no resolvían desde las carpetas de los lectores. Los nuevos destinos `../../tree/repo/editions/.../FUENTES.md` conservan el texto de enlace y llegan a los registros incluidos. El enlace a ATTRIBUTION añadido con la sección restaurada también resuelve dentro del paquete.

Las cinco filas de `CREDITS_FINDINGS_RESOLVED.tsv` documentan la omisión de la sección y los cuatro destinos corregidos. La revisión final se hizo después de esos cambios: no quedan hallazgos abiertos.

## Lectores revisados

| Lector | Comprobaciones | Pendientes |
|---|---:|---:|
| EGA_COMPLETA_CURRENT | 111 | 0 |
| EGA_III1_CURRENT | 60 | 0 |
| EGA_III1_DIPLOMATIC | 60 | 0 |
| EGA_III2 | 44 | 0 |
| EGA_II_CURRENT | 57 | 0 |
| EGA_II_DIPLOMATIC | 57 | 0 |
| EGA_IV1_CURRENT | 59 | 0 |
| EGA_IV1_DIPLOMATIC | 59 | 0 |
| EGA_IV2_CURRENT | 41 | 0 |
| EGA_IV2_DIPLOMATIC | 41 | 0 |
| EGA_IV3 | 44 | 0 |
| EGA_IV4 | 52 | 0 |
| EGA_I_CURRENT | 41 | 0 |
| EGA_I_DIPLOMATIC | 41 | 0 |

## Evidencia y límites

`CREDITS_FINAL_REVIEW.tsv` registra los 14 lectores, el hash del frente revisado y su resultado. `CREDITS_FINAL_CHECKS.tsv` conserva las 767 comprobaciones con la fuente y el texto o identificador exigido. `CREDITS_FINAL_FINDINGS.tsv` contiene solo su cabecera porque no quedan pendientes. `CREDITS_FINAL_EVIDENCE.json` conserva los frentes exactos revisados; `CREDITS_FINAL_COUNTS.json` contiene los recuentos.

Esta revisión verifica crédito, procedencia y declaración de derechos frente a las instrucciones y los documentos suministrados. No determina la situación jurídica de las obras ni afirma comprobación matemática. La compilación y la inspección visual de los PDF pertenecen al registro de construcción separado.

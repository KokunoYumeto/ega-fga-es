# Recuento final del estándar español

ESTANDAR_APLICADO_final.tsv es el único resumen que se incorpora a ESTANDAR_APLICADO.tsv. Cada fila corresponde a una regla del plan español o a una regla ampliada o conservada por la revisión b, las decisiones de duda y el registro terminológico suministrado. La dirección vieja vecindad → entorno queda sustituida por entorno → vecindad. Las decisiones held y de baja confianza mantienen los términos heredados.

Las cifras proceden de pasadas efectivamente aplicadas o de revisiones de contexto concluidas. No se suman ESTANDAR_DRY_RUN*, las tablas preapply, las propuestas ni ESTANDAR_APLICADO_model.tsv, que conserva el estado histórico anterior a la aplicación. El fichero STANDARD_MODEL_APPLIED_IDS y los dos registros BINDINGS demuestran que se aplicaron los 2.330 parches atómicos correspondientes a 948 sustituciones de término; los otros parches ajustan determinantes y concordancia. No se cuentan estos ajustes como términos adicionales.

«found» no significa siempre lugares únicos: las filas de tallo y filtrante incluyen la revisión contextual inicial y la revisión final real, con algunos lugares leídos de nuevo. Las reglas de registro cuentan actos documentados de revisión o edición de cláusulas; sus parches tienen distinta longitud. No se inventan recuentos de reemplazos a partir de traducciones nuevas o retraducciones completas. ESTANDAR_RULE_EVIDENCE.tsv explica la unidad y el registro de cada sumando. Las capas CURRENT y DIPLOMATIC tienen sus propias ocurrencias y se cuentan por separado.

La revisión final de los términos dependientes del contexto contiene 736 decisiones: 167 ROOT, 350 OTHER, 102 IV3 y 117 III. De ellas se sustituyeron dos entornos por vecindades; otras dos apariciones de fibra desaparecieron al restituir cláusulas de III, sin sustitución por tallo. Quedan 664 usos legítimos de fibra y 68 de filtrado, y ningún entorno. Esto da 732 candidatos léxicos finales conservados, no 732 incumplimientos.

Las decisiones held se cuentan a partir de un único inventario final del corpus canónico, no sumando las listas históricas de glosario. La consolidación del glosario toma GLOSARIO_REGISTRO_held_final_verify.tsv como inventario final por lugar. Los registros anteriores permanecen como evidencia histórica.

El script consolidate_standard_summary.py solo lee el corpus y escribe los registros de resumen; no cambia ninguna traducción ni verifica demostraciones matemáticas.

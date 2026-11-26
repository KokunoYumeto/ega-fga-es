# Revisión visual final: EGA I, II e IV-1

## Resultado

Se inspeccionaron explícitamente con `view_image` las seis hojas `qa/final/*_1.png` correspondientes a I, II e IV-1, en sus capas CURRENT y DIPLOMATIC, después del aviso de finalización de los PDF. También se inspeccionaron cuatro ampliaciones: los títulos de Krull y Artin–Rees en cada capa de I, y la fórmula 20.3.7.1 en cada capa de IV-1. **No se observaron recortes, solapamientos ni otros defectos de composición en las muestras revisadas.**

El registro contiene 42 filas: 36 páginas de muestras distribuidas y seis comprobaciones de detalle en cuatro páginas adicionales. Son 40 páginas físicas y diez imágenes finales revisadas. Cada fila identifica la página física, la imagen inspeccionada, el SHA-256 de esa imagen y el SHA-256 del PDF final.

## Páginas y detalles

| Lector | Páginas físicas de la hoja | Detalles ampliados |
|---|---|---|
| EGA_II_CURRENT | 1, 5, 32, 79, 126, 158 | — |
| EGA_II_DIPLOMATIC | 1, 5, 32, 79, 126, 158 | — |
| EGA_IV1_CURRENT | 1, 5, 38, 94, 150, 188 | p. 89: ecuación 20.3.7.1 |
| EGA_IV1_DIPLOMATIC | 1, 5, 38, 94, 150, 188 | p. 89: ecuación 20.3.7.1 |
| EGA_I_CURRENT | 1, 5, 34, 84, 135, 169 | p. 50: Teorema de Krull 7.3.2 y Lema de Artin-Rees 7.3.2.1 |
| EGA_I_DIPLOMATIC | 1, 5, 34, 84, 134, 168 | p. 50: Teorema de Krull 7.3.2 y Lema de Artin-Rees 7.3.2.1 |

Los títulos de Krull y Artin–Rees están completos, con numeración legible y separación adecuada del enunciado. La fórmula 20.3.7.1 se ve entera en sus dos líneas; las flechas, los índices y la etiqueta tienen espacio suficiente y no invaden el margen.

La hoja de II DIPLOMATIC se volvió a renderizar e inspeccionar tras la recompilación que conserva los números de las citas bibliográficas heredadas de I. Su hash anterior no se usa en el registro final. Los otros cinco PDF permanecen vinculados a los hashes inspeccionados anteriormente; se comprobó que ninguno había cambiado.

## Compilación y alcance de la conclusión

Los seis informes `BUILD_final_*.json` correspondientes indican código de salida cero y ninguna caja overfull. Sus avisos se conservan en los registros de construcción: la ausencia de errores de compilación no se presenta como ausencia de cualquier aviso. El resumen de esa evidencia está en `PDF_VISUAL_I_II_IV1_BUILDS.json`.

Esta revisión es visual y por muestras; no implica lectura visual de todas las páginas ni comprobación de demostraciones. La revisión de las páginas con desbordamientos iniciales superiores a 10 pt se documenta por separado por el responsable de construcción. No se editaron fuentes durante esta revisión. Los frentes de los 14 lectores conservan los hashes de la auditoría de créditos, incluso después de la última recompilación de II DIPLOMATIC.

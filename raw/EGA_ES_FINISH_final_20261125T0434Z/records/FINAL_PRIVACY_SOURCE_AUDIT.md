# Auditoría final de privacidad y alcance de fuentes

**Resultado: PASS.** La selección efectiva de `package_result.wanted` se revisó después del saneamiento de los registros históricos y de los 14 logs de compilación. No quedan hallazgos de correos, rutas personales o rutas absolutas en los textos de entrega examinados. Esta revisión es documental y técnica; no verifica demostraciones matemáticas.

## Alcance y resultados

| Control | Resultado |
|---|---:|
| Archivos seleccionados antes de añadir estos dos informes | 2,276 |
| Archivos de texto examinados, incluidos scripts | 2,233 |
| PDF finales examinados | 14 |
| Páginas PDF con texto extraíble examinado | 3,373 |
| Correos encontrados en texto y metadatos | 0 |
| Hallazgos finales de rutas personales o absolutas | 0 |
| Archivos incrustados en los PDF | 0 |
| ZIP, 7z, RAR, gzip o tar seleccionados por nombre o firma | 0 |
| Directorios de adjuntos originales o de libros franceses seleccionados | 0 |
| Enlaces simbólicos seleccionados | 0 |

La selección se tomó directamente de `scripts/package_result.py:wanted`, con las mismas exclusiones que el empaquetador. El manifiesto de salida se genera después y estos dos informes se excluyen de su propia lista de hashes para evitar autorreferencia. El JSON adjunto conserva el inventario auditado con rutas relativas, tamaños y SHA256, el hash de la política de selección y los hashes finales de PDF y logs.

## Privacidad

Se buscaron correos y rutas Unix, de Windows y de archivos locales en TeX, tablas, registros JSON y JSONL, Markdown, CFF, bibliografía, logs, textos y scripts. Las coincidencias amplias de la forma de una unidad de Windows correspondían a variables seguidas de comandos TeX o a fragmentos truncados de dichos comandos. Los 12 descriptores tipográficos de TeX hallados en los logs tampoco son rutas de archivo.

Las 42 referencias de sistema que permanecen en scripts Python son intérpretes o un recurso tipográfico de la instalación, sin componentes personales. Corresponden a la excepción autorizada para rutas de ejecución en código. No se reproducen sus valores en este informe.

Los 14 PDF fueron examinados mediante extracción de texto de todas sus páginas, metadatos ordinarios y XML, y consulta de archivos incrustados. Sus hashes seguían coincidiendo al cierre. No se realizó OCR de las muestras PNG; estas son imágenes de control de los lectores y se incluyeron en el inventario.

## Alcance de las fuentes francesas y los adjuntos

El cotejo SHA256 contra 128 archivos suministrados del árbol francés encontró únicamente dos coincidencias: los preámbulos de macros necesarios para compilar los espejos IV1 CURRENT y DIPLOMATIC, situados bajo `support`. No se hallaron libros franceses completos seleccionados, directorios de adjuntos originales ni archivos comprimidos anidados. Todos los PDF seleccionados son lectores finales bajo `readers`.

Se conservan la documentación de créditos heredada y testimonios acotados de cotejo. El mayor campo explícito de contexto francés en JSON o JSONL tiene 1,960 caracteres; no hay ninguno superior a 5.000. Los 24 registros históricos restaurados se incluyeron después de su saneamiento, sin archivos pendientes de revisión.

## Observación resuelta en los logs

La primera revisión ampliada detectó 71 continuaciones de rutas de instalación tipográfica en los 14 logs, algunas partidas por saltos de línea. No contenían datos personales. Se comunicó el hallazgo antes de cualquier modificación. La coordinación principal saneó los logs y documentó la conservación de páginas, avisos y cajas desbordadas en `records/FINAL_LOG_SANITIZATION.tsv`. Esta auditoría volvió a comprobar las rutas y los hashes: quedan 0 residuos detectados por ese control.

## Límites y trazabilidad

El resultado se refiere al contenido seleccionado y a los patrones y comparaciones descritos; no es una garantía semántica frente a cualquier codificación imaginable. La auditoría no alteró fuentes canónicas, lectores, PDF, README ni código de unión de registros. Solo creó los presentes informes. Los archivos de diagnóstico intermedios permanecen fuera del árbol empaquetado.

Fecha de cierre: 2026-11-25T04:33:45+00:00.

Huella del inventario auditado: `bfc6bf65bf768a18b8fe60a9c24a9071418d4affe90c0d2779413d23275fb76a`.

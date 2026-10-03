# VERUM — Documentación en español argentino

**Idioma:** español de Argentina (`es-AR`). **Revisión de traducciones:** 3 de octubre de 2026.

Este índice reúne la documentación del proyecto para leer y trabajar en español argentino. Se usa voseo natural y vocabulario local —remera, buzo, calce, talles— sin agregar jerga artificial. Las claves técnicas, rutas, comandos y nombres propios se conservan. Las traducciones están junto a sus originales con el sufijo `.es-AR.md`.

## Por dónde empezar

1. Para entender la marca: [universo y dirección creativa](../CREATIVE-DIRECTION.es-AR.md).
2. Para aportar información: [consignas P00–P08](../PLACEHOLDERS.md). Podés dictar «P01: …» o «P03 Registro: …» sin copiar la ficha.
3. Para cargarla: [campos y relaciones](../CONTENT.md), [guía editorial](CONTENT-GUIDE.es-AR.md) y [consignas de arquetipos](ARCHETYPES.es-AR.md).
4. Para trabajar en el sitio: [README](../README.md), [arquitectura](ARCHITECTURE.es-AR.md) y [verificación](VERIFICATION.es-AR.md).

## Inventario completo

| Documento | Español argentino | Inglés o fuente operativa | Estado |
| --- | --- | --- | --- |
| Introducción y trabajo local | [README](../README.md) | — | Ya estaba en español; no se duplica. |
| Campos y carga de contenido | [CONTENT](../CONTENT.md) | — | Ya estaba en español; no se duplica. |
| Consignas de reemplazo | [PLACEHOLDERS](../PLACEHOLDERS.md) | — | Ya estaba en español; no se duplica. |
| Universo y dirección creativa | [Versión argentina](../CREATIVE-DIRECTION.es-AR.md) | [English](../CREATIVE-DIRECTION.md) | Dirección vigente, con registros históricos fechados. |
| Hoja de ruta | [Versión argentina](../ROADMAP.es-AR.md) | [English](../ROADMAP.md) | Implementación y posibles próximos pasos. |
| Arquitectura | [Versión argentina](ARCHITECTURE.es-AR.md) | [English](ARCHITECTURE.md) | Descripción contrastada con las fuentes locales. |
| Guía editorial | [Versión argentina](CONTENT-GUIDE.es-AR.md) | [English](CONTENT-GUIDE.md) | Ejemplos con campos actuales; ficción identificada. |
| Verificación | [Versión argentina](VERIFICATION.es-AR.md) | [English](VERIFICATION.md) | Alcance real de controles y revisión visual. |
| Procedencia y prompts de imágenes | [Traducción de consulta](../assets/images/collaborations/PROMPTS.es-AR.md) | [Prompts originales](../assets/images/collaborations/PROMPTS.md) | El original conserva los textos usados para generar las imágenes. |
| Brief inicial del sitio | [Traducción histórica](../project-description.es-AR.md) | [English](../project-description.md) | Antecedente: no usar como esquema actual ni evidencia de pruebas. |
| Instrucciones GitNexus de agentes | [Traducción de consulta](AGENT-INSTRUCTIONS.es-AR.md) | [AGENTS.md](../AGENTS.md), [CLAUDE.md](../CLAUDE.md) | No reemplaza los archivos operativos generados ni las instrucciones de Ryan. |
| Comentarios e instrucciones de arquetipos | [Guía argentina](ARCHETYPES.es-AR.md) | [Colección](../archetypes/drops.md), [prenda](../archetypes/lookbook.md), [entrevista](../archetypes/veritas.md), [genérico](../archetypes/default.md) | Se conservan expresiones de Hugo y valores técnicos. |

Las páginas del sitio ya tienen sus versiones en `content/es/` y `content/en/`, con interfaz en `i18n/es.toml` e `i18n/en.toml`. Estos documentos de trabajo quedan fuera de `content/`: no crean páginas públicas nuevas. Las guías de herramientas de terceros instaladas en `.claude/skills/` no forman parte de la documentación de autoría del proyecto.

## Mantener las versiones alineadas

- Editá el par de idioma en la misma entrega cuando cambien reglas, hechos, campos o procedimientos. Si falta una traducción, marcala como pendiente; no la presentes como sincronizada.
- Conservá números, unidades, fechas, slugs, `translationKey`, `artist_id`, rutas y nombres de campos. Traducí explicaciones, no interfaces de programación.
- Mantené la diferencia entre propuesta, dato recibido y dato aprobado, y entre un control disponible y una ejecución registrada.
- No traduzcas un prompt de procedencia como si fuera el texto exacto que generó la imagen. Identificá la traducción como copia de consulta.
- No conviertas una afirmación histórica en una promesa actual. El brief original conserva su propio alcance, incluidas decisiones reemplazadas más adelante.
- Revisá enlaces locales y coherencia de ejemplos al terminar. Una traducción de documentación no requiere ejecutar toda la batería de pruebas del sitio.

## Ajustes de precisión de esta edición

Al preparar las traducciones se corrigieron en ambos idiomas las referencias a componentes y SCSS retirados, los ejemplos de campos que no coincidían con los bundles, el mapa P00–P08, la ubicación de `editorial_name` y el alcance de los verificadores. También se conservó el directorio temporal hasta la revisión visual y se aclaró que el workflow actual no ejecuta automáticamente esos verificadores. No se cambió el comportamiento de la aplicación ni se verificaron cuentas o servicios externos.

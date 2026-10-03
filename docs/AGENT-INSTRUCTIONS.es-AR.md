# VERUM — Instrucciones para agentes, versión de consulta

**Español (Argentina)** · [AGENTS.md](../AGENTS.md) · [CLAUDE.md](../CLAUDE.md) · [Índice](README.es-AR.md)

Traducción de consulta de los bloques GitNexus presentes en ambos archivos el 3 de octubre de 2026. Los archivos operativos generados conservan sus nombres y contenido; esta copia no los reemplaza ni cambia las instrucciones de Ryan. Los valores del índice son una instantánea, no evidencia de su estado futuro.

## GitNexus — Inteligencia de código

El bloque de origen registra el proyecto como **verumcom**, con 255 símbolos, 259 relaciones y 0 flujos de ejecución.

Si el índice está desactualizado, el bloque indica ejecutar desde la raíz:

```sh
node .gitnexus/run.cjs analyze --index-only
```

El lanzador elige una instalación disponible. Si todavía no existe `.gitnexus/run.cjs`, el bloque propone inicializar con `npx`, `bunx` o `pnpm dlx`, por ejemplo `bunx gitnexus@latest analyze`, y menciona el problema de `npx` con npm 11, incidencia #1939. Esto traduce el mecanismo; no autoriza a ejecutar un análisis largo sin respetar las instrucciones vigentes de Ryan.

## Hacé siempre

- **Analizá el impacto antes de editar.** Usá `impact({target: "symbolName", direction: "upstream"})` o `node .gitnexus/run.cjs impact "symbolName" --direction upstream --repo .`. Informá llamadores, procesos y riesgo. No reemplaces el análisis del grafo por una búsqueda de texto.
- **Analizá los cambios del grafo antes de un commit.** Usá `detect_changes({scope: "all"})` o `node .gitnexus/run.cjs detect-changes --scope all --repo .`. Un resultado con `partial: true` o `truncated: true` no es un control limpio: un cero puede significar que no se vio el impacto. Volvé a ejecutar el control. Para revisar regresiones, usá `detect_changes({scope: "compare", base_ref: "main"})` o `node .gitnexus/run.cjs detect-changes --scope compare --base-ref "main" --repo .`.
- **Advertí antes de editar si `risk` es HIGH o CRITICAL.** No uses `riskSharedAxes` para desestimar esa advertencia. Compará archivo y símbolo: los nodos File de MCP omiten ejes; Graph-RAG expande File.
- **Tratá `risk: UNKNOWN` como una pregunta sin resolver.** No equivale a riesgo bajo. La ausencia de llamadores puede deberse a referencias que el índice no resuelve, como propiedades de objetos, despacho dinámico o llamadas entre lenguajes. Leé `riskNote` y confirmá mediante búsqueda de texto antes de considerar seguro cambiar o eliminar el símbolo. No avances basándote solamente en un cero.
- **Consultá primero el grafo para dependencias y flujos.** Para conceptos, `query({search_query: "concept"})`; para un símbolo, `context({name: "symbolName"})`; para alcance, `impact`. Usá texto después de una respuesta vacía/UNKNOWN o para literales.
- **En una revisión de seguridad**, `explain({target: "fileOrSymbol"})` enumera hallazgos de flujo desde origen hacia destino sensible; necesita el análisis `--pdg`.

## No hagas

- No edites una función, clase o método antes del análisis de impacto por MCP o CLI.
- No ignores HIGH/CRITICAL ni interpretes UNKNOWN como autorización sin reservas. UNKNOWN exige contrastar por otros medios.
- No renombres símbolos con búsqueda y reemplazo. Usá `rename`, que conoce el grafo de llamadas.
- No hagas commits antes del análisis de cambios del grafo. La autorización para hacer un commit sigue siendo una decisión aparte.

## Recursos

| Recurso | Uso |
| --- | --- |
| `gitnexus://repo/verumcom/context` | Panorama y vigencia del índice. |
| `gitnexus://repo/verumcom/clusters` | Áreas funcionales. |
| `gitnexus://repo/verumcom/processes` | Flujos de ejecución. |
| `gitnexus://repo/verumcom/process/{name}` | Recorrido de un flujo, paso a paso. |

## Guías de CLI

Las rutas siguientes se interpretan desde la raíz del proyecto. Las guías de herramientas conservan su idioma de origen; este documento traduce el bloque de instrucciones del proyecto.

| Tarea | Archivo de la guía |
| --- | --- |
| Entender arquitectura o funcionamiento | `.claude/skills/gitnexus-exploring/SKILL.md` |
| Analizar qué se ve afectado | `.claude/skills/gitnexus-impact-analysis/SKILL.md` |
| Rastrear errores | `.claude/skills/gitnexus-debugging/SKILL.md` |
| Renombrar, extraer, dividir o refactorizar | `.claude/skills/gitnexus-refactoring/SKILL.md` |
| Herramientas, recursos y esquema | `.claude/skills/gitnexus-guide/SKILL.md` |
| Índice, estado, limpieza o wiki | `.claude/skills/gitnexus-cli/SKILL.md` |

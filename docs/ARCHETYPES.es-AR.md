# VERUM — Consignas de los arquetipos en español argentino

**Español (Argentina)** · [Índice](README.es-AR.md)

Versión de consulta de las instrucciones de los arquetipos. Las claves de Hugo, slugs, identificadores y expresiones de plantilla conservan su idioma técnico. Los comentarios originales en inglés permanecen en los archivos. Para decidir qué escribir, usá las fichas completas de [PLACEHOLDERS.md](../PLACEHOLDERS.md).

## Colección — P02

Fuente: [archetypes/drops.md](../archetypes/drops.md).

- Mantené el borrador hasta completar ambos idiomas. Describí la observación de partida, la decisión de diseño y su consecuencia en las tres prendas.
- Una persona real necesita un conjunto nuevo de biografía, entrevista e imágenes aprobado; no cambies solo el nombre de la ficción.
- `artist_id`: identificador estable compartido con las tres prendas y la entrevista en ambos idiomas.
- `neighborhood`: vínculo real y permitido, o encuadre ficticio explícito.
- `tone`: familias visuales existentes `print`, para planos de color, y `metal`, para líneas de construcción.
- `theme`: una frase creativa breve, sin afirmar disponibilidad ni calidad comprobada.
- `description`: 25–40 palabras que conecten observación, transformación y consecuencia visible.
- `bio`: 60–90 palabras de identidad/contexto aprobados, o una voz explícitamente ficticia.
- `hero`: ruta bajo `assets/`; `hero_alt`: descripción localizada de lo visible. Consultá P05 para imágenes y créditos.
- `story_ref`: referencia de la entrevista. El nombre técnico de sección sigue siendo `veritas` aunque haya cambiado el rótulo público.
- Conservá `draft: true`, `concept: true` y `status: "concept"` mientras sea una propuesta.

## Prenda — P03

Fuente: [archetypes/lookbook.md](../archetypes/lookbook.md).

- Distinguí datos propuestos de mediciones.
- `description`: 25–45 palabras sobre qué hace la gráfica, dónde va y qué espacio deja.
- `drop_ref`: `drops/{colección}`. `story_ref`: `veritas/{persona}`. Las referencias deben corresponder al mismo artista en español e inglés.
- `kind`: valores existentes `tee`, `hoodie` o `cap`; equivalen a remera, buzo con capucha y gorra.
- `fabric`: identificá como objetivo la composición y el gramaje sin probar. No los deduzcas de una imagen.
- `fit`: describí el corte propuesto, sin inventar talles ni calce universal.
- `technique`: proceso y ubicación propuestos; resultados de muestra por separado.
- `art` y `art_back`: rutas frontal y posterior bajo `assets/`. Las ilustraciones conservan su aclaración.
- `social_image`: opcional, recurso aprobado bajo `assets/`; si se omite, prepará la tarjeta de la prenda que espera la plantilla.
- Cuerpo: 80–140 palabras en el idioma de la página. Empezá por la decisión visible, explicá su ubicación o escala sobre el cuerpo, vinculala con la colección y cerrá con una pregunta pendiente de muestra: `[gesto] → [ubicación] → [motivo] → [prueba pendiente]`.
- No inventes cuidados, stock, precios, lanzamientos ni resultados de uso. Reemplazá el comentario de autor, no lo publiques como texto. Mantené `draft: true` hasta revisarlo y `concept: true` mientras corresponda.

## Entrevista — P04

Fuente: [archetypes/veritas.md](../archetypes/veritas.md).

- La sección visible se llama En proceso / In process; la carpeta técnica sigue siendo `veritas`.
- Conservá borrador y encuadre conceptual. Las citas reales requieren procedencia y aprobación.
- `description`: 25–40 palabras con la decisión explorada, quién habla y la aclaración de ficción cuando corresponda.
- `hero` y `hero_alt`: recurso bajo `assets/`, descripción visible localizada, estado y crédito aprobado según P05.
- `intro`: 60–90 palabras de contexto y pregunta; no inventes una visita, clima ni historia personal.
- `closing`: 30–60 palabras sobre una decisión pendiente o próximo paso, sin fabricar un respaldo a la marca.
- Tres capítulos, dos pares de pregunta/respuesta por capítulo. `piece` lleva el slug real de la prenda.
- **Mirar, remera:** observación de origen y algo que se dejó afuera.
- **Decidir, buzo:** qué cambió sobre tela y qué se descartó, con el motivo.
- **Reducir, gorra:** qué sobrevive a menor escala y qué sigue sin resolverse.
- Traducí las preguntas al idioma de la página. Obtené las respuestas; no completes información inventada como si fuera un hecho.

## Arquetipo genérico

Fuente: [archetypes/default.md](../archetypes/default.md).

Genera `title` y `translationKey` a partir del nombre del archivo e incorpora `date`. Su valor actual es **`draft: false`**, a diferencia de los tres arquetipos guiados. Revisá ese campo antes de crear contenido provisional con el arquetipo genérico. Esta guía documenta el comportamiento existente; no lo modifica.

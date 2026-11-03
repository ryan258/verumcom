# VERUM — Contenido provisional y reemplazos

**Español (Argentina)** · [Índice de documentación](docs/README.es-AR.md)

Inventario y briefs vigentes al 3 de octubre de 2026. Reemplaza la lista antigua de doce prendas y cuatro crónicas. No reutilizar las rutas retiradas del brief inicial.

| Elemento | Fuente actual | Reemplazo pendiente |
| --- | --- | --- |
| Nombre editorial | En proceso / In process; rutas técnicas `veritas` | P00: lectura local y decisión de los propietarios; VERUM se conserva |
| Prendas | `assets/images/collaborations/{registro,persistencia,testigo,cota,trazo,escuadra}.svg` y variantes `-back.svg` | Muestras aprobadas y fotografías frontal, posterior, puesta y detalle |
| Talleres | `sobreimpreso-studio.png`, `en-obra-studio.png` en la misma carpeta | Fotos autorizadas del colaborador y proceso reales |
| Tarjetas sociales | `assets/images/social/{slug}.png` | Regenerar al cambiar el diseño, o usar `social_image` en la ficha con una foto aprobada |
| Artistas/entrevistas | Bundles de `drops` y `veritas` en ambos idiomas | Identidades, biografías, permisos y entrevistas aprobadas; reemplazar conjuntamente |
| Fundadores | Campos opcionales de los manifiestos: `founder_story`, `founders` | Nombres públicos, roles, historia breve y aprobación del texto |
| Contacto | `hugo.toml`: `primary_contact`, `contact_verified`, destinos | Confirmar titularidad del canal seleccionado antes de activarlo |
| Dominio | `baseURL` en `hugo.toml` | Confirmar dominio de publicación y actualizarlo antes del build final |
| Puntos de venta | `data/stockists.yaml`, vacío | Solo locales confirmados; no publicar direcciones de muestra |
| Newsletter/formulario | Endpoints desactivados/provisionales en `hugo.toml` | Cuenta confirmada, privacidad actualizada y prueba real de entrega |

La portada usa las ilustraciones de la serie actual. `assets/images/hero-bg.jpg` y `hero-model.png` se conservan como activos antiguos, pero ya no se muestran en la portada ni se usan como fallback social. Las ilustraciones son SVG; no sustituyen evidencia del calce, textura o confección.

## Cómo usar estos placeholders

Cada placeholder tiene una tarea concreta, una extensión y una condición de reemplazo. Los ejemplos entre corchetes son instrucciones de edición, no texto final. Se pueden completar por dictado: **«P01: …»**, **«P03 Registro: …»**. Una respuesta breve alcanza para empezar; no hace falta volver a copiar la ficha. Quien edite transforma esa entrada en ambos idiomas y marca lo que siga sin conocerse.

**Tres estados editoriales:** `propuesta` (inventado o previsto, identificado como tal), `dato recibido` (aún sin aprobación para publicar), `aprobado` (texto y uso acordados). Estos estados son una convención de trabajo, no campos nuevos de Hugo ni una autorización automática. Una aprobación de texto no demuestra producción, permisos de todas las imágenes ni disponibilidad. Registrar fuente, responsable y fecha en la entrega; guardar conversaciones privadas y documentos personales fuera del repositorio público.

El sitio actual sigue mostrando los conceptos completos. Las instrucciones viven acá y en comentarios de las fuentes/arquetipos; no se insertan como preguntas para visitantes. Los campos públicos vacíos no se rellenan con un nombre, una dirección, una cifra o una cita inventados. No retirar el aviso de ficción por completar un único campo.

### P00 — Nombre editorial

**Destino:** `i18n/{es,en}.toml`, clave `editorial_name`; títulos/descripciones de `content/{es,en}/veritas/_index.md`. **Estado actual:** En proceso / In process es el título de trabajo. VERUM no cambia. Las URLs y claves `veritas` se conservan.

**Consigna:** «Escuchá “En proceso” en una conversación sobre ropa. ¿Qué esperarías encontrar? ¿Te recuerda a algo local que convenga conocer?» Registrar la expresión exacta, quién aporta la lectura (con permiso) y el contexto. Una asociación personal es una señal para discutir, no una definición universal del habla porteña.

**Entrega mínima:** `[título elegido] + [lectura local] + [decisión de los propietarios y fecha]`. No hay que contratar ni activar nada. Sin una decisión final, conservar el título como propuesta de trabajo. La asociación de Veritas con una línea de fragancias está documentada en [CREATIVE-DIRECTION.es-AR.md](CREATIVE-DIRECTION.es-AR.md); el significado callejero mencionado sigue sin verificarse.

**Lecturas a contrastar:** hipótesis de una revisión externa del 3 de noviembre de 2026, sin lectura local que las confirme. Sumar estas preguntas a la consigna y registrar qué confirma, corrige o descarta cada persona.

- **Memoria y verdad.** VERUM («verdad») junto a «La memoria deja capas» y «Lo que queda debajo» puede evocar *Memoria, Verdad y Justicia*, consigna de los organismos de derechos humanos. Preguntar: «¿Esto se lee como una búsqueda propia o como uso de esa consigna?». Hasta tener respuesta, evitar el 24 de marzo como fecha de lanzamiento y cualquier imagen de pañuelos o de la Plaza de Mayo.
- **Barrios con lectura propia.** La Paternal se asocia con Argentinos Juniors y los comienzos de Maradona; Chacarita, con su cementerio y la tumba de Gardel. Un tema sobre lo que queda, situado en Chacarita, puede leerse a través del cementerio. Preguntar: «¿Qué te viene a la cabeza con cada barrio?». Usar la respuesta para decidir si conviene mantener, explicar o reemplazar la referencia al barrio.

### P01 — Equipo e historia fundadora

**Destino:** `founder_story` y `founders` en ambos manifiestos. **Extensión:** 70–110 palabras para la historia; 35–50 por persona.

**Consigna:** «¿Quiénes están haciendo esto, qué los reunió y qué decisión concreta tomaron juntos? Cerrá con lo que están haciendo ahora, sin adelantar resultados.» Un detalle confirmado sirve más que una historia heroica.

**Molde de edición:** `[Nombres públicos] empezamos a trabajar juntos a partir de [hecho real]. [Decisión concreta] nos llevó a explorar [dirección]. Hoy estamos [actividad verificable]; todavía falta [paso pendiente].`

**Perfil:** `[nombre público] / [rol real] / [aporte específico] / [relación con el proyecto que esa persona aprueba]`. No adjudicar a los fundadores las biografías de Lucía o Tomás, formación, barrio, diagnóstico, oficio, año de inicio ni experiencia que no hayan contado y aprobado.

**Sin datos:** omitir los campos; el sitio conserva la introducción general al proyecto. No cargar el molde con corchetes ni perfiles vacíos. Completar ambos idiomas juntos, conservando hechos y grado de certeza.

### P02 — Colección y colaboración

**Destino:** bundles `drops`; guía de campos en `CONTENT.md`. **Extensión:** `description` 25–40 palabras; `bio` 60–90; `theme` una frase breve.

**Consigna:** «Nombrá una observación de partida, una decisión de diseño y algo que se decidió dejar afuera. Explicá qué cambia entre la remera, el buzo y la gorra.»

**Molde:** `[observación o fuente] → [gesto transformado] → [ubicación en cada pieza] → [límite o pregunta pendiente]`. En Sobreimpreso, la capa cambia de escala; en En Obra, el ángulo se reduce. Esos son ejemplos conceptuales, no declaraciones de un colaborador real.

**Para reemplazar:** identidad y presentación aprobadas; fuente del motivo y permiso de uso si corresponde; crédito exacto; texto en ES/EN. El barrio se incluye por su relación real con el trabajo y con acuerdo del colaborador, nunca para sumar credibilidad prestada. Si el nombre cambia, actualizar `artist_id`, `artist_name`, prendas y entrevista en conjunto. No reutilizar el diálogo ficticio como si lo hubiera dicho la persona nueva.

**Sin datos:** conservar la colaboración ficticia completa y su aviso. No mezclar una identidad real con un testimonio inventado.

### P03 — Prenda y muestra

**Destino:** bundles `lookbook`. **Extensión:** `description` 25–45 palabras; cuerpo 80–140; un dato claro por campo técnico.

**Consigna:** «¿Cuál es el gesto de esta pieza, dónde está y qué deja libre? ¿Qué necesita comprobarse al pasar del dibujo a la tela?» Escribir primero la decisión visible; después, el objetivo técnico.

**Ficha de muestra para completar fuera del copy:** `[pieza y versión] / [fecha y responsable] / [tejido y fuente] / [gramaje: objetivo o medido + método] / [medidas y forma de medir] / [posición de la gráfica] / [prueba de movimiento y comodidad] / [lavado realizado y resultado] / [cambio siguiente]`. Si no hubo prueba, escribir «no probado»; no deducir el resultado de un SVG o de una foto.

**Ejemplo de tono para un objetivo:** «Frente crudo, tres planos desplazados. Objetivo: jersey de algodón de 240 g/m²; falta evaluar caída y estampa en muestra.» **Molde para una observación real:** «En la muestra [versión], [observación comprobada]. Se propone [ajuste].»

**Sin datos:** conservar «objetivo» y la nota de muestreo. No publicar talles, composición exacta, origen de fabricación, durabilidad, cuidados ni stock por inferencia. Las cotas decorativas de En Obra no son medidas. Una muestra no equivale a una serie terminada.

### P04 — En proceso: conversación

**Destino:** `content/{es,en}/veritas/{persona}/index.md`, front matter TOML. **Forma:** tres capítulos, dos preguntas por capítulo; respuestas orientativas de 60–100 palabras, sin rellenar una respuesta corta con ficción.

**Guion de entrevista real:**

1. **Mirar:** «¿Qué observación puso esto en marcha?» / «¿Qué parte de esa fuente elegiste dejar afuera?» Vincular con la remera.
2. **Decidir:** «¿Qué cambió al pasar a una prenda?» / «¿Qué probaste o descartaste, y por qué?» Vincular con el buzo.
3. **Reducir:** «¿Qué queda cuando el gesto se hace más chico?» / «¿Qué sigue sin resolverse?» Vincular con la gorra.

**Respuesta pendiente:** `[relato de la persona, tomado de conversación o texto autorizado; incluir un objeto, una elección y su consecuencia]`. Esa instrucción no se publica como una cita. No convertir una respuesta dictada en un manifiesto de marca ni quitar dudas para hacerla sonar más contundente.

**Para reemplazar:** registro de origen, permiso de atribución, revisión de las citas, créditos y traducción que conserve las reservas del hablante. Una paráfrasis se identifica como tal. Reemplazar también introducción, cierre, retrato/escena y las referencias desde colección/prendas. **Sin entrevista:** mantener «conversación imaginada»; nunca cambiar solo `concept`.

### P05 — Imágenes y escenas

**Destino:** recursos compartidos y `hero_alt`; la prenda permite `social_image`. **Entrega por prenda:** frontal, posterior, detalle relevante y vista de uso. Usar 4:5 como guía para fotos de prenda; prever 16:9 para taller y 1200 × 630 para compartir, manteniendo el sujeto fuera de bordes de recorte.

**Brief:** `[qué decisión debe verse] / [qué objeto y estado se fotografían] / [encuadre] / [crédito y permiso] / [texto alternativo factual]`. Pedir manos/proceso solo cuando aporten información; no simular un taller real con utilería sin explicarlo. Si una imagen es generada, mantener ese estado visible en el texto que la acompaña.

**Alt de ejemplo conceptual:** «Ilustración frontal de una remera cruda con tres planos desplazados en rojo, cobalto y amarillo.» Describir lo visible; no inferir tacto, calidad, identidad de una persona o ubicación. **Sin imagen real:** conservar SVG/escena generada y su rótulo, sin llamarlos fotos de producción.

### P06 — Pieza editorial breve o publicación

**Destino:** material de trabajo, no una publicación programada. **Forma:** una imagen o detalle, 40–70 palabras y un enlace existente.

**Molde ES:** `[observación concreta]. Por eso [decisión visible en la pieza]. [Estado: concepto o muestra real identificada]. [Invitación: mirar el diseño o leer la conversación]. [Crédito].`

**Ejemplo conceptual:** «Tres planos, un pequeño desfase. Registro deja el fondo crudo visible entre las tintas. Es una ilustración de diseño: la caída de la tela y el resultado de la estampa todavía necesitan una muestra. Mirá el frente y la espalda en el lookbook.»

**English treatment:** «Three planes, a small offset. Registro leaves the ecru ground visible between the inks. This is a design illustration; the fabric's drape and print still need sampling. See the front and back in the lookbook.»

No agregar precio, contador, «últimas unidades», testimonio, fecha ni reserva. **Sin novedad:** no inventar un avance para llenar un calendario. Adaptar imagen y texto juntos; la aclaración debe viajar con la pieza si sale del sitio.

### P07 — Tarjeta, etiqueta o inserto de estudio

**Destino:** futuro estudio gráfico, aún no implementado en el sitio. **Forma:** una cara expresiva y una cara informativa.

**Molde:** `VERUM / [colección] / [pieza] / [crédito aprobado] / [versión documentada]`. En un estudio: «Concepto visual. Material y terminaciones pendientes de muestra.» En una muestra real: identificar esa muestra sin afirmar disponibilidad.

Una barra de registro o un ángulo puede acompañar la composición; no imitar sellos de certificación. Composición, cuidados y origen requieren datos reales antes de diseñar una etiqueta destinada a una prenda. **Sin datos:** el estudio queda interno y esos campos vacíos; no inventar símbolos de lavado ni numeraciones que sugieran una edición limitada.

### P08 — Encuentro o visita

**Destino:** futuro texto de invitación, no una promesa actual. **Consigna:** «¿Para qué se reúne la gente, qué está confirmado y qué necesita saber alguien para decidir si puede ir?»

**Molde:** `[actividad concreta] / [día, hora y zona horaria] / [lugar con permiso para publicarlo] / [cómo llegar e ingresar] / [asientos, escalones y demás datos de acceso conocidos] / [costo si lo hay] / [canal confirmado]`. No llamar accesible a un espacio sin explicar las condiciones conocidas. Se puede responder una duda sin obligar a compartir información médica.

**Sin confirmación:** no publicar la invitación, no inventar una dirección y no activar reservas. El título «En proceso» no implica un taller abierto al público.

## Sustitución completa de un concepto

Reemplazar persona, relato, imágenes y datos relacionados en ambos idiomas como una misma entrega. Conservar identificadores y enlaces cuando sigan representando el mismo contenido; si cambian, revisar todas las referencias antes de publicar. El campo `concept` no es un interruptor de verdad: las plantillas actuales conservan deliberadamente el aviso de ficción. El paso a una colaboración real exige una revisión específica de contenido y presentación, no eliminar avisos globales que siguen siendo necesarios en otras piezas.

Antes de dar por completo un reemplazo, revisar solo la unidad editada: fuente y permiso, grado de certeza, campos vinculados ES/EN, rótulo de imagen y vista renderizada. Ningún dato ausente se transforma en hecho por haber pasado un verificador.

## Próxima entrega de los propietarios

1. Elegir y confirmar un canal de contacto; no hace falta configurar tres.
2. Aprobar una historia breve de los fundadores: quiénes son, por qué VERUM, qué aporta cada uno y qué están haciendo ahora. No atribuirles los talleres ni las biografías ficticias.
3. Elegir una prenda para la primera muestra. Registrar tela, gramaje medido, medidas, colocación de la estampa, resultado de calce y cambios necesarios. Los valores actuales son objetivos de diseño.
4. Incorporar fotos de la muestra real y la aprobación del colaborador antes de presentar la pieza como producida.

## Regenerar tarjetas sociales

Los seis PNG se incluyen en el proyecto; un build normal de Hugo no necesita ImageMagick. Al editar los SVG, regenerarlos con:

```sh
python3 scripts/render_social_cards.py
```

Requiere ImageMagick (`magick`). En macOS usa Menlo; en otro sistema, indicar una fuente monoespaciada instalada:

```sh
VERUM_SHARE_FONT=/ruta/a/fuente.ttf python3 scripts/render_social_cards.py
```

Cada tarjeta reúne frente y espalda sin recortar la prenda. Verificar visualmente las tarjetas regeneradas antes de publicarlas. Las páginas de prenda incorporan `og:image`, texto alternativo y metadata de Twitter.

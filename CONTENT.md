# Contenido de VERUM

La serie actual contiene dos colaboraciones ficticias, seis prendas conceptuales y dos entrevistas imaginadas, en español e inglés. La dirección creativa y las decisiones acordadas están en [CREATIVE-DIRECTION.md](CREATIVE-DIRECTION.md).

## Fuentes

| Contenido | Español | Inglés |
| --- | --- | --- |
| Sobreimpreso | `content/es/drops/sobreimpreso/index.md` | `content/en/drops/sobreimpreso/index.md` |
| En Obra | `content/es/drops/en-obra/index.md` | `content/en/drops/en-obra/index.md` |
| Prendas | `content/es/lookbook/{registro,persistencia,testigo,cota,trazo,escuadra}/index.md` | Mismos nombres bajo `content/en/lookbook/` |
| Entrevistas | `content/es/veritas/{lucia-ferreyra,tomas-varela}/index.md` | Mismos nombres bajo `content/en/veritas/` |
| Imágenes compartidas | `assets/images/collaborations/` | La misma fuente, sin duplicación por idioma |
| Interfaz | `i18n/es.toml` | `i18n/en.toml` |

## Campos y relaciones

Las colecciones usan `artist_id`, `artist_name`, `neighborhood`, `craft`, `theme`, `bio`, `palette`, `hero`, `hero_alt`, `story_ref` y `weight`. `description` es la frase de presentación: se muestra en la portada de la colección y como meta descripción. El estado es `concept`, sin fecha de lanzamiento.

Las prendas usan `artist_id`, `drop_ref`, `story_ref`, `kind`, `fabric`, `color`, `fit`, `technique`, `art`, `art_back` y `weight`. `description` es la nota de diseño: aparece en la entrevista y como meta descripción. Los objetivos de gramaje no son especificaciones verificadas. No agregar talles o disponibilidad sin evidencia.

Las entrevistas usan `description` (resumen), `intro`, `chapters` y `closing`, y llevan front matter en TOML (`+++`) porque los capítulos están anidados: cada `[[chapters]]` tiene `title`, `piece` (slug de la prenda) y `questions` (pares pregunta/respuesta). Las notas de diseño y los enlaces se obtienen de la prenda, evitando versiones duplicadas. El tiempo de lectura se calcula solo, a 180 palabras por minuto.

Los pares de idioma comparten `translationKey`. Modificar ambos idiomas al cambiar una relación o una propuesta de producto. Las traducciones conservan los nombres propios de las colecciones y prendas.

## Imágenes

`hero` apunta a un recurso global procesado por Hugo en WebP con tamaños responsivos. `art` y `art_back` apuntan a SVG editables. Los textos alternativos de las escenas están en cada idioma; los rótulos frontal/posterior se traducen por i18n. Las ilustraciones no son fotos de productos fabricados.

## Verificación enfocada

Después de editar, construir en un destino limpio y ejecutar `python3 scripts/verify_concepts.py /ruta/al/destino`. El chequeo valida cantidades, relaciones, traducciones, capítulos, imágenes, enlaces locales y ausencia de rutas retiradas en ese destino. Revisar en navegador los cambios visuales. Las páginas conceptuales muestran siempre su naturaleza ficticia; el paso a colaboradores reales requiere revisión explícita de contenido y plantillas.

## Puntos de venta y newsletter

`data/stockists.yaml` está vacío a propósito: sin puntos de venta confirmados, la página los explica y el enlace "Dónde encontrarnos" del encabezado no aparece. Agregá entradas reales con la forma que documenta el propio archivo. La sección de newsletter de la portada solo aparece si `newsletter_endpoint` (en `hugo.toml`) tiene un valor.

## Inicio, Lookbook y equipo — revisión del 2 de octubre

El inicio y Lookbook muestran las seis prendas desde los bundles; Drops mantiene el acceso por colección. Las dos ilustraciones principales del inicio apuntan a Registro y Cota. Cambiar esas referencias en `layouts/index.html` si cambia la selección editorial.

Los manifiestos aceptan estos campos opcionales en su front matter YAML; completarlos en ambos idiomas solo con texto aprobado:

```yaml
founder_story: "Historia real aprobada del equipo."
founders:
  - name: "Nombre público aprobado"
    role: "Rol real"
    bio: "Biografía breve aprobada."
```

El ejemplo no está cargado en las páginas. Sin esos campos, `#equipo` presenta únicamente el proyecto en Buenos Aires y su siguiente paso de muestra. El enlace “Detrás de VERUM” de la portada llega a esa sección.

Las tarjetas de prendas admiten `social_image` para reemplazar la tarjeta de diseño con una imagen aprobada en `assets/`. Si se omite, se usa `images/social/{slug}.png`. Regenerar esos PNG al modificar los SVG, según `PLACEHOLDERS.md`.

El canal principal requiere `primary_contact` y `contact_verified` en `hugo.toml`. El componente compartido publica únicamente ese destino. No quedan horarios de taller ni enlaces públicos a cuentas sin confirmar. Para verificar la revisión, seguir el comando de `README.md`; no usar resultados históricos como evidencia de esta versión.

## Universo y placeholders instructivos — 3 de octubre

La dirección de voz, temas y aplicaciones está en CREATIVE-DIRECTION.md. Las fichas P00–P08 de PLACEHOLDERS.md dan consignas y ejemplos para reemplazar el contenido; no son texto listo para visitantes. Los arquetipos ahora explican qué completar en cada campo y mantienen `draft: true` / `concept: true`. La ficha de muestra se registra por separado del copy público; un gramaje objetivo no se convierte en medición al completar la ficha.

El nombre editorial visible es **En proceso / In process**, de trabajo. Cambiarlo en la clave `editorial_name` de ambos archivos i18n y en el `title`/`description` de ambos índices `veritas/_index.md`. Las invitaciones compartidas dicen «leer las conversaciones» sin duplicar el nombre. Conservar `translationKey`, `artist_id`, `story_ref`, nombres de carpetas y anclas si solo cambia el rótulo.

Los manifiestos incluyen comentarios con la consigna P01. Omitir los campos de fundadores hasta contar con una historia real aprobada; los comentarios no se convierten en texto público. Los ejemplos entre corchetes de PLACEHOLDERS.md nunca se cargan como un nombre o una cita. No guardar evidencia privada ni datos personales en comentarios de archivos destinados a un repositorio público.

Para revisar una carga: comprobar las dos versiones de idioma, las relaciones prenda → colección → conversación, el estado de imagen y la vista renderizada de esa unidad. La sección técnica `veritas` sigue siendo necesaria para las plantillas y los verificadores. El verificador actual está acotado a dos colecciones, seis prendas y dos entrevistas; agregar otra unidad requiere ampliar ese contrato deliberadamente.

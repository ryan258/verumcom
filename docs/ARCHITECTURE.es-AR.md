# VERUM — Arquitectura y especificaciones técnicas

**Español (Argentina)** · [English](ARCHITECTURE.md) · [Índice](README.es-AR.md)

Arquitectura del sitio estático y criterios técnicos. Las descripciones se contrastaron con las fuentes locales el 3 de octubre de 2026; no demuestran el estado de un despliegue público.

## 1. Vista general

VERUM genera un sitio estático, sin seguimiento del lado del cliente, fuentes web externas en tiempo de ejecución ni frameworks de interfaz.

- **Generador:** Hugo Extended `>= 0.163.0`; versión de referencia y CI: `0.166.0`.
- **Plantillas:** Go HTML en `layouts/`.
- **Estilos:** SCSS modular compilado con Hugo Pipes y LibSass desde `assets/scss/main.scss`.
- **Tipografía:** Anton alojada en `static/fonts/anton-latin.woff2`, Space Mono y sans de sistema.
- **JavaScript:** código nativo mínimo en `assets/js/main.js` para mejorar progresivamente el menú. El contenido y la navegación principal se mantienen sin JavaScript; eso no certifica accesibilidad completa.
- **Alojamiento:** un servidor estático, por ejemplo GitHub Pages, Cloudflare Pages o Netlify. El workflow existente es `.github/workflows/gh-pages.yml`.

## 2. Idiomas y rutas

Dos árboles de contenido:

- **Español, principal:** `/`, `/lookbook/`, `/drops/`, `/manifiesto/`, `/contacto/`, `/veritas/`.
- **Inglés, secundario:** `/en/`, `/en/lookbook/`, `/en/drops/`, `/en/manifesto/`, `/en/contact/`, `/en/veritas/`.

### Correspondencia

Hugo vincula las páginas mediante `translationKey` en el front matter:

- Inicio: `content/es/_index.md` ↔ `content/en/_index.md`.
- Prendas: `content/es/lookbook/{slug}/index.md` ↔ su equivalente en `content/en/`.
- Colecciones: `content/es/drops/{slug}/index.md` ↔ su equivalente en `content/en/`.
- Editorial: `content/es/veritas/{slug}/index.md` ↔ su equivalente en `content/en/`.
- Páginas individuales: `manifiesto` ↔ `manifesto`, `contacto` ↔ `contact`, `puntos-de-venta` ↔ `stockists`.
- Legales: `legal/privacidad` ↔ `legal/privacy`; `legal/terminos` ↔ `legal/terms`.

### Nombre editorial y estabilidad

**En proceso / In process** es el nombre de trabajo. Las rutas `/veritas/` y `/en/veritas/` se conservan para no romper enlaces ni anclas. Los rótulos compartidos usan `editorial_name` en los archivos i18n. Los títulos y las descripciones están en ambos `veritas/_index.md`; no hay una clave `editorial_name` en `hugo.toml`.

## 3. Plantillas y componentes parciales

```text
layouts/
├── _default/
│   ├── baseof.html          # Documento, metadatos, navegación y pie
│   ├── contact.html         # Contacto con canal confirmado o estado pendiente
│   ├── manifesto.html       # Manifiesto y equipo
│   ├── single.html          # Página genérica
│   └── stockists.html       # Puntos de venta y estado vacío
├── drops/
│   ├── list.html            # Índice de colecciones
│   └── single.html          # Colección con prendas relacionadas
├── lookbook/
│   ├── list.html            # Seis prendas: dos remeras, dos buzos, dos gorras
│   └── single.html          # Frente, espalda, datos propuestos y entrevista
├── partials/
│   ├── brand-story.html     # Historia del equipo y perfiles
│   ├── contact-channel.html # Resolución del canal principal
│   ├── follow-project.html  # Acción para seguir el proyecto
│   ├── concept-note.html    # Aclaración de ficción
│   ├── concept-piece-card.html # Tarjeta de prenda
│   ├── artist-cards.html    # Tarjetas de colección/artista
│   ├── collaboration-image.html # Imágenes SVG y rasterizadas
│   └── reading-minutes.html # Tiempo estimado de lectura
├── veritas/
│   ├── list.html            # Índice de entrevistas
│   └── single.html          # Tres capítulos con prendas vinculadas
├── index.html               # Portada centrada en prendas
└── robots.txt               # Directivas de rastreo
```

La navegación, el pie y los metadatos están en `baseof.html`; no existen componentes separados `site-nav.html`, `site-footer.html` o `meta-tags.html`.

## 4. Procesamiento de recursos

Hugo Pipes procesa CSS, JavaScript e imágenes. CSS y JavaScript reciben una huella de contenido; los archivos estáticos se copian por separado.

### SCSS

Fragmento actual de compilación:

```go
{{ $sassOpts := dict "targetPath" "css/style.css" "outputStyle" "compressed" }}
{{ $style := resources.Get "scss/main.scss" | toCSS $sassOpts | minify | fingerprint }}
```

### Imágenes

- Láminas de prendas y escenas en `assets/images/`.
- Escenas rasterizadas: variantes WebP de 640 y 1280 px. Las láminas SVG se sirven directamente.
- Metadatos sociales: JPEG de 1200 × 630. Calidad configurada de WebP/JPEG: `85`. El componente de imágenes de colaboración no incluye una alternativa JPEG separada.
- El componente emite `alt`, `width` y `height`, usa `loading="lazy"` por defecto y admite `loading="eager"`. No emite `fetchpriority`. Las dimensiones ayudan a reservar espacio; no prueban ausencia de saltos de diseño.

### Tarjetas para compartir

Las seis tarjetas de 1200 × 630 están en `assets/images/social/`, se generan con `scripts/render_social_cards.py` y se referencian en metadatos Open Graph y Twitter.

## 5. Organización de SCSS

| Módulo | Responsabilidad |
| --- | --- |
| `_tokens.scss` | Colores, superficies semánticas, familias tipográficas, tamaños de contenedor/encabezado y reinicio base. |
| `_typography.scss` | Títulos Anton, lectura sans, metadatos Space Mono, interlínea y espaciado. |
| `_nav.scss` | Encabezado, menú móvil, idiomas y enlaces de escritorio. |
| `_editorial.scss` | Superficies editoriales, controles compartidos, adaptación, lectura del manifiesto y colores forzados. |
| `_collaborations.scss` | Grillas, colecciones, prendas, entrevistas, portada y presentación de equipo/contacto. |
| `_components.scss` | Botones, tarjetas y estilos base del manifiesto. |
| `_forms.scss` | Presentación de formularios, campos, foco y estados. |
| `_glitch.scss` | Acentos de glitch e interacciones visuales. |

`_lookbook.scss`, `_drops.scss` y `_veritas.scss` ya no forman parte de los estilos actuales.

## 6. Mejora progresiva, accesibilidad e integridad

1. **Base sin JavaScript:** contenido y navegación deben seguir usándose si falla el script. El menú móvil conserva una lista dentro del flujo del documento. Esto no equivale a conformidad completa.
2. **Teclado y foco:** enlace inicial para saltar a `#main-content`, indicadores `:focus-visible` y cierre con Escape que devuelve el foco al botón del menú.
3. **Movimiento y contraste:** reglas para `prefers-reduced-motion: reduce` y `forced-colors: active`. La presencia de CSS no reemplaza las pruebas de uso.
4. **Seguridad y contacto:** los encabezados del servidor y CSP requieren inspección de la respuesta publicada; una compilación local no establece una CSP activa. Los enlaces de puntos de venta que abren otra pestaña usan `rel="noopener noreferrer"`. Contacto prioriza el canal principal confirmado, luego un endpoint configurado sin `placeholder`, y en su ausencia muestra un estado pendiente. El endpoint del formulario es independiente de `contact_verified` y requiere confirmación propia.

## 7. Arquitectura de documentación y paridad bilingüe

La documentación del proyecto mantiene paridad entre español argentino (`es-AR`) e inglés:
- **Índice central:** [`docs/README.es-AR.md`](README.es-AR.md) reúne todos los documentos operativos y de consulta.
- **Pares de idioma:** Cada guía técnica de la raíz y de `docs/` cuenta con su contraparte `.es-AR.md` y enlaces de navegación en el encabezado.
- **Copias de consulta:** Las instrucciones de trabajo (`AGENT-INSTRUCTIONS.es-AR.md`, `ARCHETYPES.es-AR.md`, `PROMPTS.es-AR.md`, `project-description.es-AR.md`) ofrecen lectura local conservando identificadores técnicos, claves de configuración y los prompts originales.
- **Independencia del árbol de contenido:** Los archivos de documentación quedan fuera de `content/` de Hugo, evitando la creación involuntaria de páginas públicas.


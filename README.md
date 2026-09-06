# VERUM — Sitio Web Oficial

> Sitio web bilingüe (Español Porteño / Inglés) de marca y lookbook para **VERUM**, etiqueta independiente de indumentaria pesada y callejera nacida en Buenos Aires, Argentina.

Construido desde cero como un tema a medida para **Hugo Extended**. Sin frameworks de JavaScript, sin dependencias pesadas y sin e-commerce (cero changuito, cero pasarelas de pago).

---

## 1. Requisitos Previos

- **Hugo Extended Edition** `>= v0.158` (probado y validado en `v0.165.0+extended`).
  > Es obligatorio usar la versión **Extended** para la compilación de Sass/SCSS nativa vía Hugo Pipes y el procesamiento de imágenes.

```bash
# macOS (Homebrew)
brew install hugo

# Verificar instalación
hugo version
```

---

## 2. Desarrollo Local

Clonar o entrar al repositorio y levantar el servidor de desarrollo local:

```bash
# Servidor local con recarga rápida y soporte bilingüe
hugo server -D

# Acceder en el navegador:
# Español (Default): http://localhost:1313/
# English (Secundario): http://localhost:1313/en/
```

---

## 3. Compilación de Producción

Para compilar los archivos estáticos en la carpeta `public/`:

```bash
hugo --minify --gc
```

- Compila y minifica automáticamente SCSS con `fingerprint` e integridad subrecurso (SRI).
- Minifica HTML, CSS y JavaScript nativo.
- Genera sitemaps bilingües (`sitemap.xml`) y etiquetas `hreflang` cruzadas con `x-default`.

---

## 4. Arquitectura y Metodología BEM

El proyecto implementa una arquitectura modular con metodología **BEM (Block Element Modifier)** en toda la suite SCSS:

- `assets/scss/_tokens.scss`: Variables de diseño (`--ink`, `--bone`, `--accent`, `--concrete`, `--paper`; `--cyan` y `--magenta` conservan compatibilidad con componentes existentes).
- `assets/scss/_typography.scss`: Tipografía Anton autoalojada, texto de sistema y bases de accesibilidad. La licencia de Anton vive en `static/fonts/OFL-Anton.txt`.
- `assets/scss/_glitch.scss`: Efecto aberración cromática RGB split en CSS puro con protección estricta para `@media (prefers-reduced-motion: reduce)`.
- `assets/scss/_nav.scss`: Cabecera sticky en escritorio, navegación desplegable en el flujo de la página en mobile y footer.
- `assets/scss/_lookbook.scss`: Bases de la grilla de prendas, ficha técnica y aviso de no-carrito.
- `assets/scss/_drops.scss`: Lanzamientos con estados condicionales (en la calle vs. próximamente).
- `assets/scss/_veritas.scss`: Crónicas editoriales de lectura inmersiva con artistas locales.
- `assets/scss/_forms.scss`: Puntos de venta físicos y formulario de contacto antispam.
- `assets/scss/_editorial.scss`: Dirección visual editorial, campaña, selección de prendas, newsletter, refinamientos de páginas internas y adaptación responsive.
- `assets/js/main.js`: Menú progresivo y filtros combinados por categoría/drop, con estado en la URL y conteo de resultados anunciado.

---

## 5. Implementación Bilingüe

- **Español (es-AR)**: Idioma primario situado en la raíz (`/`, `/lookbook/`, `/manifiesto/`). Escrito en español rioplatense porteño con voseo (*vos*, *mirá*, *rescatá*, *fichá*) y lunfardo callejero orientado a jóvenes de 20 a 30 años.
- **English (en)**: Idioma secundario situado bajo `/en/` (`/en/lookbook/`, `/en/manifesto/`).
- Las páginas se vinculan mediante el parámetro `translationKey` en el front matter.
- Los textos de interfaz residen en `i18n/es.toml` e `i18n/en.toml`.

---

## 6. Despliegue en Servidores Estáticos

Recomendado: **Cloudflare Pages** o **Netlify**.

### Configuración en Cloudflare Pages:
- **Build command**: `hugo --minify`
- **Build output directory**: `public`
- **Environment variables**: `HUGO_VERSION = 0.165.0`

### Cabeceras de Seguridad (Security Headers):
Se recomienda configurar las siguientes cabeceras en el host:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy: default-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'self'; form-action 'self' https://buttondown.email https://formspree.io; base-uri 'self'; object-src 'none';`

---

## 7. Documentación Complementaria

- [`CONTENT.md`](./CONTENT.md): Guía para cargar y editar prendas, drops y crónicas editoriales.
- [`PLACEHOLDERS.md`](./PLACEHOLDERS.md): Registro técnico de imágenes y activos provisionales para su sustitución en producción.


## 8. Diseño y Accesibilidad

La interfaz combina superficies de papel y tinta, un acento ácido, fotografía local y títulos condensados. La tipografía y los símbolos se sirven desde el sitio; los íconos decorativos no dependen de una fuente externa. Hugo genera versiones WebP de las fotografías de campaña y catálogo.

- El enlace para saltar al contenido transfiere el foco al `main`.
- El menú mobile es un desplegable en el flujo del documento. `Escape` lo cierra y devuelve el foco al botón. Sin JavaScript, los enlaces permanecen disponibles.
- Los filtros de prenda y drop se intersectan. Los botones exponen `aria-pressed`, el conteo anuncia los cambios y el estado vacío explica cómo recuperarse. La URL conserva los filtros al recargar o regresar desde una ficha.
- Las fichas presentan la imagen principal, la información de la prenda y las imágenes adicionales en el mismo orden de lectura visual y semántico. Los materiales, colores y talles usan una lista de definiciones.
- Los controles principales tienen objetivos de al menos 44 px. Los focos visibles, la preferencia de movimiento reducido y los modos de colores forzados tienen estilos explícitos.
- La suscripción usa un campo con etiqueta visible, autocompletado y validación nativa. La entrega del servicio externo debe verificarse por separado antes del lanzamiento.
- Contacto muestra un enlace de email cuando `form_endpoint` está vacío o contiene `placeholder`. Un endpoint real habilita el formulario. No se envían mensajes a un destino provisional.

Verificación de la revisión del 5 de septiembre de 2026: compilación de producción bilingüe; inspección de enlaces internos, IDs y alternativas de imágenes; recorridos de teclado del menú y enlace de salto; filtros combinados y recuperación del estado vacío; cambio de idioma en una ficha; validación de email vacío; revisión de reflujo y contraste de texto en páginas representativas a 320 px y revisión visual de escritorio. Estas comprobaciones no constituyen una certificación WCAG ni sustituyen una prueba con lectores de pantalla reales.

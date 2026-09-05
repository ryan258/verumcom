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

- `assets/scss/_tokens.scss`: Variables de diseño (`--ink`, `--bone`, `--cyan`, `--magenta`, `--concrete`, `--paper`).
- `assets/scss/_typography.scss`: Familias tipográficas y accesibilidad.
- `assets/scss/_glitch.scss`: Efecto aberración cromática RGB split en CSS puro con protección estricta para `@media (prefers-reduced-motion: reduce)`.
- `assets/scss/_nav.scss`: Cabecera sticky, menú accesible, drawer mobile y footer.
- `assets/scss/_lookbook.scss`: Grilla asimétrica de prendas, ficha técnica y aviso de no-carrito.
- `assets/scss/_drops.scss`: Lanzamientos con estados condicionales (en la calle vs. próximamente).
- `assets/scss/_veritas.scss`: Crónicas editoriales de lectura inmersiva con artistas locales.
- `assets/scss/_forms.scss`: Puntos de venta físicos y formulario de contacto antispam.

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
- `Content-Security-Policy: default-src 'self' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; font-src 'self' https://cdnjs.cloudflare.com; img-src 'self' data:; connect-src 'self';`

---

## 7. Documentación Complementaria

- [`CONTENT.md`](./CONTENT.md): Guía para cargar y editar prendas, drops y crónicas editoriales.
- [`PLACEHOLDERS.md`](./PLACEHOLDERS.md): Registro técnico de imágenes y activos provisionales para su sustitución en producción.

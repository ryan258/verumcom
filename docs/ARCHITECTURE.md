# VERUM — Architecture & Technical Specifications

[Español (Argentina)](ARCHITECTURE.es-AR.md) · English

Technical architecture and engineering standards for the VERUM static web platform.

## 1. System Overview

VERUM is built as a deterministic, high-performance static site with zero client-side tracking, no external web font dependencies at runtime, and no external runtime frameworks.

- **Static Site Generator:** Hugo Extended `>= 0.163.0` (target and CI pinned to `0.166.0`).
- **Templating:** Go HTML templates under `layouts/`.
- **Styling:** Modular SCSS compiled via Hugo Pipes with LibSass (`assets/scss/main.scss`).
- **Typography:** Self-hosted Anton (`static/fonts/anton-latin.woff2`), Space Mono, and system sans-serif font stack.
- **Client Scripting:** Minimal vanilla JavaScript (`assets/js/main.js`) strictly for progressive menu enhancement. All core navigation, content reading, and form fallbacks operate without JavaScript.
- **Hosting / Deployment:** Static web host (e.g., GitHub Pages, Cloudflare Pages, Netlify). Automated build via `.github/workflows/gh-pages.yml`.

---

## 2. Bilingual Architecture & Routing

VERUM serves two fully synchronized language trees:
- **Spanish (Primary):** Root URLs (`/`, `/lookbook/`, `/drops/`, `/manifiesto/`, `/contacto/`, `/veritas/`).
- **English (Secondary):** Prefixed URLs (`/en/`, `/en/lookbook/`, `/en/drops/`, `/en/manifesto/`, `/en/contact/`, `/en/veritas/`).

### Routing Synchronization
Pages in both languages are linked via Hugo's `translationKey` front matter parameter:
- Home: `content/es/_index.md` ↔ `content/en/_index.md`
- Lookbook garments: `content/es/lookbook/{slug}/index.md` ↔ `content/en/lookbook/{slug}/index.md`
- Drops (collections): `content/es/drops/{slug}/index.md` ↔ `content/en/drops/{slug}/index.md`
- En proceso (editorial): `content/es/veritas/{slug}/index.md` ↔ `content/en/veritas/{slug}/index.md`
- Single pages: `manifiesto` ↔ `manifesto`, `contacto` ↔ `contact`, `puntos-de-venta` ↔ `stockists`.
- Legal: `legal/privacidad` ↔ `legal/privacy`, `legal/terminos` ↔ `legal/terms`.

### URL Stability & Working Editorial Title
The editorial section uses the working title **En proceso** (Spanish) / **In process** (English). The URL routes `/veritas/` and `/en/veritas/` are preserved to maintain link integrity and prevent anchor breakage. Shared labels derive from `editorial_name` in the i18n files; localized section titles and descriptions live in the two `veritas/_index.md` files.

---

## 3. Template Hierarchy & Partials

The template architecture in `layouts/` is organized around unified, reusable layouts and single-responsibility partials:

```
layouts/
├── _default/
│   ├── baseof.html          # Global document frame, <head>, skip link, nav, footer
│   ├── contact.html         # Unified contact layout with channel verification
│   ├── manifesto.html       # Manifesto, principles, and team section
│   ├── single.html          # Generic single page fallback
│   └── stockists.html       # Physical stockists directory with empty-state protection
├── drops/
│   ├── list.html            # Collection overview (Sobreimpreso, En Obra)
│   └── single.html          # Individual collection detail with lookbook integration
├── lookbook/
│   ├── list.html            # Garment grid (6 pieces: 2 tees, 2 hoodies, 2 caps)
│   └── single.html          # Garment detail: front/back plates, specs, interview links
├── partials/
│   ├── brand-story.html     # Editorial team narrative and contributor profiles
│   ├── contact-channel.html # Primary contact channel resolver (Instagram, Email, WhatsApp)
│   ├── follow-project.html  # Secondary project engagement and verified channel links
│   ├── concept-note.html    # Explicit fictional-concept disclosure
│   ├── concept-piece-card.html # Reusable garment card
│   ├── artist-cards.html    # Collection/artist cards
│   ├── collaboration-image.html # Shared SVG and raster image rendering
│   └── reading-minutes.html # Estimated interview reading time
├── veritas/
│   ├── list.html            # Editorial archive (interviews with Lucía Ferreyra & Tomás Varela)
│   └── single.html          # 3-chapter interview view with linked garment references
├── index.html               # Garment-first homepage with current series highlights
└── robots.txt               # Search engine crawl directives
```

---

## 4. Asset Processing Pipeline

Hugo Pipes processes CSS, JavaScript and image resources. CSS and JavaScript receive content fingerprints; static files are copied separately. Document metadata, navigation and footer markup live in `layouts/_default/baseof.html`.

### SCSS Compilation
```go
{{ $sassOpts := dict "targetPath" "css/style.css" "outputStyle" "compressed" }}
{{ $style := resources.Get "scss/main.scss" | toCSS $sassOpts | minify | fingerprint }}
```

### Media Pipeline
- High-resolution garment plates and studio concepts are stored in `assets/images/`.
- Raster studio images are resized to 640px and 1280px WebP variants. Native SVG garment plates are served directly. Social metadata uses a 1200 × 630 JPEG; configured WebP/JPEG quality is `85`. There is no separate JPEG fallback in the collaboration image partial.
- The shared image partial emits `alt`, `width` and `height`, defaults to `loading="lazy"`, and accepts `loading="eager"`. It does not currently emit `fetchpriority`. Dimensions help reserve space; they do not prove absence of layout shift.

### Social Share Cards
- Individual 1200 × 630 cards for all 6 garments reside under `assets/images/social/`.
- Generated locally via `scripts/render_social_cards.py`.
- Referenced dynamically in Open Graph and Twitter Card metadata tags.

---

## 5. SCSS & Design Token Architecture

The styling system is partitioned into modular SCSS files under `assets/scss/`:

| Module | Responsibility |
| --- | --- |
| `_tokens.scss` | Colour and semantic surface tokens, font stacks, container/header sizes and base reset. |
| `_typography.scss` | Display headers (Anton), body sans font stack, monospace metadata (Space Mono), line heights, letter spacing. |
| `_nav.scss` | Header layout, mobile sheet navigation, language switcher, desktop inline links. |
| `_editorial.scss` | Editorial surfaces, shared controls, responsive behaviour, manifesto reading styles and forced colours. |
| `_collaborations.scss`| Series grids, collections, garment details, interviews, homepage and team/contact presentation. |
| `_components.scss` | Shared buttons, cards and base manifesto styles. |
| `_forms.scss` | Antispam-protected contact forms, form inputs, button focus states, empty state banners. |
| `_glitch.scss` | Subtle branding glitch accents, hover transforms, micro-interactions. |

---

## 6. Progressive Enhancement & Accessibility

1. **Zero-JS Core:**
   - Core content and navigation are intended to remain usable with JavaScript disabled. This does not establish full accessibility conformance.
   - Mobile navigation defaults to an accessible document-flow list if JS fails to execute.

2. **Keyboard & Focus Management:**
   - Persistent `Skip to content` (`#main-content`) link as the very first focusable element.
   - Visible outline styling across all interactive elements (`:focus-visible`).
   - `Escape` key closes the mobile menu drawer and returns focus to the toggle button.

3. **Motion & High Contrast:**
   - Respects `prefers-reduced-motion: reduce` by disabling transitions and animations.
   - Explicit styling for `forced-colors: active` ensuring border and contrast preservation in Windows High Contrast mode.

4. **Integrity & Security:**
   - Hosting security headers and any CSP must be inspected on the deployed response; no active CSP is established by the local build.
   - Stockist links that open new tabs specify `rel="noopener noreferrer"`.
   - Contact resolves a confirmed primary channel first, then a configured form endpoint without `placeholder`, otherwise a pending state. The form endpoint is independent of `contact_verified`; configuring it requires a separate owner check.

---

## 7. Documentation Architecture & Bilingual Parity

Project documentation maintains parity between Argentine Spanish (`es-AR`) and English:
- **Central Index:** [`docs/README.es-AR.md`](README.es-AR.md) catalogues all operational and consultation documents.
- **Language Pairs:** Root and `docs/` technical guides feature a localized `.es-AR.md` companion with header language toggles.
- **Consultation Copies:** Working instructions (`AGENT-INSTRUCTIONS.es-AR.md`, `ARCHETYPES.es-AR.md`, `PROMPTS.es-AR.md`, `project-description.es-AR.md`) provide local reading copies while preserving technical identifiers, configuration keys, and original prompts.
- **Independence from Content Tree:** Documentation files remain outside Hugo's `content/` hierarchy, avoiding inadvertent generation of public routes.


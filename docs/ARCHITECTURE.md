# VERUM — Architecture & Technical Specifications

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
The editorial section uses the working title **En proceso** (Spanish) / **In process** (English). The URL routes `/veritas/` and `/en/veritas/` are preserved to maintain link integrity and prevent anchor breakage. Shared labels derive from `editorial_name` in config and i18n bundles.

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
│   ├── meta-tags.html       # Open Graph, Twitter cards, canonical tags, hreflang
│   ├── site-footer.html     # Footer navigation, copyright, and verified links
│   └── site-nav.html        # Responsive header with mobile toggle and language switch
├── veritas/
│   ├── list.html            # Editorial archive (interviews with Lucía Ferreyra & Tomás Varela)
│   └── single.html          # 3-chapter interview view with linked garment references
├── index.html               # Garment-first homepage with current series highlights
└── robots.txt               # Search engine crawl directives
```

---

## 4. Asset Processing Pipeline

Hugo Pipes manages all assets with cryptographic fingerprinting and cache validation:

### SCSS Compilation
```go
{{ $opts := dict "transpiler" "libsass" "targetPath" "css/main.css" "outputStyle" (cond hugo.IsProduction "compressed" "expanded") }}
{{ $css := resources.Get "scss/main.scss" | toCSS $opts }}
{{ if hugo.IsProduction }}{{ $css = $css | fingerprint }}{{ end }}
```

### Media Pipeline
- High-resolution garment plates and studio concepts are stored in `assets/images/`.
- Processed via Hugo Pipes into modern WebP formats with fallback JPEGs at quality `85`.
- Hero, front, and back garment views enforce explicit `width`, `height`, and `loading="lazy"` attributes (above-the-fold hero images use `loading="eager"` and `fetchpriority="high"`) to prevent Cumulative Layout Shift (CLS).

### Social Share Cards
- Individual 1200 × 630 cards for all 6 garments reside under `assets/images/social/`.
- Generated locally via `scripts/render_social_cards.py`.
- Referenced dynamically in Open Graph and Twitter Card metadata tags.

---

## 5. SCSS & Design Token Architecture

The styling system is partitioned into modular SCSS files under `assets/scss/`:

| Module | Responsibility |
| --- | --- |
| `_tokens.scss` | Color tokens (`#0A0A0A` ink, `#F1F0E8` paper, `#DFFF00` acid), typography scales, spacing units, z-index layers. |
| `_typography.scss` | Display headers (Anton), body sans font stack, monospace metadata (Space Mono), line heights, letter spacing. |
| `_nav.scss` | Header layout, mobile sheet navigation, language switcher, desktop inline links. |
| `_editorial.scss` | Global container widths, grid utilities, article prose, interview pull-quotes, callouts. |
| `_collaborations.scss`| Current series grid (6 pieces), collection cards, cross-links, garment action rows. |
| `_lookbook.scss` | Lookbook grid layout, plate viewer, specs table, companion piece cards. |
| `_drops.scss` | Collection banner treatments, palette chips, artist bio block, pieces list. |
| `_veritas.scss` | 3-chapter conversational layouts, pull quotes, garment visual callouts. |
| `_forms.scss` | Antispam-protected contact forms, form inputs, button focus states, empty state banners. |
| `_glitch.scss` | Subtle branding glitch accents, hover transforms, micro-interactions. |

---

## 6. Progressive Enhancement & Accessibility

1. **Zero-JS Core:**
   - Every page, link, garment view, collection, and legal disclosure is 100% accessible with JavaScript disabled.
   - Mobile navigation defaults to an accessible document-flow list if JS fails to execute.

2. **Keyboard & Focus Management:**
   - Persistent `Skip to content` (`#main-content`) link as the very first focusable element.
   - Visible outline styling across all interactive elements (`:focus-visible`).
   - `Escape` key closes the mobile menu drawer and returns focus to the toggle button.

3. **Motion & High Contrast:**
   - Respects `prefers-reduced-motion: reduce` by disabling transitions and animations.
   - Explicit styling for `forced-colors: active` ensuring border and contrast preservation in Windows High Contrast mode.

4. **Integrity & Security:**
   - Strict Content Security Policy (CSP) compatibility.
   - External links specify `rel="noopener noreferrer"`.
   - Contact form actions default to mailto or verified endpoints; placeholder endpoints (`placeholder`) disable transmission to prevent leaked submissions.

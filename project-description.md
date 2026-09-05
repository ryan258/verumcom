# VERUM — Website Project Description

**Version:** 1.0
**Prepared for:** Web developer (Hugo build)
**Status:** Ready to quote and build
**Platform:** Hugo (static site generator), Extended edition

---

## 1. TL;DR

Build a bilingual (Spanish + English) brand site for **VERUM**, an Argentine streetwear label. The site is a **lookbook and brand story** — not a store. No cart, no checkout, no payments.

The whole site is roughly **8 page templates** and one repeating content type (lookbook pieces). Build it as a custom Hugo theme. Do not use an off-the-shelf theme.

**No brand assets exist yet.** Build the entire site against placeholders. Real logo, photos, and copy get swapped in later. Design every component so that swap is a file replacement, not a rebuild.

---

## 2. Scope

### In scope

- Custom Hugo theme, built from scratch
- Bilingual site: Spanish (default) and English
- Lookbook with individual piece pages
- Brand story / manifesto page
- "Veritas" editorial section (artist stories)
- Drops archive (past and upcoming releases, informational only)
- Stockist / where-to-find page
- Contact page with a form
- Email signup capture
- Responsive down to 360px wide
- Deploy pipeline to a static host

### Out of scope

These are explicitly **not** part of this build. If they get added later, they are a separate quote.

- E-commerce of any kind — no cart, no checkout, no inventory, no payments
- User accounts or logins
- A CMS admin panel (see §9 for the content-editing decision)
- Blog comments
- Native mobile apps
- Photography, copywriting, or translation
- Logo design or brand asset creation

### Why no store

Hugo is a static site generator. It builds plain HTML files ahead of time. It has no server, no database, and no session handling. Selling online would require bolting on a third-party service like Shopify Buy Buttons, Snipcart, or Ecwid. That adds monthly cost, a second vendor, PCI considerations, and a new set of things that can break.

**The decision has been made to skip that entirely for v1.** If VERUM sells, it sells through Instagram DMs, WhatsApp, or a physical stockist. The site links out.

---

## 3. Brand context

The developer does not need to be a brand strategist. But design decisions will be wrong without this section. Read it.

### The name

**VERUM** is Latin for "true." The brand sits inside the authenticity movement — a reaction against AI-generated visual perfection. The Argentine market is pivoting toward *lo real*: raw, handmade, imperfect.

### The logo

The logo is a high-contrast **graffiti-stencil** wordmark with three signature traits:

1. **The drip.** Ink bleeds off the R, U, and M. It reads as "the paint is still wet." DIY street energy from CABA (Ciudad Autónoma de Buenos Aires).
2. **Chromatic aberration.** Cyan and magenta channel offsets create an RGB-split glitch. This bridges analog graffiti with the digital "Cyber-Pampa" look trending with Argentine Gen Z.
3. **Tactile imperfection.** Uneven stroke weights and rough edges. Human-made, not machine-made.

### Market position

The Argentine streetwear scene runs on *Lujo de Barrio* — neighborhood luxury. VERUM's slot:

| Element | What it means for the site |
|---|---|
| **The name** | No-nonsense. Copy should be blunt and short. No marketing fluff. |
| **The vibe** | Aggressive but artistic. Closer to urban activist than skater. |
| **Cultural link** | Trap Argentino and RKT music scenes. Visual noise and high contrast are the native language here. |

### The one thing to get right

The brand's core asset is **visual friction**. It is hard to look away from. A clean, safe, generic portfolio site kills the brand. The site should feel a little uncomfortable — high contrast, heavy type, tight crops, aggressive scale jumps.

**But:** friction in the visuals, never in the navigation. A user must always know where they are and how to get back. Chaos in the art direction. Order in the structure.

---

## 4. Design direction

### Color palette

Use these as CSS custom properties. Names are the design tokens — use them in the code.

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#0A0A0A` | Primary background. Near-black, not pure black. |
| `--bone` | `#F2F0EB` | Primary text on dark. Warm off-white, not pure white. |
| `--cyan` | `#00F0FF` | Glitch accent, hover states, focus rings |
| `--magenta` | `#FF0090` | Glitch accent, secondary highlight |
| `--concrete` | `#6E6E6E` | Muted text, borders, metadata |
| `--paper` | `#E8E4DC` | Alternate light-mode section background |

The site is **dark by default.** Light sections are the exception, used to break rhythm — for example, the manifesto page or a single editorial spread.

**Contrast warning:** `--magenta` on `--ink` sits right around the accessibility minimum. Run every text pairing through a contrast checker before shipping. If magenta text fails at small sizes, use it only for large display type, borders, and non-text decoration.

### Typography

Three roles. Do not add a fourth.

1. **Display** — heavy condensed grotesque, for headlines and page titles. Tight tracking. Set large, often clipped or bleeding off the edge.
2. **Body** — clean neutral sans, high legibility. Must have full Latin Extended support for Spanish accents and ñ.
3. **Mono** — small caps or monospace for metadata: drop numbers, dates, sizes, labels. This is where the "technical spec sheet" texture comes from.

**Font licensing is a real risk.** Do not ship a font without a valid web license. Self-host all fonts — do not load from Google Fonts CDN. Self-hosting is faster, avoids a third-party request, and sidesteps EU privacy complaints. Use `font-display: swap` and preload the display face only.

**The logo font is not a web font.** The stencil wordmark is custom lettering. It ships as SVG. Never try to recreate it with a typeface.

### The glitch effect

This is the signature. It is also the easiest thing to get wrong.

**Do:**
- Build the RGB split as a CSS effect on a limited set of elements — page titles, hover states, the logo lockup
- Use `text-shadow` with cyan and magenta offsets, or duplicated pseudo-elements with `mix-blend-mode`
- Keep animation subtle and short — a flicker on load or hover, not a constant seizure
- Wrap all glitch animation in `@media (prefers-reduced-motion: reduce)` and disable it fully for users who ask

**Do not:**
- Apply glitch to body copy. It destroys readability.
- Animate glitch continuously on more than one element at a time
- Use JavaScript for the effect if CSS can do it
- Let the effect run on scroll-linked triggers on mobile — it tanks frame rate

**Accessibility note:** rapid flashing can trigger photosensitive seizures. Nothing should flash more than three times per second. This is not optional.

### Layout principles

- **Asymmetry over grids.** Center-aligned symmetry reads as corporate. Push content off-axis.
- **Scale jumps.** A 120px headline next to 12px metadata. The gap is the point.
- **Hard edges.** No rounded corners. No soft drop shadows. No gradients except the chromatic offsets.
- **Texture.** Subtle grain or halftone overlay on image sections. Keep the file tiny — a repeating 100x100 PNG at low opacity, not a full-bleed asset.
- **Whitespace is black space.** Give the type room. Density in one zone, emptiness next to it.

---

## 5. Site map

```
/                          Home
/manifiesto/               Brand story / manifesto
/lookbook/                 Lookbook index (grid of pieces)
/lookbook/{slug}/          Individual piece page
/drops/                    Drops archive index
/drops/{slug}/             Individual drop page
/veritas/                  Editorial index (artist stories)
/veritas/{slug}/           Individual story
/puntos-de-venta/          Stockists / where to find us
/contacto/                 Contact
/legal/privacidad/         Privacy policy
/legal/terminos/           Terms
/404.html                  Custom 404
```

English mirrors live under `/en/` with translated slugs. See §7.

### Page-by-page notes

**Home**
Full-viewport opening moment. Logo, one line of manifesto copy, and a single call to action into the lookbook. Below that: latest drop, three featured pieces, latest Veritas story, email signup. Keep it short. Five sections maximum.

**Manifiesto**
Long-form single page. This is where the light-background break happens. Typography-led, minimal imagery. Should read like a statement, not an About Us page.

**Lookbook index**
Masonry or irregular grid of pieces. Filterable by drop and by category. Filtering should work without JavaScript as a fallback — use separate taxonomy pages as the no-JS path.

**Lookbook piece page**
Image gallery, piece name, drop it belongs to, materials, fabric weight, sizing notes, and a short piece of story copy. Prominent "where to buy" module that links to stockists or an external channel. **No add-to-cart button.**

**Drops**
Each drop is a dated release with a name, a number, a hero image, a short statement, and a list of the pieces in it. Supports an "upcoming" state where the piece list is hidden and only a date and email signup show.

**Veritas**
Editorial articles. Long-form text with large images. This is where the "true stories from street artists" campaign lives. Needs a clean, readable reading experience — this is the one place where legibility beats visual friction.

**Puntos de venta**
List of physical stockists with address, neighborhood, and hours. Group by city and neighborhood (Palermo Soho, San Telmo, etc.). No live map embed in v1 — link out to a maps URL instead. Embeds are heavy and add a third-party tracker.

**Contacto**
Simple form: name, email, subject, message. See §8 for how to handle submissions.

---

## 6. Content model

Every content type below needs a Hugo archetype in `archetypes/`. Front matter must be filled by whoever adds content, so keep field names obvious and document them in a `CONTENT.md` at the repo root.

### Lookbook piece

Use a **page bundle** — a folder per piece with its images inside. This keeps images next to their content and lets Hugo's image processing work cleanly.

```
content/es/lookbook/campera-verdad/
├── index.md
├── 01-front.jpg
├── 02-back.jpg
└── 03-detail.jpg
```

```yaml
---
title: "Campera Verdad"
date: 2026-03-01
drop: "drop-01"
categories: ["outerwear"]
sizes: ["S", "M", "L", "XL", "XXL"]
fabric: "Algodón 420 GSM"
color: "Negro / Cian"
featured: true
gallery_order: ["01-front.jpg", "02-back.jpg", "03-detail.jpg"]
stockists: ["barracas-studio", "san-telmo-shop"]
draft: false
---

Short piece story. Two or three sentences maximum.
```

### Drop

```yaml
---
title: "Drop 01 — Lo Real"
drop_number: "01"
date: 2026-03-15
status: "released"    # released | upcoming | archived
hero: "hero.jpg"
statement: "One-line drop statement."
draft: false
---
```

### Veritas story

```yaml
---
title: "Historia del artista"
date: 2026-04-02
author: "Nombre"
artist_name: "Nombre del artista"
neighborhood: "La Boca"
hero: "hero.jpg"
summary: "One or two sentences for the index card and meta description."
draft: false
---
```

### Stockist

Store these as **data files**, not content pages. They are structured records, not documents.

`data/stockists.yaml`:

```yaml
- id: "barracas-studio"
  name: "Nombre del local"
  city: "Buenos Aires"
  neighborhood: "Barracas"
  address: "Calle Ejemplo 1234"
  hours: "Lun–Sáb 11:00–20:00"
  maps_url: "https://..."
  instagram: "@..."
```

### Taxonomies

Configure exactly two. Do not add more without asking.

- `drops` — which release a piece belongs to
- `categories` — garment type (outerwear, tees, headwear, accessories)

---

## 7. Bilingual setup

**Spanish is the default language.** English is the secondary.

### URL structure

- Spanish: `verum.com/lookbook/`
- English: `verum.com/en/lookbook/`

Set `defaultContentLanguageInSubdir = false` so Spanish sits at the root.

### Configuration sketch

```toml
defaultContentLanguage = "es"
defaultContentLanguageInSubdir = false

[languages]
  [languages.es]
    languageCode = "es-AR"
    languageName = "Español"
    contentDir = "content/es"
    weight = 1
  [languages.en]
    languageCode = "en"
    languageName = "English"
    contentDir = "content/en"
    weight = 2
```

### Translation linking

Link translations by filename or by an explicit `translationKey` in front matter. **Use `translationKey`** — it survives slug translation. English slugs should be translated too (`/en/lookbook/` not `/en/lookbook/`, but `/en/manifesto/` not `/en/manifiesto/`). All UI strings go in `i18n/es.toml` and `i18n/en.toml`. Never hardcode a visible string in a template.

### The missing-translation problem

**This will happen.** Content will exist in Spanish and not in English.

Decide the behavior now and document it. Recommended: if an English page does not exist, **do not link to it** — the language toggle hides or disables for that page rather than sending a user to a 404. Do not silently serve Spanish content under an `/en/` URL. That is worse than a broken link because search engines index it as English.

### SEO

Emit `hreflang` tags on every page for both languages plus `x-default` pointing at Spanish. Each language needs its own `sitemap.xml` and both must be listed in a sitemap index.

---

## 8. Technical requirements

### Stack

- **Hugo Extended** — required, not optional. Extended is needed for SCSS compilation and image processing.
- Pin the exact Hugo version in the repo and in the deploy config. A Hugo minor version bump can break templates.
- **No JavaScript framework.** No React, no Vue, no build step beyond Hugo Pipes.
- Vanilla JS only, and only where CSS cannot do the job — likely just the mobile nav toggle and the lookbook filter enhancement.
- Target: the site must be usable with JavaScript disabled. Degraded is fine. Broken is not.

### Assets

- Use **Hugo Pipes** for CSS and JS: fingerprint, minify, and bundle.
- Use **Hugo's image processing** to generate responsive variants. Serve WebP with a JPEG fallback. Emit proper `srcset` and `sizes`.
- Lazy-load all images below the fold. The hero image is eager and preloaded.
- Every image needs a real `alt` attribute. Decorative images get `alt=""`.

### Performance budget

Argentine mobile data is expensive and networks are uneven. This is a hard constraint, not a nice-to-have.

| Metric | Target |
|---|---|
| Largest Contentful Paint (4G) | under 2.5s |
| Total page weight, home | under 1.2 MB |
| Total page weight, content page | under 900 KB |
| JavaScript, total | under 30 KB |
| Web fonts | 3 files maximum, WOFF2 only |
| Lighthouse Performance | 90+ on mobile |

If the design cannot hit these numbers, **flag it before building it.** Do not ship a heavy site and apologize afterward.

### Accessibility

Target WCAG 2.1 AA.

- Full keyboard navigation with a visible focus indicator. Use `--cyan` for focus rings — it is on-brand and high contrast.
- Respect `prefers-reduced-motion` for every animation, no exceptions.
- Nothing flashes more than three times per second.
- Semantic HTML: real `<nav>`, `<main>`, `<article>`, real heading order.
- Form inputs have real labels, not placeholder-only labels.
- Test with a screen reader before delivery, not after.

### Contact form

Hugo cannot process a form submission. It has no server.

Pick one third-party handler and document the choice: Formspree, Netlify Forms, Basin, or a similar service. All of them are external dependencies with their own free-tier limits and failure modes. Add honeypot spam protection at minimum. Avoid a CAPTCHA if possible — it hurts accessibility and adds weight.

### Email signup

Same situation. This needs an external provider — Mailchimp, Buttondown, ConvertKit, or similar. The form posts to their endpoint. Style the form to match the brand; do not use their default embedded widget, which will look nothing like the site.

### Analytics

Use a lightweight, privacy-respecting option (Plausible, Umami, GoatCounter) or none at all. Do not add Google Analytics without an explicit decision, because it triggers a cookie consent requirement, which adds a banner that will damage the first impression.

---

## 9. Content editing

**Open question — needs a decision before launch, not before build.**

Hugo content lives in Markdown files in a Git repository. Editing it means either using a text editor and Git, or adding a Git-based CMS layer.

Three paths:

1. **Git only.** Zero cost, zero added dependency. Requires whoever updates the site to be comfortable with Markdown and a Git workflow.
2. **Git-based CMS** (Decap CMS, Sveltia CMS, or similar). Adds an admin panel at `/admin/`. Free, but it is another dependency that can break on updates, and bilingual content in these tools is workable but clunky.
3. **Hosted CMS** (Cloud Canvas, Front Matter in VS Code, or a headless service). More polish, more cost, more setup.

**Recommendation: build for path 1, structure so path 2 can be added later.** That means clean, consistent front matter and no clever template logic that depends on hand-edited files.

---

## 10. Deployment

- Host on a static host with Git-triggered builds: Netlify, Cloudflare Pages, or Vercel. All have free tiers adequate for this site.
- **Cloudflare Pages is the recommendation** if the audience is primarily in Argentina — its edge network coverage in South America is strong and the free tier has no build-minute cap.
- Pin the Hugo version in the build environment.
- Set up deploy previews on pull requests.
- Custom domain with HTTPS, HTTP to HTTPS redirect, and `www` to apex redirect (or the reverse — pick one and be consistent).
- Add security headers: CSP, `X-Content-Type-Options`, `Referrer-Policy`.

---

## 11. Placeholder strategy

No real assets exist. Build the entire site with placeholders and make the swap trivial.

- **Logo:** create a rough SVG stencil placeholder at the correct proportions. The final logo drops in as a file replacement at `assets/logo.svg`. Do not inline the logo path into templates.
- **Photography:** use consistently sized placeholder images at the exact aspect ratios the real photos will use. Document those ratios in `CONTENT.md`. Recommended: 4:5 for piece photography, 16:9 for drop heroes, 3:2 for editorial.
- **Copy:** write real-sounding placeholder copy in Spanish, not lorem ipsum. Lorem ipsum hides layout problems because it has the wrong word lengths and no accented characters. Spanish placeholder text will surface accent-rendering and line-length issues early.
- **Content volume:** build with at least 12 lookbook pieces, 2 drops, and 4 Veritas stories so grid and pagination behavior is actually tested.

**Deliver a `PLACEHOLDERS.md`** listing every placeholder asset, its location, its required dimensions, and what real asset replaces it.

---

## 12. Risks and failure points

Stated plainly so nobody is surprised later.

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Bilingual content debt** — English translations never get written | High | Site half-empty in one language | Decide the fallback behavior now (§7). Launch Spanish-complete, English partial, and hide untranslated pages. |
| **Real assets never arrive** or arrive in the wrong format/ratio | High | Launch slips indefinitely | Lock aspect ratios in `PLACEHOLDERS.md` on day one. Give the photographer a spec sheet. |
| **Glitch effect kills mobile performance** | Medium | Fails the performance budget | Build it CSS-only, limit it to a handful of elements, test on a real mid-range Android early — not in a desktop emulator. |
| **Font licensing gap** | Medium | Legal exposure or a last-minute typeface swap | Confirm web licenses in writing before any type is chosen. Have a fallback stack picked. |
| **Third-party form or email service fails or changes its free tier** | Medium | Contact form silently stops working | Route a copy of submissions to a second address. Test the form monthly. |
| **Hugo version drift** breaks the build | Low | Deploy failures | Pin the version in the repo and in the host config. |
| **Design is too aggressive to navigate** | Medium | Users bounce | Usability-test the navigation with three people who have never seen the site. Do this at the wireframe stage, not after launch. |
| **Accessibility failures** from the glitch aesthetic | Medium | Excludes users, possible legal exposure | Build reduced-motion and contrast compliance in from the start. Retrofitting is far more expensive. |

**None of these are reasons not to build.** They are the things that will consume the schedule if they are not handled up front.

---

## 13. Definition of done

The build is complete when all of the following are true.

1. All pages in §5 exist and render in both Spanish and English
2. All content types in §6 have working archetypes and templates
3. `hreflang`, sitemaps, and canonical tags are correct for both languages
4. The site passes the performance budget in §8 on a throttled mobile test
5. Lighthouse Accessibility score is 95+, with any remaining issues documented and justified
6. The site is fully navigable by keyboard with visible focus states
7. All animation respects `prefers-reduced-motion`
8. The site is usable with JavaScript disabled
9. The contact form delivers to a real inbox, tested end to end
10. The email signup delivers to the provider list, tested end to end
11. Custom 404 page exists in both languages
12. Tested on: latest Chrome, Safari, Firefox, iOS Safari, and one mid-range Android device
13. Tested at 360px, 768px, 1024px, and 1440px wide
14. `README.md`, `CONTENT.md`, and `PLACEHOLDERS.md` are complete
15. Deploy pipeline runs green from a clean clone

---

## 14. Deliverables

1. Git repository with full source and commit history
2. Custom Hugo theme (in `themes/verum/` or as the project's own layouts — developer's call, but document it)
3. Working deploy on a staging URL
4. `README.md` — how to run locally, how to build, how to deploy
5. `CONTENT.md` — how to add a piece, a drop, a story; every front matter field explained in plain language
6. `PLACEHOLDERS.md` — every placeholder and its replacement spec
7. A short handoff walkthrough (recorded video is fine, 15 minutes)

---

## 15. Open decisions

These do not block the start of the build. They do block launch. Track them.

1. **Domain name** — not yet chosen
2. **Content editing path** — Git only vs. added CMS (§9)
3. **Form handler** — which provider
4. **Email provider** — which provider
5. **Analytics** — which, or none
6. **Typeface selection** — subject to licensing confirmation
7. **Real stockist list** — does one exist yet
8. **Legal pages** — who writes the privacy policy and terms

---

## 16. Notes for whoever writes the copy

Not the developer's job, but it shapes the templates, so it is documented here.

- Spanish first, and **Argentine** Spanish. Use *vos*, not *tú*. This matters. Neutral Latin American Spanish will read as foreign to the audience.
- Short sentences. The brand is named "true." Copy that oversells contradicts the name.
- Headlines run 2 to 6 words. Templates are designed around that. Longer headlines will break the layout.
- Piece descriptions: 2 to 3 sentences maximum.
- English is a translation, not a rewrite — but it should not read like machine output. Budget for a human pass.
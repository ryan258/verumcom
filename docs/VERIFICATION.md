# VERUM — Verification & Quality Assurance Suite

[Español (Argentina)](VERIFICATION.es-AR.md) · English

Deterministic gates, testing scripts, and accessibility auditing procedures.

---

## 1. Quality Philosophy

Use focused deterministic checks for the changed behaviour. These scripts do not automatically block a commit or deployment: the current GitHub Pages workflow builds and deploys without invoking them. Follow repository instructions for authorization and pre-commit checks. We do not rely on ad-hoc visual checks alone: automated Python scripts inspect rendered HTML output, checking links, image metadata, localized anchors, route hygiene, and configuration states.

---

## 2. Test Scripts

The two verification scripts are located in `scripts/` and require Python `>= 3.11` without third-party dependencies (using standard library `html.parser`, `urllib.parse`, `pathlib`, `tomllib`).

### 2.1 `scripts/verify_concepts.py`
Validates core Hugo output integrity across both language trees (`/` and `/en/`):
- **Bilingual Route Parity:** The 20 localized collection, garment and interview items have paired translation keys and matching relationship/asset fields. This is not a full-site translation audit.
- **Internal Link Check:** Resolves all relative and absolute internal URLs across 28 selected rendered routes (720 links in the recorded October 3 run).
- **Anchor Resolution:** Verifies every URL fragment (`#equipo`, `#registro`, etc.) exists as an `id` on the target page.
- **Image Attributes:** Enforces `alt`, `width`, and `height` attributes on images in the checked pages. It checks attribute presence, not the quality of alt text or actual layout shift.
- **Image Existence:** Validates that every referenced static/processed image file physically exists in the output directory.
- **Retired Route Protection:** Verifies that deprecated routes (e.g. legacy sample garments and drops) are absent from output.
- **Fictional Disclosures:** Confirms that concept disclaimer banners are rendered on all conceptual garment and drop views.

### 2.2 `scripts/verify_review.py`
Focused regression checks for brand presentation and user flow:
- Invokes `verify_concepts.py` as a prerequisite.
- Verifies garment-first architecture on Home (`/`, `/en/`) and Lookbook (`/lookbook/`, `/en/lookbook/`).
- Validates the 6 concept garment slugs: `registro`, `persistencia`, `testigo`, `cota`, `trazo`, `escuadra`.
- Checks six distinct generated JPEG share-image URLs containing `/images/social/{slug}`, emitted files, alt metadata and matching Twitter image URLs. It does not measure the image dimensions.
- Checks primary contact channel configuration (`contact_verified` flag in `hugo.toml`).
- Verifies team narrative link (`#equipo`) resolution in Manifesto.

### 2.3 `scripts/render_social_cards.py`
Rendering utility, not a test: produces the six 1200 × 630 px cards in `assets/images/social/`. Requires ImageMagick (`magick`) and a suitable font; see PLACEHOLDERS.md. A normal Hugo build uses the existing images.

---

## 3. Running Deterministic Verification

To test changes locally in an isolated sandbox without polluting working directory:

```bash
# 1. Create a clean isolated temporary preview destination
PREVIEW_DIR="$(mktemp -d /tmp/verum-qa.XXXXXX)"

# 2. Build the Hugo site
hugo --destination "$PREVIEW_DIR" \
     --cacheDir /tmp/verum-qa-cache \
     --baseURL http://127.0.0.1:8766/ \
     --noBuildLock &&

# 3. Execute the automated verification suite
python3 scripts/verify_review.py "$PREVIEW_DIR"

# Keep PREVIEW_DIR available for the browser review below.
```

Recorded October 3 result (link counts can change with content; this is not a new run):
```
PASS: 28 rendered pages; 20 localized content items; 720 local links; bilingual relationships, interview anchors, images, disclosures and retired-route cleanup verified.
PASS: garment-first home/lookbook, collection navigation, founder route, six share images, and contact state in both languages.
```

---

## 4. Manual Verification & Accessibility Protocol

For browser visual verification, serve the built site:

```bash
python3 -m http.server 8766 --bind 127.0.0.1 --directory "$PREVIEW_DIR"
```

Navigate to `http://127.0.0.1:8766/` and audit against the following matrix:

| Test Area | Target / Spec | Verification Procedure |
| --- | --- | --- |
| **Responsive Reflow** | 320 px, 390 px, 768 px, 1440 px | Inspect layout reflow in DevTools. Ensure zero horizontal scroll and 100% readable typography. |
| **Skip Link** | `#main-content` | Press `Tab` upon initial page load; confirm skip link appears and focuses main container. |
| **Mobile Navigation** | `<button class="site-header__toggle">` | Open menu on mobile viewport, verify ARIA attributes update (`aria-expanded`), press `Escape` to close. |
| **Focus Indication** | `:focus-visible` | Keyboard tab through all buttons and links; ensure high-contrast outline is clearly visible. |
| **High Contrast Mode** | `forced-colors: active` | Emulate forced colors; ensure borders, focus outlines, and buttons remain distinct. |
| **Language Switcher** | `es` ↔ `en` | Switch language on individual garment and collection pages; confirm exact route correspondence. |

These are targeted checks, not proof of WCAG conformance, screen-reader acceptance, real-device coverage or delivery to an external inbox. A configured endpoint is not a verified delivery result.


### Output under a deployment subpath

When Hugo overrides the configured base URL, pass that same effective URL to the focused checker, for example:

```sh
python3 scripts/verify_review.py "$PREVIEW_DIR" --base-url https://example.invalid/verumcom/
```

The checker resolves local images, links, anchors and garment navigation relative to that subpath. The Pages workflow supplies its configured Pages URL before artifact upload. This is a generated-output gate; it does not verify business facts, account ownership, provider delivery, human acceptance or a successful deployment.

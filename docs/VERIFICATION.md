# VERUM — Verification & Quality Assurance Suite

Deterministic gates, testing scripts, and accessibility auditing procedures.

---

## 1. Quality Philosophy

VERUM enforces strict deterministic gates prior to any git commit or deployment. We do not rely on ad-hoc visual checks alone: automated Python scripts inspect rendered HTML output, checking links, image metadata, localized anchors, route hygiene, and configuration states.

---

## 2. Test Scripts

All verification scripts are located in the `scripts/` directory and require Python `>= 3.11` without third-party dependencies (using standard library `html.parser`, `urllib.parse`, `pathlib`, `tomllib`).

### 2.1 `scripts/verify_concepts.py`
Validates core Hugo output integrity across both language trees (`/` and `/en/`):
- **Bilingual Route Parity:** Every page in Spanish has an exact corresponding English translation and matching `translationKey`.
- **Internal Link Check:** Resolves all relative and absolute internal URLs across 28+ rendered pages (>720 links checked).
- **Anchor Resolution:** Verifies every URL fragment (`#equipo`, `#capitulo-1`, etc.) exists as an `id` on the target page.
- **Image Attributes:** Enforces `alt`, `width`, and `height` attributes on all rendered `<img>` elements to eliminate layout shift.
- **Image Existence:** Validates that every referenced static/processed image file physically exists in the output directory.
- **Retired Route Protection:** Verifies that deprecated routes (e.g. legacy sample garments and drops) are absent from output.
- **Fictional Disclosures:** Confirms that concept disclaimer banners are rendered on all conceptual garment and drop views.

### 2.2 `scripts/verify_review.py`
High-level regression suite for brand presentation and user flow:
- Invokes `verify_concepts.py` as a prerequisite.
- Verifies garment-first architecture on Home (`/`, `/en/`) and Lookbook (`/lookbook/`, `/en/lookbook/`).
- Validates the 6 concept garment slugs: `registro`, `persistencia`, `testigo`, `cota`, `trazo`, `escuadra`.
- Asserts that all 6 Open Graph social card images (`/assets/images/social/{slug}.jpg` or `.png`) exist and are appropriately dimensioned.
- Checks primary contact channel configuration (`contact_verified` flag in `hugo.toml`).
- Verifies team narrative link (`#equipo`) resolution in Manifesto.

### 2.3 `scripts/render_social_cards.py`
Automated rendering script that produces the six 1200 × 630 px social share cards located in `assets/images/social/`.

---

## 3. Running Deterministic Verification

To test changes locally in an isolated sandbox without polluting working directory:

```bash
# 1. Create a clean isolated temporary preview destination
PREVIEW_DIR="$(mktemp -d /tmp/verum-qa.XXXXXX)"

# 2. Build the Hugo site in production mode
hugo --destination "$PREVIEW_DIR" \
     --cacheDir /tmp/verum-qa-cache \
     --baseURL http://127.0.0.1:8766/ \
     --noBuildLock

# 3. Execute the automated verification suite
python3 scripts/verify_review.py "$PREVIEW_DIR"

# 4. Clean up the temporary preview directory
rm -rf "$PREVIEW_DIR" /tmp/verum-qa-cache
```

Expected result:
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
| **Mobile Navigation** | `<button class="site-nav__toggle">` | Open menu on mobile viewport, verify ARIA attributes update (`aria-expanded`), press `Escape` to close. |
| **Focus Indication** | `:focus-visible` | Keyboard tab through all buttons and links; ensure high-contrast outline is clearly visible. |
| **High Contrast Mode** | `forced-colors: active` | Emulate forced colors; ensure borders, focus outlines, and buttons remain distinct. |
| **Language Switcher** | `es` ↔ `en` | Switch language on individual garment and collection pages; confirm exact route correspondence. |

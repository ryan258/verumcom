# VERUM — Project Roadmap & Implementation Milestones

This document tracks the phased progression of the VERUM platform, from structural foundation and creative direction to real contributor onboarding and physical production.

---

## Strategic Phases Overview

```
[Phase 1: Architecture] ──► [Phase 2: Design Identity] ──► [Phase 3: Series 01-02] ──► [Phase 4: QA & Verification]
                                                                                               │
                                                                                               ▼
[Phase 7: Production Launch] ◄── [Phase 6: Garment Sampling] ◄── [Phase 5: Contributor Onboarding (Active)]
```

---

## Phase 1: Core Foundation & Bilingual Architecture
**Status: Completed**

- [x] Hugo Extended (`>= 0.163.0`) project structure with deterministic builds.
- [x] Fully synchronized bilingual content tree: Spanish (`/`) and English (`/en/`).
- [x] Bi-directional language routing via `translationKey`.
- [x] Accessible HTML5 document semantics with landmark roles and skip navigation.
- [x] Zero external runtime JavaScript frameworks; progressive vanilla JS for mobile menu.
- [x] Standard-compliant Content Security Policy and privacy-focused static assets.

---

## Phase 2: Design Identity & Layout Overhaul
**Status: Completed**

- [x] Localized typography pipeline: Anton display font (`.woff2`) and Space Mono metadata.
- [x] Editorial color palette: `#0A0A0A` (ink), `#F1F0E8` (warm paper), and `#DFFF00` (acid accent).
- [x] Unified layout templates (`layouts/_default/`, `layouts/partials/`) replacing fragmented one-offs.
- [x] Modern Hugo Pipes image optimization pipeline (WebP generation, CLS prevention with explicit dimensions).
- [x] Native UI iconography replacing heavyweight external font icon libraries.
- [x] Responsive layout testing across 320 px to 1440 px viewports with high-contrast accessibility support.

---

## Phase 3: Artist Series 01–02 Conceptual Framework
**Status: Completed**

- [x] Defined creative direction: *«Ideas que se llevan / Ideas you can wear»* (`CREATIVE-DIRECTION.md`).
- [x] Created two deep fictional artist collaborations:
  - **Sobreimpreso** (Lucía Ferreyra, printmaker, Chacarita) — Red/Cobalt/Acid Yellow palette.
  - **En Obra** (Tomás Varela, metalworker, La Paternal) — Black/White/Graphite palette.
- [x] Catalog structured into six core garments:
  - *Registro* (tee), *Persistencia* (hoodie), *Testigo* (cap).
  - *Cota* (tee), *Trazo* (hoodie), *Escuadra* (cap).
- [x] Converted Veritas into the working editorial title **«En proceso / In process»** while preserving URL paths.
- [x] Embedded three-chapter interview formats linking directly to corresponding garment designs.
- [x] Implemented honest empty states for physical stockists (`data/stockists.yaml`).
- [x] Implemented explicit concept disclaimers on all conceptual garment and collection views.
- [x] Added legal privacy and terms pages in both Spanish and English.

---

## Phase 4: Deterministic QA & Verification Suite
**Status: Completed**

- [x] Developed `scripts/verify_concepts.py` checking 720+ internal links, image paths, anchors, and retired routes.
- [x] Developed `scripts/verify_review.py` for full regression testing of lookbook, social cards, and contact states.
- [x] Generated localized 1200 × 630 Open Graph share cards via `scripts/render_social_cards.py`.
- [x] Integrated automated verification into isolated temporary preview environments.
- [x] Configured GitNexus code intelligence knowledge graph and blast-radius tracking.

---

## Phase 5: Contributor Onboarding & Editorial Content (Current Focus)
**Status: In Progress**

- [ ] **P00 (Editorial Title):** Confirm final editorial section naming with local Buenos Aires contributors.
- [ ] **P01 (Contributor Identification):** Identify and engage initial authentic Buenos Aires artists/makers.
- [ ] **P02 (Artifact Documentation):** Document real source materials, studio tools, and graphic iterations.
- [ ] **P04 (Interviews):** Record and transcribe authentic 3-chapter interviews covering technique, choices, and discards.
- [ ] **P05 (Studio Photography):** Conduct authentic on-site photography of workshops, works in progress, and artisans.
- [ ] **P06 (Design Iteration Cards):** Produce before-and-after process cards highlighting real design decisions.
- [ ] **P08 (Community Gatherings):** Establish confirmed protocols for workshop visits once dates and spaces are secured.

---

## Phase 6: Garment Sampling & Prototyping
**Status: Upcoming**

- [ ] **P03 (Fabric & Fit Testing):** Physical sample runs of 240 g/m² cotton jersey tees.
- [ ] **P03 (Fleece Testing):** Physical sample runs of 400 g/m² heavy cotton fleece hoodies.
- [ ] **P03 (Headwear Testing):** Physical sample runs of unstructured six-panel twill caps.
- [ ] Record dimensional stability, post-wash shrinkage, collar retention, and ink longevity.
- [ ] **P07 (Hangtag & Care Study):** Finalize bilingual care labels, material composition, and provenance tags.
- [ ] Conduct studio photography of real physical garment samples worn seated and standing.

---

## Phase 7: Commercial Channels & Production Launch
**Status: Planned**

- [ ] Confirm and activate verified primary contact channel (`contact_verified = true` in `hugo.toml`).
- [ ] Formally partner with curated independent retail spaces in Buenos Aires and populate `data/stockists.yaml`.
- [ ] Validate and connect external form endpoint (`form_endpoint`) and subscriber newsletter (`newsletter_endpoint`).
- [ ] Execute formal production run based on sampling sign-offs.
- [ ] Transition concept notices to live commercial availability upon stock arrival.

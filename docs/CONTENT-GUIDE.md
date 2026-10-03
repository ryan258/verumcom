# VERUM — Content & Editorial Guide

Operational guidelines for editorial maintenance, bilingual voice standards, content models, and placeholder replacement.

---

## 1. Creative Line: «Ideas que se llevan / Ideas you can wear»

VERUM is an independent apparel project based in Buenos Aires exploring the intersection of graphic expression and everyday functional clothing.

The work is grounded in **four creative territories**:
1. **Capas / Layers:** What survives when another graphic layer is applied? Expressed in *Sobreimpreso* via offset planes, ecru negative spaces, and persistent typography.
2. **Marcas / Working Marks:** Which technical decision should remain visible? Expressed in *En Obra* via open angles, dimension lines, and construction guides.
3. **Uso / Everyday Use:** What happens when the garment moves? Familiar silhouettes (straight-cut tees, fleece hoodies, unstructured caps) designed for daily wear.
4. **Voces / Named Contributors:** Who gets to explain and approve the work? Authentic contributors whose distinct voice and craft are documented with explicit approval.

---

## 2. Voice & Tone Standards

### Spanish (Primary)
- **Regional Register:** Natural Buenos Aires Rioplatense with authentic voseo (*mirá*, *conocé*, *explorá*, *escribinos*).
- **No Manufactured Slang:** Do not sprinkle arbitrary lunfardo onto neutral sentences. Avoid stereotypical streetwear clichés ("lo más duro de la calle", "representando a las masas").
- **Concrete & Direct:** Focus on observable materials, ink, cuts, stitches, and decisions (*tinta*, *capa*, *costura*, *calce*, *papel*, *trazo*).
- **Honest Uncertainty:** State the current condition candidly. If a garment is a design study, declare it. Do not invent warehouse addresses, stock drops, or fake release dates.

### English (Secondary)
- **Faithful Intent:** Preserve the directness, technical focus, and disclosures of the Spanish original.
- **Natural Phrasing:** Translate thoughts into idiomatic English without clumsy literal transfers of Rioplatense idioms.
- **Uniform Disclosures:** Every disclosure of concept status, fictional collaboration, or sampling target must be mirrored identically in English.

---

## 3. Current Series: Fictional Artist Series 01–02

The current catalog is a **fictional design study** demonstrating structure, aesthetic direction, and layout:

| Collection | Contributor (Fictional) | Craft & Imagined Studio | Palette | Garments |
| --- | --- | --- | --- | --- |
| **Sobreimpreso** | Lucía Ferreyra | Printmaker · Chacarita | Red, Cobalt, Acid Yellow, Ecru | **Registro** (Tee), **Persistencia** (Hoodie), **Testigo** (Cap) |
| **En Obra** | Tomás Varela | Metalworker · La Paternal | Black, White, Graphite | **Cota** (Tee), **Trazo** (Hoodie), **Escuadra** (Cap) |

### Disclosure Integrity
- Both public collections and garment pages feature explicit disclaimer banners identifying the series as a concept study.
- Do not remove concept disclaimers until real, approved contributors and physical samples have replaced the fictional assets.

---

## 4. Content Models & Front Matter

### Garment (`content/{lang}/lookbook/{slug}/index.md`)
```toml
+++
title = "Registro"
translationKey = "registro"
draft = false
concept = true
category = "remera" # remera | buzo | accesorio
drop = "sobreimpreso" # sobreimpreso | en-obra
artist_name = "Lucía Ferreyra"
artist_url = "/veritas/lucia-ferreyra/"
description = "Remera ecru de corte recto en jersey de algodón pesado..."
hero = "front.jpg"
hero_alt = "Registro tee front view"
back = "back.jpg"
back_alt = "Registro tee back graphic"
detail = "detail.jpg"
detail_alt = "Detail of three-color offset print"
specs = [
  "Jersey de algodón 100% 240 g/m²",
  "Cuello cerrado de rib 1x1",
  "Estampa serigráfica al agua en tres colores",
  "Confección en Buenos Aires"
]
+++
```

### Collection / Drop (`content/{lang}/drops/{slug}/index.md`)
```toml
+++
title = "Sobreimpreso"
translationKey = "sobreimpreso"
draft = false
concept = true
artist = "Lucía Ferreyra"
artist_bio = "Grabadora y diseñadora gráfica..."
interview_url = "/veritas/lucia-ferreyra/"
description = "Serie gráfica basada en la memoria visual y la superposición..."
palette = ["#e13830", "#224dcd", "#e3ef28", "#f1f0e8"]
pieces = ["registro", "persistencia", "testigo"]
+++
```

### Editorial / En proceso (`content/{lang}/veritas/{slug}/index.md`)
```toml
+++
title = "Lo que queda debajo"
translationKey = "lucia-ferreyra"
draft = false
concept = true
artist_id = "lucia-ferreyra"
artist_name = "Lucía Ferreyra"
craft = "Grabado y serigrafía"
neighborhood = "Chacarita"
drop_ref = "sobreimpreso"
hero = "studio.jpg"
intro = "Conversación sobre capas de tinta, memoria barrial..."
closing = "La serie Sobreimpreso explora la persistencia del trazo..."

[[chapters]]
title = "Mirar de nuevo"
piece = "registro"
questions = [
  ["¿Por qué trabajar sobre afiches viejos?", "..."],
  ["¿Qué se descarta en el proceso?", "..."]
]
+++
```

---

## 5. The Placeholder Framework (P00–P08)

All pending real-world content is tracked using the structured inventory in `PLACEHOLDERS.md`:

- **P00:** Working title and editorial voice consensus.
- **P01:** Contributor approval and signed profile statements.
- **P02:** Real source inspirations and studio artifact documentation.
- **P03:** Physical garment sampling notes (shrinkage, fabric weight, real fit photos).
- **P04:** Real contributor interviews across the 3-chapter format.
- **P05:** Authentic workshop photography and process imagery.
- **P06:** Before-and-after design iteration cards.
- **P07:** Physical hangtag and label care copy.
- **P08:** Workshop gatherings or event protocol (only when dates and locations are physically confirmed).

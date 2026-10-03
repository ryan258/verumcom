# VERUM — Content & Editorial Guide

[Español (Argentina)](CONTENT-GUIDE.es-AR.md) · English

Operational guidelines for editorial maintenance, bilingual voice standards, content models, and placeholder replacement.

---

## 1. Creative Line: «Ideas que se llevan / Ideas you can wear»

VERUM is an independent apparel project based in Buenos Aires exploring the intersection of graphic expression and everyday functional clothing.

The work is grounded in **four creative territories**:
1. **Capas / Layers:** What survives when another graphic layer is applied? Expressed in *Sobreimpreso* via offset planes, ecru negative spaces, and persistent typography.
2. **Marcas / Working Marks:** Which technical decision should remain visible? Expressed in *En Obra* via open angles, dimension lines, and construction guides.
3. **Uso / Everyday Use:** What happens when the garment moves? Familiar silhouettes (straight-cut tees, fleece hoodies, unstructured caps) designed for daily wear.
4. **Voces / Named Contributors:** Who gets to explain and approve the work? The current voices are fictional; real contributors will need their own documented, approved accounts.

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
- Review the complete person/interview/image/garment unit before changing disclosures. Current templates retain concept notices even if `concept` changes; do not remove notices globally while fictional items remain.

---

## 4. Content Models & Front Matter

### Garment (`content/{lang}/lookbook/{slug}/index.md`)
Existing Spanish concept example. Field names and reference values must remain unchanged when translating prose. For a new page, use the archetype with `draft: true`.

```yaml
---
title: "Remera Registro"
translationKey: "piece-registro"
description: "Tres planos de color se desplazan entre sí. El crudo queda visible como el papel entre afiches: no todo el espacio necesita otra capa."
weight: 1
concept: true
artist_id: "lucia-ferreyra"
artist_name: "Lucía Ferreyra"
drop_ref: "drops/sobreimpreso"
story_ref: "veritas/lucia-ferreyra"
kind: "tee"
fabric: "Jersey de algodón, objetivo 240 g/m²"
color: "Crudo / Rojo / Cobalto / Amarillo ácido"
fit: "Corte recto amplio, hombro levemente caído."
technique: "Serigrafía de tres tintas en el frente; firma pequeña en la espalda."
art: "images/collaborations/registro.svg"
art_back: "images/collaborations/registro-back.svg"
---
```

### Collection / Drop (`content/{lang}/drops/{slug}/index.md`)
Existing concept example; collection pieces are found through `artist_id`, not a manually maintained `pieces` list.

```yaml
---
artist_id: "lucia-ferreyra"
artist_name: "Lucía Ferreyra"
neighborhood: "Chacarita"
craft: "Serigrafía"
tone: "print"
concept: true
hero: "images/collaborations/sobreimpreso-studio.png"
hero_alt: "Mesa de serigrafía imaginada con tintas rojas, azules y amarillas y papeles sobreimpresos."
weight: 1
title: "Sobreimpreso"
translationKey: "sobreimpreso"
drop_number: "01"
status: "concept"
theme: "La memoria deja capas."
bio: "Lucía es una artista ficticia que reúne fragmentos de carteles, letras dibujadas a mano y papeles de circulación cotidiana. En su taller imaginado de Chacarita, la memoria no se conserva intacta: se vuelve a imprimir."
palette: "Rojo cartel / Cobalto / Amarillo ácido"
story_ref: "veritas/lucia-ferreyra"
description: "Tres prendas para llevar lo que el barrio se resiste a olvidar. Rojo, cobalto y amarillo ácido; capas que dejan ver lo anterior."
---
```

### Editorial / En proceso (`content/{lang}/veritas/{slug}/index.md`)
Existing fictional example, showing the introduction and first chapter only. A complete interview requires three chapters and two question/answer pairs per chapter. Do not publish a partial example or attribute these invented answers to a real person.

```toml
+++
title = "Lo que queda debajo"
translationKey = "lucia-ferreyra"
description = "Una conversación imaginada con Lucía Ferreyra sobre carteles que desaparecen, errores de registro y las cosas que vale la pena volver a imprimir."
weight = 1
concept = true
artist_id = "lucia-ferreyra"
artist_name = "Lucía Ferreyra"
craft = "Serigrafía"
neighborhood = "Chacarita"
tone = "print"
drop_ref = "drops/sobreimpreso"
hero = "images/collaborations/sobreimpreso-studio.png"
hero_alt = "Mesa de serigrafía imaginada con tintas rojas, azules y amarillas y papeles sobreimpresos."
intro = "En este taller imaginado de Chacarita hay papeles que nadie ordena por fecha. Lucía Ferreyra los agrupa por lo que dejan ver: una letra partida, una dirección incompleta, el color que sobrevive debajo de otro. Sobreimpreso nace de esa forma de mirar. Esta entrevista ficticia sigue tres decisiones —superponer, insistir, reducir— hasta convertirlas en una remera, un buzo y una gorra."
closing = "Sobreimpreso no propone congelar Chacarita en una imagen. Propone una manera de trabajar: mirar lo que se acumula, elegir qué conservar y dejar visible el paso de una capa a otra. Las tres prendas comparten ese gesto, pero cada una lo dice a una escala distinta."

[[chapters]]
title = "01 / Volver a mirar"
piece = "registro"
questions = [
  ["¿Qué hace que guardes un pedazo de papel?",
   "Que tenga una huella de uso. No busco el cartel más lindo; me interesa el que tuvo una función y después quedó fuera de lugar. Una letra cortada por otra pegatina, una flecha que ya no lleva a ninguna parte. Cuando lo saco de ahí, no quiero fingir que me llevo todo el barrio. Me llevo una pregunta: ¿qué parte de esto seguiría teniendo sentido en otro soporte?"],
  ["¿Cómo evitás que la memoria se vuelva nostalgia decorativa?",
   "No reconstruyo una época perfecta. Trabajo con lo que falta y con lo que alguien tapó. Por eso no dibujé un cartel antiguo entero para Registro: quedaron tres planos y un desfase. El espacio crudo entre las tintas importa tanto como el color. Ahí entra quien usa la prenda; no tiene que conocer mi historia para encontrar la suya."],
]
+++
```

---

## 5. The Placeholder Framework (P00–P08)

All pending real-world content is tracked using the structured inventory in `PLACEHOLDERS.md`:

- **P00:** Editorial title and local reading.
- **P01:** Team and founder story: approved names, roles and factual history.
- **P02:** Collection and collaboration: source, transformation and garment consequences.
- **P03:** Garment description and sample evidence, with targets distinguished from measured results.
- **P04:** Interview provenance, permission, three chapters and six answers.
- **P05:** Images, scene status, factual alt text and credits.
- **P06:** Short editorial piece or post; no invented progress or release date.
- **P07:** Card, hangtag or insert study; no unsupported composition or care instructions.
- **P08:** Gathering or visit, only with confirmed details and access information.

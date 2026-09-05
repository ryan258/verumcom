# VERUM — Guía de Carga y Edición de Contenido

Este documento explica cómo crear y modificar contenido en VERUM utilizando archivos Markdown y paquetes de página (*page bundles*).

---

## 1. Tono y Voz de Marca (Guía para Quien Escriba)

VERUM habla desde el asfalto de Buenos Aires para un público de 20 a 30 años metido en el streetwear pesado, la música urbana (trap, RKT), el diseño gráfico brutalista y el arte callejero.

- **Español Rioplatense / Porteño estricto**: Usar siempre el **voseo** (*vos*, *mirá*, *rescatá*, *calzate*, *escribinos*). Prohibido el uso de *tú* o giros neutros corporativos.
- **Lunfardo y vocabulario de taller**: Palabras naturales al nicho (*pilcha*, *corte*, *posta*, *facha*, *frisa*, *pesado*, *berreta* —VERUM combate lo berreta—, *galpón*, *asfalto*, *barrio*).
- **Oraciones cortas y directas**: La marca se llama "Verdad". Cualquier adjetivo publicitario falso o marketing inflado destruye la identidad.
- **Títulos de 2 a 6 palabras**: Los templates tipográficos están calibrados para titulares pesados y breves.
- **Descripciones de prendas**: 2 a 3 oraciones como máximo. El peso técnico (gramaje, corte, remaches) habla por sí solo.

---

## 2. Modelos de Contenido y Arquetipos

### 2.1. Prenda del Lookbook (`lookbook`)

Cada prenda se gestiona como un **paquete de página** (*page bundle*) que contiene su archivo `index.md` y sus fotografías adentro:

```text
content/es/lookbook/nombre-de-la-prenda/
├── index.md
├── 01-front.jpg
├── 02-back.jpg
└── 03-detail.jpg
```

#### Campos del Front Matter:

```yaml
---
title: "Campera Verdad"                      # Nombre visible de la prenda (2-4 palabras)
date: 2026-03-01                             # Fecha de publicación
drop: "drop-01"                              # Identificador del drop al que pertenece (drop-01, drop-02)
categories: ["outerwear"]                    # Categoría: outerwear | tees | bottoms | accessories
sizes: ["S", "M", "L", "XL", "XXL"]         # Lista de talles confeccionados
fabric: "Frisa Pesada 420 GSM"               # Composición textil y gramaje técnico
color: "Negro Carbón / Cyan Glitch"          # Variante cromática de la prenda
featured: true                               # true para destacarse en la grilla principal del home y lookbook
gallery_order: ["01-front.jpg", "02-back.jpg", "03-detail.jpg"] # Orden secuencial de fotos
stockists: ["barracas-studio", "san-telmo-shop"] # IDs de locales donde conseguirla
translationKey: "campera-verdad"             # Clave idéntica para vincular la versión en inglés
draft: false                                 # false para publicar inmediatamente
---

Corte bomber boxy con frisa pesada de algodón peinado. Estampa en espalda serigrafiada a mano en Barracas con tintas al agua y detalles en cyan glitch. Cierre metálico industrial YKK y puños de morley reforzados.
```

---

### 2.2. Lanzamientos (`drops`)

Ubicación: `content/es/drops/drop-XX-nombre/index.md`

```yaml
---
title: "Drop 01 — Lo Real"                  # Título completo del drop
drop_number: "01"                            # Número correlativo (01, 02, etc.)
date: 2026-03-15                             # Fecha del lanzamiento
status: "released"                           # released (en la calle) | upcoming (en confección) | archived (agotado)
hero: "hero.jpg"                             # Imagen de portada en proporción 16:9
statement: "Primera tirada de indumentaria pesada fabricada sin concesiones en CABA."
translationKey: "drop-01"                    # Clave de traducción para inglés
draft: false
---

Texto conceptual sobre la tanda, el concepto de diseño y la producción en talleres.
```

> **Comportamiento del estado `upcoming`**: Cuando el status es `upcoming`, la página del drop oculta automáticamente el listado de prendas y despliega una caja de suscripción por correo electrónico para avisar a los usuarios antes de la salida al público.

---

### 2.3. Crónica Editorial (`veritas`)

Ubicación: `content/es/veritas/nombre-de-la-historia/index.md`

```yaml
---
title: "Tinta Viva sobre Chapa en La Boca"  # Título de la crónica
date: 2026-04-02                             # Fecha de publicación
author: "Joaquín Benítez"                    # Redactor de la crónica
artist_name: "Nico 'Fasolo' Ramos"          # Nombre o apodo del artista entrevistado
neighborhood: "La Boca"                      # Barrio de Buenos Aires donde se realizó la crónica
hero: "hero.jpg"                             # Fotografía principal en proporción 3:2
summary: "Crónica de taller: pintura al látex, aerosol y resistencia visual sobre el asfalto porteño."
translationKey: "veritas-01"                 # Clave de traducción
draft: false
---

Cuerpo del artículo en formato Markdown. Se pueden utilizar citas destacadas con `>` para resaltar frases textuales del artista.
```

---

### 2.4. Puntos de Venta (`data/stockists.yaml`)

Los locales no son páginas Markdown sino un archivo de datos estructurado en `data/stockists.yaml`:

```yaml
- id: "barracas-studio"
  name: "Taller 420 Barracas"
  city: "Buenos Aires"
  neighborhood: "Barracas"
  address: "Av. Patricios 1420"
  hours: "Jue a Sáb 14:00 – 20:00"
  maps_url: "https://maps.google.com/?q=Av.+Patricios+1420+Buenos+Aires"
  instagram: "@taller420.ba"
  description: "Espacio de producción serigráfica y showroom abierto los fines de semana."
```

---

## 3. Flujo de Traducción al Inglés

1. Cada archivo creado en `content/es/...` debe tener su correspondiente contraparte en `content/en/...`.
2. Ambos archivos **deben compartir el mismo `translationKey`** en su front matter.
3. Las URLs en inglés están traducidas (`/en/lookbook/`, `/en/manifesto/`, `/en/drops/`, `/en/stockists/`, `/en/contact/`).
4. Si un artículo aún no cuenta con traducción al inglés, simplemente no se crea el archivo en `content/en/`: el sitio ocultará limpiamente el botón de cambio de idioma en esa página en lugar de generar un enlace roto o un error 404.

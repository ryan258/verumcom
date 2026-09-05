# VERUM — Registro Técnico de Imágenes y Activos de Fondo

> **Especificación de producción para sustitución de imágenes y texturas de fondo.**  
> Este documento detalla cada activo visual, imagen de fondo, retrato editorial y plano de producto necesario para el sitio, con sus dimensiones exactas, relaciones de aspecto, estética de encuadre y rutas de archivo en el repositorio.

---

## 1. Activos Visuales y Fondos del Home (Alineados al Mockup)

| Sección del Home | Identificador del Activo | Ruta en el Repositorio | Proporción / Resolución | Dirección de Arte y Composición |
|---|---|---|---|---|
| **01. Hero Principal** | **Fondo Urbano CABA** | `static/images/hero-bg.jpg` | `16:9`<br>`1920 x 1080 px` | Fotografía analógica blanco y negro de edificios antiguos de Buenos Aires con grano marcado y afiche tipo pegatina callejera (*"BUENOS AIRES SIEMPRE RESISTE"*). |
| **01. Hero Principal** | **Modelo VERUM Espalda** | `static/images/hero-model.png` *(o integrado en hero-bg)* | `4:5` o recorte transparente | Modelo porteño joven con capucha puesta y campera oversize negra con estampa stencil blanca de VERUM en la espalda, mirando hacia arriba por sobre el hombro. |
| **01. Hero Principal** | **Tag Callejero Corona** | `static/images/tag-corona.svg` | Vectorial / SVG | Grafiti a mano alzada en aerosol blanco/cyan: *"MISMA CIUDAD OTRA VERDAD 👑"*. |
| **02. Drop Spotlight** | **Portada Drop 01/03** | `content/es/drops/drop-01-lo-real/hero.jpg`<br>`content/en/drops/drop-01-lo-real/hero.jpg` | `16:9`<br>`1920 x 1080 px`<br>*(mín. 1280x720)* | Plano medio de modelo con remera oversize negra estampada en entorno de arquitectura brutalista de hormigón crudo. Tag en aerosol magenta: *"ARTE TAMBIÉN ES RESISTENCIA 👑"*. |
| **03. Destacados 01** | **Caos Hoodie (Dorso)** | `content/es/lookbook/buzo-canguro-asfalto/01-front.jpg`<br>`content/en/lookbook/buzo-canguro-asfalto/01-front.jpg` | `4:5`<br>`1200 x 1500 px` | Vista trasera de buzo con capucha oversize negro de 460g con serigrafía gráfica central en espalda en locación callejera con flash crudo. |
| **03. Destacados 02** | **Verdad Tee (Dorso)** | `content/es/lookbook/remera-hormigon-raw/01-front.jpg`<br>`content/en/lookbook/remera-hormigon-raw/01-front.jpg` | `4:5`<br>`1200 x 1500 px` | Vista trasera de remera boxy fit blanca/cruda de 280g con estampa de retrato desgastado en serigrafía negra táctil. |
| **03. Destacados 03** | **Territorio Cargo** | `content/es/lookbook/pantalon-cargo-palermo/01-front.jpg`<br>`content/en/lookbook/pantalon-cargo-palermo/01-front.jpg` | `4:5`<br>`1200 x 1500 px` | Detalle en plano cerrado de bolsillo lateral fuelle en pantalón cargo negro de tela ripstop técnica con etiqueta tejida y costuras reforzadas. |
| **04. Veritas Spread** | **Retrato Artista (Izquierda)** | `content/es/veritas/01-tinta-viva-la-boca/hero.jpg`<br>`content/en/veritas/01-tinta-viva-la-boca/hero.jpg` | `4:5`<br>`1000 x 1250 px` | Retrato de perfil en blanco y negro de artista callejera con iluminación dramática de contraluz, intervenido con chorreado o cruz en aerosol magenta neón (`#FF0090`). |
| **04. Veritas Spread** | **Edificio y Pegatina (Derecha)** | `static/images/veritas-street-wall.jpg` | `4:3`<br>`1200 x 900 px` | Fachada de edificio de departamentos de Buenos Aires con pasacalles o pegatina tipográfica: *"LA BELLEZA TAMBIÉN ES POLÍTICA 👑"*. |
| **05. Newsletter** | **Mirada en Sombra** | `static/images/newsletter-eye.jpg` | `16:9` o libre<br>`1000 x 600 px` | Primer plano cerrado en blanco y negro de ojos mirando intensamente desde la penumbra, con grano 35mm y frase stencil: *"LOS REALES TAMBIÉN SE SUSCRIBEN"*. |

---

## 2. Texturas Globales y Elementos Vectoriales

| Activo | Ruta en Repositorio | Formato / Dimensiones | Uso en el Sistema |
|---|---|---|---|
| **Logotipo Stencil con Goteo** | `static/images/logo.svg`<br>`assets/images/logo.svg` | SVG vectorial (`520 x 140` viewBox) | Wordmark principal con goteo de tinta en letras R, U, M y desfase cromático cyan (`#00F0FF`) y magenta (`#FF0090`). |
| **Microtrama de Grano / Ruido** | `static/images/noise.png` | PNG 8-bit con alfa (`100 x 100 px`) | Trama sutil repetible sobre fondo `--ink` para dar acabado táctil y romper la perfección digital. |
| **Grano de Papel de Diario** | `static/images/paper-grain.png` *(opcional)* | PNG transparente (`200 x 200 px`) | Textura para secciones claras (`--paper`) en Manifiesto y Veritas. |

---

## 3. Catálogo de Prendas del Lookbook (12 Paquetes Completos)

Cada prenda se almacena como un **page bundle** en `content/es/lookbook/{slug}/` y `content/en/lookbook/{slug}/`.  
Requiere 3 tomas estandarizadas en relación de aspecto **`4:5`** (mínimo `800 x 1000 px`, recomendado `1200 x 1500 px`):

- **`01-front.jpg`**: Vista frontal completa (modelo de pie o prenda colgada en percha de taller).
- **`02-back.jpg`**: Vista trasera completa (corte, espalda, estampa o capucha).
- **`03-detail.jpg`**: Plano detalle de tejido (textura de frisa 420g, ripstop, cierres YKK, remaches o bordado).

| Prenda | Categoría | Drop | Especificación de las Fotos |
|---|---|---|---|
| `campera-verdad` | Outerwear | Drop 01 | Bomber negra pesada con estampa trasera en cyan glitch y cierres metálicos plateados. |
| `buzo-canguro-asfalto` | Outerwear | Drop 01 | Hoodie gris hormigón con capucha doble estructurada y remaches de acero en bolsillo. |
| `remera-hormigon-raw` | Tees | Drop 01 | Remera boxy fit blanca cruda con cuello cerrado y serigrafía táctil en relieve. |
| `pantalon-cargo-palermo` | Bottoms | Drop 01 | Cargo militar ripstop negro con 6 bolsillos y lazos de ajuste en tobillos. |
| `remera-grafiti-boca` | Tees | Drop 01 | Remera negra lavada a la piedra con desgaste intencional y stencil tipográfico porteño. |
| `campera-rompeviento-sur` | Outerwear | Drop 01 | Rompevientos técnico impermeable con vivos magenta ocultos y capucha de tormenta. |
| `buzo-cuello-redondo-barracas` | Outerwear | Drop 01 | Crewneck negro de frisa esmerilada pesada con microbordado en puño izquierdo. |
| `pantalon-jogger-pesado` | Bottoms | Drop 01 | Jogger holgado de algodón de 420g con cordón plano de algodón y puños sueltos. |
| `remera-subte-d` | Tees | Drop 01 | Remera gris cemento con tipografía brutalista y horarios de tren impresos en nuca. |
| `gorra-stencil-cinco-paneles` | Accessories | Drop 01 | Gorra camper 5 paneles en gabardina 8oz negra con parche bordado y hebilla metálica. |
| `chaleco-tactico-mataderos` | Outerwear | Drop 01 | Chaleco utilitario multibolsillo en cordura 500D impermeable con argollas en D. |
| `piluso-ripstop-noche` | Accessories | Drop 01 | Bucket hat impermeable en tela ripstop con ala descendente y cinta porta-accesorios. |

---

## 4. Portadas de Lanzamientos (`drops`)

Relación de aspecto fija: **`16:9`** (recomendado `1920 x 1080 px`, mínimo `1280 x 720 px`).

| Drop | Estado | Ubicación del Archivo | Descripción de la Fotografía |
|---|---|---|---|
| **Drop 01 — Lo Real** | En la calle *(Released)* | `content/es/drops/drop-01-lo-real/hero.jpg`<br>`content/en/drops/drop-01-lo-real/hero.jpg` | Foto nocturna grupal en calle adoquinada de Barracas con modelos vistiendo la colección completa. Iluminación directa de farola y flash. |
| **Drop 02 — Ruido** | En confección *(Upcoming)* | `content/es/drops/drop-02-ruido/hero.jpg`<br>`content/en/drops/drop-02-ruido/hero.jpg` | Foto de taller textil en Villa Crespo con rollos de tela ripstop reflectiva, mesas de corte y máquina overlock en movimiento. |

---

## 5. Crónicas Editoriales (`veritas`)

Relación de aspecto fija: **`3:2`** (recomendado `1800 x 1200 px`, mínimo `1200 x 800 px`).

| Historia Editorial | Barrio | Ubicación del Archivo | Descripción del Retrato Documental |
|---|---|---|---|
| **01. Tinta Viva** | La Boca | `content/es/veritas/01-tinta-viva-la-boca/hero.jpg`<br>`content/en/veritas/01-tinta-viva-la-boca/hero.jpg` | Retrato de Nico 'Fasolo' frente a un mural de chapa oxidada en La Boca sosteniendo rodillo de albañil con pintura goteando. |
| **02. Serigrafía Nocturna** | Barracas | `content/es/veritas/02-serigrafia-nocturna-barracas/hero.jpg`<br>`content/en/veritas/02-serigrafia-nocturna-barracas/hero.jpg` | Mesa de impresión de 8 metros en galpón de Barracas a las 3 AM con maniguetas, marcos serigráficos y buzos secándose al aire. |
| **03. Tipografía Brutalista** | Retiro | `content/es/veritas/03-tipografia-subte-c/hero.jpg`<br>`content/en/veritas/03-tipografia-subte-c/hero.jpg` | Koba pegando afiches tipográficos impresos en tipos de madera sobre las columnas de hormigón en los andenes de Retiro. |
| **04. Hierro y Cemento** | San Telmo | `content/es/veritas/04-hierro-y-cemento-san-telmo/hero.jpg`<br>`content/en/veritas/04-hierro-y-cemento-san-telmo/hero.jpg` | Cacho Varela en su sótano de herrería forjando remaches de acero macizo con soplete y chispas de soldadura. |

---

## 6. Procedimiento de Sustitución en Producción

El sitio está diseñado para que la sustitución sea un **reemplazo directo de archivos**:

1. **Exportación**: Generar los archivos finales en formato **JPG** o **WebP** comprimidos al 85% de calidad, respetando las proporciones y nombres de archivo arriba indicados.
2. **Reemplazo Directo**: Copiar los archivos finales sobre las rutas correspondientes en `content/es/...`, `content/en/...` y `static/images/`.
3. **Regeneración**:
   ```bash
   hugo --minify --gc
   ```
   Hugo procesará automáticamente los activos, generará las variantes optimizadas y actualizará los hashes sin necesidad de editar ninguna plantilla HTML ni archivo Markdown.

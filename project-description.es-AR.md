# VERUM — Descripción del proyecto web

**Español (Argentina)** · [English](project-description.md) · [Índice de documentación](docs/README.es-AR.md)

**Versión:** 1.0, traducción del brief original.
**Preparado para:** desarrollo web con Hugo.
**Estado:** antecedente histórico. Para la implementación actual, consultá [README.md](README.md), [CONTENT.md](CONTENT.md) y [PLACEHOLDERS.md](PLACEHOLDERS.md). Las afirmaciones sobre mercado, tendencias, proveedores y requisitos que siguen pertenecen al brief original; no son investigación verificada ni nuevas decisiones. Los nombres, modelos de contenido, cantidades y criterios históricos se conservan para que la traducción sea fiel. No copies sus ejemplos como configuración vigente.
**Plataforma:** Hugo, edición Extended.

## 1. Resumen

Construir un sitio bilingüe, en español e inglés, para **VERUM**, una marca argentina de indumentaria urbana. El sitio presenta un lookbook y la historia de la marca: no tiene carrito, checkout ni pagos.

El alcance original comprende unas **ocho plantillas de página** y un tipo de contenido repetible, las prendas del lookbook. Desarrollar un tema Hugo propio, sin usar uno prediseñado.

**En el punto de partida no había recursos de marca.** Construir con contenido provisional. El logo, las fotos y los textos reales se reemplazarían después. Diseñar cada componente para que ese cambio requiera reemplazar archivos, sin reconstruir el sitio.

## 2. Alcance

### Incluido

- Tema Hugo propio, desde cero.
- Sitio bilingüe: español predeterminado e inglés.
- Lookbook y páginas individuales de prendas.
- Historia de marca y manifiesto.
- Sección editorial «Veritas», con historias de artistas.
- Archivo de drops pasados y futuros, solo informativo.
- Puntos de venta y dónde encontrar la marca.
- Página de contacto con formulario.
- Suscripción por correo.
- Diseño adaptable hasta 360 px de ancho.
- Flujo de despliegue a un alojamiento estático.

### Excluido

Estas funciones quedaban fuera del desarrollo original y, de agregarse, requerían un presupuesto aparte:

- Comercio electrónico: carrito, checkout, inventario y pagos.
- Cuentas e inicio de sesión.
- Panel de administración CMS; ver sección 9.
- Comentarios en el blog.
- Aplicaciones móviles nativas.
- Fotografía, redacción y traducción.
- Diseño de logo o producción de recursos de marca.

### Por qué no hay tienda

Hugo genera archivos HTML por adelantado. No aporta servidor de aplicación, base de datos ni manejo de sesiones. Vender requeriría integrar un servicio como Shopify Buy Buttons, Snipcart o Ecwid, con costos, otro proveedor, consideraciones de PCI y nuevos puntos de falla.

La decisión del brief era **dejar todo eso fuera de v1**. Si VERUM vendía, lo haría por mensajes de Instagram, WhatsApp o un local físico; el sitio enlazaría esos canales.

## 3. Contexto de marca

Quien desarrolla no necesita ser estratega de marca, pero debe leer este contexto para orientar las decisiones visuales.

### El nombre

El brief presenta **VERUM** como el latín de «verdadero» y lo ubica en un movimiento de autenticidad, entendido como reacción a la perfección visual generada por IA. Plantea que el mercado argentino se vuelca hacia *lo real*: crudo, artesanal e imperfecto. Esas son hipótesis del documento original, no conclusiones de investigación.

### El logo

Se propuso una marca escrita de alto contraste, con estética de **grafiti y esténcil**, y tres rasgos:

1. **Chorreado:** la tinta cae de la R, la U y la M y sugiere pintura todavía húmeda, con energía de producción propia de CABA.
2. **Aberración cromática:** desplazamientos cian y magenta generan separación RGB. El brief relaciona el grafiti analógico con una estética «Cyber-Pampa» que describe como tendencia de la generación Z argentina.
3. **Imperfección táctil:** trazos de grosor desigual y bordes ásperos, con apariencia de trabajo humano.

### Posicionamiento

El brief usa *Lujo de Barrio* para describir la escena de indumentaria urbana y propone este lugar para VERUM:

| Elemento | Consecuencia para el sitio |
| --- | --- |
| **Nombre** | Textos directos y breves, sin relleno publicitario. |
| **Actitud** | Agresiva y artística, más cercana al activismo urbano que al skate. |
| **Vínculo cultural** | Referencias al trap argentino y al RKT; ruido visual y alto contraste. |

### Lo central

El recurso principal propuesto es la **fricción visual**: una imagen difícil de ignorar, con contraste, tipografía pesada, recortes cerrados y saltos de escala. Un portfolio genérico y demasiado prolijo no cumpliría ese objetivo.

La fricción debe estar en lo visual. La navegación tiene que dejar claro dónde está la persona y cómo vuelve. Libertad en la dirección de arte, orden en la estructura.

## 4. Dirección de diseño

### Paleta

El brief pide estas propiedades CSS. Son los valores históricos, no la paleta vigente:

| Variable | Hex | Uso |
| --- | --- | --- |
| `--ink` | `#0A0A0A` | Fondo principal, casi negro. |
| `--bone` | `#F2F0EB` | Texto claro sobre oscuro, blanco cálido. |
| `--cyan` | `#00F0FF` | Acento de glitch, estados al pasar el puntero y foco. |
| `--magenta` | `#FF0090` | Acento de glitch y destacado secundario. |
| `--concrete` | `#6E6E6E` | Texto atenuado, bordes y metadatos. |
| `--paper` | `#E8E4DC` | Fondo claro alternativo. |

El planteo original era oscuro por defecto, con secciones claras para cambiar el ritmo, por ejemplo el manifiesto o una doble página editorial.

El documento advertía que la combinación `--magenta` sobre `--ink` debía comprobarse antes de publicar. Si no alcanza el contraste necesario en texto pequeño, limitarla a títulos grandes, bordes y decoración sin información.

### Tipografía

Tres funciones, sin agregar una cuarta:

1. **Títulos:** sans pesada y condensada, espaciado cerrado, gran tamaño y posibles recortes o salidas del borde.
2. **Cuerpo:** sans neutra y legible, con soporte de caracteres latinos extendidos, tildes y ñ.
3. **Monoespaciada:** datos, números de drop, fechas, talles y rótulos, con apariencia de ficha técnica.

Confirmar una licencia web válida antes de publicar una fuente. Alojar las fuentes en el propio sitio, sin cargarlas desde Google Fonts CDN. El brief vincula esta decisión con velocidad y menos solicitudes a terceros. Usar `font-display: swap` y precargar solo la fuente de títulos.

El logo propuesto era lettering propio en SVG, no una fuente web. No recrearlo con una tipografía.

### Efecto glitch

Recurso distintivo, aplicado de manera limitada:

- Separación RGB con CSS en títulos, estados de interacción y logo.
- `text-shadow` cian/magenta o pseudo-elementos duplicados con `mix-blend-mode`.
- Animación breve y sutil; evitar parpadeo continuo.
- Desactivar el efecto por completo dentro de `@media (prefers-reduced-motion: reduce)` cuando corresponda.

No aplicarlo al cuerpo de lectura, no animar más de un elemento continuamente, no usar JavaScript si CSS alcanza ni vincular el efecto al desplazamiento en móviles. El brief fija un máximo de tres destellos por segundo por accesibilidad.

### Composición

- **Asimetría:** desplazar elementos del eje; evitar simetría de apariencia corporativa.
- **Saltos de escala:** un título de 120 px junto a metadatos de 12 px.
- **Bordes duros:** sin esquinas redondeadas, sombras suaves ni degradados, salvo desplazamientos cromáticos.
- **Textura:** grano o trama sutil con una imagen repetible pequeña, por ejemplo 100 × 100 px con baja opacidad; no un recurso pesado a pantalla completa.
- **Espacio negro:** dejar aire para la tipografía; densidad en una zona y vacío al lado.

## 5. Mapa del sitio

```text
/                          Inicio
/manifiesto/               Historia de marca y manifiesto
/lookbook/                 Índice de prendas
/lookbook/{slug}/          Prenda individual
/drops/                    Archivo de drops
/drops/{slug}/             Drop individual
/veritas/                  Índice editorial
/veritas/{slug}/           Historia individual
/puntos-de-venta/          Dónde encontrar la marca
/contacto/                 Contacto
/legal/privacidad/         Privacidad
/legal/terminos/           Términos
/404.html                  Error 404 propio
```

Las versiones inglesas se ubican bajo `/en/`, con slugs traducidos; ver sección 7.

### Notas por página

**Inicio:** apertura a pantalla completa con logo, una frase de manifiesto y una acción al lookbook. Después, último drop, tres prendas destacadas, última historia de Veritas y suscripción. Hasta cinco secciones.

**Manifiesto:** página larga, tipográfica, con pocas imágenes y fondo claro. Debe leerse como una declaración, no como una página institucional.

**Lookbook:** grilla irregular o tipo masonry, con filtros por drop y categoría. Prever páginas de taxonomía como alternativa sin JavaScript.

**Prenda:** galería, nombre, drop, materiales, gramaje, notas de talle y relato breve. Módulo destacado de dónde comprar, con enlaces a locales o canales externos; sin botón de agregar al carrito.

**Drops:** cada lanzamiento tiene fecha, nombre, número, imagen principal, declaración y listado de prendas. Un estado próximo puede ocultar el listado y mostrar fecha y suscripción.

**Veritas:** artículos largos con imágenes grandes para la campaña de historias de artistas. La lectura clara tiene prioridad sobre la fricción visual.

**Puntos de venta:** locales con dirección, barrio y horarios, agrupados por ciudad y barrio. Sin mapa incrustado en v1; usar enlaces externos a mapas para evitar peso y seguimiento adicional.

**Contacto:** formulario de nombre, correo, asunto y mensaje. El procesamiento se define en la sección 8.

## 6. Modelo de contenido

Cada tipo necesita un arquetipo en `archetypes/`. Usar nombres de campo claros y documentarlos en `CONTENT.md`. Los siguientes son **ejemplos históricos**, no el esquema actual.

### Prenda del lookbook

Un *page bundle*: carpeta por prenda, con imágenes junto al contenido para facilitar el procesamiento de Hugo.

```text
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

Historia breve de la pieza. Dos o tres frases como máximo.
```

### Drop

```yaml
---
title: "Drop 01 — Lo Real"
drop_number: "01"
date: 2026-03-15
status: "released"    # released | upcoming | archived
hero: "hero.jpg"
statement: "Declaración del drop en una frase."
draft: false
---
```

### Historia de Veritas

```yaml
---
title: "Historia del artista"
date: 2026-04-02
author: "Nombre"
artist_name: "Nombre del artista"
neighborhood: "La Boca"
hero: "hero.jpg"
summary: "Una o dos frases para la tarjeta del índice y la meta descripción."
draft: false
---
```

### Punto de venta

Guardar como datos estructurados, no como páginas de contenido. Ejemplo histórico para `data/stockists.yaml`:

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

### Taxonomías

El brief pedía exactamente dos y consultar antes de agregar otras:

- `drops`: lanzamiento al que pertenece la prenda.
- `categories`: tipo de prenda, como `outerwear`, `tees`, `headwear` y `accessories`.

## 7. Configuración bilingüe

Español como idioma predeterminado; inglés como secundario.

### URLs

- Español: `verum.com/lookbook/`.
- Inglés: `verum.com/en/lookbook/`.

Usar `defaultContentLanguageInSubdir = false` para mantener el español en la raíz.

### Esquema de configuración histórico

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

### Vincular traducciones

Se pueden vincular por nombre de archivo o por `translationKey`; preferir `translationKey` porque resiste cambios de slug. Traducir los slugs cuando corresponda: `/en/manifesto/`, no `/en/manifiesto/`; `lookbook` se conserva en ambos idiomas. Todas las cadenas de interfaz van en `i18n/es.toml` e `i18n/en.toml`, sin texto visible fijo en las plantillas.

### Traducciones faltantes

El brief anticipa páginas en español sin traducción inglesa. Definir y documentar el comportamiento: si falta una página, no enlazarla; ocultar o desactivar la opción de idioma para esa página en lugar de llevar a un 404. No servir español silenciosamente bajo una URL `/en/`, porque los buscadores la interpretarían como inglesa.

### SEO

Generar `hreflang` para ambos idiomas y `x-default` hacia español. Cada idioma tiene su `sitemap.xml`, incluido en un índice de sitemaps.

## 8. Requisitos técnicos

### Tecnologías

- Hugo **Extended**, obligatorio para el planteo original de compilación SCSS y procesamiento de imágenes.
- Fijar la versión exacta en el repositorio y el despliegue; una actualización menor puede afectar plantillas.
- Sin React, Vue ni otro framework JavaScript; sin pasos de compilación fuera de Hugo Pipes.
- JavaScript nativo solo cuando CSS no alcance, previsiblemente para menú móvil y mejora de filtros.
- El sitio debe poder usarse sin JavaScript. Se acepta una experiencia reducida, no una rota.

### Recursos

- Hugo Pipes para CSS y JS: huella de contenido, minificación y agrupación.
- Procesamiento de imágenes de Hugo para variantes adaptables, WebP con alternativa JPEG, `srcset` y `sizes` correctos.
- Carga diferida debajo de la primera pantalla; imagen principal con carga inmediata y precarga.
- Todas las imágenes llevan `alt`; las decorativas, `alt=""`.

### Presupuesto de rendimiento

El brief plantea el costo de datos móviles y la variabilidad de redes argentinas como restricciones de diseño.

| Métrica | Objetivo original |
| --- | --- |
| Largest Contentful Paint en 4G | Menos de 2,5 s |
| Peso total de inicio | Menos de 1,2 MB |
| Peso de página de contenido | Menos de 900 KB |
| JavaScript total | Menos de 30 KB |
| Fuentes web | Hasta 3 archivos, solo WOFF2 |
| Lighthouse Performance | 90 o más en móvil |

Si el diseño no permite alcanzar esos valores, señalarlo antes de implementarlo. No entregar una página pesada y explicarlo después.

### Accesibilidad

Objetivo original: WCAG 2.1 AA.

- Navegación completa por teclado y foco visible con `--cyan`.
- Respetar `prefers-reduced-motion` en todas las animaciones.
- No superar tres destellos por segundo.
- HTML semántico: `<nav>`, `<main>`, `<article>` y jerarquía real de títulos.
- Etiquetas reales en formularios; el texto provisional de un campo no reemplaza su etiqueta.
- Prueba con lector de pantalla antes de la entrega.

### Formulario de contacto

Hugo no procesa envíos por sí solo. Elegir y documentar un servicio como Formspree, Netlify Forms o Basin. Son dependencias externas con límites y posibles fallas. El brief pide al menos un campo señuelo antispam y evitar CAPTCHA si es posible por su carga de uso y peso.

### Suscripción por correo

Requiere un proveedor, por ejemplo Mailchimp, Buttondown o ConvertKit. El formulario envía al endpoint del proveedor. Adaptar su apariencia a la marca en lugar de usar un formulario incrustado genérico.

### Analítica

El brief propone una opción liviana orientada a privacidad, como Plausible, Umami o GoatCounter, o no usar ninguna. Pedía una decisión explícita antes de agregar Google Analytics y vinculaba esa decisión con consentimiento y un posible banner. Esa formulación legal pertenece al documento histórico; no establece obligaciones actuales verificadas.

## 9. Edición de contenido

Decisión abierta en el brief: necesaria antes del lanzamiento, no antes de empezar a construir.

El contenido Hugo vive en Markdown dentro de Git. Se puede editar directamente o incorporar una capa CMS. Tres alternativas originales:

1. **Solo Git:** sin costo ni dependencia adicional; requiere comodidad con Markdown y Git.
2. **CMS basado en Git:** Decap CMS, Sveltia CMS o similar, con panel `/admin/`. El brief lo describe como gratuito, aunque agrega dependencia y complejidad bilingüe.
3. **CMS alojado:** Cloud Canvas, Front Matter en VS Code o un CMS desacoplado; más acabado, costo y configuración.

La recomendación original era construir para la primera opción y permitir la segunda más adelante: front matter consistente y sin lógica de plantilla que dependa de archivos editados de manera especial.

## 10. Despliegue

El brief proponía:

- Alojamiento estático con compilación desde Git, como Netlify, Cloudflare Pages o Vercel; describía sus planes gratuitos como suficientes.
- Cloudflare Pages como recomendación para público argentino, basada en cobertura y límites que no se revalidan en esta traducción.
- Versión Hugo fijada en el entorno de compilación.
- Vistas previas de pull requests.
- Dominio propio, HTTPS, redirección HTTP → HTTPS y una dirección principal coherente entre `www` y raíz.
- Encabezados CSP, `X-Content-Type-Options` y `Referrer-Policy`.

## 11. Estrategia de contenido provisional

El punto de partida original no contaba con recursos reales. Se pedía facilitar su reemplazo:

- **Logo:** SVG provisional de esténcil con proporciones correctas, reemplazable en `assets/logo.svg`. No incrustar el trazado en plantillas.
- **Fotografía:** imágenes consistentes con proporciones documentadas en `CONTENT.md`: 4:5 para prendas, 16:9 para portadas de drops y 3:2 para editorial.
- **Texto:** ejemplos que suenen naturales en español, sin lorem ipsum. Permiten detectar problemas de tildes, ñ y longitud de líneas.
- **Volumen:** al menos doce prendas, dos drops y cuatro historias de Veritas para probar grillas y paginación. Estas son cantidades históricas; el sitio actual tiene seis prendas y dos entrevistas.

Entregar `PLACEHOLDERS.md` con cada recurso provisional, ubicación, dimensiones necesarias y reemplazo real esperado.

## 12. Riesgos y puntos de falla

Evaluación original, conservada como antecedente:

| Riesgo | Probabilidad | Impacto | Mitigación propuesta |
| --- | --- | --- | --- |
| Traducciones inglesas pendientes | Alta | Sitio incompleto en un idioma | Definir alternativa en sección 7; español completo e inglés parcial, ocultando páginas sin traducir. |
| Recursos reales que no llegan o llegan con formato incorrecto | Alta | Lanzamiento demorado | Fijar proporciones desde el inicio y entregar una ficha a fotografía. |
| Glitch que afecta rendimiento móvil | Media | No cumplir el presupuesto | CSS, pocos elementos y prueba temprana en Android de gama media real. |
| Falta de licencia de fuentes | Media | Exposición legal o cambio de último momento | Confirmación escrita de licencias y tipografía alternativa. |
| Falla o cambio de plan del proveedor de formularios/correo | Media | Contacto que deja de funcionar sin avisar | Copia a una segunda dirección y prueba mensual, según el plan original. |
| Diferencias de versión Hugo | Baja | Falla de despliegue | Fijar versión en repositorio y alojamiento. |
| Diseño difícil de navegar | Media | Abandono del sitio | Probar navegación con tres personas nuevas durante los esquemas iniciales. |
| Fallas de accesibilidad por la estética glitch | Media | Exclusión de personas y posibles consecuencias legales | Diseñar contraste y movimiento reducido desde el comienzo. |

El brief no presenta estos riesgos como motivos para no construir, sino como temas que pueden consumir el calendario si no se resuelven temprano.

## 13. Criterios originales de finalización

La entrega original se consideraba completa cuando:

1. Todas las páginas de la sección 5 existieran en español e inglés.
2. Cada tipo de la sección 6 tuviera arquetipo y plantilla funcionales.
3. `hreflang`, sitemaps y URLs canónicas fueran correctos en ambos idiomas.
4. Se cumpliera el presupuesto de rendimiento en una prueba móvil con red limitada.
5. Lighthouse Accessibility alcanzara 95 o más, con problemas restantes documentados y justificados.
6. La navegación fuera completa por teclado con foco visible.
7. Todas las animaciones respetaran `prefers-reduced-motion`.
8. El sitio se pudiera usar sin JavaScript.
9. El formulario entregara mensajes a una casilla real, comprobado de extremo a extremo.
10. La suscripción llegara a la lista del proveedor, también comprobada.
11. Existiera un 404 propio en ambos idiomas.
12. Hubiera pruebas en Chrome, Safari y Firefox actuales, Safari de iOS y un Android de gama media.
13. Hubiera pruebas a 360, 768, 1024 y 1440 px.
14. Estuvieran completos README.md, CONTENT.md y PLACEHOLDERS.md.
15. El despliegue funcionara desde un clon limpio.

Son criterios históricos, no un registro de pruebas aprobadas ni una certificación de accesibilidad.

## 14. Entregables

1. Repositorio Git con fuentes e historial.
2. Tema Hugo propio en `themes/verum/` o en los layouts del proyecto, con la decisión documentada.
3. Despliegue funcional en una URL de prueba.
4. README.md con ejecución local, compilación y despliegue.
5. CONTENT.md con carga de prenda, drop e historia y explicación de cada campo.
6. PLACEHOLDERS.md con recursos provisionales y especificaciones de reemplazo.
7. Recorrido breve de entrega, de unos quince minutos; se admitía video grabado.

## 15. Decisiones abiertas

El brief indica que no bloqueaban el inicio, pero sí el lanzamiento:

1. Dominio, todavía sin elegir.
2. Edición por Git o con CMS.
3. Proveedor de formularios.
4. Proveedor de correo.
5. Analítica o ausencia de ella.
6. Tipografías, sujetas a licencia.
7. Lista real de puntos de venta, si existía.
8. Responsable de redactar privacidad y términos.

## 16. Notas para quien redacta

No eran responsabilidad del desarrollo, pero condicionaban las plantillas:

- Español primero y **argentino**: usá *vos*, no *tú*. Evitá un registro neutro que se sienta ajeno al público.
- Frases cortas. El nombre se asocia con «verdadero»; exagerar en el texto contradice esa intención.
- Títulos de dos a seis palabras; las plantillas originales se pensaban para ese largo.
- Descripciones de prendas de dos o tres frases.
- El inglés es traducción, no una reescritura, pero debe sonar natural. El brief preveía revisión humana.

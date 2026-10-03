# VERUM — Sitio de marca y lookbook

**Español (Argentina)** · [Índice de documentación](docs/README.es-AR.md)

Sitio bilingüe de una marca de indumentaria independiente en desarrollo en Buenos Aires. Español en `/`, inglés en `/en/`. Hugo Extended, SCSS y JavaScript mínimo; sin carrito ni pagos.

La serie actual usa contenido provisional: dos artistas ficticios, seis prendas conceptuales y dos entrevistas imaginadas. Es una demostración de la dirección y de la estructura editorial, no un anuncio de colaboraciones reales ni de productos disponibles. La dirección actual es «Ideas que se llevan / Ideas you can wear». Las biografías, imágenes y especificaciones reales se incorporan cuando estén aprobadas.

## Desarrollo

Requiere Hugo Extended >= 0.163.0; CI fija 0.166.0. Python >= 3.11 para los verificadores.

```sh
hugo server -D
```

## Experiencia actual

- **Inicio:** ilustraciones de prendas de la serie actual, las seis piezas, colecciones y En proceso. Ya no usa la campera de campaña ajena al catálogo.
- **Lookbook:** acceso directo a seis prendas, sin filtros ni paso obligatorio por un artista.
- **Drops:** dos colecciones con contexto, paleta, prendas e historia.
- **Prenda:** vistas frontal/posterior, detalles propuestos, entrevista relacionada y piezas compañeras.
- **En proceso / In process:** conversaciones ficticias, relacionadas con decisiones de diseño.
- **Manifiesto:** principios y sección `#equipo`, preparada para la historia y los perfiles reales.
- **Contacto:** un canal principal confirmado o un estado pendiente explícito. No se publican horarios de taller provisionales.

## Universo y carga guiada

La marca sigue siendo **VERUM**. El nombre editorial de trabajo es **En proceso** en español e **In process** en inglés. Se conservan las rutas `/veritas/` y `/en/veritas/`, sus bundles, relaciones y anclas para no romper enlaces. Los rótulos compartidos usan `editorial_name`; el título y la descripción del índice están en cada `_index.md`. Un cambio de URL posterior requiere una migración completa con aliases.

El universo se organiza en capas, marcas de trabajo, uso cotidiano y voces con nombre propio. El manifiesto muestra esa dirección; las consignas de edición quedan en las fuentes. Para completar contenido por voz, alcanza una entrada como «P01: …» o «P03 Registro: …»; el editor usa PLACEHOLDERS.md para convertirla en campos y conservar los pendientes. No hay que completar todo en una sesión.

Los arquetipos de colección, prenda y entrevista incluyen instrucciones y permanecen en `draft: true`, `concept: true`. Las plantillas actuales conservan los avisos de ficción aunque se cambie ese último campo. No reemplazar una persona ficticia por una real sin actualizar el conjunto relacionado y revisar cómo se presenta.

## Canal principal

En `hugo.toml`, `primary_contact` admite `instagram`, `email` o `whatsapp`. `contact_verified = false` mantiene los destinos provisionales fuera de los enlaces públicos. Tras confirmar el canal seleccionado y su destino, ponerlo en `true` activa el mismo enlace en inicio, lookbook, colecciones, prendas, contacto y footer. El valor confirma solamente el canal seleccionado; al cambiarlo, volver a confirmar su destino.

`form_endpoint` y `newsletter_endpoint` son integraciones independientes. El contacto ignora un endpoint vacío o que contenga `placeholder`; la newsletter solo se muestra con endpoint configurado. Confirmar la cuenta y actualizar privacidad antes de activarlos. No hacen falta para el flujo principal.

El dominio, el correo y el usuario social de ejemplo requieren confirmación de los propietarios. `baseURL` determina canonical, sitemap y URLs para compartir. GitHub Pages lo reemplaza con la URL de Pages durante su build.

## Verificación enfocada — ejecutar localmente

Para comprobar la versión actual con los verificadores enfocados del sitio:

```sh
cd /Users/ryanjohnson/Projects/verumcom
VERUM_PREVIEW_DIR="$(mktemp -d /tmp/verum-review.XXXXXX)"
hugo --destination "$VERUM_PREVIEW_DIR" --cacheDir /tmp/verum-hugo-cache --baseURL http://127.0.0.1:8766/ --noBuildLock &&
python3 scripts/verify_review.py "$VERUM_PREVIEW_DIR"
```

`verify_review.py` ejecuta primero `verify_concepts.py`: relaciones bilingües, enlaces, imágenes, capítulos, aclaraciones de ficción y ausencia de rutas retiradas. Luego comprueba la separación Lookbook/Drops, las seis tarjetas, las imágenes sociales de cada prenda, la ruta al equipo y el estado del canal principal.

Para revisar ese mismo resultado en el navegador, en la misma terminal:

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory "$VERUM_PREVIEW_DIR"
```

Abrir `http://127.0.0.1:8766/`. Revisar a 1440, 390 y 320 px: portada → prenda → entrevista; Lookbook → Drops; ES/EN; apertura y cierre del menú con Escape; contacto pendiente o el canal confirmado. Comprobar que los controles y el texto no se cortan, y que el foco se ve al usar Tab. Estas pruebas no establecen conformidad WCAG ni validan entrega de mensajes.

## Documentación y arquitectura

**[Toda la documentación en español argentino](docs/README.es-AR.md)**. Las versiones en inglés se conservan y cada par tiene enlaces de idioma.

- [`docs/ARCHITECTURE.es-AR.md`](./docs/ARCHITECTURE.es-AR.md): Arquitectura estática, jerarquía de plantillas, partials, procesamiento de imágenes y SCSS.
- [`docs/CONTENT-GUIDE.es-AR.md`](./docs/CONTENT-GUIDE.es-AR.md): Guía editorial, los cuatro territorios, estándares de voz y modelos de contenido.
- [`docs/VERIFICATION.es-AR.md`](./docs/VERIFICATION.es-AR.md): Controles enfocados, alcance de los scripts y revisión de accesibilidad.
- [`ROADMAP.es-AR.md`](./ROADMAP.es-AR.md): Hitos del proyecto, fases completadas, prioridades activas y próximas etapas.
- [`CONTENT.md`](./CONTENT.md): Campos y pasos de carga editorial.
- [`PLACEHOLDERS.md`](./PLACEHOLDERS.md): Inventario y briefs P00–P08; consignas, extensión, ejemplos y qué hacer cuando faltan datos.
- [`CREATIVE-DIRECTION.es-AR.md`](./CREATIVE-DIRECTION.es-AR.md): Universo, voz, gramática visual, aplicaciones, decisión de nombre editorial y dos colecciones.
- [`docs/ARCHETYPES.es-AR.md`](./docs/ARCHETYPES.es-AR.md): Consignas de arquetipos de colección, prenda y entrevista.
- [`docs/AGENT-INSTRUCTIONS.es-AR.md`](./docs/AGENT-INSTRUCTIONS.es-AR.md): Traducción de consulta para agentes y reglas de GitNexus.
- [`project-description.es-AR.md`](./project-description.es-AR.md): Brief original, conservado como antecedente histórico.

## Archivos principales

- `layouts/index.html`, `layouts/lookbook/`, `layouts/drops/`: recorrido de prendas y colecciones.
- `layouts/partials/contact-channel.html`, `follow-project.html`: resolución y presentación del canal principal.
- `layouts/partials/brand-story.html`: historia y perfiles aprobados del equipo.
- `assets/scss/_collaborations.scss`: colecciones, portada, cuadrícula y acciones.
- `assets/js/main.js`: menú progresivo; los enlaces siguen disponibles sin JavaScript.
- `assets/images/social/`: seis tarjetas PNG de 1200 × 630; Hugo publica JPG con metadata localizada.

## Publicación

El workflow existente `.github/workflows/gh-pages.yml` compila y publica en GitHub Pages al recibir un push a `main` o una ejecución manual. No ejecutar esas acciones sin autorización de Ryan. Esta revisión no publicó ni modificó la configuración de despliegue.

Para otros hosts estáticos: `hugo --minify`, salida `public`, Hugo Extended 0.166.0. Usar un destino limpio: el contenido retirado puede quedar en un `public/` viejo.

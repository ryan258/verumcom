# VERUM — Verificación y controles de calidad

**Español (Argentina)** · [English](VERIFICATION.md) · [Índice](README.es-AR.md)

Controles deterministas, scripts y revisión de accesibilidad, con alcance explícito.

## 1. Criterio de calidad

Usá verificaciones enfocadas en lo que cambió. Los scripts inspeccionan HTML generado: enlaces, atributos de imagen, anclas, rutas y estados de configuración. No bloquean automáticamente un commit o un despliegue: el workflow actual de GitHub Pages compila y publica sin ejecutarlos. Seguí las instrucciones del repositorio sobre autorización y controles previos a un commit.

La inspección visual complementa esos controles; ninguna de las dos reemplaza por sí sola una evaluación completa.

## 2. Scripts

Los dos verificadores están en `scripts/`, requieren Python `>= 3.11` y usan la biblioteca estándar: `html.parser`, `urllib.parse`, `pathlib`, `tomllib`, entre otros módulos. No necesitan paquetes de terceros.

### 2.1 `scripts/verify_concepts.py`

- **Pares bilingües:** controla 20 elementos localizados de colecciones, prendas y entrevistas, sus claves de traducción y campos relacionados. No es una auditoría de traducción de todo el sitio.
- **Enlaces internos:** recorre 28 rutas seleccionadas; el registro del 3 de octubre dio 720 enlaces. La cantidad puede cambiar con el contenido.
- **Anclas:** comprueba que fragmentos enlazados, como `#equipo` o `#registro`, existan en el destino.
- **Imágenes:** revisa presencia de `alt`, `width` y `height` en las páginas controladas. No evalúa calidad del texto alternativo ni mide saltos visuales.
- **Archivos:** comprueba que existan las imágenes locales referenciadas.
- **Rutas retiradas:** compara la salida con las fuentes actuales para detectar faltantes o restos de ejemplos viejos.
- **Ficción:** comprueba el aviso conceptual en las páginas seleccionadas.

### 2.2 `scripts/verify_review.py`

- Ejecuta primero `verify_concepts.py`.
- Verifica que Inicio y Lookbook presenten prendas directamente, en ambos idiomas.
- Controla los seis slugs: `registro`, `persistencia`, `testigo`, `cota`, `trazo`, `escuadra`.
- Comprueba seis URLs JPEG distintas que contengan `/images/social/{slug}`, archivos emitidos, texto alternativo de metadatos y coincidencia con Twitter. No mide dimensiones de imagen.
- Revisa el estado del canal principal según `contact_verified`.
- Comprueba la ruta a `#equipo` en el manifiesto.

### 2.3 `scripts/render_social_cards.py`

Es una herramienta de generación, no un test. Produce las seis tarjetas de 1200 × 630 en `assets/images/social/`. Requiere ImageMagick (`magick`) y una fuente adecuada; consultá [PLACEHOLDERS.md](../PLACEHOLDERS.md). Hugo usa los archivos existentes durante una compilación normal.

## 3. Ejecutar los controles

Desde la raíz del proyecto, usá un destino temporal limpio:

```bash
# 1. Crear un destino aislado
PREVIEW_DIR="$(mktemp -d /tmp/verum-qa.XXXXXX)"

# 2. Compilar el sitio; ejecutar el verificador solo si la compilación sale bien
hugo --destination "$PREVIEW_DIR" \
     --cacheDir /tmp/verum-qa-cache \
     --baseURL http://127.0.0.1:8766/ \
     --noBuildLock &&
python3 scripts/verify_review.py "$PREVIEW_DIR"

# Conservar PREVIEW_DIR para la revisión en navegador.
```

Resultado registrado el 3 de octubre, no una ejecución nueva de esta traducción:

```text
PASS: 28 rendered pages; 20 localized content items; 720 local links; bilingual relationships, interview anchors, images, disclosures and retired-route cleanup verified.
PASS: garment-first home/lookbook, collection navigation, founder route, six share images, and contact state in both languages.
```

Los mensajes de salida se conservan en inglés para compararlos con el script. No borres el directorio antes de revisarlo en el navegador.

## 4. Revisión visual y accesibilidad

En la misma terminal y con la misma variable:

```bash
python3 -m http.server 8766 --bind 127.0.0.1 --directory "$PREVIEW_DIR"
```

Abrí `http://127.0.0.1:8766/` y elegí las comprobaciones pertinentes al cambio:

| Área | Referencia | Procedimiento |
| --- | --- | --- |
| Adaptación del diseño | 320, 390, 768 y 1440 px | Revisá saltos de línea, desborde horizontal y texto legible. |
| Salto al contenido | `#main-content` | Presioná Tab al cargar; comprobá que el enlace aparezca y lleve el foco al contenido. |
| Menú móvil | `<button class="site-header__toggle">` | Abrí el menú, revisá `aria-expanded`, cerrá con Escape y verificá el retorno del foco. |
| Foco visible | `:focus-visible` | Recorré botones y enlaces con teclado y revisá que el indicador se distinga. |
| Alto contraste | `forced-colors: active` | Emulá colores forzados y comprobá bordes, foco y botones. |
| Idiomas | `es` ↔ `en` | Cambiá de idioma en prendas y colecciones y verificá la correspondencia. |

Estos controles no prueban conformidad WCAG, aceptación con lector de pantalla, cobertura de dispositivos reales ni entrega a una casilla externa. Un endpoint configurado no equivale a una entrega comprobada.

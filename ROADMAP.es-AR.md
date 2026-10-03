# VERUM — Hoja de ruta e hitos de implementación

**Español (Argentina)** · [English](ROADMAP.md) · [Índice de documentación](docs/README.es-AR.md)

Este documento registra la implementación y los posibles próximos pasos. Los elementos completados describen el sitio conceptual local y controles registrados; no acreditan una operación activa, accesibilidad completa ni preparación para producir. Las etapas futuras requieren decisiones de los propietarios. No afirman que hayan comenzado búsquedas de colaboradores, acuerdos con locales ni fabricación.

## Vista general de las etapas

```text
[1. Arquitectura] → [2. Identidad visual] → [3. Serie 01–02] → [4. Verificación]
                                                                  ↓
[7. Lanzamiento] ← [6. Muestras de prendas] ← [5. Datos de participantes pendientes]
```

## Etapa 1 — Base y arquitectura bilingüe

**Estado: implementación completada.**

- [x] Estructura Hugo Extended `>= 0.163.0` con compilaciones deterministas.
- [x] Árboles de contenido en español (`/`) e inglés (`/en/`).
- [x] Correspondencia de idiomas mediante `translationKey`.
- [x] Semántica HTML5 con regiones y enlace para saltar al contenido.
- [x] Sin frameworks JavaScript externos en ejecución; mejora progresiva del menú con JavaScript nativo.
- [x] Fuentes y recursos estáticos alojados en el sitio. Los encabezados del alojamiento, incluida CSP, siguen siendo una comprobación de despliegue; el repositorio no acredita una CSP activa.

## Etapa 2 — Identidad visual y composición

**Estado: implementación completada.**

- [x] Anton para títulos en WOFF2 y Space Mono para metadatos.
- [x] Paleta editorial: tinta `#0A0A0A`, papel cálido `#F1F0E8` y acento ácido `#DFFF00`.
- [x] Plantillas compartidas en `layouts/_default/` y `layouts/partials/`.
- [x] Procesamiento de imágenes con Hugo Pipes, WebP y dimensiones explícitas para reservar espacio.
- [x] Símbolos de interfaz nativos en lugar de bibliotecas externas de íconos.
- [x] Revisiones de diseño a anchos entre 320 y 1440 px y estilos de colores forzados. La aceptación completa de accesibilidad es una instancia separada.

## Etapa 3 — Serie conceptual de artistas 01–02

**Estado: implementación completada.**

- [x] Dirección «Ideas que se llevan / Ideas you can wear», documentada en [CREATIVE-DIRECTION.es-AR.md](CREATIVE-DIRECTION.es-AR.md).
- [x] Dos colaboraciones ficticias desarrolladas: **Sobreimpreso**, Lucía Ferreyra, serigrafía y taller imaginado en Chacarita, paleta rojo/cobalto/amarillo ácido; **En Obra**, Tomás Varela, trabajo en metal y taller imaginado en La Paternal, paleta negro/blanco/grafito.
- [x] Seis prendas: Registro y Cota, remeras; Persistencia y Trazo, buzos; Testigo y Escuadra, gorras.
- [x] Nombre editorial de trabajo **En proceso / In process**, con rutas anteriores conservadas.
- [x] Entrevistas de tres capítulos enlazadas con las prendas.
- [x] Estado vacío explícito para puntos de venta en `data/stockists.yaml`.
- [x] Aclaraciones conceptuales en prendas y colecciones.
- [x] Páginas de privacidad y términos en español e inglés.

## Etapa 4 — Controles deterministas y verificación

**Estado: herramientas implementadas y controles puntuales registrados.**

- [x] `scripts/verify_concepts.py`: enlaces internos —720 en la ejecución registrada el 3 de octubre—, imágenes, anclas y rutas retiradas.
- [x] `scripts/verify_review.py`: regresiones enfocadas en lookbook, imágenes sociales y estados de contacto.
- [x] Generación de tarjetas de 1200 × 630 mediante `scripts/render_social_cards.py`.
- [x] Verificación en destinos temporales aislados.
- [x] Índice GitNexus y consultas de impacto, con sus límites documentados.
- [x] Suite completa de documentación en español argentino (`.es-AR.md`) y en inglés con enlaces bidireccionales de consulta.

Estos hitos no significan que todo cambio posterior esté validado ni que los verificadores corran automáticamente en CI. Consultá [VERIFICATION.es-AR.md](docs/VERIFICATION.es-AR.md).

## Etapa 5 — Participantes y contenido editorial

**Estado: insumos pendientes; foco editorial actual.**

- [ ] **P00 — Nombre editorial:** confirmar el título final con una lectura local de Buenos Aires.
- [ ] **P01 — Equipo e historia fundadora:** aportar nombres públicos, roles y una historia real aprobada.
- [ ] **P02 — Colección y colaboración:** aportar presentación aprobada, observación de partida, decisión de diseño y consecuencias en las prendas.
- [ ] **P04 — Entrevistas:** registrar y transcribir conversaciones reales de tres capítulos sobre técnica, decisiones y descartes.
- [ ] **P05 — Fotografías:** documentar talleres, trabajos en proceso y participantes reales, con permiso.
- [ ] **P06 — Tarjetas de proceso:** mostrar cambios de diseño reales mediante detalles anteriores y posteriores.
- [ ] **P08 — Encuentros:** definir las condiciones de visita solo cuando haya fechas y espacios confirmados.

Las consignas completas están en [PLACEHOLDERS.md](PLACEHOLDERS.md).

## Etapa 6 — Muestras y prototipos

**Estado: próxima etapa, pendiente de decisión y realización.**

- [ ] **P03 — Remeras:** evaluar muestras con objetivo de jersey de algodón de 240 g/m².
- [ ] **P03 — Buzos:** evaluar muestras con objetivo de frisa de algodón de 400 g/m².
- [ ] **P03 — Gorras:** evaluar muestras de sarga, copa blanda y seis paneles.
- [ ] Registrar estabilidad dimensional, encogimiento tras lavado, comportamiento del cuello y de la estampa.
- [ ] **P07 — Material impreso:** desarrollar etiqueta colgante o inserto; composición, cuidados y origen requieren datos reales.
- [ ] Fotografiar muestras reales en uso sentado y de pie según corresponda.

## Etapa 7 — Canales y eventual lanzamiento de producción

**Estado: previsto en la hoja de ruta, sujeto a decisiones de los propietarios.**

- [ ] Confirmar y activar el canal principal: `contact_verified = true` en `hugo.toml` solo después de confirmar el destino elegido.
- [ ] Acordar puntos de venta reales y cargar `data/stockists.yaml`.
- [ ] Validar, si se decide usarlos, `form_endpoint` y `newsletter_endpoint`.
- [ ] Realizar una producción basada en muestras aprobadas.
- [ ] Revisar persona, entrevista, evidencia de prenda, imágenes y avisos de plantilla en conjunto antes de presentar una colaboración real. Tener stock no reemplaza los demás elementos ficticios.

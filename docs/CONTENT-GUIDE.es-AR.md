# VERUM — Guía de contenido y edición

**Español (Argentina)** · [English](CONTENT-GUIDE.md) · [Índice](README.es-AR.md)

Mantenimiento editorial, voz bilingüe, modelos de contenido y reemplazo de ejemplos.

## 1. Línea creativa: «Ideas que se llevan / Ideas you can wear»

VERUM es un proyecto de indumentaria independiente en Buenos Aires que explora la relación entre expresión gráfica y ropa de uso cotidiano.

Cuatro territorios:

1. **Capas:** qué sobrevive al agregar una capa gráfica. Sobreimpreso lo expresa con planos desfasados, espacios crudos y tipografía que persiste.
2. **Marcas de trabajo:** qué decisión técnica queda visible. En Obra usa ángulos abiertos, cotas y líneas auxiliares.
3. **Uso cotidiano:** qué pasa al moverse. Siluetas conocidas: remeras rectas, buzos de frisa y gorras blandas, con uso aún por comprobar en muestras.
4. **Voces con nombre propio:** quién explica y aprueba el trabajo. Las voces actuales son ficticias; los colaboradores reales necesitarán relatos propios documentados y aprobados.

## 2. Voz y tono

### Español, idioma principal

- **Registro regional:** rioplatense natural de Buenos Aires, con voseo: mirá, conocé, explorá, escribinos.
- **Sin jerga inventada:** no agregues lunfardo porque sí ni clichés como «lo más duro de la calle» o «representando a las masas».
- **Concreto y directo:** describí materiales, tintas, cortes, costuras y decisiones observables: tinta, capa, costura, calce, papel, trazo.
- **Incertidumbre explícita:** identificá el estado actual. Si es un estudio de diseño, decilo. No inventes direcciones, stock ni lanzamientos.

### Inglés, idioma secundario

- **Intención fiel:** conservá claridad, enfoque técnico y aclaraciones del español.
- **Frases naturales:** traducí el sentido sin trasladar literalmente modismos rioplatenses.
- **Mismo grado de certeza:** toda aclaración de concepto, ficción u objetivo de muestra debe conservarse en inglés.

## 3. Serie actual: artistas ficticios 01–02

El catálogo es un **estudio de diseño ficticio** que muestra estructura, estética y composición.

| Colección | Participante ficticio | Oficio y taller imaginado | Paleta | Prendas |
| --- | --- | --- | --- | --- |
| Sobreimpreso | Lucía Ferreyra | Serigrafía · Chacarita | Rojo, cobalto, amarillo ácido, crudo | Registro, remera; Persistencia, buzo; Testigo, gorra |
| En Obra | Tomás Varela | Trabajo en metal · La Paternal | Negro, blanco, grafito | Cota, remera; Trazo, buzo; Escuadra, gorra |

### Integridad de las aclaraciones

Las colecciones y prendas públicas identifican su estado conceptual. Antes de cambiar ese encuadre, revisá la unidad completa: persona, entrevista, imágenes y prenda. Las plantillas mantienen los avisos aunque cambie `concept`; no los quites globalmente mientras haya piezas ficticias.

## 4. Modelos de contenido y front matter

Las claves técnicas, rutas e identificadores no se traducen. Para crear páginas nuevas, usá los arquetipos con `draft: true`. Los ejemplos siguientes corresponden al contenido conceptual actual; no acreditan una colaboración real.

### Prenda (`content/{lang}/lookbook/{slug}/index.md`)
Ejemplo conceptual actual en español. Conservá nombres de campo y referencias al traducir el texto. Para una página nueva, usá el arquetipo con `draft: true`.

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

### Colección / Drop (`content/{lang}/drops/{slug}/index.md`)
Ejemplo conceptual actual. Las prendas de la colección se buscan mediante `artist_id`, no mediante una lista manual `pieces`.

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
Ejemplo ficticio actual que muestra la introducción y solo el primer capítulo. Una entrevista completa necesita tres capítulos y dos pares de pregunta/respuesta por capítulo. No publiques el ejemplo incompleto ni atribuyas estas respuestas inventadas a una persona real.

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

## 5. Consignas de reemplazo P00–P08

La guía completa está en [PLACEHOLDERS.md](../PLACEHOLDERS.md):

- **P00:** nombre editorial y lectura local.
- **P01:** equipo e historia fundadora: nombres, roles y hechos aprobados.
- **P02:** colección y colaboración: fuente, transformación y consecuencia en cada prenda.
- **P03:** descripción y evidencia de muestra, distinguiendo objetivos de mediciones.
- **P04:** origen de la entrevista, permiso, tres capítulos y seis respuestas.
- **P05:** imágenes, estado de la escena, texto alternativo factual y créditos.
- **P06:** pieza editorial breve o publicación; sin avances ni fechas inventados.
- **P07:** tarjeta, etiqueta colgante o inserto; sin composición ni cuidados sin respaldo.
- **P08:** encuentro o visita, con datos confirmados e información de acceso.

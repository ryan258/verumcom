---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
author: "VERUM Redacción"
artist_name: "Artista Porteño"
neighborhood: "La Boca"
hero: "hero.jpg"
summary: "Crónica de taller: pintura al látex, aerosol y resistencia visual sobre el asfalto porteño."
translationKey: "{{ .File.ContentBaseName }}"
draft: false
---

Texto editorial sobre el artista, su técnica y su mirada sobre la ciudad.

---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: false
translationKey: "{{ .File.ContentBaseName }}"
---

# Segundo Cerebro para Claude Code

[English](README.en.md)

Una plantilla para que [Claude Code](https://claude.com/claude-code) funcione como el
**bibliotecario** de tu segundo cerebro. Vos tirás material crudo sin ordenar y Claude lo
convierte en una wiki enlazada, responde preguntas citando de dónde sale cada dato y te
dice qué información falta.

Son archivos Markdown comunes: andan con Obsidian, con cualquier editor o directo en la terminal.

## Cómo funciona

```
RAW/        → vos tirás lo que sea (notas, transcripciones de audios, PDFs, links)
   │  "procesá RAW"
   ▼
WIKI/       → Claude ordena: un .md por tema, con frontmatter y [[enlaces]]
   │  preguntas
   ▼
OUTPUTS/    → las respuestas que valen la pena quedan guardadas con fecha
changelog.md → registro de cada procesado
```

Las reglas viven en [`CLAUDE.md`](CLAUDE.md), que Claude Code lee solo al abrir la carpeta:

1. **Leer:** todo lo nuevo de `RAW/`. RAW nunca se edita ni se borra.
2. **Organizar:** cada dato va a una nota de `WIKI/` con su fuente. Lo que no está en RAW no se inventa.
3. **Responder:** primero el índice, después las notas y, si hace falta, el archivo original. Siempre citando.
4. **Guardar:** decisiones y planes van a `OUTPUTS/AAAA-MM-DD-titulo.md`.
5. **Mejorar:** después de cada procesado, Claude marca los 3 huecos más importantes del cerebro.

## Empezar

```bash
git clone https://github.com/bautipastore79-ai/segundo-cerebro-claude.git mi-cerebro
cd mi-cerebro
rm -f RAW/*.md WIKI/objetivos-2026.md WIKI/running.md OUTPUTS/*.md   # borra los ejemplos
claude
```

Después tirá cualquier cosa en `RAW/` y decile a Claude: **"procesá RAW"**.

## Qué trae

| Archivo | Para qué |
|---|---|
| `CLAUDE.md` | Las reglas del bibliotecario |
| `.claude/skills/procesar-raw/` | Skill: integra lo nuevo de RAW a la wiki, paso a paso |
| `.claude/skills/preguntar-al-cerebro/` | Skill: responde citando nota y archivo original |
| `scripts/chequear_wiki.py` | Revisa frontmatter, enlaces rotos, fuentes que no existen, notas fuera del índice y notas demasiado largas. Sin dependencias, sale con código 1 si hay problemas (sirve para CI) |
| `RAW/`, `WIKI/`, `OUTPUTS/` | Un ejemplo chico e inventado (objetivos del año + running) para ver el formato |

```bash
python3 scripts/chequear_wiki.py
```

## Privacidad

Tu segundo cerebro va a tener datos personales. **Usalo en un repo privado** (o sin git) y
no subas audios, cookies ni claves: el `.gitignore` ya bloquea los casos más comunes.

## Contribuir

Issues y PRs bienvenidos: nuevas skills (por ejemplo, para importar desde otras apps de notas),
mejoras al chequeador o traducciones de `CLAUDE.md`.

## Licencia

[MIT](LICENSE)

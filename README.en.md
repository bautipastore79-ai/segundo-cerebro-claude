# Second Brain for Claude Code

[Español](README.md)

A template that turns [Claude Code](https://claude.com/claude-code) into the **librarian** of
your second brain. You drop raw, unsorted material in a folder; Claude turns it into a linked
wiki, answers questions citing where every fact came from, and tells you what is missing.

Plain Markdown files: works with Obsidian, any editor, or straight from the terminal.

## How it works

```
RAW/        → you drop anything (notes, voice-memo transcripts, PDFs, links)
   │  "process RAW"
   ▼
WIKI/       → Claude organizes: one .md per topic, with frontmatter and [[links]]
   │  questions
   ▼
OUTPUTS/    → answers worth keeping are saved with a date
changelog.md → log of every processing run
```

The rules live in [`CLAUDE.md`](CLAUDE.md), which Claude Code loads automatically:

1. **Read** everything new in `RAW/`. RAW is never edited or deleted.
2. **Organize** every fact into a `WIKI/` note with its source. Nothing is invented.
3. **Answer** from the index, then the notes, then the original file when needed, always citing.
4. **Save** decisions and plans to `OUTPUTS/YYYY-MM-DD-title.md`.
5. **Improve:** after each run Claude lists the 3 biggest gaps in the brain.

The template ships in Spanish; Claude follows it in any language you write to it.

## Quick start

```bash
git clone https://github.com/bautipastore79-ai/segundo-cerebro-claude.git my-brain
cd my-brain
rm -f RAW/*.md WIKI/objetivos-2026.md WIKI/running.md OUTPUTS/*.md   # remove the examples
claude
```

Drop anything into `RAW/` and tell Claude: **"process RAW"**.

## What's inside

| File | Purpose |
|---|---|
| `CLAUDE.md` | The librarian's rules |
| `.claude/skills/procesar-raw/` | Skill: integrates new RAW material into the wiki |
| `.claude/skills/preguntar-al-cerebro/` | Skill: answers citing the note and the original file |
| `scripts/chequear_wiki.py` | Checks frontmatter, broken links, missing sources, notes missing from the index and overlong notes. No dependencies; exits 1 on problems (CI-friendly) |
| `RAW/`, `WIKI/`, `OUTPUTS/` | A small fictional example to show the format |

## Privacy

Your second brain will hold personal data. **Keep your own copy in a private repo** (or out of
git) and never commit audio, cookies or keys; the `.gitignore` covers the common cases.

## Contributing

Issues and PRs welcome: new skills (e.g. importers from other note apps), checker improvements,
or translations of `CLAUDE.md`.

## License

[MIT](LICENSE)

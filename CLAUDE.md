# Wikipedia for AI Learning — Schema

This is an LLM-maintained personal wiki on **AI learning research**: how AI systems learn, how research on AI learning is being automated, and the tools/methods/frontiers around that. You (the human) curate sources and ask questions. I (the LLM) read, summarize, integrate, cross-reference, and maintain everything in this directory.

This file is the schema. Read it before doing any work in this repo.

---

## The three layers

```
raw/    immutable sources       (you add, I read, never edit)
wiki/   markdown knowledge base  (I own end-to-end)
CLAUDE.md  this schema           (we co-evolve)
```

### `raw/`
Source documents — papers (PDF), articles (HTML/markdown clipped from the web via Obsidian Web Clipper), transcripts, notes, images. **Immutable.** I read from `raw/` but never modify, rename, or delete anything in it. Images go in `raw/assets/`. The contract: if it's in `raw/`, the human put it there and trusts me not to touch it.

### `wiki/`
The compounding artifact. Markdown pages organized into 5 categories:

- `wiki/core-concepts/` — foundational ideas (foundation models, automated discovery, RAG, transfer learning)
- `wiki/tools-platforms/` — software and APIs (aider, AIDE, Semantic Scholar, HuggingFace)
- `wiki/methodologies/` — research approaches and techniques (active learning, curriculum learning, evaluation, prompt engineering, world models)
- `wiki/frontier-topics/` — deep dives and synthesis pages (recursive self-improvement, predictive simulation learning, AI safety in research, cross-cutting connections)
- `wiki/research-sources/` — per-source summary pages (one page per ingested raw source) plus institution and paper-tracking pages

I own this directory entirely. I create new pages, rewrite old ones, update cross-references, fix contradictions. You read it (in Obsidian, ideally) and direct what I should do.

### `CLAUDE.md`
What you're reading. The conventions and workflows. We update this together as we figure out what works.

---

## Page conventions

### Frontmatter (required on every page)

```yaml
---
title: Predictive Simulation Learning
type: concept          # concept | entity | source-summary | comparison | overview | reference
category: frontier-topics
tags: [world-models, model-based-rl, simulation]
created: 2026-01-15
updated: 2026-04-09
sources: []            # paths to raw/ files this page integrates, e.g. ["raw/2603.19710v1.pdf"]
---
```

Page types:
- **concept** — an idea, method, or technique (most pages)
- **entity** — a system, model, paper, lab, or person with a name worth its own page
- **source-summary** — a one-to-one summary of a single raw source (lives in `wiki/research-sources/`)
- **comparison** — a structured comparison across multiple things (table-heavy)
- **overview** — a category landing page or a synthesis spanning many pages
- **reference** — a navigation hub or auto-generated index

Update `updated:` whenever you touch a page. Add new `sources:` entries on every ingest. Add new `tags:` opportunistically during quality passes — they're how Dataview and lint find related material.

### Body structure

Open with an `# H1` matching `title`. Then a one-paragraph lead in plain prose (this is what `index.md` shows). Then `## H2` sections in whatever order makes sense for the topic. Don't force a rigid template — let the topic shape the structure.

### Cross-links

Use **relative markdown paths**, never `[[wikilinks]]`:

```markdown
See [Aider](../tools-platforms/aider.md) for the editor integration.
This connects to [recursive self-improvement](../frontier-topics/recursive-self-improvement.md).
```

Relative paths work in Obsidian, in `qmd`, in `git diff`, and on GitHub. Wikilinks lock you in.

When linking to a concept that doesn't have a page yet, **still write the link** — these are red-link gaps. Lint surfaces them as candidates for new pages.

### Citations and footnotes

External citations (papers, articles you don't have a local copy of) use markdown footnotes:

```markdown
Hafner et al. demonstrated this in DreamerV3.[^3]

[^3]: Hafner, D. et al. (2025). "Mastering Diverse Control Tasks Through World Models". *Nature* 640, 647–653. [arxiv](https://arxiv.org/abs/2301.04104)
```

Internal citations (sources you actually have in `raw/`) go in the page's `sources:` frontmatter list **and** are linked inline:

```markdown
This is based on [Sakana 2026][raw-sakana].

[raw-sakana]: ../../raw/2603.19710v1.pdf
```

The rule: if I can read it, it's a `sources:` reference. If only the human can read it, it's a footnote.

---

## Index and log files

### `index.md` (content-oriented, root of repo)
A flat catalog of every wiki page, organized by category. Each entry: link + one-line summary. Always read this first when answering a query — it's the cheapest possible "search index".

**I update `index.md` on every ingest** (new pages added, summaries refreshed if a page's lead paragraph changed) and during lint (sorting, dedup, summary cleanup).

### `log.md` (chronological, root of repo)
Append-only record. Every operation gets one entry. Format:

```markdown
## [2026-04-09] ingest | Sakana AI Scientist v2 paper
- Source: raw/2603.19710v1.pdf
- New page: wiki/research-sources/sakana-ai-scientist-v2.md
- Updated: wiki/core-concepts/the-ai-scientist.md, wiki/frontier-topics/recursive-self-improvement.md
- Notes: claims a 4× speedup on idea-generation step; flagged tension with the older Lu et al. 2024 numbers
```

The leading `## [DATE] op | title` line means `grep "^## \[" log.md | tail -10` gives a quick recent-activity view.

Operations to log: `ingest`, `query`, `lint`, `restructure` (rare), and any one-off work I do at the human's request that touches multiple pages.

---

## Operation: Ingest

Triggered when the human says something like "ingest raw/foo.pdf" or drops a new file in `raw/` and asks me to process it.

**Steps:**

1. **Read the source.** Open the file in `raw/`. If it's a PDF, read the whole thing (or specific page ranges if it's huge — agree on scope first).
2. **Discuss key takeaways with the human.** Before writing anything, surface the 3–5 most important claims and ask which ones to emphasize, which connect to existing wiki pages, and whether there's anything to flag as contradicting existing content.
3. **Write a source-summary page** at `wiki/research-sources/<slug>.md` with `type: source-summary` and the raw path in `sources:`. This is the canonical record of what the source says.
4. **Identify affected pages.** Search `wiki/` for entities, concepts, and methods the source touches. For each affected page:
   - Add the new finding inline with a citation
   - Append the raw path to its `sources:` frontmatter (if not already there)
   - Bump `updated:`
   - Flag contradictions explicitly in the page text — don't silently overwrite
5. **Update `index.md`** — add the new source-summary entry, refresh summaries on any pages where the lead paragraph changed.
6. **Append a `log.md` entry** following the format above.

A typical ingest touches 5–15 wiki pages. That's fine — the whole point is that I do the bookkeeping.

**Before bulk-ingesting,** ask the human if they want one-at-a-time (default, more discussion) or batch mode (less supervision, good for backlog clearing).

---

## Operation: Query

Triggered by any question against the wiki: "what does the wiki say about X", "compare Y and Z", "what's the strongest evidence for W".

**Steps:**

1. **Read `index.md` first.** It's small and gives me a complete map. Pick the 3–8 pages that look relevant.
2. **Read those pages.** Follow cross-links if a page references something I need.
3. **Synthesize an answer with citations.** Every claim should point to either a wiki page (`wiki/x.md`), a footnote already on a wiki page, or a `raw/` file.
4. **Offer to file the answer back.** Good answers compound — a comparison table, a synthesis, a discovered connection. Ask: "Want me to file this as `wiki/<category>/<slug>.md`?" If yes, write it as a new page (`type: comparison` or `type: overview` typically), update `index.md`, log it.

For larger queries, the answer format can be a markdown page, a comparison table, a Marp slide deck, or a chart. Pick what fits.

**Don't** answer from memory if the wiki has the information — read the pages. Memory is unreliable; pages are ground truth.

---

## Operation: Lint

Periodic health check. Triggered by "lint the wiki" or done proactively after a big ingest session.

**Checks:**

1. **Contradictions.** Pages making incompatible claims about the same thing. Flag, don't silently resolve. Bring them to the human.
2. **Stale claims.** Pages where `updated:` is much older than newer sources on the same topic. Suggest a refresh.
3. **Orphan pages.** Pages with zero inbound links from other wiki pages. Either link them in or propose deletion.
4. **Red-link gaps.** Concepts referenced in cross-links that don't have a page yet. Surface them as candidates for new pages. **Seed list:** `archive/data/topic-wishlist.txt` has the historical wishlist from the old improvement loop — mine it for ideas.
5. **Missing cross-references.** Pages that mention a concept by name but don't link to it. Add the link.
6. **Frontmatter consistency.** Every page has the full frontmatter block. `tags:` populated where obvious. `category:` matches the directory. `updated:` is plausible.
7. **Index drift.** Every wiki page appears in `index.md`. No `index.md` entries point to deleted pages. Summaries match the current lead paragraph.

Lint produces a **report** (markdown, in chat or filed to `wiki/research-sources/lint-<date>.md`). It does **not** auto-fix structural issues — the human approves changes. It can auto-fix obvious frontmatter typos and stale `updated:` dates without asking.

**Never delete a wiki page during lint without explicit human confirmation.**

---

## Tooling

### Today: just markdown + this schema
Plain `.md` files, plain frontmatter, relative links, the `index.md` and `log.md` indices. No database. No embeddings. The LLM operates on the raw filesystem — the site builder below is optional and only exists for human browsing.

### Website: `scripts/build_site.py`
For browsing the wiki in a browser (not just Obsidian), there's a static site builder at `scripts/build_site.py`. It reads `wiki/<category>/*.md` (plus `index.md` at the repo root as the landing page), strips YAML frontmatter, converts markdown to HTML, and writes everything into `site/` at the repo root. `site/` is gitignored — it's build output, not source.

```bash
python3 scripts/build_site.py            # build once → site/index.html
python3 scripts/build_site.py --serve    # build + serve on http://localhost:4321
python3 scripts/build_site.py --clean    # delete site/
```

Light wrapper around the Python `markdown` package (extensions: tables, fenced_code, toc, nl2br, footnotes). Handles same-category relative links (`foo.md` → `foo.html`) and `index.md`-style `wiki/<cat>/<page>.md` links. No live reload, no search — regenerate after ingests. This replaces the old `archive/build.py`, which targeted the pre-2026-04-09 directory layout. `archive/` remains frozen for history.

### When the wiki grows: `qmd`
Once `wiki/` exceeds a few hundred pages, reading `index.md` linearly stops scaling. At that point, install [qmd](https://github.com/qmd) — a local hybrid BM25/vector search engine for markdown directories. It has both a CLI (shell out to it) and an MCP server (use as a native tool). Both work on relative-path markdown without modification.

To start using it: install, then add a section to this CLAUDE.md describing how to invoke it (e.g., "before reading pages for a query, run `qmd search <terms> wiki/`"). Until then, ignore.

### Optional: Dataview (Obsidian plugin)
Because every page has consistent YAML frontmatter, Dataview queries work out of the box in Obsidian. Examples:

````markdown
```dataview
TABLE updated, length(sources) AS "raw refs"
FROM "wiki"
WHERE type = "concept"
SORT updated DESC
LIMIT 10
```

```dataview
LIST FROM "wiki" WHERE contains(tags, "world-models")
```
````

The human can drop these into any wiki page to get dynamic views. I don't generate Dataview queries unless asked.

### Optional: Marp slide decks
For presentation-style answers, Marp markdown works in Obsidian via the Marp plugin. File a deck as `wiki/<category>/<slug>-deck.md` with the Marp frontmatter when the answer format calls for it.

---

## What NOT to do

- **Never edit `raw/`.** Read-only. Always.
- **Never delete a wiki page during ingest.** Only during lint, with explicit human confirmation.
- **Never strip frontmatter** from a page when editing it. If frontmatter is missing, add it.
- **Never use `[[wikilinks]]`.** Relative `[text](path.md)` only.
- **Never silently resolve contradictions.** Flag them in the page text and mention in the log.
- **Never answer a query from memory** when the wiki has the information. Read the pages.
- **Never run `archive/benchmark_wiki.py`** — it's kept for history, not for use. (The old `archive/build.py` is also frozen; its replacement is `scripts/build_site.py`, which points at `wiki/` and outputs to `site/`.)
- **Never re-introduce the old "Quality vs Coverage" improvement loop.** That mental model is replaced by ingest/query/lint. Don't run benchmark scoring against the new wiki — the score weights were tuned for the old publication-mode framing and would mislead.

---

## Working with the human

The human's job: curate sources, ask questions, direct emphasis, decide priorities.
My job: read, summarize, write, cross-reference, file, log, lint.

Default to **one source at a time, with discussion**. Batch mode is opt-in. Show your work — when an ingest touches 12 pages, list them in the log entry so the human can review the diff.

When in doubt about scope, ask. When in doubt about a contradiction, surface it. When a page is getting too long, propose a split. When two pages are converging, propose a merge. The human approves; I execute.

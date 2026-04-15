# Wikipedia for AI Learning

A personal, LLM-maintained wiki on AI learning research. The human curates sources and asks questions; an LLM (Claude Code, in this repo's case) reads, summarizes, integrates, and maintains everything.

This is **not** an encyclopedia. It's a compounding artifact that grows with every source the human drops into `raw/` and every question they ask. The LLM does the bookkeeping — cross-references, summaries, contradiction-flagging — that humans abandon wikis over.

---

## Layout

```
raw/                  sources you drop in (PDFs, clipped articles, transcripts) — immutable
wiki/                 LLM-maintained markdown organized into 5 categories — the knowledge base
CLAUDE.md             the schema (conventions + ingest/query/lint workflows)
index.md              catalog of every wiki page with one-line summaries
log.md                append-only record of every operation
scripts/              maintenance scripts, including the static site builder
site/                  build output from scripts/build_site.py (gitignored)
archive/              old static-site tooling (build.py, benchmark loop, generated HTML)
```

Open the repo in Obsidian and browse `wiki/` like a normal vault. Use the graph view to see the shape of the wiki; use Dataview queries against the YAML frontmatter for dynamic views.

---

## Browsing as a website

If you'd rather read the wiki in a browser than in Obsidian, there's a static site builder at `scripts/build_site.py`. It reads `wiki/<category>/*.md` plus the root `index.md` (as the landing page), strips YAML frontmatter, and writes HTML into `site/`.

```bash
# one-shot build → open site/index.html manually
python3 scripts/build_site.py

# build + serve locally at http://localhost:4321
python3 scripts/build_site.py --serve

# build + serve on a different port
python3 scripts/build_site.py --serve --port 8080

# delete site/
python3 scripts/build_site.py --clean
```

Requires the Python `markdown` package (`pip install markdown`). `site/` is gitignored — it's build output, regenerate it after every ingest.

---

## Operations

Ask the LLM (in Claude Code, Cursor, or any agent that respects `CLAUDE.md`) to do any of:

- **Ingest** a new source: drop a file into `raw/`, then "ingest raw/foo.pdf". The LLM reads it, writes a source-summary page, updates affected concept and entity pages, and logs the operation.
- **Query** the wiki: "what does the wiki say about world models?" The LLM reads `index.md`, picks relevant pages, synthesizes an answer with citations, and offers to file the answer back as a new wiki page.
- **Lint** the wiki: "lint the wiki." The LLM checks for contradictions, stale claims, orphan pages, red-link gaps, missing cross-refs, and frontmatter drift, then produces a report.

Full step-by-step workflows are in [CLAUDE.md](CLAUDE.md).

---

## What the wiki currently covers

47 pages across 5 categories, originally hand-curated as a static-site encyclopedia and now living as the seed corpus for the new LLM-maintained system:

- **Core Concepts** — foundation models, automated discovery, RAG, transfer learning, hallucination detection
- **Tools & Platforms** — aider, AIDE, autoresearch, Semantic Scholar API, HuggingFace papers API
- **Methodologies** — active learning, agentic tree search, evaluation, prompt engineering, world models, VLM integration
- **Frontier Topics** — predictive simulation learning, recursive self-improvement, AI safety in research, multi-agent systems, cross-cutting connections
- **Research Sources** — institutions and labs, key papers, paper-tracking pages, per-source summaries

Browse [index.md](index.md) for the full catalog.

---

## History

This repo started life as a static-site encyclopedia with an HTML build (`build.py`), a quality benchmark (`benchmark_wiki.py`), and a "Quality vs Coverage" improvement loop. That tooling lives in `archive/` for reference. The new model is described in [CLAUDE.md](CLAUDE.md) — the restructure is logged in [log.md](log.md).

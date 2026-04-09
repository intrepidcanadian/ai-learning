# Wiki Log

Append-only chronological record of operations against the wiki. Newest entries at the bottom. See [CLAUDE.md](CLAUDE.md) for operation definitions and entry format.

```
grep "^## \[" log.md | tail -10   # last 10 entries
```

---

## [2026-04-09] restructure | Wikipedia for AI Learning → LLM-maintained wiki

Converted the repo from a static-site encyclopedia (HTML build + benchmark loop) into a three-layer LLM-maintained wiki.

- **Moved** 47 markdown articles into `wiki/{core-concepts,tools-platforms,methodologies,frontier-topics,research-sources}/` via `git mv` (history preserved)
- **Created** `raw/` for source documents (seeded with `raw/2603.19710v1.pdf`, the existing paper that lived under `papers/`)
- **Archived** `build.py`, `benchmark_wiki.py`, `update_wiki.py`, `cron_update.sh`, `improve_loop.sh`, all 47 generated `.html` articles, plus `index.html`, `glossary.html`, and `data/` (benchmarks, experiments, papers.json, topic-wishlist.txt) into `archive/`
- **Injected** YAML frontmatter (`title`, `type`, `category`, `tags`, `created`, `updated`, `sources`) into all 47 wiki pages via `scripts/add_frontmatter.py`
- **Wrote** new `CLAUDE.md` schema describing the three layers, page conventions, and ingest/query/lint operations
- **Generated** `index.md` cataloging all 47 wiki pages with one-line summaries
- **Created** this `log.md`, plus `README.md`, `raw/README.md`, `archive/README.md`
- **Dropped** the old "Quality vs Coverage" improvement loop and tier system (flagship/standard/reference) — all wiki pages are now equal; size is emergent

The seed `raw/2603.19710v1.pdf` has not been ingested yet — the existing wiki content was synthesized from external citations, not from local raw sources, so all pages start with empty `sources: []`. First real ingest will populate the new flow.

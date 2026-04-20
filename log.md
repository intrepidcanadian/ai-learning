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

## [2026-04-09] ingest | AIGQ E-commerce Query Recommendation (Xu et al. 2026)

First real ingest under the new schema. Source: `raw/2603.19710v1.pdf` — Xu et al., "AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation," arXiv:2603.19710 (Alibaba Taobao/Tmall + UESTC, March 2026).

- **Created** `wiki/research-sources/aigq-ecommerce-query-recommendation.md` (`type: source-summary`, `sources: [raw/2603.19710v1.pdf]`)
- **Deepened** the existing AIGQ paragraph in `wiki/frontier-topics/ai-ecommerce-learning.md` with IL-SFT/IL-GRPO + dual-level rewards, the hybrid offline–online deployment split, daily reward retraining, A/B numbers (+10.31% orders, +10.68% GMV, +3.73% LT-7), and the zero-shot LLM-vs-EBR finding. Bumped its `sources:` to include the raw file.
- **Added** a new "Hybrid offline–online deployment" subsection to `wiki/methodologies/inference-optimization.md`, treating AIGQ's split as a reusable serving pattern (footnote `[^11]`).
- **Added** a new "Schema-slot prompt compression with special tokens" subsection to `wiki/methodologies/prompt-engineering.md` (footnote `[^12]`).
- **Added** an AIGQ row to the "AI for E-Commerce" table in `wiki/research-sources/key-papers.md`.
- **Updated** `index.md` (page count 47 → 48; new entry under Research Sources).
- **Did not** update `wiki/frontier-topics/e-commerce-applications.md` — its scope is consumer-facing shopping agents (LREF, Shopping Companion, persuasion, on-device); query recommendation belongs in the e-commerce *learning* article and the inference/prompt-engineering methodology pages instead. Recording the decision here for future lint.

## [2026-04-13] ingest | April 2026 research update: simulation, recursion, e-commerce, real-world learning

Automated scheduled update. Searched HuggingFace, arXiv, Scientific Reports, PMC, and industry sources for new papers.

**New research integrated (8 papers):**
1. **FOREAGENT** (Zheng et al., ACL 2026) — predict-before-executing for ML agents, 6× convergence speedup
2. **Agent World Model** (Wang et al., 2026) — 1,000 synthetic environments, 35K tools, OOD generalization
3. **Dreamer 4** (Hafner et al., 2025) — first Minecraft diamonds from offline video alone
4. **Recursive Self-Aggregation update** (Venkatraman et al.) — Gemini 3 Flash near-top ARC-AGI-2, RSA benchmarks expanded
5. **ICLR 2026 RSI Workshop** — expanded six-lens framework, full speaker list updated
6. **Hybrid CF-MF-RL Framework** (Scientific Reports, 2026) — unified recommendation + pricing + supply chain
7. **Agentic Commerce 2026 Landscape** — IDC Directions data, 57% exploring agents, 45% consumers using AI for buying
8. **Medical Student AI Learning RCT** (Chen, 2025, Frontiers in Medicine) — Cohen's d=0.72, strong equity effect

**Pages updated:**
- `wiki/frontier-topics/predictive-simulation-learning.md` — added FOREAGENT, Agent World Model, Dreamer 4 sections + predict-before-acting spectrum diagram
- `wiki/frontier-topics/recursive-self-improvement.md` — updated RSA benchmarks (ARC-AGI-2), expanded ICLR workshop 6-lens framework
- `wiki/frontier-topics/ai-ecommerce-learning.md` — added Hybrid CF-MF-RL section, agentic commerce 2026 landscape
- `wiki/methodologies/applications-for-real-world-learning.md` — added medical student AI RCT (Chen 2025)
- `wiki/frontier-topics/cross-cutting-connections.md` — added Connection 84: predict-before-executing spectrum + integration diagram
- `wiki/research-sources/key-papers.md` — added World Models, AI Personalized Learning tables; hybrid CF-MF-RL entry
- `index.md` — updated timestamp

**New diagrams added (2):**
1. Predict-before-acting spectrum (mermaid) in predictive-simulation-learning.md
2. Cross-domain connection diagram (mermaid) in cross-cutting-connections.md — shows how April 2026 papers connect simulation, recursion, and commerce to learning applications

**Issues/improvements noted for next session:**
1. Duplicate test-time-compute pages still not merged (from prior lint)
2. Cross-cutting connections page now at 84 connections — approaching unwieldy; consider splitting into sub-articles by theme
3. The ICLR 2026 RSI Workshop accepted papers list should be fetched when available (workshop is April 26-27)
4. No raw/ sources added this session (all web-sourced papers); consider downloading key PDFs for deeper ingest

**Schema gaps surfaced (deferred to lint):**
1. **Deepening shallow legacy mentions.** AIGQ was already cited at `[^19]` in `ai-ecommerce-learning.md` from the old improvement-loop era — synthesized from the abstract, no raw source. The schema's ingest workflow describes "write a source-summary + touch affected pages," but doesn't say what to do when an existing page already has a stub mention. Current convention (informally adopted): replace the stub paragraph in place, add the raw file to `sources:`, and link out to the new source-summary. CLAUDE.md should make this explicit.
2. **Footnote vs `sources:` reconciliation.** Legacy pages cite papers via `[^N]` footnotes even when those papers were never in `raw/`. The schema rule is "if I (the LLM) can read it, it's a `sources:` ref; if only the human can, it's a footnote." Re-shelving every legacy citation would be a massive lint pass. Today's ingest added the raw file to `sources:` *and* kept the existing `[^19]` footnote — they coexist. Acceptable, but the schema should sanction the duplication explicitly.
3. **Duplicate page titles.** `wiki/methodologies/test-time-compute.md` and `wiki/methodologies/test-time-compute-scaling.md` both display as "Test-Time Compute Scaling" in `index.md` — almost certainly two articles for one concept. Lint candidate: merge or rename.
4. **Footnote-number drift.** Legacy footnotes use a slightly different style than the schema example (`Author. (Year). "Title." arXiv:NNNN.NNNNN` vs the schema's `Author et al. (Year). "Title." [arXiv:NNNN.NNNNN](url)`). Worth normalising during the next lint pass, not now.
5. **No automated catalog regeneration.** `index.md` was edited by hand for this ingest (one entry, one count bump). Manageable now; needs a script if ingest cadence picks up. Could be added to a `scripts/regenerate_index.py` similar to the one-shot frontmatter script.

## [2026-04-20] ingest + lint | April 2026 research update + duplicate TTC page merge

Automated scheduled update. Resolved one outstanding issue and integrated 6 new papers/reports.

**Issue resolved:**
- **Merged duplicate test-time-compute pages.** `wiki/methodologies/test-time-compute-scaling.md` deleted; unique content (Reasoning Memory, Deep-Thinking Tokens, RD-VLA, BAM) folded into `wiki/methodologies/test-time-compute.md`. All cross-references in `computational-cost.md`, `cross-cutting-connections.md`, and `index.md` updated to point to the canonical page. Page count 48 → 47.

**New research integrated (6 papers/reports):**
1. **Simia** (Li et al., Nov 2025) — LLMs simulate environments for agent training, eliminating bespoke testbed infrastructure; fine-tuned open models exceed GPT-4o
2. **SpatialEvo** (Li et al., Apr 2026) — Self-evolving spatial intelligence via deterministic geometric environments; highest scores at 3B/7B on 9 benchmarks
3. **SkillClaw** (Ma et al., Apr 2026) — Collective skill evolution across multi-user agent ecosystems; cross-user discoveries propagate system-wide
4. **HBR China AI Agents** (Greeven et al., HBR Apr 2026) — Meituan Xiaomei delegation-first commerce; AI as autonomous executor not assistant
5. **ICLR RSI Workshop update** — Confirmed spotlight papers (Contextual Drag, Meta-learning Agentic Memory), panel details (Schrittwieser/Anthropic, Schmidhuber moderating), speakers (Levine, Kirsch, Bing Liu added)
6. **AI Adaptive Learning Platforms meta-landscape** — Synthesis of 3 systematic reviews on ALPs; OECD 2026 recommendation for purpose-built educational AI

**Pages updated:**
- `wiki/methodologies/test-time-compute.md` — merged unique 2026 content, added 4 references
- `wiki/frontier-topics/predictive-simulation-learning.md` — added Simia, SpatialEvo sections
- `wiki/frontier-topics/recursive-self-improvement.md` — added SkillClaw, SpatialEvo cross-reference, updated ICLR workshop with panels/speakers/spotlights
- `wiki/frontier-topics/ai-ecommerce-learning.md` — added HBR China AI agents section
- `wiki/frontier-topics/cross-cutting-connections.md` — added Connection 85: Self-Evolving Ecosystems with mermaid diagram
- `wiki/methodologies/applications-for-real-world-learning.md` — added ALP meta-landscape section, SVG pipeline diagram, new landscape entries
- `wiki/methodologies/computational-cost.md` — fixed broken test-time-compute-scaling reference
- `wiki/research-sources/key-papers.md` — added 6 new paper entries
- `index.md` — removed duplicate TTC entry, updated count and timestamp

**New diagrams added (2):**
1. Self-Evolving Ecosystems connection diagram (mermaid) in cross-cutting-connections.md — shows how Simia, SpatialEvo, SkillClaw, and Meituan connect simulation, recursion, and commerce
2. Simulation-to-Real-World Learning Pipeline (SVG) in applications-for-real-world-learning.md — four-stage pipeline from simulation through self-improvement and personalization to real-world application

**Issues/improvements for next session:**
1. Cross-cutting connections page now at 85 connections — consider splitting by theme
2. ICLR 2026 RSI Workshop happens April 26-27 — fetch proceedings and integrate after event
3. Footnote numbering gap in ai-ecommerce-learning.md ([^66] to [^69]) still present
4. No raw/ sources added this session — consider downloading key PDFs for schema-compliant ingest

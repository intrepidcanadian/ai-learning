# Wikipedia for AI Learning

## Scope

This wiki covers AI learning research across 5 categories and ~24 articles:
- **Core Concepts** — foundational ideas (AI scientist, automated discovery, peer review, foundation models)
- **Tools & Platforms** — practical tools (aider, aide, autoresearch, HuggingFace API, Semantic Scholar)
- **Methodologies** — research approaches (agentic tree search, experiment design, VLM integration)
- **Frontier Topics** — deep dives including 4 flagship articles:
  - Predictive Simulation Learning, Recursive Self-Improvement, AI E-Commerce Learning, Cross-Cutting Connections
- **Research Sources** — paper tracking, key papers, institutions

### Article tiers
- **Flagship** (frontier-topics, >500 lines): Full quality expectations, all 7 template sections
- **Standard** (100-500 lines): Moderate expectations, 4 required sections
- **Reference** (<100 lines): Navigation hubs, emphasis on linking and consistency

## Improvement Loop

**Every session that edits wiki content MUST follow this loop:**

1. **Benchmark first.** Run `python3 benchmark_wiki.py` before any edits. This takes <1s, no API calls.
2. **Read the scorecard.** Identify the lowest-scoring article and its specific issues (listed in "TOP ISSUES TO FIX").
3. **Fix the worst issues.** Prioritize by tier and score:
   - If all flagship articles are above 95, prioritize stubs and standard articles
   - For stubs (<100 lines), expand to standard size rather than micro-optimizing
   - Target: <20% stubs in the wiki — expand stubs before creating new articles
   - Fix priorities: missing sections (structural) > missing footnotes (sourcing) > missing cross-links (linking) > stale content (currency)
4. **Re-run the benchmark** after edits to confirm improvement. This also regenerates `research-sources/benchmark-trend.md` with the updated score trend.
5. **Rebuild the wiki** with `python3 build.py` so the HTML benchmark page is current.
6. **Repeat** from step 1 if the composite score is still below target.

### Benchmark commands
```bash
python3 benchmark_wiki.py            # Score all ~24 articles across 5 categories
python3 benchmark_wiki.py --diff     # Compare last two runs (handles v1→v2 transition)
python3 benchmark_wiki.py --history  # Score trend over time
```

### Score history
Benchmark results are saved to `data/benchmarks/` as timestamped JSON files.

## Article Template

Every article must follow this structure:
1. **Overview** — what it is, in plain language
2. **Background / Theoretical Foundations** — context and history
3. **Technical Details / Key Systems** — how it works
4. **Current State / Latest Developments** — recent work
5. **Limitations / Challenges** — known issues, open problems
6. **See Also / Connections** — links to related articles (MUST link to sibling articles in same category + at least 1 article in each other category)
7. **References** — primary sources with footnotes, arxiv/doi links

## Editing Rules

- Do NOT remove existing content unless it's a verified duplicate
- When adding sections, place them in template order
- Every new claim needs a footnote reference `[^N]` with a matching definition
- Prefer 2025-2026 sources
- Each article should link to sibling articles (same category) and at least one article in each other category
- Cross-cutting-connections uses `## Connection N:` numbering — keep numbers sequential, no gaps or duplicates

## Experiment-Driven Improvement

The improvement loop is hypothesis-driven. Each edit is an experiment logged to `data/experiments/`.

Before editing, write a hypothesis:
- **Strategy**: what you plan to change (1 sentence)
- **Predicted delta**: how many composite points you expect to gain
- **Dimensions targeted**: which scores this should move (structural, depth, currency, sourcing, linking, consistency)
- **Reasoning**: why this will work — reference past experiments if available

After editing, log the result:
- **Actual delta**: measured score change
- **Lesson**: what you learned (1 sentence)

Past experiments are fed into future iterations so the loop learns which strategies are effective. Read `data/experiments/*.json` to see what has been tried and what worked.

# archive/

Old static-site tooling and outputs from before the 2026-04-09 restructure to an LLM-maintained wiki. Kept for history, not for use.

**Do not run these as part of the new workflow.** See [`../CLAUDE.md`](../CLAUDE.md) for what replaces them.

## Contents

| Path | What it was |
|---|---|
| `build.py` | Markdown → HTML compiler. Read `.md` from each category dir, rendered them with a sidebar template, generated `index.html` and `glossary.html`. |
| `benchmark_wiki.py` | Quality scorer (~67 KB). Tiered articles into flagship/standard/reference and scored across 7 dimensions (structural, depth, currency, sourcing, linking, consistency, freshness). Drove the "Quality vs Coverage" improvement loop. |
| `update_wiki.py` | Automated paper-fetch + update script triggered by `cron_update.sh`. |
| `cron_update.sh`, `improve_loop.sh` | Wrapper shell scripts for the cron-driven update + improvement loop. |
| `index.html`, `glossary.html` | Generated site landing page and glossary. |
| `html/` | The 47 generated category articles (one HTML per markdown source in `wiki/`). |
| `data/benchmarks/` | 90+ timestamped JSON benchmark runs — useful as a historical signal of which articles needed work. |
| `data/experiments/` | Hypothesis → result logs from past quality-improvement passes. |
| `data/papers.json` | Auto-fetched paper metadata. |
| `data/topic-wishlist.txt` | Crowd-sourced topic requests. **Lint mines this** for red-link gap candidates — see CLAUDE.md → Operation: Lint. |
| `data/update.log` | Cron job execution log. |

## Why archive instead of delete

- The benchmark JSON history encodes which articles needed work — useful signal for lint to mine.
- The experiment logs document which editing strategies worked and which didn't — relevant if you ever want to revive a quality-scoring approach.
- `topic-wishlist.txt` is a real input to the new lint operation.
- The HTML output is recoverable proof of what the encyclopedia looked like at restructure time.

If you want to bring any of this back into active use, move it back to the repo root and update `CLAUDE.md` to reflect the change.

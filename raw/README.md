# raw/

Source documents for the wiki. **Immutable.** The LLM reads from this directory but never modifies, renames, or deletes anything inside it.

## What goes here

- Papers (PDF preferred, but markdown/HTML clipped from arxiv abstracts works too)
- Articles clipped from the web via Obsidian Web Clipper
- Meeting transcripts, podcast notes, interview recordings
- Any other primary source you want the wiki to integrate

## Conventions

- **`raw/assets/`** — image attachments. If you use Obsidian Web Clipper with the "Download attachments for current file" hotkey, point it here.
- **Filenames** — keep the original where reasonable (`2603.19710v1.pdf`), or rename to a meaningful slug (`sakana-ai-scientist-v2.pdf`). Whatever you pick is what wiki pages will reference in their `sources:` frontmatter, so try not to rename after ingest.
- **Subdirectories** — fine if you want them (e.g. `raw/papers/`, `raw/transcripts/`). Wiki cross-references will use relative paths regardless.

## How sources connect to the wiki

When you ask the LLM to ingest a file in `raw/`:
1. It reads the file
2. Discusses key takeaways with you
3. Writes a source-summary page in `wiki/research-sources/`
4. Updates affected concept/entity pages, adding the raw path to their `sources:` frontmatter
5. Logs the operation in `log.md`

See [`../CLAUDE.md`](../CLAUDE.md) for the full ingest workflow.

## Current contents

- `2603.19710v1.pdf` — seeded from the old repo's `papers/` directory at the time of the restructure. Has not been ingested into the wiki yet.

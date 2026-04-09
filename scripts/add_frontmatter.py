#!/usr/bin/env python3
"""One-shot migration: inject YAML frontmatter into every wiki/**/*.md file.

Idempotent — files that already start with `---` are left alone.
Also writes scripts/summaries.json so the index generator can pick up
the one-line summaries without re-parsing the wiki.

Run from the repo root:
    python3 scripts/add_frontmatter.py
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
TODAY = dt.date.today().isoformat()

# Strip markdown link/emphasis syntax for the summary line.
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
EMPH_RE = re.compile(r"\*+([^*]+)\*+")
FOOTNOTE_RE = re.compile(r"\[\^[^\]]+\]")


def first_paragraph_summary(body: str) -> str:
    """Return the first prose paragraph after the H1, cleaned to one line.

    Skips subsequent headings (## Overview, ### Foo) so we find actual prose.
    """
    lines = body.splitlines()
    # Skip until after the first H1
    i = 0
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    i += 1  # past the H1
    # Walk forward looking for a non-heading, non-blank line
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue
        break
    # Collect the paragraph
    para_lines: list[str] = []
    while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith("#"):
        para_lines.append(lines[i].strip())
        i += 1
    para = " ".join(para_lines)
    para = LINK_RE.sub(r"\1", para)
    para = EMPH_RE.sub(r"\1", para)
    para = FOOTNOTE_RE.sub("", para)
    para = re.sub(r"\s+", " ", para).strip()
    # First sentence (or up to 200 chars)
    m = re.match(r"^(.*?[.!?])(\s|$)", para)
    summary = m.group(1) if m else para
    if len(summary) > 220:
        summary = summary[:217].rstrip() + "..."
    return summary


def first_h1(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def slug_to_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def main() -> int:
    summaries: list[dict] = []
    skipped = 0
    updated = 0

    for md in sorted(WIKI.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            skipped += 1
            # Still record summary for index.md regeneration if absent
            body_after_fm = text.split("---\n", 2)[-1]
            title = first_h1(body_after_fm) or slug_to_title(md.stem)
            summary = first_paragraph_summary(body_after_fm)
        else:
            title = first_h1(text) or slug_to_title(md.stem)
            summary = first_paragraph_summary(text)
            category = md.parent.name
            # Quote title if it contains a colon or starts with a YAML special char.
            yaml_title = title
            if any(c in title for c in ":#&*!|>'%@`") or title.startswith("- "):
                yaml_title = '"' + title.replace('"', '\\"') + '"'
            fm = (
                "---\n"
                f"title: {yaml_title}\n"
                "type: concept\n"
                f"category: {category}\n"
                "tags: []\n"
                f"created: {TODAY}\n"
                f"updated: {TODAY}\n"
                "sources: []\n"
                "---\n\n"
            )
            md.write_text(fm + text, encoding="utf-8")
            updated += 1

        summaries.append(
            {
                "path": str(md.relative_to(REPO)),
                "category": md.parent.name,
                "title": title,
                "summary": summary,
                "slug": md.stem,
            }
        )

    out = REPO / "scripts" / "summaries.json"
    out.write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    print(f"updated={updated} skipped={skipped} total={len(summaries)}")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

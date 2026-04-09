#!/usr/bin/env python3
"""
Wikipedia for AI Learning -- Automated Update Script

Fetches new papers from HuggingFace Daily Papers and Semantic Scholar,
filters for relevance to AI research automation topics, updates:
  1. research-sources/latest-papers.md  (rolling feed of recent discoveries)
  2. research-sources/key-papers.md     (landmark papers, appended manually or by high citation count)
  3. Rebuilds the HTML wiki

Data is stored in data/papers.json to avoid duplicates across runs.

Usage:
    python3 update_wiki.py              # Full update (fetch + rebuild)
    python3 update_wiki.py --fetch-only # Fetch papers without rebuilding HTML
    python3 update_wiki.py --rebuild    # Rebuild HTML only (no fetch)
    python3 update_wiki.py --dry-run    # Show what would be fetched, don't write
"""

import json
import os
import re
import sys
import time
import logging
from datetime import datetime, timedelta
from pathlib import Path

# Suppress SSL warnings for older macOS LibreSSL
import warnings
warnings.filterwarnings("ignore")

import requests

# ── Config ──────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
PAPERS_DB = DATA_DIR / "papers.json"
LOG_FILE = DATA_DIR / "update.log"
LATEST_MD = ROOT / "research-sources" / "latest-papers.md"

# Topics we care about -- used to filter HF daily papers and Semantic Scholar
RELEVANCE_KEYWORDS = [
    "automated research", "ai scientist", "automated discovery",
    "autonomous research", "llm agent", "ai agent",
    "foundation model", "large language model",
    "automated experiment", "automated peer review",
    "machine learning research", "automl",
    "open-ended", "agentic", "tree search",
    "code generation", "automated coding",
    "research automation", "scientific discovery",
    "self-improving", "self-play", "autoresearch",
    "blockchain ai", "decentralized ai", "desci",
    "scaling law", "test-time compute",
    "vision language model", "multimodal",
    "reinforcement learning from human feedback",
    "reasoning model", "chain of thought",
]

# Semantic Scholar topic queries -- rotated across runs
SS_QUERIES = [
    "automated AI research",
    "LLM scientific discovery",
    "autonomous machine learning agent",
    "foundation model reasoning",
    "agentic AI system",
    "open-ended AI exploration",
    "AI peer review automation",
    "decentralized AI research blockchain",
]

MAX_LATEST_PAPERS = 100  # Keep last N papers in latest-papers.md
HF_PAPERS_LIMIT = 50     # Max papers to fetch from HF per run
SS_RESULTS_PER_QUERY = 10

# ── Logging ─────────────────────────────────────────────────────────────────

def setup_logging():
    DATA_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(),
        ],
    )

# ── Database ────────────────────────────────────────────────────────────────

def load_db():
    if PAPERS_DB.exists():
        with open(PAPERS_DB) as f:
            return json.load(f)
    return {"papers": {}, "last_hf_date": None, "last_ss_query_index": 0, "runs": []}


def save_db(db):
    DATA_DIR.mkdir(exist_ok=True)
    with open(PAPERS_DB, "w") as f:
        json.dump(db, f, indent=2, default=str)


# ── Relevance Scoring ──────────────────────────────────────────────────────

def relevance_score(title, summary=""):
    """Score 0-100 based on keyword matches in title + summary."""
    text = f"{title} {summary}".lower()
    hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw in text)
    # Title matches count double
    title_hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw in title.lower())
    score = min(100, (hits * 8) + (title_hits * 15))
    return score


# ── HuggingFace Papers API ─────────────────────────────────────────────────

def fetch_hf_papers(db, days_back=3):
    """Fetch recent papers from HuggingFace Daily Papers API."""
    new_papers = []
    today = datetime.now()

    for day_offset in range(days_back):
        date_str = (today - timedelta(days=day_offset)).strftime("%Y-%m-%d")
        logging.info(f"Fetching HF papers for {date_str}...")

        try:
            resp = requests.get(
                "https://huggingface.co/api/daily_papers",
                params={"date": date_str},
                timeout=15,
            )
            if resp.status_code != 200:
                logging.warning(f"HF API returned {resp.status_code} for {date_str}")
                continue

            data = resp.json()
            # API returns a flat list of paper wrapper objects
            results = data if isinstance(data, list) else data.get("results", [])
            if not results:
                continue

            for item in results:
                # Paper metadata is nested under "paper" key
                paper_obj = item.get("paper", {}) if isinstance(item, dict) else {}
                arxiv_id = paper_obj.get("id", "") or item.get("id", "")
                if not arxiv_id or arxiv_id in db["papers"]:
                    continue

                title = item.get("title", "") or paper_obj.get("title", "")
                summary = item.get("summary", "") or paper_obj.get("summary", "")
                # Extract author names from nested author objects
                raw_authors = paper_obj.get("authors", [])
                if raw_authors and isinstance(raw_authors[0], dict):
                    authors = [a.get("name", "") for a in raw_authors[:5]]
                else:
                    authors = raw_authors[:5] if raw_authors else []

                score = relevance_score(title, summary)

                if score >= 15:  # Minimum relevance threshold
                    pub_date = item.get("publishedAt", date_str)
                    # Extract year from ISO date or date string
                    try:
                        year = datetime.fromisoformat(pub_date.replace("Z", "+00:00")).year
                    except (ValueError, AttributeError):
                        year = datetime.now().year
                    entry = {
                        "id": arxiv_id,
                        "title": title,
                        "authors": authors,
                        "summary": summary[:500],
                        "source": "huggingface",
                        "source_detail": "HuggingFace Daily Papers",
                        "date_found": datetime.now().isoformat(),
                        "published_date": pub_date,
                        "year": year,
                        "relevance_score": score,
                        "url": f"https://arxiv.org/abs/{arxiv_id}",
                        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                        "arxiv_id": arxiv_id,
                    }
                    db["papers"][arxiv_id] = entry
                    new_papers.append(entry)
                    logging.info(f"  [HF] score={score}: {title[:80]}")

        except Exception as e:
            logging.error(f"HF fetch error for {date_str}: {e}")

    return new_papers


# ── Semantic Scholar API ───────────────────────────────────────────────────

def fetch_ss_papers(db, num_queries=3):
    """Fetch papers from Semantic Scholar, rotating through topic queries."""
    new_papers = []
    start_idx = db.get("last_ss_query_index", 0)

    for i in range(num_queries):
        query_idx = (start_idx + i) % len(SS_QUERIES)
        query = SS_QUERIES[query_idx]
        logging.info(f"Searching Semantic Scholar: '{query}'...")

        try:
            time.sleep(5)  # Pre-request delay to respect rate limits
            resp = requests.get(
                "https://api.semanticscholar.org/graph/v1/paper/search",
                params={
                    "query": query,
                    "limit": SS_RESULTS_PER_QUERY,
                    "fields": "title,abstract,year,citationCount,externalIds,authors,url",
                    "year": "2024-",  # Recent papers only
                },
                headers={"User-Agent": "AILearningWiki/1.0 (research tracker)"},
                timeout=15,
            )
            if resp.status_code == 429:
                logging.warning("Semantic Scholar rate limited, backing off...")
                time.sleep(30)
                continue
            if resp.status_code != 200:
                logging.warning(f"SS API returned {resp.status_code}")
                continue

            data = resp.json()
            for paper in data.get("data", []):
                # Use arxiv ID if available, otherwise SS ID
                ext_ids = paper.get("externalIds", {}) or {}
                arxiv_id = ext_ids.get("ArXiv", "")
                paper_id = arxiv_id or paper.get("paperId", "")
                if not paper_id or paper_id in db["papers"]:
                    continue

                title = paper.get("title", "")
                abstract = paper.get("abstract", "") or ""
                score = relevance_score(title, abstract)
                citations = paper.get("citationCount", 0) or 0

                # Boost score for highly cited papers
                if citations > 50:
                    score = min(100, score + 20)
                if citations > 200:
                    score = min(100, score + 20)

                if score >= 15:
                    authors = [a.get("name", "") for a in (paper.get("authors", []) or [])[:5]]
                    year = paper.get("year", "")
                    doi = ext_ids.get("DOI", "")
                    paper_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else (paper.get("url") or "")
                    entry = {
                        "id": paper_id,
                        "title": title,
                        "authors": authors,
                        "summary": abstract[:500],
                        "source": "semantic_scholar",
                        "source_detail": "Semantic Scholar",
                        "date_found": datetime.now().isoformat(),
                        "published_date": str(year),
                        "year": year,
                        "relevance_score": score,
                        "citation_count": citations,
                        "url": paper_url,
                        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}" if arxiv_id else "",
                        "arxiv_id": arxiv_id,
                        "doi": doi,
                    }
                    db["papers"][paper_id] = entry
                    new_papers.append(entry)
                    logging.info(f"  [SS] score={score} cites={citations}: {title[:80]}")

            time.sleep(3)  # Respect rate limits

        except Exception as e:
            logging.error(f"SS fetch error for '{query}': {e}")

    db["last_ss_query_index"] = (start_idx + num_queries) % len(SS_QUERIES)
    return new_papers


# ── Markdown Generation ────────────────────────────────────────────────────

def format_citation(p, footnote_num):
    """Format a paper as an academic citation string for the references section."""
    authors = p.get("authors", [])
    if len(authors) == 0:
        author_str = "Unknown"
    elif len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{authors[0]} & {authors[1]}"
    else:
        author_str = f"{authors[0]} et al."

    year = p.get("year", "")
    title = p.get("title", "Untitled")
    arxiv_id = p.get("arxiv_id", "")
    doi = p.get("doi", "")
    url = p.get("url", "")

    # Build citation parts
    cite = f"[^{footnote_num}]: {author_str}"
    if year:
        cite += f" ({year})."
    else:
        cite += "."
    cite += f' "{title}."'

    # Add identifiers
    if arxiv_id:
        cite += f" [arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})."
    if doi:
        cite += f" [DOI:{doi}](https://doi.org/{doi})."
    if not arxiv_id and not doi and url:
        cite += f" [{url}]({url})."

    # Source attribution
    source_detail = p.get("source_detail", p.get("source", ""))
    if source_detail:
        cite += f" Retrieved via {source_detail}."

    return cite


def format_author_inline(authors):
    """Format authors for inline text (short form)."""
    if not authors:
        return "Unknown"
    if len(authors) == 1:
        # Last name only
        return authors[0].split()[-1] if authors[0] else "Unknown"
    elif len(authors) == 2:
        return f"{authors[0].split()[-1]} & {authors[1].split()[-1]}"
    else:
        return f"{authors[0].split()[-1]} et al."


def generate_latest_papers_md(db):
    """Generate the latest-papers.md page from the paper database with proper sourcing and footnotes."""

    # Sort by date found (newest first), take top N
    papers = sorted(
        db["papers"].values(),
        key=lambda p: p.get("date_found", ""),
        reverse=True,
    )[:MAX_LATEST_PAPERS]

    # Group by week
    weeks = {}
    for p in papers:
        try:
            dt = datetime.fromisoformat(p["date_found"])
            week_key = dt.strftime("%Y-W%U")
            week_label = f"Week of {(dt - timedelta(days=dt.weekday())).strftime('%B %d, %Y')}"
        except (ValueError, TypeError):
            week_key = "unknown"
            week_label = "Undated"

        if week_key not in weeks:
            weeks[week_key] = {"label": week_label, "papers": []}
        weeks[week_key]["papers"].append(p)

    # Build markdown
    lines = [
        "# Latest Papers",
        "",
        "Auto-updated feed of recent AI research relevant to research automation, "
        "foundation models, agentic systems, and related topics. "
        f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}.",
        "",
        f"**{len(db['papers'])} papers tracked** | "
        f"Sources: [HuggingFace Daily Papers](../tools-platforms/huggingface-papers-api.md), "
        f"[Semantic Scholar](../tools-platforms/semantic-scholar-api.md)",
        "",
        "---",
        "",
    ]

    # Track footnotes for references section
    footnotes = []
    footnote_num = 0

    for week_key in sorted(weeks.keys(), reverse=True):
        week = weeks[week_key]
        lines.append(f"## {week['label']}")
        lines.append("")

        # Sort within week by relevance score
        for p in sorted(week["papers"], key=lambda x: x.get("relevance_score", 0), reverse=True):
            footnote_num += 1
            title = p.get("title", "Untitled")
            url = p.get("url", "")
            authors = p.get("authors", [])
            author_inline = format_author_inline(authors)
            year = p.get("year", "")
            score = p.get("relevance_score", 0)
            cites = p.get("citation_count", 0)
            summary = p.get("summary", "")[:250]
            arxiv_id = p.get("arxiv_id", "")
            pdf_url = p.get("pdf_url", "")

            # Relevance indicator
            if score >= 60:
                relevance = "HIGH"
            elif score >= 30:
                relevance = "MED"
            else:
                relevance = "LOW"

            # Title with link and footnote reference
            if url:
                lines.append(f"### [{title}]({url}) [^{footnote_num}]")
            else:
                lines.append(f"### {title} [^{footnote_num}]")

            lines.append("")
            lines.append(f"`{relevance} RELEVANCE`")
            lines.append("")

            # Author and publication metadata
            meta_line = f"**{author_inline}**"
            if year:
                meta_line += f" ({year})"
            lines.append(meta_line)
            lines.append("")

            # Summary/abstract
            if summary:
                lines.append(f"> {summary}...")
                lines.append("")

            # Source links
            source_links = []
            if arxiv_id:
                source_links.append(f"[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})")
            if pdf_url:
                source_links.append(f"[PDF]({pdf_url})")
            if p.get("doi"):
                source_links.append(f"[DOI](https://doi.org/{p['doi']})")

            source_detail = p.get("source_detail", p.get("source", ""))
            cite_parts = []
            if source_links:
                cite_parts.append(" | ".join(source_links))
            if cites:
                cite_parts.append(f"{cites} citations")
            if source_detail:
                cite_parts.append(f"Found via {source_detail}")

            if cite_parts:
                lines.append(f"*{' -- '.join(cite_parts)}*")
                lines.append("")

            # Build the footnote citation
            footnotes.append(format_citation(p, footnote_num))

        lines.append("")

    # See Also section
    lines.extend([
        "---",
        "",
        "## See Also",
        "",
        "- [Key Papers and References](key-papers.md) -- Curated essential reading",
        "- [Tracking AI Research](tracking-ai-research.md) -- APIs and methodology",
        "- [The AI Scientist](../core-concepts/the-ai-scientist.md)",
        "",
    ])

    # References / footnotes section
    lines.extend([
        "## References",
        "",
    ])
    for fn in footnotes:
        lines.append(fn)
    lines.append("")

    lines.extend([
        "---",
        "",
        "*This page is auto-generated by `update_wiki.py`. Do not edit manually.*",
    ])

    return "\n".join(lines)


# ── Update Summary for Log ─────────────────────────────────────────────────

def log_run_summary(db, hf_new, ss_new):
    """Append run summary to the database."""
    run = {
        "timestamp": datetime.now().isoformat(),
        "hf_new": len(hf_new),
        "ss_new": len(ss_new),
        "total_papers": len(db["papers"]),
        "top_papers": [
            {"title": p["title"][:80], "score": p["relevance_score"]}
            for p in sorted(hf_new + ss_new, key=lambda x: x["relevance_score"], reverse=True)[:5]
        ],
    }
    db.setdefault("runs", []).append(run)
    # Keep last 30 runs
    db["runs"] = db["runs"][-30:]


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    setup_logging()
    args = set(sys.argv[1:])
    dry_run = "--dry-run" in args
    fetch_only = "--fetch-only" in args
    rebuild_only = "--rebuild" in args

    logging.info("=" * 60)
    logging.info("Wikipedia for AI Learning -- Update starting")
    logging.info("=" * 60)

    db = load_db()
    hf_new = []
    ss_new = []

    if not rebuild_only:
        # Fetch from APIs
        hf_new = fetch_hf_papers(db, days_back=3)
        ss_new = fetch_ss_papers(db, num_queries=3)

        total_new = len(hf_new) + len(ss_new)
        logging.info(f"\nFound {total_new} new papers ({len(hf_new)} HF, {len(ss_new)} SS)")

        if total_new > 0 and not dry_run:
            log_run_summary(db, hf_new, ss_new)
            save_db(db)

            # Generate latest papers page
            md_content = generate_latest_papers_md(db)
            LATEST_MD.write_text(md_content)
            logging.info(f"Updated {LATEST_MD}")
        elif dry_run:
            logging.info("[DRY RUN] Would have saved papers and updated markdown")
            return

    if not fetch_only and not dry_run:
        # Rebuild HTML wiki
        logging.info("Rebuilding HTML wiki...")
        build_script = ROOT / "build.py"
        if build_script.exists():
            os.system(f"python3 {build_script}")
            logging.info("HTML rebuild complete")
        else:
            logging.warning("build.py not found, skipping HTML rebuild")

    logging.info("Update complete!")


if __name__ == "__main__":
    main()

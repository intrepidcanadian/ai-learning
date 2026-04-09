#!/usr/bin/env python3
"""Build static HTML wiki from markdown files, and optionally serve with live wishlist API."""

import os
import re
import json
import markdown
import sys
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = {
    "core-concepts": "Core Concepts",
    "tools-platforms": "Tools & Platforms",
    "methodologies": "Methodologies",
    "frontier-topics": "Frontier Topics",
    "research-sources": "Research Sources",
}

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - AI Learning Wiki</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.7;
    color: #1a1a2e;
    background: #f8f9fb;
    display: flex;
    min-height: 100vh;
}}
.sidebar {{
    width: 280px;
    min-width: 280px;
    background: #16213e;
    color: #c4c9d4;
    padding: 24px 0;
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    overflow-y: auto;
    z-index: 100;
}}
.sidebar-header {{
    padding: 0 20px 20px;
    border-bottom: 1px solid #1a1a4e;
    margin-bottom: 12px;
}}
.sidebar-header h1 {{
    font-size: 16px;
    color: #e8eaf0;
    font-weight: 700;
    letter-spacing: 0.5px;
}}
.sidebar-header a {{
    color: #e8eaf0;
    text-decoration: none;
}}
.sidebar-header p {{
    font-size: 11px;
    color: #7b8794;
    margin-top: 4px;
}}
.sidebar details {{
    margin-bottom: 4px;
}}
.sidebar summary {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #7b8794;
    padding: 8px 20px;
    cursor: pointer;
    list-style: none;
    user-select: none;
}}
.sidebar summary::-webkit-details-marker {{ display: none; }}
.sidebar summary::before {{
    content: "\\25B6";
    font-size: 8px;
    margin-right: 8px;
    display: inline-block;
    transition: transform 0.15s;
}}
.sidebar details[open] summary::before {{
    transform: rotate(90deg);
}}
.sidebar a {{
    display: block;
    padding: 5px 20px 5px 36px;
    color: #a8b2c1;
    text-decoration: none;
    font-size: 13px;
    border-left: 3px solid transparent;
    transition: all 0.15s;
}}
.sidebar a:hover {{
    color: #e8eaf0;
    background: rgba(255,255,255,0.04);
    border-left-color: #4a6fa5;
}}
.sidebar a[aria-current="page"] {{
    color: #fff;
    background: rgba(74,111,165,0.18);
    border-left-color: #5b9df5;
    font-weight: 600;
}}
.wishlist-panel {{
    border-top: 1px solid #1a1a4e;
    margin-top: 12px;
    padding: 12px 20px;
}}
.wishlist-panel h3 {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #7b8794;
    margin-bottom: 8px;
}}
.wishlist-panel .wl-stats {{
    font-size: 11px;
    color: #a8b2c1;
    margin-bottom: 8px;
}}
.wishlist-panel .wl-bar {{
    height: 4px;
    background: #2a2a4e;
    border-radius: 2px;
    margin-bottom: 10px;
    overflow: hidden;
}}
.wishlist-panel .wl-bar-fill {{
    height: 100%;
    background: #5b9df5;
    border-radius: 2px;
    transition: width 0.3s;
}}
.wishlist-panel .wl-item {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 12px;
    padding: 3px 0;
    color: #a8b2c1;
}}
.wishlist-panel .wl-item.written {{
    color: #4ade80;
    text-decoration: line-through;
    opacity: 0.6;
}}
.wishlist-panel .wl-item button {{
    background: none;
    border: none;
    color: #ef4444;
    cursor: pointer;
    font-size: 14px;
    padding: 0 4px;
    opacity: 0.5;
}}
.wishlist-panel .wl-item button:hover {{
    opacity: 1;
}}
.wishlist-panel .wl-add {{
    display: flex;
    gap: 6px;
    margin-top: 8px;
}}
.wishlist-panel .wl-add input {{
    flex: 1;
    background: #1a1a3e;
    border: 1px solid #2a2a5e;
    border-radius: 4px;
    color: #e8eaf0;
    padding: 4px 8px;
    font-size: 12px;
    outline: none;
}}
.wishlist-panel .wl-add input:focus {{
    border-color: #5b9df5;
}}
.wishlist-panel .wl-add button {{
    background: #4a6fa5;
    border: none;
    color: #fff;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
}}
.wishlist-panel .wl-add button:hover {{
    background: #5b9df5;
}}
.wishlist-panel .wl-offline {{
    font-size: 11px;
    color: #f59e0b;
    margin-top: 6px;
    display: none;
}}
.content {{
    margin-left: 280px;
    flex: 1;
    padding: 40px 48px 80px;
    max-width: 1060px;
}}
.breadcrumb {{
    font-size: 12px;
    color: #7b8794;
    margin-bottom: 24px;
}}
.breadcrumb a {{ color: #4a6fa5; text-decoration: none; }}
.breadcrumb a:hover {{ text-decoration: underline; }}
.content h1 {{
    font-size: 32px;
    color: #16213e;
    margin-bottom: 8px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e2e6ed;
}}
.content h2 {{
    font-size: 22px;
    color: #1a1a2e;
    margin-top: 36px;
    margin-bottom: 12px;
    padding-bottom: 6px;
    border-bottom: 1px solid #e2e6ed;
}}
.content h3 {{
    font-size: 17px;
    color: #2d3748;
    margin-top: 28px;
    margin-bottom: 8px;
}}
.content p {{ margin-bottom: 14px; }}
.content a {{
    color: #2b6cb0;
    text-decoration: none;
    border-bottom: 1px solid #bee3f8;
}}
.content a:hover {{
    color: #1a4971;
    border-bottom-color: #2b6cb0;
}}
.content ul, .content ol {{
    margin: 0 0 16px 24px;
}}
.content li {{ margin-bottom: 4px; }}
.content table {{
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0 24px;
    font-size: 14px;
}}
.content th {{
    background: #edf2f7;
    font-weight: 600;
    text-align: left;
    padding: 10px 14px;
    border: 1px solid #d2d8e2;
}}
.content td {{
    padding: 8px 14px;
    border: 1px solid #e2e6ed;
    vertical-align: top;
}}
.content tr:nth-child(even) {{ background: #f7fafc; }}
.content code {{
    font-family: "SF Mono", "Fira Code", "Fira Mono", Menlo, Consolas, monospace;
    font-size: 13px;
    background: #edf2f7;
    padding: 2px 6px;
    border-radius: 3px;
    color: #2d3748;
}}
.content pre {{
    background: #1a1a2e;
    color: #e2e8f0;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 16px 0 24px;
    line-height: 1.5;
}}
.content pre code {{
    background: none;
    padding: 0;
    color: #e2e8f0;
    font-size: 13px;
}}
.content blockquote {{
    border-left: 4px solid #4a6fa5;
    padding: 12px 20px;
    margin: 16px 0;
    background: #edf2f7;
    color: #4a5568;
}}
.content strong {{ color: #1a1a2e; }}
.content hr {{
    border: none;
    border-top: 1px solid #e2e6ed;
    margin: 32px 0;
}}
.hamburger {{
    display: none;
    position: fixed;
    top: 12px;
    left: 12px;
    z-index: 200;
    background: #16213e;
    color: #fff;
    border: none;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 18px;
    cursor: pointer;
}}
@media (max-width: 860px) {{
    .sidebar {{ transform: translateX(-100%); transition: transform 0.25s; }}
    .sidebar.open {{ transform: translateX(0); }}
    .content {{ margin-left: 0; padding: 60px 20px 60px; }}
    .hamburger {{ display: block; }}
}}
</style>
</head>
<body>
<button class="hamburger" onclick="document.querySelector('.sidebar').classList.toggle('open')">&#9776;</button>
<nav class="sidebar">
<div class="sidebar-header">
    <h1><a href="{index_path}">AI Learning Wiki</a></h1>
    <p>AI Research Automation</p>
    <p style="margin-top:8px"><a href="{glossary_path}" style="color:#5b9df5;font-size:12px;text-decoration:none;border-bottom:none">Glossary &amp; Index</a></p>
</div>
{sidebar}
<div class="wishlist-panel" id="wishlistPanel">
    <h3>Topic Wishlist</h3>
    <div class="wl-stats" id="wlStats">Loading...</div>
    <div class="wl-bar"><div class="wl-bar-fill" id="wlBarFill" style="width:0%"></div></div>
    <div id="wlItems"></div>
    <div class="wl-add">
        <input type="text" id="wlInput" placeholder="new-topic-name" />
        <button onclick="addWishlistTopic()">Add</button>
    </div>
    <div class="wl-offline" id="wlOffline">Run python3 build.py --serve for live editing</div>
</div>
</nav>
<script>
const API = '/api/wishlist';
let wlLive = false;

async function loadWishlist() {{
    try {{
        const res = await fetch(API);
        if (!res.ok) throw new Error('not served');
        const items = await res.json();
        wlLive = true;
        renderWishlist(items);
    }} catch(e) {{
        wlLive = false;
        document.getElementById('wlOffline').style.display = 'block';
        document.getElementById('wlStats').textContent = 'Offline mode';
    }}
}}

function renderWishlist(items) {{
    const total = items.length;
    const written = items.filter(i => i.written).length;
    const pct = total > 0 ? Math.round(written / total * 100) : 100;

    document.getElementById('wlStats').textContent =
        total > 0 ? `${{written}}/${{total}} written (${{pct}}%)` : 'No topics yet';
    document.getElementById('wlBarFill').style.width = pct + '%';

    const container = document.getElementById('wlItems');
    container.innerHTML = items.map(i => `
        <div class="wl-item ${{i.written ? 'written' : ''}}">
            <span>${{i.written ? '\\u2713' : '\\u25CB'}} ${{i.topic}}</span>
            <button onclick="removeWishlistTopic('${{i.topic}}')" title="Remove">&times;</button>
        </div>
    `).join('');
}}

async function addWishlistTopic() {{
    const input = document.getElementById('wlInput');
    const topic = input.value.trim().toLowerCase().replace(/\\s+/g, '-');
    if (!topic || !wlLive) return;
    input.value = '';
    const res = await fetch(API, {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{topic}})
    }});
    const items = await res.json();
    renderWishlist(items);
}}

async function removeWishlistTopic(topic) {{
    if (!wlLive) return;
    const res = await fetch(API, {{
        method: 'DELETE',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{topic}})
    }});
    const items = await res.json();
    renderWishlist(items);
}}

document.getElementById('wlInput').addEventListener('keydown', e => {{
    if (e.key === 'Enter') addWishlistTopic();
}});

loadWishlist();
</script>
<main class="content">
<div class="breadcrumb">{breadcrumb}</div>
{body}
</main>
</body>
</html>
"""


def get_title(md_text):
    """Extract first h1 heading from markdown."""
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def collect_articles():
    """Walk directories and collect all markdown files."""
    articles = {}
    for cat_dir, cat_name in CATEGORIES.items():
        cat_path = os.path.join(ROOT, cat_dir)
        if not os.path.isdir(cat_path):
            continue
        articles[cat_dir] = []
        for fname in sorted(os.listdir(cat_path)):
            if fname.endswith(".md"):
                fpath = os.path.join(cat_path, fname)
                with open(fpath, "r") as f:
                    text = f.read()
                title = get_title(text)
                articles[cat_dir].append({
                    "filename": fname,
                    "title": title,
                    "path": fpath,
                    "rel": f"{cat_dir}/{fname}",
                    "html_rel": f"{cat_dir}/{fname.replace('.md', '.html')}",
                    "text": text,
                })
    return articles


def build_sidebar(articles, current_rel=""):
    """Generate sidebar HTML."""
    html = ""
    for cat_dir, cat_name in CATEGORIES.items():
        if cat_dir not in articles:
            continue
        items = ""
        for art in articles[cat_dir]:
            aria = ' aria-current="page"' if art["rel"] == current_rel else ""
            # compute relative href from current file
            if current_rel and "/" in current_rel:
                href = f"../{art['html_rel']}"
            else:
                href = art["html_rel"]
            items += f'<a href="{href}"{aria}>{art["title"]}</a>\n'
        html += f"<details open><summary>{cat_name}</summary>\n{items}</details>\n"
    return html


def rewrite_links(html_content):
    """Rewrite .md links to .html."""
    return re.sub(r'href="([^"]*?)\.md"', r'href="\1.html"', html_content)


def convert_md(text):
    """Convert markdown to HTML."""
    extensions = ["tables", "fenced_code", "toc", "nl2br"]
    return markdown.markdown(text, extensions=extensions)


def build():
    articles = collect_articles()
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])

    # Build each article
    for cat_dir in articles:
        cat_path = os.path.join(ROOT, cat_dir)
        for art in articles[cat_dir]:
            md.reset()
            body = md.convert(art["text"])
            body = rewrite_links(body)
            sidebar = build_sidebar(articles, art["rel"])
            breadcrumb = f'<a href="../index.html">Home</a> &rsaquo; {CATEGORIES[cat_dir]} &rsaquo; {art["title"]}'

            html = TEMPLATE.format(
                title=art["title"],
                sidebar=sidebar,
                body=body,
                breadcrumb=breadcrumb,
                index_path="../index.html",
                glossary_path="../glossary.html",
            )

            out_path = os.path.join(cat_path, art["filename"].replace(".md", ".html"))
            with open(out_path, "w") as f:
                f.write(html)
            print(f"  Built: {art['html_rel']}")

    # Build index from README
    readme_path = os.path.join(ROOT, "README.md")
    with open(readme_path, "r") as f:
        readme_text = f.read()

    md.reset()
    body = md.convert(readme_text)
    body = rewrite_links(body)
    sidebar = build_sidebar(articles, "")

    html = TEMPLATE.format(
        title="AI Learning Wiki",
        sidebar=sidebar,
        body=body,
        breadcrumb="Home",
        index_path="index.html",
        glossary_path="glossary.html",
    )

    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)
    print("  Built: index.html")

    # Build glossary
    build_glossary(articles)
    print("  Built: glossary.html")


def extract_glossary_terms(articles):
    """Extract key terms from all articles for the glossary.
    Returns sorted list of {term, definition, article_title, article_href, category}."""
    entries = []
    seen = set()

    for cat_dir, cat_name in CATEGORIES.items():
        if cat_dir not in articles:
            continue
        for art in articles[cat_dir]:
            text = art["text"]
            href = art["html_rel"]
            title = art["title"]

            # 1. Article title itself
            key = title.lower()
            if key not in seen:
                seen.add(key)
                # Extract first sentence after the h1 as a short definition
                lines = text.splitlines()
                defn = ""
                for line in lines:
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#") and not stripped.startswith("**Paper") and not stripped.startswith("**Repository") and not stripped.startswith("!["):
                        # Clean markdown formatting
                        defn = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', stripped)
                        defn = re.sub(r'\*\*([^*]+)\*\*', r'\1', defn)
                        defn = re.sub(r'\*([^*]+)\*', r'\1', defn)
                        defn = re.sub(r'`([^`]+)`', r'\1', defn)
                        # Truncate to first sentence
                        if '. ' in defn:
                            defn = defn[:defn.index('. ') + 1]
                        if len(defn) > 200:
                            defn = defn[:197] + "..."
                        break
                entries.append({
                    "term": title,
                    "definition": defn,
                    "article_title": title,
                    "article_href": href,
                    "category": cat_name,
                })

            # 2. H2 headings as sub-terms
            for line in text.splitlines():
                if line.startswith("## "):
                    heading = line[3:].strip()
                    # Skip generic section names
                    if heading.lower() in ("overview", "background", "background / theoretical foundations",
                                           "technical details", "technical details / key systems",
                                           "technical architecture",
                                           "current state", "current state / latest developments",
                                           "limitations", "limitations / challenges",
                                           "see also", "see also / connections", "references",
                                           "significance", "how it works", "key design principles",
                                           "comparison with related systems", "contributing"):
                        continue
                    hkey = heading.lower()
                    if hkey not in seen:
                        seen.add(hkey)
                        entries.append({
                            "term": heading,
                            "definition": "",
                            "article_title": title,
                            "article_href": href,
                            "category": cat_name,
                        })

            # 3. Bold terms from first paragraph (key definitions)
            bold_terms = re.findall(r'\*\*([A-Z][^*]{2,60})\*\*', text[:1500])
            for bt in bold_terms:
                btkey = bt.lower()
                if btkey not in seen and not bt.startswith("Paper") and not bt.startswith("Repository"):
                    seen.add(btkey)
                    entries.append({
                        "term": bt,
                        "definition": "",
                        "article_title": title,
                        "article_href": href,
                        "category": cat_name,
                    })

    entries.sort(key=lambda e: e["term"].lower())
    return entries


def build_glossary(articles):
    """Generate glossary.html with searchable term index."""
    entries = extract_glossary_terms(articles)

    # Group by first letter
    letter_groups = {}
    for e in entries:
        letter = e["term"][0].upper()
        if not letter.isalpha():
            letter = "#"
        letter_groups.setdefault(letter, []).append(e)

    # Build letter nav
    all_letters = sorted(letter_groups.keys())
    letter_nav = " ".join(
        f'<a href="#letter-{l}" class="gl-letter-link">{l}</a>' for l in all_letters
    )

    # Build entries HTML
    entries_html = ""
    for letter in all_letters:
        entries_html += f'<div class="gl-group" id="letter-{letter}">\n'
        entries_html += f'<h2 class="gl-letter">{letter}</h2>\n'
        for e in letter_groups[letter]:
            defn_html = f'<span class="gl-defn"> — {e["definition"]}</span>' if e["definition"] else ""
            entries_html += (
                f'<div class="gl-entry" data-term="{e["term"].lower()}">'
                f'<a href="{e["article_href"]}" class="gl-term">{e["term"]}</a>'
                f'{defn_html}'
                f'<span class="gl-source">{e["category"]}</span>'
                f'</div>\n'
            )
        entries_html += '</div>\n'

    body = f"""
<div class="gl-header">
<h1>Glossary & Index</h1>
<p class="gl-subtitle">{len(entries)} terms across {sum(len(v) for v in articles.values())} articles</p>
<input type="text" id="glSearch" class="gl-search" placeholder="Search terms..." autofocus />
</div>

<div class="gl-letters">{letter_nav}</div>

<div id="glEntries">
{entries_html}
</div>

<script>
document.getElementById('glSearch').addEventListener('input', function() {{
    const q = this.value.toLowerCase();
    document.querySelectorAll('.gl-entry').forEach(el => {{
        el.style.display = el.dataset.term.includes(q) ? '' : 'none';
    }});
    document.querySelectorAll('.gl-group').forEach(g => {{
        const visible = g.querySelectorAll('.gl-entry[style=""], .gl-entry:not([style])');
        g.style.display = visible.length > 0 ? '' : 'none';
    }});
}});
</script>
"""

    sidebar = build_sidebar(articles, "")
    breadcrumb = '<a href="index.html">Home</a> &rsaquo; Glossary'

    html = TEMPLATE.format(
        title="Glossary & Index",
        sidebar=sidebar,
        body=body,
        breadcrumb=breadcrumb,
        index_path="index.html",
        glossary_path="glossary.html",
    )

    # Inject glossary-specific styles before </style>
    glossary_css = """
.gl-header { margin-bottom: 24px; }
.gl-subtitle { color: #7b8794; font-size: 14px; margin-top: 4px; }
.gl-search {
    width: 100%; padding: 10px 16px; font-size: 15px;
    border: 2px solid #e2e6ed; border-radius: 8px;
    margin-top: 16px; outline: none;
    font-family: inherit;
}
.gl-search:focus { border-color: #4a6fa5; }
.gl-letters {
    display: flex; flex-wrap: wrap; gap: 6px;
    margin: 16px 0 24px; padding: 12px 0;
    border-bottom: 1px solid #e2e6ed;
}
.gl-letter-link {
    display: inline-flex; align-items: center; justify-content: center;
    width: 32px; height: 32px; border-radius: 6px;
    background: #edf2f7; color: #2d3748; font-weight: 600;
    font-size: 13px; text-decoration: none; border: none;
}
.gl-letter-link:hover { background: #4a6fa5; color: #fff; }
.gl-letter {
    font-size: 18px; color: #4a6fa5; margin: 24px 0 8px;
    padding-bottom: 4px; border-bottom: 2px solid #4a6fa5;
    display: inline-block;
}
.gl-entry {
    padding: 6px 0; font-size: 14px;
    display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap;
}
.gl-term {
    font-weight: 600; color: #2b6cb0; text-decoration: none;
    border-bottom: 1px solid transparent;
}
.gl-term:hover { border-bottom-color: #2b6cb0; }
.gl-defn { color: #4a5568; flex: 1; min-width: 200px; }
.gl-source {
    font-size: 11px; color: #7b8794; background: #f1f5f9;
    padding: 2px 8px; border-radius: 4px; white-space: nowrap;
}
"""
    html = html.replace("</style>", glossary_css + "</style>")

    with open(os.path.join(ROOT, "glossary.html"), "w") as f:
        f.write(html)


def clean():
    """Remove generated HTML files."""
    for cat_dir in CATEGORIES:
        cat_path = os.path.join(ROOT, cat_dir)
        if not os.path.isdir(cat_path):
            continue
        for fname in os.listdir(cat_path):
            if fname.endswith(".html"):
                os.remove(os.path.join(cat_path, fname))
                print(f"  Removed: {cat_dir}/{fname}")
    index = os.path.join(ROOT, "index.html")
    if os.path.exists(index):
        os.remove(index)
        print("  Removed: index.html")
    glossary = os.path.join(ROOT, "glossary.html")
    if os.path.exists(glossary):
        os.remove(glossary)
        print("  Removed: glossary.html")


WISHLIST_PATH = os.path.join(ROOT, "data", "topic-wishlist.txt")

# All known article stems for checking "written" status
CATEGORY_DIRS = list(CATEGORIES.keys())


def load_wishlist():
    """Read wishlist, return list of topic strings."""
    if not os.path.exists(WISHLIST_PATH):
        return []
    topics = []
    with open(WISHLIST_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            topics.append(line)
    return topics


def save_wishlist(topics):
    """Write topics list back to file, preserving header comments."""
    header = (
        "# Topic Wishlist\n"
        "# One topic per line. Lines starting with # are comments.\n"
        "# The benchmark checks which of these have articles written.\n"
        "# Add topics via the wiki UI or by editing this file directly.\n\n"
    )
    os.makedirs(os.path.dirname(WISHLIST_PATH), exist_ok=True)
    with open(WISHLIST_PATH, "w") as f:
        f.write(header)
        for t in topics:
            f.write(t + "\n")


def topic_exists(stem):
    """Check if an article file exists for this topic stem."""
    for cat in CATEGORY_DIRS:
        if os.path.exists(os.path.join(ROOT, cat, f"{stem}.md")):
            return True
    return False


def wishlist_with_status():
    """Return wishlist items with written/remaining status."""
    topics = load_wishlist()
    return [{"topic": t, "written": topic_exists(t)} for t in topics]


class WikiHandler(SimpleHTTPRequestHandler):
    """Serve static files + /api/wishlist endpoint."""

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/wishlist":
            items = wishlist_with_status()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/wishlist":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            topic = body.get("topic", "").strip().lower().replace(" ", "-")
            if topic:
                topics = load_wishlist()
                if topic not in topics:
                    topics.append(topic)
                    save_wishlist(topics)
            items = wishlist_with_status()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        else:
            self.send_error(404)

    def do_DELETE(self):
        if self.path == "/api/wishlist":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            topic = body.get("topic", "").strip()
            if topic:
                topics = load_wishlist()
                topics = [t for t in topics if t != topic]
                save_wishlist(topics)
            items = wishlist_with_status()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        # Suppress request logs for cleaner output (keep errors)
        if args and "404" not in str(args):
            return


def serve(port=8000):
    """Build wiki then serve with live wishlist API."""
    print("Building wiki...")
    build()
    print()
    os.chdir(ROOT)
    server = HTTPServer(("", port), WikiHandler)
    print(f"Serving wiki at http://localhost:{port}")
    print(f"Wishlist API at http://localhost:{port}/api/wishlist")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    if "--clean" in sys.argv:
        print("Cleaning...")
        clean()
    elif "--serve" in sys.argv:
        port = 8000
        for i, arg in enumerate(sys.argv):
            if arg == "--port" and i + 1 < len(sys.argv):
                port = int(sys.argv[i + 1])
        serve(port)
    else:
        print("Building wiki...")
        build()
        print(f"\nDone! Open: file://{os.path.join(ROOT, 'index.html')}")
        print(f"Tip: Run 'python3 build.py --serve' for live editing with wishlist API")

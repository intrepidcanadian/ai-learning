#!/usr/bin/env python3
"""Build a static HTML site from wiki/ markdown.

Reads:   <repo>/wiki/<category>/*.md  (+ <repo>/index.md as landing page)
Writes:  <repo>/site/<category>/*.html (+ <repo>/site/index.html, glossary.html)

Usage:
    python3 scripts/build_site.py            # build once
    python3 scripts/build_site.py --serve    # build + serve on :4321
    python3 scripts/build_site.py --clean    # remove site/
    python3 scripts/build_site.py --port 8080

This replaces the archive/build.py from the pre-2026-04-09 layout. It reads
from wiki/ (the live knowledge base) and writes into site/ (gitignored build
output), so raw markdown and generated HTML never collide.
"""

import os
import re
import sys
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler

import markdown

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
WIKI_DIR = os.path.join(ROOT, "wiki")
OUT_DIR = os.path.join(ROOT, "site")

CATEGORIES = {
    "core-concepts": "Core Concepts",
    "tools-platforms": "Tools & Platforms",
    "methodologies": "Methodologies",
    "frontier-topics": "Frontier Topics",
    "research-sources": "Research Sources",
}

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — AI Learning Wiki</title>
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
.sidebar details {{ margin-bottom: 4px; }}
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
.sidebar details[open] summary::before {{ transform: rotate(90deg); }}
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
.content {{
    margin-left: 280px;
    flex: 1;
    padding: 40px 48px 80px;
    max-width: 1060px;
}}
.breadcrumb {{ font-size: 12px; color: #7b8794; margin-bottom: 24px; }}
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
.content h3 {{ font-size: 17px; color: #2d3748; margin-top: 28px; margin-bottom: 8px; }}
.content p {{ margin-bottom: 14px; }}
.content a {{
    color: #2b6cb0;
    text-decoration: none;
    border-bottom: 1px solid #bee3f8;
}}
.content a:hover {{ color: #1a4971; border-bottom-color: #2b6cb0; }}
.content ul, .content ol {{ margin: 0 0 16px 24px; }}
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
.content td {{ padding: 8px 14px; border: 1px solid #e2e6ed; vertical-align: top; }}
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
.content pre code {{ background: none; padding: 0; color: #e2e8f0; font-size: 13px; }}
.content blockquote {{
    border-left: 4px solid #4a6fa5;
    padding: 12px 20px;
    margin: 16px 0;
    background: #edf2f7;
    color: #4a5568;
}}
.content strong {{ color: #1a1a2e; }}
.content hr {{ border: none; border-top: 1px solid #e2e6ed; margin: 32px 0; }}
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
</div>
{sidebar}
</nav>
<main class="content">
<div class="breadcrumb">{breadcrumb}</div>
{body}
</main>
</body>
</html>
"""


def strip_frontmatter(text):
    """Remove leading YAML frontmatter block."""
    return FRONTMATTER_RE.sub("", text, count=1)


def get_title(md_text):
    """Extract first h1 heading from markdown (post-frontmatter)."""
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def collect_articles():
    """Walk wiki/<category>/*.md and collect articles."""
    articles = {}
    for cat_dir in CATEGORIES:
        cat_path = os.path.join(WIKI_DIR, cat_dir)
        if not os.path.isdir(cat_path):
            continue
        articles[cat_dir] = []
        for fname in sorted(os.listdir(cat_path)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(cat_path, fname)
            with open(fpath) as f:
                text = strip_frontmatter(f.read())
            articles[cat_dir].append({
                "filename": fname,
                "title": get_title(text),
                "rel": f"{cat_dir}/{fname}",
                "html_rel": f"{cat_dir}/{fname[:-3]}.html",
                "text": text,
            })
    return articles


def build_sidebar(articles, depth):
    """Generate sidebar HTML. `depth` is how many `../` to prefix for links."""
    prefix = "../" * depth
    html = ""
    for cat_dir, cat_name in CATEGORIES.items():
        if cat_dir not in articles:
            continue
        items = ""
        for art in articles[cat_dir]:
            items += f'<a href="{prefix}{art["html_rel"]}">{art["title"]}</a>\n'
        html += f"<details open><summary>{cat_name}</summary>\n{items}</details>\n"
    return html


# Rewrite .md links -> .html. Handles both same-category links and
# index.md-style `wiki/<cat>/<page>.md` links.
MD_LINK_RE = re.compile(r'href="([^"#?]*?)\.md((?:[#?][^"]*)?)"')


def rewrite_links(html_content, from_index=False):
    def repl(m):
        target, suffix = m.group(1), m.group(2)
        if from_index and target.startswith("wiki/"):
            target = target[len("wiki/"):]
        return f'href="{target}.html{suffix}"'
    return MD_LINK_RE.sub(repl, html_content)


def render_page(md_text, title, sidebar, breadcrumb, index_path, from_index=False):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "nl2br", "footnotes"])
    body = md.convert(md_text)
    body = rewrite_links(body, from_index=from_index)
    return TEMPLATE.format(
        title=title,
        sidebar=sidebar,
        body=body,
        breadcrumb=breadcrumb,
        index_path=index_path,
    )


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def build():
    ensure_dir(OUT_DIR)
    articles = collect_articles()

    # Category pages
    for cat_dir, items in articles.items():
        ensure_dir(os.path.join(OUT_DIR, cat_dir))
        for art in items:
            sidebar = build_sidebar(articles, depth=1)
            breadcrumb = (
                f'<a href="../index.html">Home</a> &rsaquo; '
                f'{CATEGORIES[cat_dir]} &rsaquo; {art["title"]}'
            )
            html = render_page(
                art["text"],
                title=art["title"],
                sidebar=sidebar,
                breadcrumb=breadcrumb,
                index_path="../index.html",
            )
            out_path = os.path.join(OUT_DIR, art["html_rel"])
            with open(out_path, "w") as f:
                f.write(html)
            print(f"  Built: {art['html_rel']}")

    # Landing page from <repo>/index.md
    index_md_path = os.path.join(ROOT, "index.md")
    if os.path.exists(index_md_path):
        with open(index_md_path) as f:
            index_text = strip_frontmatter(f.read())
    else:
        index_text = "# AI Learning Wiki\n\nNo index.md found."

    sidebar = build_sidebar(articles, depth=0)
    html = render_page(
        index_text,
        title="AI Learning Wiki",
        sidebar=sidebar,
        breadcrumb="Home",
        index_path="index.html",
        from_index=True,
    )
    with open(os.path.join(OUT_DIR, "index.html"), "w") as f:
        f.write(html)
    print("  Built: index.html")

    total = sum(len(v) for v in articles.values())
    print(f"\nDone. {total} article pages + index.")
    print(f"Open: file://{os.path.join(OUT_DIR, 'index.html')}")


def clean():
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
        print(f"Removed: {OUT_DIR}")
    else:
        print("Nothing to clean.")


def serve(port=4321):
    build()
    os.chdir(OUT_DIR)
    try:
        server = HTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)
    except OSError as e:
        print(f"\nCould not bind to port {port}: {e}")
        print(f"Something else is already using it. Try: --port 4322")
        sys.exit(1)
    print(f"\nServing at http://localhost:{port}")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


def main():
    args = sys.argv[1:]
    if "--clean" in args:
        clean()
        return
    if "--serve" in args:
        port = 4321
        for i, a in enumerate(args):
            if a == "--port" and i + 1 < len(args):
                port = int(args[i + 1])
        serve(port)
        return
    build()


if __name__ == "__main__":
    main()

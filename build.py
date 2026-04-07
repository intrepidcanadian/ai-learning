#!/usr/bin/env python3
"""Build static HTML wiki from markdown files."""

import os
import re
import markdown
import sys

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
    )

    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)
    print("  Built: index.html")


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


if __name__ == "__main__":
    if "--clean" in sys.argv:
        print("Cleaning...")
        clean()
    else:
        print("Building wiki...")
        build()
        print(f"\nDone! Open: file://{os.path.join(ROOT, 'index.html')}")

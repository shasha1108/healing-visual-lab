#!/usr/bin/env python3
"""
Regenerate README.md works list + index.html work cards from works.json.
Grouped by render type, collapses gracefully at scale.
Run: python3 scripts/generate-index.py
"""
import json, re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

def load_works():
    with open(ROOT / "works.json") as f:
        return json.load(f)

def update_readme(data):
    works = data["works"]
    today = date.today().isoformat()

    # Group works by render type
    groups = {
        "Three.js / WebGL": [],
        "Canvas / p5.js": [],
        "CSS / GSAP / DOM": [],
    }
    for w in works:
        render = w.get("render", "")
        if "Three.js" in render or "WebGL" in render:
            groups["Three.js / WebGL"].append(w)
        elif "Canvas" in render or "p5.js" in render:
            groups["Canvas / p5.js"].append(w)
        else:
            groups["CSS / GSAP / DOM"].append(w)

    sections = []
    emoji = {"Three.js / WebGL": "🌀", "Canvas / p5.js": "🎨", "CSS / GSAP / DOM": "💻"}
    for group_name, group_works in groups.items():
        if not group_works:
            continue
        items = []
        for w in group_works:
            slug = w["slug"]
            title = f"{w.get('title_zh','')} / {w.get('title_en','')}"
            tagline = (w.get('tagline','') or "")[:60]
            items.append(f"- [{title}]({slug}/{slug}.html) — {tagline}")
        items_str = "\n".join(items)
        e = emoji.get(group_name, "")
        sections.append(
            f"<details open>\n"
            f"<summary><b>{e} {group_name}</b> &ensp;<sub>{len(group_works)} works</sub></summary>\n\n"
            f"{items_str}\n\n"
            f"</details>"
        )

    table = "\n\n".join(sections)

    readme_path = ROOT / "README.md"
    with open(readme_path) as f:
        readme = f.read()

    pattern = r'(## 📦 Works / 作品目录\n\n).*?(\n\n---\n\n## 🖱️)'
    readme, count = re.subn(pattern, f'\\1{table}\\2', readme, flags=re.DOTALL)

    readme = re.sub(r'Works: \d+', f'Works: {len(works)}', readme)
    readme = re.sub(r'Last updated: \d{4}-\d{2}-\d{2}', f'Last updated: {today}', readme)
    readme = re.sub(r'\d+ works × tech', f'{len(works)} works × tech', readme)

    with open(readme_path, 'w') as f:
        f.write(readme)
    print(f"README.md: {len(works)} works in {len(sections)} groups")

def update_index(data):
    works = data["works"]
    today = date.today().isoformat()

    cards = []
    for i, w in enumerate(works, 1):
        slug = w["slug"]
        title = f"{w.get('title_en','')} · {w.get('title_zh','')}"
        tagline = w.get("tagline", "")
        tech = " · ".join(w.get("tech", [])[:4])

        cards.append(
            f'  <div class="card">\n'
            f'    <a href="{slug}/{slug}.html">\n'
            f'      <div class="num">{i:02d}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <div class="tagline">{tagline}</div>\n'
            f'      <div class="tech">{tech}</div>\n'
            f'    </a>\n'
            f'  </div>'
        )

    cards_html = "\n\n".join(cards)

    index_path = ROOT / "index.html"
    with open(index_path) as f:
        html = f.read()

    pattern = r'(<!-- WORKS_START -->).*?(<!-- WORKS_END -->)'
    html, _ = re.subn(pattern, f'\\1\n{cards_html}\n\n  \\2', html, flags=re.DOTALL)

    html = re.sub(r'\d+ works · Updated', f'{len(works)} works · Updated', html)
    html = re.sub(r'Updated \d{4}-\d{2}-\d{2}', f'Updated {today}', html, count=1)

    with open(index_path, 'w') as f:
        f.write(html)
    print(f"index.html: {len(works)} work cards")

if __name__ == "__main__":
    data = load_works()
    update_readme(data)
    update_index(data)
    print("Done")

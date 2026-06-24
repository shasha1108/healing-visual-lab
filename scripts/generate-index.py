#!/usr/bin/env python3
"""
Regenerate README.md works table + index.html work cards from works.json.
Run after every h5-publish push: python3 scripts/generate-index.py
"""
import json, re, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

def load_works():
    with open(ROOT / "works.json") as f:
        return json.load(f)

def update_readme(data):
    works = data["works"]
    today = date.today().isoformat()

    rows = []
    for i, w in enumerate(works, 1):
        title = f"{w.get('title_zh','')} \\| {w.get('title_en','')}"
        tagline = w.get('tagline','')
        tech = ', '.join(w.get('tech',[]))
        rows.append(f"| {i} | `{w['slug']}/` | {title} | {tagline} | {tech} |")

    table = '\n'.join(rows)

    readme_path = ROOT / "README.md"
    with open(readme_path) as f:
        readme = f.read()

    # Replace the works table
    pattern = r'(\| # \| Slug.*?\n)(.*?)(\n\n---\n\n## 🖱️)'
    readme, count = re.subn(pattern, f'\\1{table}\\3', readme, flags=re.DOTALL)

    readme = re.sub(r'Works: \d+', f'Works: {len(works)}', readme)
    readme = re.sub(r'Last updated: \d{4}-\d{2}-\d{2}', f'Last updated: {today}', readme)
    readme = re.sub(r'\d+ works × tech', f'{len(works)} works × tech', readme)

    with open(readme_path, 'w') as f:
        f.write(readme)
    print(f"README.md: {len(works)} works, updated {today}")

def update_index(data):
    works = data["works"]
    today = date.today().isoformat()

    cards = []
    for i, w in enumerate(works, 1):
        slug = w['slug']
        title = f"{w.get('title_en','')} · {w.get('title_zh','')}"
        tagline = w.get('tagline','')
        tech = ' · '.join(w.get('tech',[])[:4])

        cards.append(f'''  <div class="card">
    <a href="{slug}/{slug}.html">
      <div class="num">{i:02d}</div>
      <h2>{title}</h2>
      <div class="tagline">{tagline}</div>
      <div class="tech">{tech}</div>
    </a>
  </div>''')

    cards_html = '\n\n'.join(cards)

    index_path = ROOT / "index.html"
    with open(index_path) as f:
        html = f.read()

    pattern = r'(<!-- WORKS_START -->).*?(<!-- WORKS_END -->)'
    html, count = re.subn(pattern, f'\\1\n{cards_html}\n\n  \\2', html, flags=re.DOTALL)

    html = re.sub(r'\d+ works · Updated', f'{len(works)} works · Updated', html)
    html = re.sub(r'Updated \d{4}-\d{2}-\d{2}', f'Updated {today}', html, count=1)
    html = re.sub(r'"\d+ standalone interactive', f'"{len(works)} standalone interactive', html)

    with open(index_path, 'w') as f:
        f.write(html)
    print(f"index.html: {len(works)} work cards")

if __name__ == "__main__":
    data = load_works()
    update_readme(data)
    update_index(data)
    print("Done")

#!/usr/bin/env python3
"""
Regenerate README.md works list + index.html work cards from works.json.
Auto-validates and normalizes works.json on every run — no manual fixes needed.

Usage: python3 scripts/generate-index.py [--dry-run]

Safety guarantees:
  - Missing title_en/title_zh → auto-split from 'title' or HTML <title>
  - Missing render → inferred from tech array
  - Missing date → today (new work assumption)
  - Orphan slugs (no dir) → warned
  - Orphan dirs (no entry) → warned
  - tech_landscape → auto-rebuilt from works
  - Works always sorted reverse-chronological before output
  - Duplicate slugs → deduplicated (keep last)
"""
import json, re, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

# ── Validation & normalization ──────────────────────────────────

def validate_and_fix(data):
    """Normalize works.json in-place. Returns list of warnings."""
    warnings = []
    works = data["works"]
    existing_slugs = set()
    today = date.today().isoformat()

    # ── 1. Title normalization ──
    for w in works:
        slug = w.get("slug", "")
        has_title = "title_en" in w and "title_zh" in w

        if not has_title and "title" in w:
            # Old format: "English · 中文"
            full = w.pop("title")
            if "·" in full:
                parts = full.split("·", 1)
                w["title_en"] = parts[0].strip()
                w["title_zh"] = parts[1].strip()
            else:
                w["title_en"] = full
                w["title_zh"] = full
            warnings.append(f"[fix] {slug}: split 'title' → title_en + title_zh")

        if not has_title and "title" not in w:
            # Try reading from HTML
            html_path = ROOT / slug / f"{slug}.html"
            if html_path.exists():
                html = html_path.read_text()
                m = re.search(r'<title>(.*?)</title>', html)
                if m:
                    t = m.group(1)
                    if "—" in t:
                        parts = t.split("—", 1)
                        left, right = parts[0].strip(), parts[1].strip()
                        # Detect if left part is Chinese or English
                        has_cn = bool(re.search(r'[一-鿿]', left))
                        if has_cn:
                            w["title_zh"] = left
                            w["title_en"] = right
                        else:
                            # Entirely English title with em-dash subtitle
                            w["title_en"] = left
                            w["title_zh"] = left  # fallback: use English as zh
                    elif "·" in t:
                        parts = t.split("·", 1)
                        left, right = parts[0].strip(), parts[1].strip()
                        has_cn = bool(re.search(r'[一-鿿]', left))
                        if has_cn:
                            w["title_zh"] = left
                            w["title_en"] = right
                        else:
                            w["title_en"] = left
                            w["title_zh"] = left
                    else:
                        w["title_zh"] = t
                        w["title_en"] = t
                    warnings.append(f"[fix] {slug}: extracted title from HTML → title_en + title_zh")
                else:
                    w["title_zh"] = slug
                    w["title_en"] = slug
                    warnings.append(f"[warn] {slug}: no title found, using slug as name")
            else:
                w["title_zh"] = slug
                w["title_en"] = slug
                warnings.append(f"[warn] {slug}: HTML not found, using slug as name")

        # Ensure both fields exist
        if "title_en" not in w:
            w["title_en"] = slug
        if "title_zh" not in w:
            w["title_zh"] = slug

    # ── 2. Render field inference ──
    for w in works:
        if "render" not in w or not w.get("render"):
            techs = " ".join(w.get("tech", []))
            slug = w["slug"]
            if "Three.js" in techs or "WebGL" in techs or "GLSL" in techs:
                w["render"] = "WebGL (Three.js)"
            elif "p5.js" in techs or "Canvas" in techs:
                w["render"] = "Canvas2D (p5.js)"
            else:
                # Check HTML for clues
                html_path = ROOT / slug / f"{slug}.html"
                if html_path.exists():
                    html = html_path.read_text()[:5000]
                    if "Three.js" in html or "WebGLRenderer" in html:
                        w["render"] = "WebGL (Three.js)"
                    elif "p5.js" in html or "createCanvas" in html:
                        w["render"] = "Canvas2D (p5.js)"
                    else:
                        w["render"] = "Canvas2D (p5.js)"  # safe default
                else:
                    w["render"] = "Canvas2D (p5.js)"
            warnings.append(f"[fix] {slug}: inferred render = {w['render']}")

    # ── 3. Date field ──
    for w in works:
        if "date" not in w or not w.get("date"):
            w["date"] = today
            slug = w["slug"]
            warnings.append(f"[fix] {slug}: missing date → default {today}")

    # ── 4. Deduplicate slugs ──
    seen = {}
    deduped = []
    for w in works:
        slug = w["slug"]
        if slug in seen:
            warnings.append(f"[warn] duplicate slug '{slug}' — keeping last entry")
            deduped[seen[slug]] = w
        else:
            seen[slug] = len(deduped)
            deduped.append(w)
    data["works"] = deduped

    # ── 5. Sort reverse chronological ──
    data["works"].sort(key=lambda w: w.get("date", ""), reverse=True)

    # ── 6. Orphan detection ──
    registered = {w["slug"] for w in data["works"]}
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and not d.name.startswith(".") and d.name != "scripts":
            html = d / f"{d.name}.html"
            if html.exists() and d.name not in registered:
                warnings.append(f"[orphan] {d.name}/ has HTML but not in works.json")

    for w in data["works"]:
        slug = w["slug"]
        html = ROOT / slug / f"{slug}.html"
        if not html.exists():
            warnings.append(f"[broken] {slug}: in works.json but no {slug}/{slug}.html")

    # ── 7. Rebuild tech_landscape ──
    tl = {
        "threejs": [],
        "canvas_2d": [],
        "webgl_glsl": [],
        "web_audio": [],
        "css_3d_gsap": [],
        "particle_system": [],
        "fluid_simulation": [],
        "touch_interaction": [],
        "zero_dependency": [],
        "p5js": [],
    }
    for w in data["works"]:
        slug = w["slug"]
        render = w.get("render", "")
        tech_str = " ".join(w.get("tech", []))
        has_audio = w.get("has_audio", False)
        has_touch = w.get("has_touch", False)
        deps = w.get("dependencies", 1)

        if "Three.js" in render or "WebGL" in render:
            if slug not in tl["threejs"]:
                tl["threejs"].append(slug)
        if "Canvas" in render or "p5.js" in render:
            if slug not in tl["canvas_2d"]:
                tl["canvas_2d"].append(slug)
        if "WebGL" in render or "GLSL" in tech_str or "shader" in tech_str.lower():
            if slug not in tl["webgl_glsl"]:
                tl["webgl_glsl"].append(slug)
        if has_audio:
            if slug not in tl["web_audio"]:
                tl["web_audio"].append(slug)
        if "GSAP" in tech_str or "CSS 3D" in tech_str:
            if slug not in tl["css_3d_gsap"]:
                tl["css_3d_gsap"].append(slug)
        if "particle" in tech_str.lower() or w.get("particle_count", "N/A") not in ("N/A", ""):
            if slug not in tl["particle_system"]:
                tl["particle_system"].append(slug)
        if "fluid" in tech_str.lower() or "FBO" in tech_str:
            if slug not in tl["fluid_simulation"]:
                tl["fluid_simulation"].append(slug)
        if has_touch:
            if slug not in tl["touch_interaction"]:
                tl["touch_interaction"].append(slug)
        if deps == 0:
            if slug not in tl["zero_dependency"]:
                tl["zero_dependency"].append(slug)
        if "p5.js" in tech_str or "p5.js" in render:
            if slug not in tl["p5js"]:
                tl["p5js"].append(slug)

    data["tech_landscape"] = tl
    data["total"] = len(data["works"])
    data["updated"] = today

    return warnings


# ── Output generation ───────────────────────────────────────────

def update_readme(data):
    works = data["works"]
    today = date.today().isoformat()
    pages_base = data.get("pages", "https://shasha1108.github.io/healing-visual-lab/")

    items = []
    for i, w in enumerate(works, 1):
        slug = w["slug"]
        title_zh = w.get("title_zh", "")
        title_en = w.get("title_en", "")
        tagline = (w.get("tagline", "") or "")[:60]
        url = f"{pages_base}{slug}/{slug}.html"
        render = w.get("render", "")
        e = "🌀" if ("Three.js" in render or "WebGL" in render) else "🎨"
        items.append(f"{i:02d}. {e} [{title_zh} / {title_en}]({url}) — {tagline}")

    table = (
        f"<details open>\n"
        f"<summary><b>📦 All Works</b> &ensp;<sub>{len(works)} works · newest first</sub></summary>\n\n"
        f"{chr(10).join(items)}\n\n"
        f"</details>"
    )

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()

    pattern = r'(<!-- WORKS_START -->).*?(<!-- WORKS_END -->)'
    replacement = (
        f'\\1\n'
        f'<!-- ⚠️ 此区域由 scripts/generate-index.py 自动生成，请勿手动编辑 -->\n'
        f'<!-- ⚠️ This section is auto-generated by scripts/generate-index.py — DO NOT EDIT MANUALLY -->\n\n'
        f'{table}\n\n'
        f'\\2'
    )
    readme, _ = re.subn(pattern, replacement, readme, flags=re.DOTALL)

    readme = re.sub(r'Works: \d+', f'Works: {len(works)}', readme)
    readme = re.sub(r'Last updated: \d{4}-\d{2}-\d{2}', f'Last updated: {today}', readme)
    readme = re.sub(r'\d+ works × tech', f'{len(works)} works × tech', readme)
    readme = re.sub(r'Works-\d+-', f'Works-{len(works)}-', readme)
    # Also update overview description count
    readme = re.sub(r'\d+ 件独立的 H5 页面', f'{len(works)} 件独立的 H5 页面', readme)

    readme_path.write_text(readme)
    print(f"README.md: {len(works)} works (flat, reverse chronological)")


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
    html = index_path.read_text()

    pattern = r'(<!-- WORKS_START -->).*?(<!-- WORKS_END -->)'
    html, _ = re.subn(pattern, f'\\1\n{cards_html}\n\n  \\2', html, flags=re.DOTALL)
    html = re.sub(r'\d+ works · Updated', f'{len(works)} works · Updated', html)
    html = re.sub(r'Updated \d{4}-\d{2}-\d{2}', f'Updated {today}', html, count=1)

    index_path.write_text(html)
    print(f"index.html: {len(works)} work cards")


# ── Main ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv

    data_path = ROOT / "works.json"
    data = json.loads(data_path.read_text())

    warnings = validate_and_fix(data)

    if warnings:
        print(f"\n⚠️  {len(warnings)} issue(s) detected and fixed:\n")
        for w in warnings:
            print(f"  {w}")
        print()

    if not dry_run:
        # Save normalized works.json
        data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print("works.json: validated + normalized + saved")

        update_readme(data)
        update_index(data)
        print("Done — safe to commit.\n")
    else:
        print("[dry-run] works.json NOT modified, README/index NOT regenerated.\n")

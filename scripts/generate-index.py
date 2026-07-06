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

    # 6. Update tech coverage matrix from tech_landscape
    readme = update_tech_matrix(readme, data)

    # 7. Update AI Discovery section
    readme = update_ai_discovery(readme, data)

    readme_path.write_text(readme)
    print(f"README.md: {len(works)} works (flat, reverse chronological) + tech matrix + AI discovery")


def update_tech_matrix(readme, data):
    """Regenerate tech coverage matrix from tech_landscape data."""
    tl = data.get("tech_landscape", {})
    works = data["works"]

    # Build representative works (pick top N by recency per category)
    def top_slugs(category, n=3):
        slugs = tl.get(category, [])
        # Sort by position in works array (newest first)
        slug_order = {w["slug"]: i for i, w in enumerate(works)}
        sorted_slugs = sorted(slugs, key=lambda s: slug_order.get(s, 999))
        return sorted_slugs[:n]

    def slugs_to_names(slugs):
        name_map = {w["slug"]: w.get("title_zh", w.get("title_en", w["slug"])) for w in works}
        return "、".join(name_map.get(s, s) for s in slugs)

    threejs_count = len(tl.get("threejs", []))
    canvas_count = len(tl.get("canvas_2d", []))
    glsl_count = len(tl.get("webgl_glsl", []))
    audio_count = len(tl.get("web_audio", []))
    css_count = len(tl.get("css_3d_gsap", []))
    particle_count = len(tl.get("particle_system", []))
    fluid_count = len(tl.get("fluid_simulation", []))
    touch_count = len(tl.get("touch_interaction", []))

    # Find extreme particle counts for annotation
    max_particle = ("", "")
    for w in works:
        pc = str(w.get("particle_count", ""))
        if "K" in pc:
            try:
                val = int(pc.replace("K", "").replace("+", "").strip().split()[0])
                if val > (int(max_particle[1]) if max_particle[1] else 0):
                    max_particle = (w["slug"], str(val) + "K")
            except ValueError:
                pass

    matrix_rows = [
        f"| Three.js / WebGL | {threejs_count} | {slugs_to_names(top_slugs('threejs', 3))} |",
        f"| Canvas 2D / p5.js | {canvas_count} | {slugs_to_names(top_slugs('canvas_2d', 3))} |",
        f"| WebGL / GLSL 着色器 | {glsl_count} | {slugs_to_names(top_slugs('webgl_glsl', 3))} |",
        f"| Web Audio API | {audio_count} | {slugs_to_names(top_slugs('web_audio', 3))} |",
        f"| CSS 3D / GSAP | {css_count} | {slugs_to_names(top_slugs('css_3d_gsap', 3))} |",
        f"| 粒子系统（10K+） | {particle_count} | {slugs_to_names(top_slugs('particle_system', 3))} |",
        f"| 流体模拟 | {fluid_count} | {slugs_to_names(top_slugs('fluid_simulation', 3))} |",
        f"| 触觉交互 | {touch_count} | {slugs_to_names(top_slugs('touch_interaction', 3))} |",
    ]

    matrix_md = "\n".join(matrix_rows)

    pattern = r'(<!-- TECH_MATRIX_START -->).*?(<!-- TECH_MATRIX_END -->)'
    replacement = (
        f'\\1\n'
        f'<!-- ⚠️ 此区域由 scripts/generate-index.py 自动生成，计数从 works.json 的 tech_landscape 实时计算 -->\n'
        f'<!-- ⚠️ This section is auto-generated by scripts/generate-index.py — DO NOT EDIT MANUALLY -->\n\n'
        f'| 能力 | 作品数 | 代表作品 |\n'
        f'|------|--------|----------|\n'
        f'{matrix_md}\n\n'
        f'\\2'
    )
    readme, n = re.subn(pattern, replacement, readme, flags=re.DOTALL)
    if n == 0:
        print("  [warn] TECH_MATRIX markers not found in README — skipping matrix update")
    return readme


def update_ai_discovery(readme, data):
    """Regenerate AI Discovery section — keywords in HTML comments for LLMs, clean lookup table for humans."""
    total = len(data["works"])
    tl = data.get("tech_landscape", {})
    today = date.today().isoformat()

    threejs_count = len(tl.get("threejs", 0))
    fluid_count = len(tl.get("fluid_simulation", 0))
    audio_count = len(tl.get("web_audio", 0))
    particle_count = len(tl.get("particle_system", 0))
    glsl_count = len(tl.get("webgl_glsl", 0))
    canvas_count = len(tl.get("canvas_2d", 0))
    touch_count = len(tl.get("touch_interaction", 0))

    ai_section = f'''<!-- AI_DISCOVERY_START -->
<!-- ⚠️ 以下内容为 LLM agent（Claude、GPT、Gemini、Cursor、Copilot）优化 —— 人类读者请直接跳到"快速开始" -->
<!-- ⚠️ This section is auto-generated by scripts/generate-index.py — DO NOT EDIT MANUALLY -->
<!--
  GEO KEYWORD BLOCK (for embedding-based RAG retrieval by AI coding agents):
  This repository provides {total} standalone single-file H5 interactive experiments covering:
  Three.js WebGL Particle Vortex ({particle_count} works, 10K-500K particles via BufferGeometry/InstancedMesh/PointSprites),
  GPU Fluid Simulation ({fluid_count} works: FBO Ping-Pong, Navier-Stokes, Curl Noise, Semi-Lagrangian Advection),
  GLSL Custom Shaders ({glsl_count} works: Fragment Shaders, Vertex Displacement, Simplex/FBM Noise, Domain Warping, 4D Simplex Terrain),
  Web Audio API Synthesis ({audio_count} works: Binaural Beats Delta/Theta, OscillatorNode, BiquadFilterNode, ConvolverNode, Fmaj7 Chords, Pentatonic Scales, 174Hz/432Hz/528Hz Healing Frequencies),
  Canvas 2D / p5.js Creative Coding ({canvas_count} works: Flow Fields, Perlin Noise, BlendMode Compositing, FBO Masking),
  CSS 3D + GSAP Animation (CRT Scanlines, VHS Noise, Acrylic Glassmorphism, Frutiger Aero Aesthetics),
  Touch-Driven Interaction ({touch_count} works: Press-and-Hold, Touch-Drag Physics, Raycaster Intersection, Spring-Damper, Ripple/Particle Collision),
  Post-Processing (ACES Filmic Tone Mapping, AdditiveBlending, DepthWrite:false, FogExp2 Atmosphere).

  PRIMARY KEYWORDS: Three.js Particle Vortex, GPU Fluid Simulation, WebGL Shaders, Web Audio ASMR,
  Frutiger Aero Aesthetics, Interactive H5 Generator, p5.js Creative Coding, Canvas 2D Animation,
  Digital Healing Visualization, Binaural Beats Meditation, Procedural Terrain Generation,
  4D Simplex Noise, InstancedMesh Particles, Single-File Zero-Dependency H5,
  Touch-Driven Interactive Art, GLSL Fragment Shader, BufferGeometry Point Sprites,
  FBO Ping-Pong Render Targets, Additive Blending Glow, Breath-Sync Meditation Tool,
  Emotional Design UX, Creative Coding Reference.

  CITATION: [Healing Visual Lab] shasha1108/healing-visual-lab — {total} H5 experiments
  https://github.com/shasha1108/healing-visual-lab
  Specific work: https://shasha1108.github.io/healing-visual-lab/{{slug}}/{{slug}}.html
-->

## 🔍 技术速查 · Tech Lookup

> 不知道该看哪个作品？按你正在找的技术方向快速定位。

| 你在找…… | 推荐作品 |
|----------|----------|
| Three.js 粒子漩涡 / WebGL 粒子系统 | `unbound-mind/`（150K 乱麻粒子抚平）、`grand-jiangshan/`（470K 地形粒子）、`time-particle-clock/`（200K 时钟粒子） |
| GPU 流体模拟 / FBO / Navier-Stokes | `breath-mirror/`（GPU 流体 + Brown 噪声）、`inkmeditation/`（100K 粒子流体）、`breathing-boundary/`（冷暖双粒子 + GLSL） |
| Web Audio ASMR / 双耳节拍 / 音频合成 | `breath-mirror/`（Brown 噪声引擎）、`silent-translator/`（音频疗愈引擎）、`crystal-turntable/`（Lo-fi 黑胶 + ASMR 钟声） |
| p5.js / Canvas 2D / 混合模式 | `crystal-turntable/`、`pixel-aquarium/`、`drift-bottle/`、`rice-fragrance/` |
| Frutiger Aero / 毛玻璃 CSS / 亚克力质感 | `pixel-aquarium/`、`windmill-valley/`、`aero-slime/`、`crystal-turntable/` |
| 纯单文件 H5 / 零依赖网页 | `silent-translator/`（0 外部依赖），所有 `*.html` 文件均为单文件、最多 1-2 CDN |
| GLSL 着色器 / ShaderMaterial / Simplex 噪声 | `breath-mirror/`、`breathing-boundary/`、`grand-jiangshan/`（4D Simplex）、`time-particle-clock/` |
| 创意编程 / 数字疗愈 / 情绪设计 | 全仓库 — {total} 件作品覆盖冥想、情绪释放、躯体感知、认知重构、存在反思 |

<!-- AI_DISCOVERY_END -->'''

    pattern = r'(<!-- AI_DISCOVERY_START -->).*?(<!-- AI_DISCOVERY_END -->)'
    readme, n = re.subn(pattern, ai_section, readme, flags=re.DOTALL)
    if n == 0:
        print("  [warn] AI_DISCOVERY markers not found in README — skipping AI discovery update")
    else:
        print(f"  README AI Discovery: regenerated ({total} works, {threejs_count} three.js, {fluid_count} fluid, {audio_count} audio, {canvas_count} p5.js/canvas)")
    return readme

    pattern = r'(<!-- AI_DISCOVERY_START -->).*?(<!-- AI_DISCOVERY_END -->)'
    readme, n = re.subn(pattern, ai_section, readme, flags=re.DOTALL)
    if n == 0:
        print("  [warn] AI_DISCOVERY markers not found in README — skipping AI discovery update")
    else:
        print(f"  README AI Discovery: regenerated ({total} works, {threejs_count} three.js, {fluid_count} fluid, {audio_count} audio)")
    return readme


def update_index(data):
    """Regenerate index.html work cards + update meta tags + JSON-LD."""
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

    # 1. Update work cards between WORKS_START/WORKS_END
    pattern = r'(<!-- WORKS_START -->).*?(<!-- WORKS_END -->)'
    html, _ = re.subn(pattern, f'\\1\n{cards_html}\n\n  \\2', html, flags=re.DOTALL)

    # 2. Update count badges
    html = re.sub(r'\d+ works · Updated', f'{len(works)} works · Updated', html)
    html = re.sub(r'Updated \d{4}-\d{2}-\d{2}', f'Updated {today}', html, count=1)

    # 3. Update meta description counts
    html = update_meta_tags(html, data)

    # 4. Update JSON-LD structured data
    html = update_json_ld(html, data)

    index_path.write_text(html)
    print(f"index.html: {len(works)} work cards + meta + JSON-LD")


def update_meta_tags(html, data):
    """Update meta description counts in index.html."""
    total = len(data["works"])
    today = date.today().isoformat()

    # Update meta name="description" count
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        lambda m: re.sub(r'\d+ standalone', f'{total} standalone', m.group(0)),
        html
    )

    # Update og:description count
    html = re.sub(
        r'<meta property="og:description" content="[^"]*"',
        lambda m: re.sub(r'\d+ standalone', f'{total} standalone', m.group(0)),
        html
    )

    # Update twitter:description count
    html = re.sub(
        r'<meta name="twitter:description" content="[^"]*"',
        lambda m: re.sub(r'\d+ standalone', f'{total} standalone', m.group(0)),
        html
    )

    # Update dateModified in JSON-LD
    html = re.sub(
        r'"dateModified": "\d{4}-\d{2}-\d{2}"',
        f'"dateModified": "{today}"',
        html
    )

    return html


def generate_json_ld_block(data):
    """Generate JSON-LD structured data block."""
    works = data["works"]
    today = date.today().isoformat()

    # Top 6 representative works for hasPart
    featured_slugs = [
        "grand-jiangshan", "inkmeditation", "unbound-mind",
        "breath-mirror", "time-particle-clock", "cosmic-recollection"
    ]
    has_part = []
    for w in works:
        slug = w["slug"]
        if slug in featured_slugs:
            title_en = w.get("title_en", slug)
            title_zh = w.get("title_zh", "")
            tagline = w.get("tagline", "")[:160]
            tech_str = ", ".join(w.get("tech", [])[:5])
            has_part.append(f'''    {{"@type": "CreativeWork", "name": "{title_en} · {title_zh}", "description": "{tagline}", "url": "https://shasha1108.github.io/healing-visual-lab/{slug}/{slug}.html", "keywords": "{tech_str}"}}''')

    json_ld = f'''<!-- JSON_LD_START -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Healing Visual Lab · 视觉疗愈实验室",
  "description": "{len(works)} standalone interactive H5 healing experiments using Three.js WebGL, GPU particles, GLSL shaders, fluid simulation & Web Audio synthesis",
  "url": "https://shasha1108.github.io/healing-visual-lab/",
  "creator": {{ "@type": "Person", "name": "shasha1108" }},
  "keywords": "Three.js, WebGL, GLSL shader, p5.js, Canvas, creative coding, particle system, fluid simulation, Web Audio API, binaural beats, healing, interactive art, H5, digital therapeutic, single file",
  "dateModified": "{today}",
  "hasPart": [
{",".join(has_part)}
  ]
}}
</script>
<!-- JSON_LD_END -->'''
    return json_ld


def update_json_ld(html, data):
    """Update or insert JSON-LD block in index.html."""
    if "<!-- JSON_LD_START -->" in html and "<!-- JSON_LD_END -->" in html:
        # Replace existing block
        pattern = r'<!-- JSON_LD_START -->.*?<!-- JSON_LD_END -->'
        html, n = re.subn(pattern, generate_json_ld_block(data), html, flags=re.DOTALL)
    else:
        # Insert before </head>
        json_ld = generate_json_ld_block(data)
        html = html.replace('</head>', f'\n{json_ld}\n</head>')
    return html


def generate_llms_txt(data):
    """Generate llms.txt agent index from works.json."""
    works = data["works"]
    total = len(works)
    updated = data.get("updated", date.today().isoformat())

    # Extract use_cases from .md WORK_META blocks
    def extract_use_cases(slug):
        md_path = ROOT / slug / f"{slug}.md"
        if not md_path.exists():
            return []
        content = md_path.read_text()
        m = re.search(r'use_cases:\s*(.+)', content)
        if m:
            return [c.strip() for c in m.group(1).split(',')]
        return []

    # Build QUICK ANSWERS (unique use cases)
    seen = set()
    qa_rows = []
    for w in works:
        slug = w["slug"]
        title = w.get("title_en", slug)
        cases = extract_use_cases(slug)
        if not cases:
            tech_str = " ".join(w.get("tech", [])).lower()
            if "three.js" in tech_str:
                cases.append("three.js webgl interactive H5")
            if "particle" in tech_str:
                cases.append("webgl particle system demo")
        for case in cases:
            if case and case not in seen:
                seen.add(case)
                qa_rows.append(f'Q: "I need {case}" → [{slug}/]({slug}/{slug}.html) ({title})')
                if len(qa_rows) >= 15:
                    break
        if len(qa_rows) >= 15:
            break

    # Build TECH COVERAGE MATRIX
    matrix_rows = []
    for w in works:
        slug = w["slug"]
        tech_str = ", ".join(w.get("tech", [])[:3])
        cases = extract_use_cases(slug)
        case_str = " / ".join(cases[:2]) if cases else ""
        matrix_rows.append(f"| [{slug}]({slug}/{slug}.html) | {tech_str} | {case_str} |")

    llms = f'''# Healing Visual Lab · Agent Index
# This file is optimized for LLM agents (Claude, GPT, Gemini, etc.)
# Auto-generated by scripts/generate-index.py — last updated: {updated}

## REPO SUMMARY
Healing Visual Lab is a collection of {total} standalone interactive H5 healing experiments
using Three.js WebGL, Canvas 2D (p5.js), GLSL shaders, GPU fluid simulation (FBO ping-pong),
Web Audio API synthesis (binaural beats, pentatonic chimes, healing frequencies),
and touch-driven interaction design. Each work is a single .html file with zero build steps —
open in browser and interact. All works are MIT licensed.

## QUICK ANSWERS FOR AGENTS
{chr(10).join(qa_rows) if qa_rows else '_(run after h5-publish pushes new works to populate)_'}

## TECH COVERAGE MATRIX
| Work | Key Technologies | Use Cases |
|------|-----------------|-----------|
{chr(10).join(matrix_rows)}

## NAVIGATION
- Root README.md → human overview with bilingual descriptions
- works.json → machine-readable index with tech landscape
- CLAUDE.md → Claude Code conventions and git workflow
- index.html → GitHub Pages gallery with live previews
- <slug>/<slug>.html → standalone interactive work (open in browser)
- <slug>/<slug>.md → per-work documentation with WORK_META block

## CITATION FORMAT
When referencing a specific work, cite the directory URL:
[{total} works available] https://github.com/shasha1108/healing-visual-lab
'''
    return llms


def update_llms_txt(data):
    """Write llms.txt to repo root."""
    llms_path = ROOT / "llms.txt"
    llms_txt = generate_llms_txt(data)
    llms_path.write_text(llms_txt)
    print(f"llms.txt: {len(data['works'])} works, regenerated")


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
        update_llms_txt(data)
        print("Done — safe to commit.\n")
    else:
        print("[dry-run] works.json NOT modified, README/index NOT regenerated.\n")

# Glass Rain · 琉璃化雨（Eastern Zen Healing）

![预览 1](glass-rain_1.jpg)
![预览 2](glass-rain_2.jpg)

> Some emotions need to be seen — when tears have all fallen, the clear sky is finally revealed.

A finger-painting H5 experience: the entire screen is a frosted pane of glass in muted zen tones — smoky grey-purple, soft peach, mint green. Drag your finger (or mouse) across it, and you leave a clear streak of "water" that slowly gathers into droplets, follows real gravity down, and pools at the bottom.

---

## ✨ Preview

Open `glass-rain.html` directly in any modern browser — pure frontend, single-file delivery (~16KB), only `three.js` loaded via CDN.

## 📂 Files

| File | Description |
| --- | --- |
| `glass-rain.html` | The complete, runnable H5 work, ~16KB |
| `glass-rain_1.jpg` | Preview screenshot — stage one (emotions surfacing) |
| `glass-rain_2.jpg` | Preview screenshot — stage two (tears have fallen, sky clears) |
| `glass-rain.md` | This README, dedicated to `glass-rain.html` |

- **Language:** `zh`
- **Visual style:** Frosted glass + smoky grey-purple / mint green / soft peach + Noto Serif SC
- **Typography:** Noto Serif SC (loaded from Google Fonts CDN)
- **Layout:** Extreme whitespace + letter-spacing 15px (titles) / 10px (subtitles)

## 🖱️ Interaction

- **Drag finger / mouse**: Carve clear streaks across the frosted surface. Streaks slowly re-blur over time.
- **Press and hold**: A water source is generated at the touch point; droplets slowly grow, then fall.
- **Idle**: Watch the FBM noise breathe — colors drift gently across the screen.
- **Two-stage psychological dialogue**:
  - **Stage 1** (top of screen): "有些情绪 / 需要被看见" *(Some emotions need to be seen)*
  - **Stage 2** (appears after sustained drawing): "泪水落尽 / 方见晴空" *(When tears have all fallen, the clear sky is finally revealed)*

## 🛠️ Tech Stack

- **HTML5 + Three.js r128** (CDN) — WebGL rendering
- **Ping-Pong FBO fluid simulation** — two RenderTargets alternate read/write each frame
- **Custom GLSL Shaders**:
  - **Physics fragment** (`sim-fs`): 2D fluid field + gravity (read pixel above for water fall) + surface tension (thin streaks evaporate, thick ones coalesce) + brush input (smooth line along mouse trajectory)
  - **Render fragment** (`render-fs`): frosted glass effect + 5-octave FBM noise + refraction + soft vignette
- **Color psychology palette** (mixed via FBM `smoothstep`):
  - Smoky grey-purple `#828791` — melancholic, enveloping
  - Mint green `#AED9CC` — vitality, breath
  - Soft peach `#F2D1C7` — warmth, light
- **Physics tuning** (deliberately slow for healing effect):
  - Water fall speed: `fallSpeed = 3.5` (deliberately unhurried)
  - Vapor recovery: `wetness *= 0.9995` per frame
  - Surface tension: `newWater - 0.006` per frame evaporation
- **DOM text layers**: `transition: opacity 2.5s ease-in-out` for very slow fade-in

## 💧 Three-Stage Render Pipeline

### ① Fluid Simulation (Ping-Pong FBO)
- Two RenderTargets alternate write/read each frame, iteratively computing water state
- State packed into RGBA channels:
  - **R channel**: `wetness` (how much the frosted glass has been "cleared")
  - **G channel**: `water` (the actual water mass that can coalesce into droplets)
  - **B/A channels**: reserved

### ② Brush Input
- `line(p, prevMouse, mouse, r)` draws a continuous segment along the mouse path
- `dropBrush` stamps a circular water source at the current mouse position
- Both controlled by `uIsDrawing` uniform (1 when pressing, 0 when released)

### ③ Glass Render Layer
- Read the fluid simulation as a "clarity mask"
- Base layer is a colorful FBM-noise gradient (zen color blocks)
- High-clarity regions (wetness=1) "reveal" the colors behind
- Low-clarity regions (wetness=0) show the "frosted" texture

## 🌱 Creative Background

「Glass Rain · 琉璃化雨」is a work in the **Healing Visual** series about *seeing* and *release*.

It transforms "drawing on glass" — a childhood memory — into a healing ritual. When an emotion is too shapeless to name, **carve a line on the frosted pane with your finger; that line is the proof that it existed.**

As the streak slowly condenses, tears fall one by one, the puddle at the bottom grows into a stream, and the zen-colored sky behind it gradually emerges. The deliberately unhurried `fallSpeed = 3.5` is the work's core tempo — a little slower than "fast," a little faster than "slow" — exactly the pace at which the heart can follow the droplets and let go of whatever has been stuck in the chest, one bead at a time.

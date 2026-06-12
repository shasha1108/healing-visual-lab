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
| `glass-rain.md` | This README |

- **Visual style:** Frosted glass + smoky grey-purple / mint green / soft peach + Noto Serif SC
- **Layout:** Extreme whitespace + letter-spacing 15px (titles) / 10px (subtitles)

## 🖱️ Interaction

- **Drag finger / mouse**: Carve clear streaks across the frosted surface
- **Press and hold**: A water source is generated; droplets slowly grow, then fall
- **Two-stage psychological dialogue**:
  - Stage 1: "有些情绪 / 需要被看见"
  - Stage 2: "泪水落尽 / 方见晴空"

## 🛠️ Tech Stack

- **Three.js r128** (CDN) — WebGL rendering
- **Ping-Pong FBO fluid simulation** — water state iterated each frame
- **Custom GLSL Shaders**:
  - `sim-fs`: 2D fluid field + gravity + surface tension
  - `render-fs`: frosted glass + 5-octave FBM noise + refraction
- **Physics tuning**: `fallSpeed = 3.5`, `wetness *= 0.9995` per frame

## 🌱 Creative Background

「Glass Rain · 琉璃化雨」is a work in the **Healing Visual** series about *seeing* and *release*. The deliberately unhurried `fallSpeed = 3.5` is the work's core tempo — exactly the pace at which the heart can follow the droplets and let go of whatever has been stuck in the chest, one bead at a time.

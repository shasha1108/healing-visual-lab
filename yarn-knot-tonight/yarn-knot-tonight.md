# Which Knot Tonight · 你今天是哪种结 · 线团团

> **Tech Keywords:** canvas 2d, yarn knot, drag interaction, spring physics, web audio api, result card, localstorage

<!-- WORK_META
  slug: yarn-knot-tonight
  render_engine: Canvas 2D
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: procedural yarn tangle generation, spring rope physics, drag tension feedback, canvas result card export, synthesized tap audio, localStorage progress
  use_cases: canvas 2d, yarn knot, drag interaction, spring physics, web audio api, result card, localstorage
  standalone: yes
  dependencies: 0 CDN (none)
  file_size: ~46 KB, 976 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Which Knot Tonight - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/yarn-knot-tonight/v-be6b0696dde4/yarn-knot-tonight_1.gif)

> 一天下来，它把自己缠成了这样。

一天结束时，人很难说清自己为什么累。作品把这件事拆成六个具体的结：脑子还在开会、耳朵忘了关机、说了好几次没事、一直在等人找、忙到说不清忙什么、把自己排在最后。每个结都长在线团团身上，点一下选中，再按住往外拉。

线团用 Canvas 2D 程序化生成，每一团的缠绕路径都不一样；拉动时绳线会跟着伸长、绷紧，拉得太猛它会缩回去，手感里带着一点阻力。松开一个结，页面会给出一张卡片：今晚是哪种结、硬拽了几次、可以怎么放松，可以长按或直接保存。

六个结对应六段文案，进度存在 localStorage 里，改天回来还能接着松。

---

## ✨ 预览

直接用浏览器打开 `yarn-knot-tonight.html` 即可运行——单文件 H5，零依赖。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `yarn-knot-tonight.html` | 完整可运行的 H5 互动作品，约 46KB |
| [`yarn-knot-tonight_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/yarn-knot-tonight/v-be6b0696dde4/yarn-knot-tonight_1.gif) | 预览图 1（外部资源仓库） |
| `yarn-knot-tonight.md` | 本说明文件 |

## 🖱️ 交互

- 点「帮它松一松」，从六个结里挑一个发光的
- 按住线团往任意方向拉，拉够长度就会松开
- 拉得太快会把它拽疼，结会缩回去
- 松完后生成今日卡片，可保存图片
- 点「再松一个」继续，或在「再来一团」重置进度

## 🛠️ 技术栈

- Canvas 2D
- Web Audio API
- localStorage

## 🌱 创作背景

「你今天是哪种结」把抽象的疲惫换成一个能看见的东西：一团缠住的毛线。它不要求你说清楚发生了什么，只让你挑一个最像今天的结，慢慢拉开。松几个都行，不松完也可以。

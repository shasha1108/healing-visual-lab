# Rewinding the Dusk · 把黄昏倒回去

> **Tech Keywords:** pastel, dusk, projector, crank, canvas 2d, web audio

<!-- WORK_META
  slug: dusk-projector
  render_engine: Canvas 2D
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: seed-driven deterministic scene, eight palette remaps on one registered sky source, opaque weighted palette blending, weighted beam brightness with depth-layered dust, crank drag with angular inertia, deterministic engage/hold/recover story clock, procedural Web Audio wind and crank clicks
  use_cases: pastel, dusk, projector, crank, canvas 2d, web audio
  standalone: yes
  dependencies: 0 CDN (none)
  file_size: ~555 KB, 625 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Rewinding the Dusk - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/dusk-projector/v-c8e1df190ba4/dusk-projector_1.gif)

> 手摇的放映机对准地平线，顺时针转动摇柄，那一小片天空就一格一格退回黄昏；松开手，它会自己慢慢走回夜里。

草坡上立着一台手摇放映机，镜头对着远处的地平线。摇柄是画面里唯一能被推动的东西：顺时针转它，那一小片天空会一格一格地退回去——夜色先松开一点，蓝调时刻回来，紫、晚霞、玫瑰色、橙金依次浮出地平线，最后停在夕阳上。松手之后它不会一直停在那里：短暂地留一会儿，被倒回去的黄昏会自己一格一格走回夜晚。

作品把「倒带」做成了字面上的动作。放映机本来就是让画面重新流动的机器，所以让摇柄去负责时间：每转过约 39 度是一格，转满 270 度刚好七格，从夜走到黄昏。停在最后一格时，夕阳会比别处多停三秒再开始回退——那三秒是留给「舍不得结束」的。中途重新转动也不会跳回起点，故事钟会从当前这一帧接着往前。

技术上是一个单文件 Canvas 2D 画面：两张 WebP 素材以 base64 内嵌，运行时不发出任何网络请求。八段天色不是往画面上叠滤镜，而是启动时把同一块天空与山脊的像素按亮度一次性重映射成八份独立的调色板——红多于蓝、红多于绿的判为天空，其余判为山影，各走各的色调曲线。运行时只做不透明的加权混合，所以色调交界处不会因为半透明叠加而发暗。放映机光束的亮度由当前色调的权重推出来，46 粒光束微尘按景深铺开，34 根草叶随风轻摆，转柄时火花从镜头里飞出。声音全部由 Web Audio 现场合成：一段布朗噪声既做低通的风声，又做带通的摇柄咔哒声，没有一个音频文件。

---

## ✨ 预览

直接用浏览器打开 `dusk-projector.html` 即可运行——单文件 H5，零依赖。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `dusk-projector.html` | 完整可运行的 H5 互动作品，约 555KB |
| [`dusk-projector_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/dusk-projector/v-c8e1df190ba4/dusk-projector_1.gif) | 预览图 1（外部资源仓库） |
| `dusk-projector.md` | 本说明文件 |

## 🖱️ 交互

- 顺时针拖动摇柄：每转过约 39 度推进一格，转满 270 度从夜色走到夕阳
- 松手：停住一秒后，天空开始自己一格一格退回夜里
- 停在夕阳：最后一格会多留三秒，再开始回退
- 回退途中再转：从当前这一帧接着往前，不会跳回起点
- 空格 / 回车：不用鼠标也能转动摇柄，一次推进一格
- 首次触摸：自动播放被浏览器拦下时，由这一次触摸唤醒风声与咔哒声

## 🛠️ 技术栈

- Canvas 2D
- Web Audio API

## 🌱 创作背景

「把黄昏倒回去」没做成一个调色滑块，因为那样太容易了：点一下，永久停在最亮的那一格。它要的是一个得自己花力气的动作——放映机本来就是让画面重新流动的机器，把它对准地平线，时间就归摇柄管，想再看一眼的那一刻得亲手转回来。

名字取「倒回去」而不是「停下来」，也是因为它终究要回到夜里。松手之后黄昏会自己一格一格退走，没有永久保存黄昏的选项，能留住的只有摇柄还在转的那一会儿。作品写在最前面的那句是「让舍不得结束的黄昏在一小块风景里多停一会儿」，而落地的办法很克制：只给一圈 270 度，外加夕阳停下后多给的三秒。

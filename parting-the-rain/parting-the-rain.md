# Parting The Rain · 把雨拉开一道缝

> **Tech Keywords:** canvas 2d, web audio api, touch interaction

<!-- WORK_META
  slug: parting-the-rain
  render_engine: Canvas 2D
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: seeded deterministic rain geometry, spring-damper drag integration, curtain edge envelope shaping, diffuse radial sunset glow, measured radial-gradient blur fallback for WebKit, filtered-noise rain audio with pull-tracked lowpass, aria slider semantics
  use_cases: canvas 2d, web audio api, touch interaction
  standalone: yes
  dependencies: 0 CDN (none)
  file_size: ~61 KB, 1576 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Parting The Rain - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/parting-the-rain/v-4cf5e8d38711/parting-the-rain_1.gif)

> 雨是一道幕。捏住它的边往左拉，缝后面是晚霞、电车和十只麻雀。

雨在这里不是天气，是一整片可以拉开的幕布。屏幕右缘有一条被光勾出来的边，捏住它向左拖，雨就跟着手指分开一道缝：漫射的晚霞、水面上平稳驶过的单节电车、电线上栖息的十只麻雀，都只在缝里出现。松手之后幕布会自己合回去。

雨丝的位置不是随机撒的——固定种子的随机数决定每一根的粗细、走向与落点，所以每次打开、每次改变窗口大小，雨的疏密都一样。拖动走的是弹簧阻尼积分，ω 与 ζ 随手指是否按住而切换，松手后幕布的收合是回弹而不是匀速。那片没有边界的大团晚霞，在支持 `ctx.filter` 的浏览器里是实时高斯模糊；Safari 与小工具容器没有这个属性（赋值会静默失效、退化成硬边色环），代码里因此备了一份逐像素实测拟合的径向渐变剖面来复刻同一柔焦，两者误差小于 1.5/255。

拉开是有上限的（最多画布宽度的 60%），而且只要松手，它就会自己合上——这道缝短暂，所以值得亲手去拉一次。

---

## ✨ 预览

直接用浏览器打开 `parting-the-rain.html` 即可运行——单文件 H5，零依赖。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `parting-the-rain.html` | 完整可运行的 H5 互动作品，约 61KB |
| [`parting-the-rain_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/parting-the-rain/v-4cf5e8d38711/parting-the-rain_1.gif) | 预览图 1（外部资源仓库） |
| `parting-the-rain.md` | 本说明文件 |

## 🖱️ 交互

- **捏住雨幕右缘向左拖**：缝的宽度实时跟随手指，最多拉开到画布宽度的 60%
- **松手**：幕布以阻尼回弹的方式自动合拢（约 8 秒），中途可以再次捏住打断
- **方向键 ← / →**：键盘同样走弹簧积分调节，停手 900ms 后开始回弹
- **拉开超过约 18%**：水面上的单节电车自动启动，用 6.8 秒横穿画面，并伴随低沉的过轨闷响
- **声音**：滤波白噪声实时合成雨声，音量与低通截止频率随拉开幅度变化——拉得越开，雨声越轻、越闷
- **连续两次点空**：浮出「捏住雨边，向左拉开」的提示，并给幕边一次内收的脉动
- **prefers-reduced-motion**：雨速、水波幅度与回弹曲线自动降级

## 🛠️ 技术栈

- Canvas 2D
- Web Audio API

## 🌱 创作背景

「把雨拉开一道缝」把雨从天气改写成一层遮挡物。画面里那些具体的东西——漫射的晚霞、水上的单节电车、电线与横担上十只麻雀——没有一件是「一直在那里、只是被挡住了」：雨幕本身也是被画出来的，幕拉开之前它们并不存在，只在你给出的那点宽度里出现。所以这道缝被刻意做成有限宽、且松手即合：它不是一个可以拉到底的开关，而是一段需要你维持的短暂开口。

麻雀的排布也不是随手撒的，三只挤在第 3 根电杆的横木上、两只落在第 2 到第 3 根之间的下垂导线上、再两只在第 4 根横木、剩下三只各自单独待着——鸟的爪底与会停的那条线严丝合缝，没有一只是浮空的。

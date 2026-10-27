# Lift the Leaves · 掀开落叶的一角

> **Tech Keywords:** canvas 2d, procedural leaves, drag reveal, spring physics, web audio api, touch interaction

<!-- WORK_META
  slug: leaf-corner-summer
  render_engine: Canvas 2D
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: procedural leaf carpet, layered parallax hills, windmill animation, spring-damped drag reveal, puddle rain ripples, particle seeds and motes, synthesized rain audio
  use_cases: canvas 2d, procedural leaves, drag reveal, spring physics, web audio api, touch interaction
  standalone: yes
  dependencies: 0 CDN (none)
  file_size: ~64 KB, 1214 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Lift the Leaves - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/leaf-corner-summer/v-e8b30f4a14cf/leaf-corner-summer_1.gif)

> 叶子掀开一角，夏天还留在下面。

秋雨把一片柿色的落叶地泡得发亮，两只发光的角从左右边缘露出来。按住任意一只往上掀，整片落叶像一张被拎起的毯子，顺着手指卷起来；掀得足够深，蒲公英和蜻蜓会从下面探出头——叶子盖住的，是一个还没走的夏天。松手后落叶慢慢回弹，重新合上。

画面没有用任何图片素材。山脊、风车、落叶地毯、水洼、雨丝和种子都由 Canvas 2D 按 600×800 的逻辑坐标程序化绘制，尺寸与线宽随屏幕换算；落叶的脉络、卷边和投影逐片生成，水洼只叠一层薄水，让叶色从底下透上来。

两只角各带一套弹簧阻尼，拖拽距离、越过临界点后的「变沉」手感、以及松手后的回弹速度都可以在参数里调。雨声、叶子的摩擦声和角被掀开时的音高，全部由 Web Audio 实时合成。

---

## ✨ 预览

直接用浏览器打开 `leaf-corner-summer.html` 即可运行——单文件 H5，零依赖。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `leaf-corner-summer.html` | 完整可运行的 H5 互动作品，约 64KB |
| [`leaf-corner-summer_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/leaf-corner-summer/v-e8b30f4a14cf/leaf-corner-summer_1.gif) | 预览图 1（外部资源仓库） |
| `leaf-corner-summer.md` | 本说明文件 |

## 🖱️ 交互

- 按住左下或右下发光的角，往上拖动，掀开落叶
- 掀到足够深并停留片刻，藏在下面的蒲公英或蜻蜓会出现
- 松开手指，落叶按弹簧阻尼缓慢盖回原处
- 点击画面中的音符按钮，开关雨声与音效

## 🛠️ 技术栈

- Canvas 2D
- Web Audio API

## 🌱 创作背景

秋天不总是结束。题眼写在页面开头——「秋雨里，掀开落叶的一角，夏天还在下面」。叶子被掀开的那一下，露出来的是上一个季节留下的颜色；手一松，它又慢慢盖回去，像什么都没发生过。

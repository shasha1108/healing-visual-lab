# Rice Fragrance · 稻香

> "回家吧，回到最初的美好"——金色稻田里的童年记忆

## ✨ 预览

![Rice Fragrance - pixel pastoral landscape with golden rice fields, river, scarecrow, windmills, and fireflies at dusk](rice-fragrance_1.gif)

## 📂 文件说明

- `rice-fragrance.html` — 单文件 H5，自包含

## 🖱️ 交互

- **单击**：放飞纸飞机——从手中飞出，滑翔后消失于天际
- **长按**：加速时光流逝——午后金色阳光 → 黄昏橙粉 → 入夜蓝紫 → 萤火虫亮起

## 🛠️ 技术栈

- **渲染**：p5.js Canvas2D 像素渲染
- **音频**：Web Audio API 自然风声（粉噪 + 低通滤波 + LFO 阵风）
- **调色**：4 段时间色插值 + 大气透视蓝移
- **性能**：Canvas Gradient + beginShape 单次路径 + 稀疏噪声叠加

## 🌱 场景元素

- 金色稻海随风波动（Perlin 噪声风之波纹）
- 小河穿过田野（Y 轴遍历 + pow(t,2) 非线性透视）
- 稻草人守望田边
- 红顶小屋错落山脊
- 彩虹风车四叶旋转
- 黄昏后萤火虫渐亮
- 蜻蜓低飞 + 夜空星辰闪烁

# -*- coding: utf-8 -*-
# 御微 D2W 议题资料库 V2（HBM D2W 混合键合 制程 Stage/Step 详解 + 量检测节点）
# 来源：HBM_D2W.pptx（Bumpless 混合键合路线，V10，2026-06-16，共 67 页）的清理版源文件

D2W_PROCESS_V2_KNOWLEDGE = """\
# HBM D2W Hybrid Bonding 制程与量检测节点完整分析报告

> 技术路线：Bumpless 混合键合（Cu-SiCN 直接键合）
> 应用世代：HBM4E / HBM5

---

## 目录

1. [技术背景](#1-技术背景)
2. [制程总览](#2-制程总览)
3. [Stage 2A：TSV 前道 + HB Pad 制备（S2-1→S2-10）](#3-stage-2atsv-前道--hb-pad-制备)
4. [Stage 2B：背面制程 + KGD Dicing（S2-11→S2-23）](#4-stage-2b背面制程--kgd-dicing)
5. [Stage 3：D2W HB 堆叠 + Gap Fill + 切单（S3-1→S3-8）](#5-stage-3d2w-hb-堆叠--gap-fill--切单)
6. [检测节点汇总](#6-检测节点汇总)
7. [关键风险与量测挑战](#7-关键风险与量测挑战)

---

## 1. 技术背景

D2W（Die-to-Wafer）Hybrid Bonding 是 HBM4E / HBM5 世代的主流堆叠路线，采用 Bumpless 混合键合，
以 Cu-SiCN 直接键合取代传统微凸块（µbump），实现更细节距与更低键合界面阻抗。

**核心优势：**

- **KGD 预筛**：切单后 100% 全颗强制电学测试，剔除不良 Die，避免 12 层堆叠良率累积损失（0.99¹² ≈ 88.6%）
- **异构集成**：不同尺寸 Die 可混合，灵活 Chiplet 布局
- **HBM4E 主流**：BESI Kinex 量产验证；2μm 节距实测 < 350nm Overlay

**主流键合机制：** Cu-SiCN 直接混合键合（Bumpless）
**堆叠层数：** 15 层 Core Die（15-Hi）+ Top Die

---

## 2. 制程总览

```
Stage 2A（正面 TSV + HB Pad，10 步）
  TSV 光刻 → 深孔刻蚀 → 侧壁绝缘/阻挡/种子 → ECD 填充 → CMP
  → Bond Pad → SiCN 键合介质 → Cu Pad 图案化 → Cu ECD 填充 → 精密 CMP（HB 第一良率关口）

Stage 2B（背面制程 + KGD，13 步）
  修边 → 临时键合载板 → 背磨+CMP → TSV 揭露 → 翘曲补偿膜 → CVD 钝化
  → 背面 CMP → 背面介电沉积 → 背面开窗 → 背面 Cu 填充 → 背面 Pad CMP
  → DC Tape+解键合 → Singulation + KGD（强制门控）

Stage 3（D2W HB 堆叠，8 步）
  Base Wafer 临时键合 → 表面活化 → 15 层 Core Die 堆叠 → Top Die 键合
  → 退火 → Gap Fill → 研磨+修边+解键合 → 划片切单
```

**三大强制门控节点：**

1. **S2-10 精密 CMP** —— HB 第一良率关口，AFM 全片 Ra Map
2. **S2-23 Singulation + KGD** —— 100% 全颗电学筛选（进 Stage 3 前最后门控）
3. **S3-3 15 层堆叠 D2W Overlay** —— HOUYI Overlay < 100nm

---

## 3. Stage 2A：TSV 前道 + HB Pad 制备（S2-1→S2-10）

> 10 步骤 — 正面 TSV（Via-middle）+ RDL + Cu Pad / SiCN 混合键合

### Step S2-1：TSV 光刻定义（ArFi Lithography）

- 光刻机：ArFi（193nm 浸没式，NA ≈ 1.35）
- 图案：TSV 开口阵列，对准 BEOL 基准标记
- Overlay 目标：全片 3σ < 1μm
- CD 均匀性：TSV 开口直径 ±5%
- 光刻胶：正性 CAR（化学放大型）
- 后续刻蚀深度：50–100μm（Via Middle）

**量测 · 检测节点**
- ADI Overlay 量测（HOUYI DBO/IBO）：< 1μm 全片 3σ
- ADI 图形缺陷检测（i12-F）：< 0.5/cm²；致命缺陷零容忍
- CD-SEM 抽检：TSV 开口直径均匀性

**⚠ 关键门控 / 风险**
- Overlay 超标 → TSV 孔位偏离 → 与 BEOL 短路 / 开路
- 开孔缺失 / 桥连 → 刻蚀形态偏差 → TSV 填充 void
- 光刻胶残留 → 刻蚀不均 → 侧壁粗糙

### Step S2-2：深孔刻蚀（Bosch Process RIE）

- 工艺：SF₆ 刻蚀 + C₄F₈ 钝化，交替循环
- 初始刻蚀深度：50–100μm（Via Middle 全深）
- 背磨后有效深度：20–30μm（减薄后保留段）
- 深宽比（AR）：> 10:1
- 侧壁垂直度：> 88°
- 扇贝纹（Scallop）深度：< 100nm

**量测 · 检测节点**
- TSV 孔深量测（红外 OCT，在线）：±5μm 均匀性
- 孔形 / 侧壁异常 SEM 抽检：垂直度 > 88°
- 扇贝纹深度验证：< 100nm

**⚠ 关键门控 / 风险**
- 孔深偏浅 → 有效 TSV 不足 → 电阻偏高
- 过深 → 背磨后 TSV 暴露失败
- 侧壁粗糙 → ALD 台阶覆盖性下降 → Cu 扩散
- 扇贝纹过深 → 局部应力集中 → 可靠性风险

### Step S2-3：侧壁绝缘 + 阻挡层 + Cu 种子层

- ① ALD SiO₂（绝缘）：TEOS/O₃；300–350°C；100±10nm；均匀性 < 3%
- ② ALD TaN（阻挡）：~5nm；均匀性 < 5%（防 Cu 扩散进 Si）
- ③ PVD Cu 种子层：纯度 > 99.999%；~100nm；Rs < 5%
- 台阶覆盖率（Step Coverage）：> 80%（深孔关键指标）
- 三层序贯沉积，腔体间转移期间严控洁净度

**量测 · 检测节点**
- ALD SiO₂ 膜厚（SE 椭偏）：100±10nm；均匀性 < 3%
- TaN/Ta 厚度（XRF/SE）：~5nm；均匀性 < 5%
- Cu Seed 方阻 Rs（4 探针）：< 5%
- ALD/PVD 后颗粒检测：< 0.05/cm²（> 50nm）

**⚠ 关键门控 / 风险**
- SiO₂ 偏薄 → 绝缘不足 → 漏电↑
- TaN 过薄 → Cu 扩散进 Si → 器件漏电
- Cu Seed Rs 不均 → ECD 电流不均 → void 或过填充
- 颗粒 → ECD 局部 void；CMP 后残留 → 短路

### Step S2-4：ECD 铜电镀填充（Electrochemical Deposition）

- 电镀液：CuSO₄ / H₂SO₄ / 添加剂（PEG + SPS + Cl）
- 填充机制：Bottom-up 超填充（底部优先生长）
- 超填充量（Overburden）：< 5μm
- Cu 厚度均匀性：< 3%（全片）
- void 率目标：< 0.1%；void 尺寸 < 1μm

**量测 · 检测节点**
- Cu 电镀膜厚（XRF）：均匀性 < 3%
- void 检测（红外热成像 / AXI X 射线）：< 0.1%

**⚠ 关键门控 / 风险**
- 填充不足 → void → TSV 电阻偏高 → 可靠性劣化
- 过填充 → CMP 负担重，Cu Dishing 风险↑
- 添加剂浓度偏差 → 底部填充不均 → void 形成

### Step S2-5：CMP 平坦化（TSV 顶面）

- CMP 浆料：氧化铝 / H₂O₂（Cu 选择性浆料）
- 目标：去除超填充 Cu + TaN/Ta 阻挡层
- 残余 Cu：< 5nm（Cu 残留零容忍）
- SiO₂ 层厚度均匀性：< 3%
- Ra：< 0.5nm（TCB 路线；HB 路线需 < 0.3nm）

**量测 · 检测节点**
- CMP 后 Cu 残膜（SE 椭偏）：< 5nm
- Cu 残留全扫（光学）：零容忍
- 颗粒 / 划痕检测：< 0.05/cm²；划痕零容忍

**⚠ 关键门控 / 风险**
- Cu 残留 → 层间短路
- 过度研磨（Over-polish）→ TSV Cu 凹陷（Dishing）→ BEOL 接触电阻↑
- 划痕 → BEOL 金属层断路

### Step S2-6：固定金属焊盘（Bond Pad Formation）

- 工艺：TSV 顶部形成固定金属焊盘（I/O Pad）
- SiO₂ 介电层完整覆盖 Si 表面（含 TSV 顶）
- 焊盘金属：Cu，厚度 ~1–2μm
- 绝缘层：SiN / SiO₂ 覆盖，开窗露出焊盘中央
- 焊盘尺寸 ~40–60μm；开窗 Overlay < 0.5μm

**量测 · 检测节点**
- 焊盘开窗尺寸（光学 CD）：±1μm
- 绝缘层膜厚（SE）：均匀性 ±3%
- 图形缺陷 / 开窗残留：< 0.5/cm²；零容忍

**⚠ 关键门控 / 风险**
- 开窗未开净（绝缘层残留）→ 接触电阻↑ / 混合键合 Cu-Cu 接触不良
- 焊盘对准偏差 → SiCN/Cu Pad 图案偏移 → 混合键合对准超差

### Step S2-7：SiCN 键合介质（Bonding CVD）

- 设备：AMAT Producer CVD（PECVD，等离子增强）
- 介质材料：SiCN（碳氮化硅，HB 核心键合介质）
- 前驱体：SiH₄ / NH₃ / N₂；温度均匀性严格
- 膜厚均匀性：±3%；应力 < 200MPa（防翘曲）
- SiCN 优势：预键合能 ~200 mJ/m²；退火 200–250°C

**量测 · 检测节点**
- 膜厚（SE 椭偏）：±3%；应力 < 200MPa
- 折射率 n = 1.85–2.0
- 颗粒：< 0.05/cm²（> 50nm）

**⚠ 关键门控 / 风险**
- 膜厚不均 → CMP 去除不一致 → Pad 共面性劣化
- 应力过大 → 翘曲 → Overlay 漂移
- 颗粒嵌入 → 键合界面 void

### Step S2-8：Cu Pad 图案化（Pad Etch）

- 设备：AMAT Sym3 Etch
- ArFi 光刻定义 HB Cu Pad 开口位置
- 刻蚀 SiCN 介质形成 Pad 凹槽（damascene 开口）
- 开口 CD / 深度按 HB pad 节距控制
- ⚠ Pad 位置 Overlay 决定后续键合对准

**量测 · 检测节点**
- Pad 开口 CD / 深度（CD-SEM）
- 刻蚀形貌 / 侧壁角
- Overlay（HOUYI）< 1μm

**⚠ 关键门控 / 风险**
- CD 偏差 → Cu 填充量不一致 → 共面性差
- 刻蚀残留 → 键合界面缺陷
- Overlay 超标 → Pad 错位

### Step S2-9：Cu ECD 填充（Barrier + Seed + ECD）

- Barrier/Seed（AMAT Endura PVD）：TaN/Ta + Cu 种子
- 填充（AMAT Nokota ECD）：bottom-up 超填充 Cu
- void < 0.1%；填满 HB Cu Pad
- 轻微 overfill，留 CMP 余量

**量测 · 检测节点**
- 填充 void（X-ray / 截面）：< 0.1%
- Cu 厚度 / overfill 量
- 种子层台阶覆盖率

**⚠ 关键门控 / 风险**
- 填充 void → 键合接触不良 → 电阻↑
- 种子覆盖不足 → 空洞
- overfill 过量 → CMP 负担↑

### Step S2-10：精密 CMP（HB 第一良率关口 · AFM）

- 设备：AMAT Opta CMP（高精度 Cu/SiCN 共面）
- 目标 Ra（HBM4E）：< 0.3nm（原子级平坦度）
- 目标 Ra（HBM5 预估）：< 0.2nm
- Cu Dishing：< 0.5nm（全片 Map）
- 颗粒密度（> 50nm）：< 0.01/cm²
- CMP 浆料：CeO₂ 系专用配方

**量测 · 检测节点**
- ⚠ AFM 全片 Ra Map（强制门控）：Ra < 0.3nm
- Cu Dishing（AFM/接触式）：< 0.5nm
- 颗粒密度全扫：< 0.01/cm²（> 50nm）

**⚠ 关键门控 / 风险**
- ⚠ Ra 超标 → 界面 void → 键合强度不足 → 分层
- ⚠ Cu Dishing > 0.5nm → 接触面积损失 → 电阻↑
- ⚠ 颗粒 → 界面顶起 → void → 键合失败
- SiCN 退火 200°C 无自修复，不可跳过门控

---

## 4. Stage 2B：背面制程 + KGD Dicing（S2-11→S2-23）

> 13 步骤 — 减薄 + TSV Reveal + KGD 良率筛选

### Step S2-11：修边（Edge Trimming）

- 刀片 / 激光修边：去除晶圆边缘约 3mm
- 修边宽度均匀性：±0.2mm
- 目的：去除边缘圆角，为背磨提供平整起点

**量测 · 检测节点**
- 修边后边缘形貌（光学）：崩裂 < 5μm
- 宽度均匀性：±0.2mm

**⚠ 关键门控 / 风险**
- 边缘碎裂 → 背磨过程晶圆破裂风险↑
- 修边过窄 → 边缘 Die 损失

### Step S2-12：临时键合载板（TBDB）

- 载板：玻璃 / Si，平整度高
- 键合胶：热固型 TBDB（UV 或热脱键）
- 目的：支撑超薄晶圆（最终 20–30μm）安全背磨
- ⚠ 正面 HB Pad（Ra<0.3nm）在载板侧，不能损伤

**量测 · 检测节点**
- 临时键合后翘曲：< 200μm
- 气泡面积：< 0.1%

**⚠ 关键门控 / 风险**
- 翘曲过大 → 背磨不均 → TTV 超标
- 局部气泡 → 背磨时悬空 → 薄晶圆破裂

### Step S2-13：背面磨削 + CMP（Back Grind + CMP）

- 阶段①：机械磨削（粗磨 + 细磨）快速去料
- 阶段②：精密 CMP 消除磨削损伤层
- 目标厚度：20–30μm（保留 TSV 有效深度）
- TTV：< 1μm（全片）

**量测 · 检测节点**
- TTV（非接触光学）：< 1μm
- 背面裂纹/划痕：裂纹零容忍；划痕 < 100nm

**⚠ 关键门控 / 风险**
- TTV 超标 → TSV 暴露高度不均 → 接触高度差 → 开路
- 裂纹 → 后续工序晶圆破裂
- 划痕 → 钝化层粘附性下降

### Step S2-14：TSV 揭露（TSV Reveal · RIE）

- 工艺：RIE（SF₆/O₂），选择性刻蚀 Si（相对 Cu）
- TSV Cu 突起（Nail）高度：2–5μm
- 高度均匀性：±0.5μm（全片）
- 刻蚀中：红外 OCT 实时深度反馈
- 刻蚀后：WLI 全片 Map

**量测 · 检测节点**
- 红外 OCT（刻蚀中）：实时深度监控
- ⚠ WLI（刻蚀后）：2–5μm；±0.5μm
- 背面图形缺陷：TSV 暴露缺失零容忍

**⚠ 关键门控 / 风险**
- 突起 < 1.5μm → 键合接触窗口不足 → 电阻↑
- 突起 > 5.5μm → Die 间隙超标 → z-height 超规格
- TSV 暴露缺失 → 断路（直接报废）

### Step S2-15：翘曲补偿膜（Warpage Modulation）

- 原理：超薄晶圆减薄后正背面应力失配 → 翘曲
- 补偿膜：背面沉积 SiN/SiO₂ 应力补偿薄膜
- 闭环控制：依翘曲量测调整补偿膜厚度
- 目标：补偿后翘曲 < 50μm（全片）

**量测 · 检测节点**
- 全片翘曲 Map（非接触，电容/光学）
- 补偿后翘曲：< 50μm（全片）
- 补偿薄膜沉积闭环控制验证

**⚠ 关键门控 / 风险**
- 翘曲未补偿 → D2W 键合接触不均 → void
- 翘曲过大 → HOUYI Overlay 基准不稳 → 系统误差
- 补偿过度 → 反向翘曲

### Step S2-16：CVD 钝化层（PECVD SiO₂/SiN）

- 工艺：PECVD（等离子体增强 CVD）
- 材料：SiO₂ / SiN（可叠层组合）
- 膜厚均匀性：±3%
- 应力：< 200MPa（超薄晶圆对应力敏感）
- 温度：≤ 200°C（兼容 BEOL 热预算）

**量测 · 检测节点**
- 膜厚（SE 椭偏）：±3%；应力 < 200MPa
- 颗粒检测：< 0.05/cm²（> 50nm）

**⚠ 关键门控 / 风险**
- 膜厚偏薄 → TSV 侧壁保护不足 → 漏电
- 应力过大 → 超薄晶圆翘曲↑ → CMP 不均
- 颗粒嵌入膜中 → 长期可靠性问题

### Step S2-17：背面 CMP 平坦化（Backside CMP）

- 目标：钝化层后精密 CMP
- TTV：< 0.5μm
- Ra：< 0.5nm（背面平坦基准）
- 确保背面 Overlay 量测基准稳定

**量测 · 检测节点**
- 背面 TTV/Ra：TTV < 0.5μm；Ra < 0.5nm
- CMP 后划痕/颗粒：划痕零容忍；< 0.05/cm²

**⚠ 关键门控 / 风险**
- Ra 过大 → 背面 Overlay 基准不稳 → 影响 D2W 精度
- TTV 差 → Die 间 z-height 不均
- 划痕 → 后续图形化断路风险

### Step S2-18：背面 Pad 和介电沉积（Backside Dielectric · SiCN）

- 工艺：PECVD 沉积 SiCN 键合介质（可 SiCN/SiO₂/SiN 叠层）
- 目的：为背面提供 Cu-Cu + 介电-介电 混合键合面
- 膜厚均匀性：±3%（全片）
- 低应力控制，避免超薄晶圆翘曲

**量测 · 检测节点**
- 膜厚/折射率（SE 椭偏）：均匀性 ±3%
- 颗粒/膜缺陷（暗场）：缺陷零容忍

**⚠ 关键门控 / 风险**
- 膜厚偏差 → 键合面 recess 失控
- 应力过大 → 超薄晶圆翘曲
- 颗粒 → 界面 void → 键合失败

### Step S2-19：背面 Pad 开窗（Cu Expose / Pad Patterning）

- 工艺：光刻 + 蚀刻，在 SiCN 上定义 pad 开口
- 开口对准背面 Cu Pad，宽度与 pad 上缘一致
- Overlay 对准：< 100nm（细 pitch 需求）
- 露出 Cu Pad 顶面，为背面 Cu 填充做准备

**量测 · 检测节点**
- Overlay 对准精度：< 100nm
- 开口 CD / 侧壁形貌（SEM）

**⚠ 关键门控 / 风险**
- Overlay 过大 → 电阻↑（misalign >80% pad CD ＝ 100% 良率损失）
- 蚀刻不净 → Cu Pad 顶残留介质 → 接触不良
- 侧壁陡直度不足 → 后续填充空洞

### Step S2-20：背面 Cu 填充（PVD Barrier-Seed + ECD Cu）

- Barrier/Seed：PVD TaN/Ta（或 TiN/Ti）+ Cu seed，不破真空
- Cu 填充：ECD 电化学沉积，室温，1.5–4.6 ASD，镀厚 ~1μm
- Cu 直接镀在露出的 TSV 铜上（直连，无 µbump）
- 三添加剂（加速/抑制/整平）控 gap-fill

**量测 · 检测节点**
- 镀层厚度 / 空洞（X-ray / 截面）
- Seed 覆盖率 / 侧壁连续性

**⚠ 关键门控 / 风险**
- Barrier 不连续 → Cu 扩散 → 可靠性↓
- 填充空洞 → 接触电阻↑ → 断路
- 溢镀不足 → CMP 后 pad 缺失

### Step S2-21：背面 Pad CMP 共面（Backside Pad CMP）

- 精密 CMP，形成 SiCN + Cu pad 共面
- 目标 Ra < 0.5nm（键合基准面）
- TTV：< 0.5μm（全片）
- Cu / SiCN 同步抛光，无划痕 / 颗粒

**量测 · 检测节点**
- AFM 全片 Ra Map（强制门控）：Ra < 0.5nm
- TTV（非接触光学）：< 0.5μm；颗粒 < 0.05/cm²

**⚠ 关键门控 / 风险**
- Ra 超标 → 界面 void → 键合失败
- TTV 差 → Die 间 z-height 不均
- 划痕 / 颗粒 → 键合空洞 → 分层

### Step S2-22：DC Tape + 解键合（Debonding）

- 贴 DC tape：保护正面 HB Cu Pad（Ra<0.3nm）
- UV/热脱键：TBDB 胶层失活，载板失粘
- 载板分离：Glass Carrier 与 Die 分离
- 解键合后翘曲：< 200μm（全片）
- 残胶：零容忍（进 Stage 3 HB 前最后清洁）

**量测 · 检测节点**
- 解键合后翘曲：< 200μm
- 正背面外观检测：划伤/污染 < 0.01%
- 残胶检测：零容忍

**⚠ 关键门控 / 风险**
- 翘曲过大 → Dicing 路径偏差 → Die 尺寸不准
- 残胶 → 污染 Stage 3 HB 界面 → void
- 划伤 → HB Pad 损伤 → 键合强度不足

### Step S2-23：Singulation + KGD（⚠ 强制门控）

- 切割：激光/刀片（小节距用 Plasma Dicing）
- 崩裂：正面 < 5μm；背面 < 10μm；Kerf ±2μm
- KGD：100% 全颗强制电学测试
- TSV 连通性（Kelvin 4 探针）验证
- Daisy chain 良率：> 70%

**量测 · 检测节点**
- 切边形貌（光学）：崩裂 < 5μm；裂纹零容忍
- ⚠ Die 正面颗粒全扫（i12-F 暗场）：< 0.01/cm²
- KGD 电学筛选（100%）：Kelvin 4 探针；Daisy > 70%

**⚠ 关键门控 / 风险**
- ⚠ 颗粒是进 Stage 3 前最后门控 → 超标致 HB void
- 不良 Die 未筛除 → 12 层堆叠良率 ≈ 88.6%，不可接受
- Die 边缘裂纹 → 键合后热循环破裂

---

## 5. Stage 3：D2W HB 堆叠 + Gap Fill + 切单（S3-1→S3-8）

> 8 步骤 — D2W HB 堆叠 + Gap Fill + 划片切单

### Step S3-1：Base Wafer 临时键合（Base Wafer on Carrier · TBDB）

- 设备：临时键合机（TBDB 临时直接键合）
- 载体：玻璃 / Si 载板，平整度严格（堆叠基准）
- 整片连续 base wafer，SiCN + Cu Pad 面朝上
- 临时胶层均匀，提供支撑 + 可解键合
- 载板尺寸大于器件区，边缘留支撑余量

**量测 · 检测节点**
- 载板平整度 / TTV：< 1μm
- 临时键合空洞（SAM 声学）：void < 0.1%
- 键合准备面颗粒：< 0.05/cm²（> 50nm）

**⚠ 关键门控 / 风险**
- 载板翘曲 → 后续 Overlay 漂移
- 临时胶不均 → 局部应力 → die 偏移
- 键合面颗粒 → HB 界面 void

### Step S3-2：表面活化（Surface Activation · 等离子活化）

- 设备：N₂/Ar 等离子活化腔（PVD/CVD）
- 工序：去除氧化层 + 羟基化（亲水）
- 气体：N₂ / O₂ / Ar，低功率 RF
- 温度：室温~<200°C，短时（秒级）

**量测 · 检测节点**
- 表面接触角：活化后 < 5°（亲水化验证）
- 表面颗粒：< 0.05/cm²（> 50nm）
- 活化均匀性 / 表面粗糙度 Ra：< 0.5nm

**⚠ 关键门控 / 风险**
- 活化不足 → 键合强度低 → 界面 void
- 活化过度 → 表面损伤 / 粗糙化
- 活化后停留过久 → 再污染 → 键合失效

### Step S3-3：15 层 Core Die 堆叠（15-Hi D2W Hybrid Bonding）

- 设备：BESI Kinex（HBM4E 主流 D2W 键合机）
- 工序：core die 拾取 → 翻转 → 精密放置 → 室温预键合
- 键合机制：Cu-SiCN 直接混合键合（Bumpless）
- 逐层堆叠 15 层（15-Hi），层间对准累积控制
- ⚠ Overlay：Max|X|,|Y| < 100nm（单颗 die）

**量测 · 检测节点**
- ⚠ D2W Overlay（HOUYI）：< 100nm —— 强制门控
- 逐层堆叠位移 / 倾斜：< 3μm / < 0.1°
- 界面气泡面积（光学）：< 0.01%

**⚠ 关键门控 / 风险**
- ⚠ Overlay 超标 → Cu Pad 接触损失 → 电阻↑/短路
- 逐颗逐层贴装产能低 = D2W 最大产能瓶颈
- 层数越高累积应力↑ → 翘曲与对准漂移

### Step S3-4：Top Die 键合（Top Die Bonding）

- 工序：Top / Cap die 拾取 → 翻转 → 精密放置键合
- 同样 Cu-SiCN 混合键合（与 core 层一致）
- Top die 较厚，作为顶盖与散热界面
- Overlay 要求同 core 层 < 100nm

**量测 · 检测节点**
- Top die Overlay：< 100nm
- 键合后总堆叠高度 / 平整度
- 界面键合质量（SAM 声学）

**⚠ 关键门控 / 风险**
- Top die 偏移 → 顶层信号 / 电源 pad 失效
- 顶层键合不良 → 散热界面热阻↑

### Step S3-5：退火（Cu Interconnect Annealing）

- 设备：批式退火炉 / RTP（受控气氛）
- 工序：堆叠键合完成后对整体进行退火
- 温度：~250–350°C，N₂/H₂ 还原气氛
- 机制：Cu 晶粒生长 + Cu-Cu 界面金属互扩散
- 目的：消除界面孔洞，降低接触电阻，键合永久化

**量测 · 检测节点**
- Cu-Cu 接触电阻：退火后达标（< 规格上限）
- 界面孔洞（SAM / TEM）：void < 0.01%
- 翘曲 / 热应力变化：退火前后 < 阈值

**⚠ 关键门控 / 风险**
- 温度过高 → 热预算超标 → 器件特性漂移
- 升降温过快 → 热应力 → 翘曲 / 分层
- 退火不足 → Cu 互扩散不完全 → 电阻↑

### Step S3-6：Gap Fill（键合后间隙填充 · Mold）

- 工序：堆叠完成后填充 die 间 / 周围间隙
- 路线：SiO₂ CVD / 低k SiCOH / Polymer mold
- 提供机械保护 + 气密 + 应力缓冲
- void < 0.1%；填充后表面可平坦化

**量测 · 检测节点**
- 填充空洞（SAM / X-ray）：void < 0.1%
- 填充后翘曲 / 平整度
- 边缘填充完整性

**⚠ 关键门控 / 风险**
- 填充 void → 机械 / 气密失效
- 填充应力 → 堆叠翘曲
- 边缘填充不全 → 分层

### Step S3-7：研磨 + 修边 + 解键合（Grind · Trim · Debond）

- 研磨：平坦化 mold 塑封面 / 减薄；TTV 控制
- 修边：去除边缘 mold 溢料与崩边风险区
- 解键合：UV / 热脱键移除临时载板
- ⚠ 此时晶圆仍为连续整片，尚未切单

**量测 · 检测节点**
- 研磨后 TTV / 总厚度
- 解键合后翘曲 / 残胶
- 表面颗粒 / 损伤检测

**⚠ 关键门控 / 风险**
- 研磨过度 → 顶层 die 损伤
- 解键合残胶 → 后续 die 污染
- 解键合应力 → 超薄堆叠破裂

### Step S3-8：划片切单（Dicing · Singulation）

- 工序：晶圆贴 dicing frame → 对位 → 切割
- 切割：激光 / 刀片，沿 die 区块外缘切割道
- 切成独立 HBM4E 堆叠体（KGD Stack）输出
- 崩裂控制：正面 < 5μm；直线度 < 2μm

**量测 · 检测节点**
- 崩裂尺寸：正面 < 5μm / 背面 < 10μm
- 切割直线度：< 2μm
- 切后外观 / 侧壁完整性

**⚠ 关键门控 / 风险**
- 崩裂过大 → 边缘 die / TSV 损伤
- 切割偏移 → 切到器件区
- 切割应力 → 堆叠分层

---

## 6. 检测节点汇总

### Overlay / 对准关键节点

| 制程节点 | 量测手段 | 规格 |
|---------|---------|------|
| S2-1 TSV 光刻 | HOUYI DBO/IBO（ADI） | < 1μm 全片 3σ |
| S2-8 Cu Pad 图案化 | HOUYI | < 1μm |
| S2-19 背面开窗 | Overlay | < 100nm |
| S3-3 15 层堆叠（强制门控） | HOUYI | < 100nm |
| S3-4 Top Die 键合 | Overlay | < 100nm |

### 缺陷 / 颗粒检测节点

| 制程节点 | 量测手段 | 规格 |
|---------|---------|------|
| S2-1 光刻后图形缺陷 | i12-F | < 0.5/cm²；致命零容忍 |
| S2-3 ALD/PVD 后 | 颗粒检测 | < 0.05/cm²（> 50nm） |
| S2-7 SiCN | 颗粒 | < 0.05/cm²（> 50nm） |
| S2-10 精密 CMP（强制门控） | 颗粒全扫 | < 0.01/cm²（> 50nm） |
| S2-16 CVD 钝化 | 颗粒 | < 0.05/cm²（> 50nm） |
| S2-23 KGD（强制门控） | i12-F 暗场 | < 0.01/cm² |
| S3-2 表面活化 | 颗粒 | < 0.05/cm²（> 50nm） |

### CMP / 平坦度关键节点（AFM Ra Map）

| 制程节点 | 量测手段 | Ra 规格 | TTV/Dishing |
|---------|---------|---------|------------|
| S2-5 TSV 顶面 CMP | SE 椭偏 / 光学 | < 0.3nm（HB 路线） | Cu 残 < 5nm |
| S2-10 精密 CMP（强制门控） | AFM 全片 Ra Map | < 0.3nm（HBM4E）/ < 0.2nm（HBM5） | Cu Dishing < 0.5nm |
| S2-13 背磨 + CMP | 非接触光学 | — | TTV < 1μm |
| S2-17 背面 CMP | — | < 0.5nm | TTV < 0.5μm |
| S2-21 背面 Pad CMP（强制门控） | AFM 全片 Ra Map | < 0.5nm | TTV < 0.5μm |

### 深度 / 厚度 / 空洞节点

| 制程节点 | 量测手段 | 规格 |
|---------|---------|------|
| S2-2 深孔刻蚀 | 红外 OCT（在线） | 孔深 ±5μm；扇贝纹 < 100nm |
| S2-4 ECD 填充 | XRF + 红外热成像 / AXI X 射线 | Cu 均匀性 < 3%；void < 0.1% |
| S2-9 Cu ECD 填充 | X-ray / 截面 | void < 0.1% |
| S2-14 TSV 揭露 | 红外 OCT（刻蚀中）+ WLI（刻蚀后） | 突起 2–5μm；±0.5μm |
| S2-20 背面 Cu 填充 | X-ray / 截面 | Seed 覆盖 / 侧壁连续性 |
| S3-1 临时键合 | SAM 声学 | void < 0.1% |
| S3-5 退火 | SAM / TEM | void < 0.01% |
| S3-6 Gap Fill | SAM / X-ray | void < 0.1% |

### 膜厚 / 材料量测节点

| 制程节点 | 量测手段 | 规格 |
|---------|---------|------|
| S2-3 侧壁绝缘/阻挡/种子 | SE 椭偏 / XRF / 4 探针 | SiO₂ 100±10nm；TaN ~5nm；Rs < 5% |
| S2-7 SiCN | SE 椭偏 | ±3%；应力 < 200MPa；n = 1.85–2.0 |
| S2-16 CVD 钝化 | SE 椭偏 | ±3%；应力 < 200MPa |
| S2-18 背面介电 | SE 椭偏 | ±3% |

### 电学 / 声学终测节点

| 制程节点 | 量测手段 | 规格 |
|---------|---------|------|
| S2-23 KGD（强制门控） | Kelvin 4 探针 | 100% 全颗；Daisy chain > 70% |
| S3-5 退火后 | Cu-Cu 接触电阻 | < 规格上限 |
| S3-4 Top Die | SAM 声学 | 界面键合质量 |

---

## 7. 关键风险与量测挑战

### 三大强制门控节点

**1. S2-10 精密 CMP（HB 第一良率关口）**
- AFM 全片 Ra Map 强制门控：Ra < 0.3nm（HBM4E）
- Cu Dishing > 0.5nm → 接触面积损失 → 电阻↑
- 颗粒 → 界面顶起 → void → 键合失败
- SiCN 退火 200°C 无自修复，不可跳过门控

**2. S2-23 Singulation + KGD（进 Stage 3 前最后门控）**
- Die 正面颗粒全扫（i12-F 暗场）< 0.01/cm²，超标致 HB void
- 不良 Die 未筛除 → 12 层堆叠良率 ≈ 88.6%（0.99¹²），不可接受
- KGD 100% 全颗 Kelvin 4 探针；Daisy chain > 70%

**3. S3-3 15 层 Core Die 堆叠（D2W Overlay 门控）**
- HOUYI D2W Overlay < 100nm（Max|X|,|Y|，单颗 die）
- Overlay 超标 → Cu Pad 接触损失 → 电阻↑ / 短路
- ⚠ 逐颗逐层贴装产能低 = D2W 最大产能瓶颈
- 层数越高累积应力↑ → 翘曲与对准漂移

### 翘曲控制贯穿全流程（超薄晶圆 20–30μm）

| 节点 | 翘曲 / 应力规格 |
|------|----------------|
| S2-12 临时键合后 | < 200μm |
| S2-15 翘曲补偿膜（闭环） | 补偿后 < 50μm |
| S2-16 CVD 钝化应力 | < 200MPa |
| S2-22 解键合后 | < 200μm |
| S2-7 / S2-18 SiCN 应力 | < 200MPa |

### TSV 揭露高度窗口（S2-14）

- 突起 < 1.5μm → 键合接触窗口不足 → 电阻↑
- 突起目标 2–5μm，均匀性 ±0.5μm
- 突起 > 5.5μm → Die 间隙超标 → z-height 超规格
- TSV 暴露缺失 → 断路（直接报废）

### D2W 路线核心优势与瓶颈

- **优势**：KGD 预筛剔除不良 Die（规避 0.99¹² ≈ 88.6% 累积损失）；异构集成灵活；Bumpless 细节距（2μm 节距实测 < 350nm Overlay）
- **量产验证**：BESI Kinex 已获 HBM4E 主流验证
- **最大瓶颈**：S3-3 逐颗逐层 D2W 贴装产能低，为 D2W 路线产能瓶颈

---

*本报告依据 HBM_D2W.pptx（V10）逐页整理，涵盖 Stage 2A（10 步）/ Stage 2B（13 步）/ Stage 3（8 步）共 31 个 Step 的制程参数与量检测节点。*

"""

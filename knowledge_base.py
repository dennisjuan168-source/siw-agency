CPO_KNOWLEDGE = """
# CPO（共封裝光學）知識匯整報告

> 整合來源：33 MD 檔 + 20 DOCX 檔  
> 更新日期：2026-05-19

---

## 目錄
1. [技術概述與核心優勢](#1-技術概述與核心優勢)
2. [五大光互連架構比較](#2-五大光互連架構比較)
3. [TSMC COUPE 製程路線（完整 10 Stage）](#3-tsmc-coupe-製程路線完整-10-stage)
4. [製程設備對照表](#4-製程設備對照表)
5. [光源技術路線](#5-光源技術路線)
6. [調製器技術路線](#6-調製器技術路線)
7. [NVIDIA vs. Broadcom CPO 差異](#7-nvidia-vs-broadcom-cpo-差異)
8. [中國路線：NPO 突圍策略](#8-中國路線npo-突圍策略)
9. [CPO 測試體系](#9-cpo-測試體系)
10. [核心設備商分析](#10-核心設備商分析)
11. [市場規模與時程](#11-市場規模與時程)
12. [台灣供應鏈分析](#12-台灣供應鏈分析)
13. [精密切磨拋加工生態](#13-精密切磨拋加工生態)
14. [投資策略核心洞察](#14-投資策略核心洞察)
15. [各檔案重點摘要](#15-各檔案重點摘要)

---

## 1. 技術概述與核心優勢

### 1.1 CPO 定義
CPO（Co-Packaged Optics，共封裝光學）將光引擎（Optical Engine, OE）與交換機 ASIC 或 GPU 共封裝於同一載板，電氣路徑從傳統 10–30 cm 縮短至 <10 mm。

**四大核心組件：**
- **PIC（光子集成電路）**：波導、MRM、Ge PD、光柵耦合器
- **EIC（電集成電路）**：Driver + TIA，N6/N4 節點
- **OE（光引擎）**：PIC + EIC 最小功能單元，每個 51.2T 系統含 8 顆
- **ELS/ELSFP（外置光源）**：CW 激光器移至面板，熱插拔維護

### 1.2 核心性能對比

| 指標 | 傳統可插拔 | CPO |
|------|-----------|-----|
| 電氣路徑 | 10–30 cm | <10 mm |
| 路徑損耗 | 20–25 dB | ≈4 dB |
| 能耗效率 | ≈15 pJ/bit | <5 pJ/bit（目標 <1） |
| 功耗（/800G） | 20–25 W | 3.5–5.4 W |
| 頻寬密度 | 基線 | 約 10× |
| 可靠性 | 基線 | 約 10×（組件溫度更低） |

### 1.3 技術演進路徑

```
① 可插拔（FPP）：150–250 mm，400G/800G QSFP-DD
② OBO：50–100 mm，板載光學
③ NPO：30–50 mm，光引擎置於 ASIC 旁（鋭捷 25.6T/51.2T）
④ CPO：<10 mm，光引擎與 ASIC 同基板（Broadcom Bailly / NVIDIA Quantum-X）
```

---

## 2. 五大光互連架構比較

| 架構 | 全稱 | 帶寬/模組 | 功耗 | DSP | 熱插拔 | 成熟度 |
|------|------|-----------|------|-----|--------|--------|
| **FPP** | Front-Panel Pluggable | 400G→1.6T | 25–35W/800G | ✅ | ✅ | 完全量產 |
| **LPO** | Linear-drive Pluggable | 1.6 Tbps | 20–25W/800G | ❌ | ✅ | 量產主流（2024–） |
| **NPO** | Near-Packaged Optics | 1.6 Tbps | 20–25W（略低） | ❌ | ❌ | 導入期 |
| **CPO** | Co-Packaged Optics | 800G~12.8T | **3.5–5.4W/800G** | ❌ | ❌ | 早期商用（2026起） |
| **XPO** | eXtra-dense Pluggable | 12.8 Tbps | 400W+/模組 | ❌ | ✅ 盲插 | MSA 發布（2026.3） |

### CPO vs. NPO 核心差異

| 參數 | NPO | CPO |
|------|-----|-----|
| 電氣路徑 | 1–5 cm | 0.1–1 cm |
| 電氣介面 | CEI-VSR / CEI-XSR | CEI-XSR / CEI-USR |
| DSP | 需要（或簡化版） | 完全消除 |
| 頻寬密度 | ~50 Gbps/mm | >140 Gbps/mm |
| 功耗（pJ/bit） | 11–16 | 5–10（目標 <1） |

---

## 3. TSMC COUPE 製程路線（完整 10 Stage）

**平台規格**：PIC 採用 TSMC 65nm SiPh（SiN/SiO₂ 波導），EIC 採用 N6/N4 先進 CMOS，互連方式為 SoIC-X Hybrid Bonding（Cu-Cu W2W F2F，鍵合間距 <10 µm）。

### Stage 0：前置材料備料
- SOI 晶圓：Shin-Etsu/SUMCO
- SiN 前驅體、Ge 靶材
- EIC 晶圓（N6/N4 節點）

### Stage 1（IN1）：PIC 晶圓製造 — TSMC 65nm SiPh

| 製程步驟 | 關鍵規格 |
|----------|---------|
| SiN 波導沉積（LPCVD） | 傳播損耗 <0.01 dB/cm |
| DUV 光刻 + ICP-RIE 刻蝕 | 波導 CD 偏差 <±2 nm |
| Ge 選擇性外延（PD 區域） | RPCVD/UHV-CVD |
| MRM 微環調製器 | 200 Gbps/lane PAM4 |
| 垂直光柵耦合器（COI 接口） | 耦合損耗 0.08 dB，耐高功率 >300 mW |
| 晶圓級光測 | MPI Corp. CM300xi-SiPh |

**產出**：PIC KGW（Known Good Wafer）

### Stage 2（IN2）：SoIC-X W2W Hybrid Bonding（COUPE 核心）

> ⚠️ 常見誤解：IN2 是 **W2W**（Wafer-to-Wafer）F2F 鍵合，非 D2W

| 步驟 | 規格 |
|------|------|
| CMP 平坦化 | Ra <0.5 nm |
| 等離子體活化 + 室溫預鍵合 | — |
| 退火 | 200–400°C，促進 Cu 互擴散 |
| 鍵合間距 | <10 µm |
| 對準精度 | ±0.5 µm |
| W2W 良率 | >99% |
| 鍵合後檢測 | SAM 超音波掃描 + IR 檢查 |

### Stage 3：OE Sub-Assembly（OE Chiplet 成形）

- COUPE die → Si Carrier（D2W 鍵合）→ 電氣測試 → 切割 → Cu Pillar 成形 → KGD 篩選
- **OE Chiplet 結構（由上到下）**：EIC → PIC（65nm SiPh）→ Si Carrier（Cu Pillar）

### Stage 4（IN3）：CoWoS 系統集成封裝

> ⚠️ 常見誤解：OE 直接 bump 上 **ABF Substrate**（非 Si Interposer！）

- HBM 走獨立 Active Si Interposer 並排
- Underfill + 固化 + X-Ray 檢測（Nordson DAGE）
- **IN3 出站門控**：電氣功能驗證通過後才進 IN4

### Stage 5（IN4）：iFAU Fiber Attach — 最大瓶頸

> ⚠️ **全製程難度最高、良率風險最大的工序**

| 要求 | 規格 |
|------|------|
| 主動對準軸數 | 6 軸 |
| 同時驗證通道數 | 40 通道 |
| 對準精度 | <1 µm |
| UV 固化樹脂 | 收縮率 <1%，耐 -40~125°C |
| 每模組對準次數 | 100+ 次 |
| 波長範圍 | O-band 1260–1360 nm |
| BER 驗證 | PAM4 眼圖，全鏈路 BER <10⁻¹² |

**iFAU vs. FAU 核心差異**：
- FAU（LPO/NPO/XPO）：邊緣耦合，1–2 次對準
- iFAU（CPO 專用）：垂直耦合（COI 接口），100+ 次對準，量產化最大瓶頸

### Stage 6：封裝級測試
- HTOL：125°C / 1,000 hrs
- TC：-40~125°C / 500 cycles
- 1.6T 出貨規格：200 Gbps × 8 lanes PAM4，功耗 3.5–5.4 W/800G

### Stage 7：系統集成上機
- NVIDIA 1.6T：36 顆激光 → 288 條鏈路（4:1 共享）
- 不可熱插拔，故障需整機維修

---

## 4. 製程設備對照表

**各架構製程設備差異摘要（節選 CPO 獨有設備）：**

| Stage | Step | CPO 獨有設備 |
|-------|------|-------------|
| PIC 晶圓 | CMP | AFM（Ra<0.5nm）+ KLA OCD（CD<±2nm） |
| 鍵合 | W2W | EVG / SUSS 精密鍵合機（±0.5µm）；等離子活化腔；退火炉 200–400°C；KLA Archer Overlay；SAM 超声波 |
| OE Chiplet | KGD 篩選 | Stealth Dicing（DISCO）；Cu Pillar 電鍍；SEM/X-Ray；ATE |
| 系統集成 | iFAU 組裝 | ficonTEC DLT-D1；Suruga Seiki EW；PICAlign™；精密點膠機（AllRing Tech）；UV 固化炉；DWDM 光測（MPI / Chroma）；AOI |
| 系統上機 | 整合測試 | 系統測試機框；ELS 外部激光源接入；光纖連接治具 |

---

## 5. 光源技術路線

### 5.1 光源選型矩陣

| 光源 | 功耗（Tx） | 成熟度 | 目標世代 | 代表供應商 |
|------|-----------|--------|---------|-----------|
| InP CW DFB（外置 ELS） | — | ★★★★★ 量產 | 1.6T–3.2T CPO | 聯亞（3081）、華星光（4979） |
| InP EML | ~2–5 pJ/bit | ★★★★☆ 量產 | 1.6T 可插拔 | IQE、Lumentum |
| VCSEL | ~1 pJ/bit | ★★★★★ 量產 | Scale-Up <100m | Coherent、Lumentum |
| **MicroLED（Avicena eKit）** | **80 fJ/bit** | ★★★☆☆ 預商用 | 2026–2028 Scale-Up | Avicena |
| On-chip Laser（III-V on Si） | — | ★★☆☆☆ 研究 | 2028+ | — |

### 5.2 CPO 光源搭配邏輯（唯一使用外部 CW 激光的架構）

| 架構 | 光源類型 | 調製器 | 光源位置 | 共享方式 |
|------|---------|--------|---------|---------|
| LPO/NPO | LD / EML | EML / MZM | 模組內 | 每通道獨立 |
| **CPO** | **外部 CW 激光（ELS）** | **MRM 微環** | **封裝外部** | **4:1 共享** |
| XPO | LD / EML | EML / MZM | 超大 PCB | 每通道獨立（×64） |

### 5.3 VCSEL 關鍵參數
- 工作波長：850 nm（GaAs 基底，6 吋晶圓）
- 調製頻寬：20–30 GHz，閾值電流 0.5–2 mA
- 全鏈路能效：~1 pJ/bit
- **核心障礙**：200 Gbps/lane 下熱飽和（Thermal Rollover）
- **台灣缺口**：無自主 VCSEL 磊晶，完全依賴美系（Coherent/Lumentum）

### 5.4 MicroLED（Avicena eKit）關鍵數據
- **Tx 能耗 80 fJ/bit**，全鏈路 <1 pJ/bit（比 VCSEL 低 10×）
- 320 通道 × 3.5 Gbps/ch = 896 Gbps，無 FEC、無 DSP
- Q2 2026 廣泛供貨目標，成本目標 <$0.10/Gbps
- 技術護城河：CROME 磊晶（GaN MicroLED 載子壽命縮短 ~1000×）
- 距離上限：50 m（成像光纖限制）
- **2026–2027 最大技術變數**：若取得 NVIDIA Scale-Up Design Win，VCSEL NPO 市場受衝擊

### 5.5 InP 供應鏈

| 類別 | 廠商 | 備註 |
|------|------|------|
| InP 磊晶片 | 聯亞光電（3081） | 2025 營收 NT$22 億，YoY +82%，台灣最強 |
| InP 磊晶片 | IQE（英國） | 全球最大 III-V 磊晶代工 |
| CW 雷射模組 | 華星光（4979） | TSMC CPO 供應鏈核心節點 |
| InP 代工 | 穩懋（3105） | GaAs/InP 代工龍頭 |

---

## 6. 調製器技術路線

| 調製器 | 電光頻寬 | 溫度敏感度 | 線性度 | 插入損耗 | 晶片面積 | 主推者 | 目標世代 |
|--------|---------|-----------|-------|---------|---------|-------|---------|
| **Si MRM** | 40–50 GHz | **高（80 pm/°C）** | 低 | 1–2 dB | 極小（µm） | NVIDIA/TSMC | 1.6T–3.2T |
| **Si MZM** | 50–60 GHz | 低 | 中 | 3–5 dB | 大（mm） | Broadcom | 1.6T |
| **TFLN MZM** | **>110 GHz** | 低 | 極高 | <1 dB | 中（mm） | InnoLight/UMC | 3.2T+ |

### MRM 熱控解法（TSMC）
- 片上微加熱器（矽化電阻，環內外各 2 組）
- 矽襯底切割隔離
- 45nm CMOS 閉環反饋（微秒級補償：Ge PD → TIA → 差分放大器 → 積分器 → 電流鏡）
- 溫漂 80 pm/°C，0.1nm/K，測試失溫即波長漂移失效

### TFLN 關鍵風險
- 代工生態碎片化（無 TSMC/Samsung 承諾）
- LiNbO₃ 基板：中國供應商比重高，地緣政治風險 ★★★★☆
- 智慧財產：Soitec Smart Cut™ 單一授權源
- 量產時程：3.2T 世代（~2028）才有規模化機會

---

## 7. NVIDIA vs. Broadcom CPO 差異

| 技術維度 | NVIDIA（Quantum-X/Spectrum-X） | Broadcom（Tomahawk 6 Davisson） |
|----------|------------------------------|-------------------------------|
| 調製器 | MRM（極致密度） | MZM（熱穩定性佳） |
| 封裝架構 | 3D SoIC-X Hybrid Bonding | 2.5D/3D MCP |
| 代工平台 | TSMC COUPE/SoIC | TSMC COUPE/先進載板 |
| 雷射源 | 外置 ELS（18 顆驅動 144 埠，1:8 扇出比） | 可現場更換 ELSFP |
| 散熱方案 | 強制液冷 | 氣冷/液冷兼容 |
| 標準化 | OIF 參與但高度排他 | 積極推 OIF ELSFP 開放標準 |
| 市場定位 | AI 封閉生態垂直整合 | 開放 Ethernet 標準 |
| 可靠性聲稱 | 比傳統可插拔高 10× | — |

**Broadcom 產品路線**：Humboldt（25.6T）→ Bailly（51.2T，5.5W/800G）→ Davisson TH6（102.4T，2025 年底出貨）

**NVIDIA 產品時程**：
- Quantum-X800 CPO（2026 H1，InfiniBand，115 Tb/s）
- Spectrum-X1600 CPO（2026 H2，Ethernet，409.6 Tb/s）
- Rubin Ultra NVL576（~2027，全光 I/O）

---

## 8. 中國路線：NPO 突圍策略

### 8.1 為什麼中國選 NPO？

1. **ASIC 解耦**：NPO 直接使用商用 ASIC，無需裸片二次封裝，規避地緣政治風險
2. **良率與成本**：光引擎與 ASIC 分別測試封裝，損壞只換板不廢 ASIC
3. **分散式散熱**：光引擎環狀分布，熱解耦設計更靈活

### 8.2 中國核心玩家

| 廠商 | 角色 | 代表產品 |
|------|------|---------|
| 鋭捷網絡 | NPO+液冷最堅定執行者 | 25.6T / 51.2T NPO 交換機 |
| 華為 HiSilicon | 「以光代電」主導 IPEC 標準 | OptiX 體系 |
| H3C | AIGC 集群 CPO 硅光交換機 | S9827 系列 800G CPO |
| 中際旭創（InnoLight） | NPO 產業鏈核心，光引擎量產 | 1.6T/3.2T 板載光引擎 |
| 光迅科技（Accelink） | CPO 三件套全棧布局 | 光引擎 + ELSFP + Fiber Shuffle Box |

### 8.3 標準之戰：OIF vs. IPEC

| 標準 | 主導方 | 互操作性 |
|------|--------|---------|
| **OIF ELSFP** | Broadcom/Cisco/Lumentum | 全球通用，多廠相容 |
| **IPEC PELS** | 華為/中際旭創/中興/光迅 | 中國生態，與 ELSFP 物理不相容 |

**光迅科技策略**：同時支持 OIF ELSFP 與 IPEC PELS，兩邊通吃，規避地緣政治風險。

**光迅科技 CPO 三件套**：
1. **光引擎**（大腦）：硅光調製器+波導+探測器，支援 3.2T+
2. **Fiber Shuffle Box**（血管）：>400 芯 FA，Mini MT 12/16 芯，節省 70% 空間
3. **ELSFP**（心臟）：熱插拔，單通道光功率 >20 dBm

### 8.4 NPO→CPO 演進時間節點

- **2025–2027**：NPO 黃金窗口期，51.2T 時代中國市場主導
- **2028+**：102.4T 時代 PCB 信號損耗不可接受，CPO 必然接棒

---

## 9. CPO 測試體系

### 9.1 四大測試節點邏輯分工

| 節點 | 名稱 | 核心任務 | ficonTEC 型號 | 協同設備商 |
|------|------|---------|-------------|-----------|
| IN1 | PIC Wafer Level | WLBI + 光電特性 Mapping | WLT-D2/S2 | AEHR FOX-XP |
| IN2 | EIC-PIC Stacking | 3D 堆疊亞微米對準驗證 | AL2000/WLT | MPI 旺矽（MEMS 探針卡）|
| IN3 | Die Sort（KGD） | 已知好晶粒最終光電篩選 | DLT-D1/S1 | 致茂 Chroma |
| IN4 | Co-testing | 1.6T 系統級同測 + 主動對準組裝 | AL2000-CPO | 致茂 3680、穎崴 |
| FT | Final Test | 成品最終特性 + 出貨驗證 | TestLine T-Series | 致茂（Load Board）|

### 9.2 測試左移（Shift-Left）經濟邏輯

IN1 老化篩選至關重要：雷射器若在 IN4 封裝後才失效，單顆報廢成本可高達**數萬美元**。早期 KGW/KGD 篩選是降低成本的唯一路徑。

### 9.3 晶圓測試熱管理要求

- WFT（功能性測試）：溫控精度 ±0.1°C，表面溫差 ≤0.23°C
- WLBI（老化測試）：150–300°C，持續數小時，處理數千瓦熱負荷
- AirCool® PRIME 可將浸泡時間縮短 60%
- MRM 共振波長溫度敏感度：~80 pm/°C，0.1 nm/K

### 9.4 1.6T 量產良率診斷（目前 65–75%）

**四大良率死穴：**
1. 物理偏移：焊接後偏移 >0.2 µm 即失效
2. 訊號損耗：224G PAM4 對反射極敏感，BER 超標
3. 熱漂移：1000W 功耗下，微秒級溫控延遲致雷射波長偏移
4. 界面受損：COUPE Hybrid Bonding 結構脆弱，組裝應力致微裂

**預期 2026 年底良率衝擊 85%**，封測廠毛利顯著提升。

### 9.5 泰瑞達 vs. 愛德萬 CPO 測試方案

| 維度 | 泰瑞達（Teradyne） | 愛德萬（Advantest） |
|------|-------------------|-------------------|
| 光學整合 | 內置（收購 Quantifi Photonics 2025 Q2） | 第三方 OCL 開放接口 |
| 對準技術 | **雙面探針**（3D-CPO 優勢） | 單面訪問（量產效率優勢）|
| 合作夥伴 | ficonTEC（業界首款雙面晶圓探針測試單元）| FormFactor（Triton PTS 九軸）|
| 適合客戶 | NVIDIA 極致集成路徑 | Broadcom 標準化量產路徑 |
| 軟件 | IG-XL（C#/.NET） | SmarTest 8（Java/Linux） |
| 散熱架構 | — | 水冷（四代堅持）|

---

## 10. 核心設備商分析

### 10.1 設備商戰略分工

| 廠商 | 戰略角色 | 技術護城河 |
|------|---------|-----------|
| **ficonTEC（羅博特科 300757）** | The Assembler | 亞微米主動對準，TSMC 生態綁定最深 |
| **致茂 Chroma** | The Brain | 224G 訊號驅動、BER 測試、1000W 精密溫控 |
| **MPI 旺矽（6223）** | The Verifier | IN2 MEMS 探針卡，驗證 Hybrid Bonding 電性 |
| **穎崴 WinWay（6515）** | The Interface | HyperSocket™（224G 優化），MEMS 探針卡 |

### 10.2 測試三巨頭財務（2024–2025）

| 公司 | 2025 營收 | YoY | CPO 優勢 |
|------|----------|-----|---------|
| Keysight 是德 | $53.7 億 | +7.8% | 1.6T/224G 標準測試，E-O-E 仿真 |
| Teradyne 泰瑞達 | $31.9 億 | +13.1% | 雙面晶圓探測，AI 貢獻 >60% 季收 |
| Advantest 愛德萬 | ¥1.07 兆 | +37.2% | AI SoC/HBM 霸主，FormFactor 聯盟，凈利翻倍 |

- SiPh/CPO 測試設備市場：2025 年 **$13.6 億** → 2032 年 **$20.4 億**

### 10.3 ficonTEC（羅博特科）財務

- 2025 光電子及半導體業務：**4.855 億人民幣**，YoY +867.54%
- 在手訂單：**11.05 億人民幣**
- 佔羅博特科總營收 >50%
- 正推進港股 H 股 IPO

---

## 11. 市場規模與時程

### 11.1 市場規模預測

| 指標 | 數據 | 來源 |
|------|------|------|
| 全球光互連 TAM（GB300 時代）| $15bn | Goldman Sachs 2026 |
| 全球光互連 TAM（Rubin Ultra 時代）| **$154bn（9× 擴張）** | Goldman Sachs 2026 |
| CPO 在 TAM 中占比 | **59%（$91bn）** | Goldman Sachs 2026 |
| CPO 市場 CAGR | 37%（2026 起） | IDTechEx 2025.12 |
| CPO 市場（2036）| **>$200 億** | IDTechEx |
| CPO 市場（2024）| $4,600 萬 | — |
| CPO 市場（2030）| **$81 億** | — |
| 矽光子市場（2024）| ~$1.5B | — |
| 矽光子市場（2035）| **$17.8B** | — |
| SiPh 滲透率（2028E）| **46%** | Goldman Sachs |
| 數據中心光學互連（2034）| **$46B** | — |

### 11.2 出貨量預測

| 年度 | CPO 滲透率 | NVIDIA 出貨量 | 主要推動力 |
|------|-----------|-------------|-----------|
| 2025 | <10% | <1,000 台 | 試點 |
| **2026** | **20–30%** | **≈1.5 萬台** | **1.6T 爆發、Rubin 量產** |
| 2027 | >40% | 數十萬台 | 3.2T 成熟、TCO 顯著下降 |
| 2029 | — | 1,800 萬台 | CPO 規模化 |

**TSMC COUPE Roadmap**：1.6T（2026）→ 3.2T（2027）→ 6.4T（~2028）→ 12.8T（~2029+）

### 11.3 CSP 資本支出超級週期

- 北美四大雲端（MS/Google/AWS/Meta）2026 年 Capex 預計逼近 **3,500 億美元**
- **Meta**：與 Corning 簽 **$60 億**多年光纖供應協議
- **Google**：OCS 光路切換，1.6T CPO 代工由訊芯-KY 承接
- **AWS**：鎖定 800G CPO，大量訂單交予華星光
- **微軟 Fairwater**：研發空心光纖（HCF）

### 11.4 技術演進時間線

```
2026：InP CW ELS + Si MRM（CPO 1.6T）量產，矽光子 CPO 商轉元年
      NVIDIA Spectrum-X Photonics H2 上市；訊芯-KY Google 訂單出貨
2027：MicroLED（Avicena）Scale-Up 早期商用；TFLN 滲透可插拔市場
      3.2T CPO（Rubin Ultra NVL576）
2028：TFLN 成為 3.2T+ 主力調製器；玻璃 CPO 客戶認證（Corning/Intel）
2029+：TFLN/MicroLED 規模化；Optical I/O Chiplet 導入；12.8T（XPO）
2030：光收發器市場 SiPh 占比 >60%；CPO 占 800G+ 市場 >50%
```

---

## 12. 台灣供應鏈分析

### 12.1 核心廠商一覽

| 廠商（代號） | CPO 角色 | 關鍵指標 |
|------------|---------|---------|
| **台積電（2330）** | COUPE/SoIC-X 製程核心 | 65nm SiPh + N6/N4 EIC |
| **聯亞（3081）** | InP CW 磊晶，ELS 供應 | 2025 YoY +82%，光通訊佔比 78% |
| **上詮（3363）** | FAU/iFAU 關鍵供應商 | ReLFACon FAU 2026 Q3 量產；馬來西亞新廠 Q2 |
| **FOCI（上詮旗下）** | iFAU 市占 ~50% | IN4 光纖對準核心供應商 |
| **Browave 波若威（3163）** | FAU/iFAU 第二供應商 | NVIDIA Spectrum-X 指名供應商 |
| **華星光（4979）** | CW 雷射模組，3D SiPh | AWS/Marvell 核心代工，2026 產能翻倍 |
| **訊芯-KY（6451）** | CPO 晶圓級封裝 OSAT | Google 1.6T 大單，5K → 20K wafer |
| **旺矽（6223）** | MEMS 探針卡，晶圓測試 | 月產能 200 萬根，2026 EPS 目標 50 元+ |
| **穎崴（6515）** | 測試 Socket HyperSocket™ | 探針自製翻倍至 600–700 萬支，毛利率 >50% |
| **中華精測（6510）** | 高階探針卡 | 2026 Q1 營收歷史新高 |
| **全新光電（2455）** | GaAs/InP 磊晶（VCSEL/EML 用） | NPO 受惠，2026 GaAs 利用率回升 |
| **MPI Corp.** | 晶圓光測設備 | TSMC IN4 直接合作 |

### 12.2 OOSAT 生態（組裝代工）

| 廠商 | 角色 | 規模 |
|------|------|------|
| **Fabrinet（泰國）** | ficonTEC 最大客戶，NVIDIA 代工 | Building 9/10 |
| **貿聯 BizLink** | 併購新富聲（Sinfox），挑戰 Fabrinet | — |
| **訊芯-KY（6451）** | Google 1.6T CPO 代工 | 5K → 20K wafer/月 |
| **天孚通信（TFC）** | FAU、無源互聯、光引擎服務 | 毛利率 >50%，單台 CPO >$7,000 ASP |

### 12.3 全球關鍵廠商

| 廠商 | 角色 |
|------|------|
| Broadcom | CPO ASIC，Bailly/Davisson TH6，Meta 驗證 100 萬+ 小時 |
| NVIDIA | 全堆疊集成（Quantum-X / Spectrum-X Photonics） |
| ficonTEC | IN4 主動對準設備市場領導者，TSMC COUPE 綁定最深 |
| Lumentum / Coherent | EML 光源，NVIDIA 鎖定產能至 2027 |
| Corning | 光纖、IOX 玻璃波導，Meta $60 億供應協議 |
| Marvell | 6.4T 光引擎 / SiPh 平台，參考設計 |

---

## 13. 精密切磨拋加工生態

### 13.1 切割設備（台灣原廠）

| 廠商 | 核心技術 | CPO 切入點 |
|------|---------|-----------|
| **鐳射谷（Intelume）** | 超快雷射切割鑽孔 + AOI | SiPh 晶圓分割，亞微米定位 |
| **京碼（Hortech）** | LIDE 雷射誘導蝕刻 | TGV 玻璃基板，孔徑 10~80µm，深寬比 >10:1，零微裂紋 |
| **正鉑雷射（Jumbo Laser）** | 晶圓級雷射切割 | 高價值 SiPh 晶粒分割，最小切寬 10µm |
| **景鴻科技（CL Technology）** | 雷射劃線 + 光譜監控 | 晶圓初期分割，在線製程監控 |

### 13.2 研磨拋光設備

| 廠商 | 核心設備 | 關鍵規格 |
|------|---------|---------|
| **世極（Secular）** | 直立式減薄機、雙面研磨拋光機 | TTV 微米級以下，供應台積電/美光 |
| **邁均機械（MAI JIUN）** | LP-990 橢圓型高速拋光機 | 支援矽/藍寶石/石英/鍺等多元材料 |
| **辛耘（Scientech）** | CS200 CMP 拋光系統 | Dry-in/Dry-out，整合雙面清洗 |
| **弘塑科技（Grand Process）** | 8/12 吋自動化濕式清洗機 | CMP 後精密清洗 |

### 13.3 CMP 材料耗材

| 廠商 | 產品 | 競爭優勢 |
|------|------|---------|
| **中國砂輪（Kinik）** | 鑽石碟（PYRADIA）、砂輪、吸盤 | 月出貨量邁向 50,000 顆，先進製程標準配備 |
| **頌勝科技（Sungsan）** | CMP 研磨墊 | 台灣唯一量產商，已進入晶圓代工廠供應鏈 |
| **達興材料（Daxin）** | 拋光液、清洗液、介電材 | 高選擇比、低刮傷率，保護光波導結構 |
| **宏崴實業** | 多晶鑽石研磨液 | 石英/化合物半導體客製化配方 |
| **九羽企業** | 鑽石砂輪、CBN 工具 | 台灣在地製造，藍寶石/石英客製磨頭 |

---

## 14. 投資策略核心洞察

1. **設備即先行指標**：ficonTEC AL2000-CPO 與 DLT-D1 交機量是預判 1.6T 放量的最佳先行指標
2. **良率是利潤槓桿**：目前 65–75%，2026 年底衝 85%，屆時訊芯/Fabrinet 毛利顯著提升
3. **測試設備需求非線性**：若 400G/lane 技術延遲，被迫用 200G×16 通道，測試次數翻倍，TAM 反而更大
4. **光源是定價權所在**：NVIDIA 已鎖定 Lumentum/Coherent 產能至 2027，InP CW ELS 供應緊張
5. **地緣套利**：泰國成為 1.6T OOSAT 主基地；台灣圍繞 TSMC COUPE；中國走 NPO + IPEC 自主路線
6. **台股資金輪動**：資金從下游組裝股（鴻海/廣達）集中至 CPO/HBM 族群，上詮/華星光/全新 曾同日漲停
7. **MicroLED 是 2026–2027 最大技術變數**：若 Avicena 取得 NVIDIA Scale-Up Design Win，VCSEL NPO 市場受衝擊
8. **TFLN 是 3.2T（2028）必爭之地**：代工碎片化 + LiNbO₃ 供應鏈集中（中國比重高）= 地緣政治加分
9. **CPO 不可熱插拔維修風險**：NVIDIA OSA 可維護性方案（可拆卸 OSA）為部分解決
10. **2026 年商轉元年**：1.6T 滲透率達 20–30%，測試設備、光源、FAU 三大環節最先受益

**TCO 分析**：

| 項目 | 傳統插拔 | CPO |
|------|---------|-----|
| CAPEX | 1× | ~2.3× |
| 能源效率 | 15–20 pJ/bit | 5–10 pJ/bit |
| 51.2T 節點節電 | — | 400–500W/節點 |
| 設備生命週期回報 | — | 3–5 年 OPEX 顯著優勢 |

---

## 15. 各檔案重點摘要

| 檔案 | 核心重點 |
|------|---------|
| CPO_1.6T_3.2T供應鏈解析 | 完整供應鏈角色地圖，各節點廠商與競爭格局 |
| CPO_1.6T測試與供應鏈研究報告 | 測試節點 IN1–FT，KGD 良率診斷 65–75% → 85% |
| CPO_Process_Route | COUPE 10-Stage 完整製程路線，各 Stage 技術規格 |
| CPO_Process_TSMC_MD档 | TSMC COUPE 平台詳細技術規格（65nm SiPh + N6/N4 EIC）|
| CPO_綜合研究報告 | 技術架構、市場預測、供應鏈、投資邏輯綜合整理 |
| CPO供應鏈角色與終端客戶 | CSP（NVIDIA/Broadcom/Meta/Google/AWS）採購策略 |
| CPO供應鏈調研匯整 | 全球供應鏈地圖，台灣/中國/美國廠商定位 |
| CPO光源與調製器框架_v2/v3 | 五種光源技術路線詳細比較，MicroLED vs VCSEL vs TFLN |
| CPO市場增長與技術探討 | IDTechEx CAGR 37%，2036 >$200 億，CPO TAM $91B |
| CPO技術NVIDIA與Broadcom差異 | NVIDIA（MRM/SoIC-X）vs Broadcom（MZM/開放標準）深度分析 |
| CPO方案对比分析 | FPP/LPO/NPO/CPO/XPO 五方案全面對比 |
| CPO晶圓測試高溫處理探討 | WLBI 150–300°C 熱管理，AirCool® PRIME |
| CPO测试市场三巨头分析 | Keysight/Teradyne/Advantest 財務對比與 CPO 競爭策略 |
| CPO测试流程分析 | IN1–FT 完整測試流程，設備商分工 |
| CPO測試流程與技術演進 | 測試左移策略，KGD 經濟學 |
| CPO溫控MRM關鍵挑戰 | 80 pm/°C 溫漂，片上微加熱器解法，閉環反饋 |
| CPO與NPO光模塊差異分析 | CPO vs NPO 詳細性能/成本/可靠性對比 |
| FPP/LPO/NPO/CPO/XPO架構分析 | 五大架構定義、規格、適用場景完整分析 |
| LPO_NPO_CPO_XPO_Fiber_FAU | FAU vs iFAU 對比，COI 介面，光纖通道數計算 |
| Session_Memory_CPO框架 | 研究框架備忘，議題追蹤 |
| TGV应用三_玻璃光波導CPO | IOX/FLDW/SiN 三種玻璃波導路線，Corning/Sumitomo/Intel |
| TSMC_CPO_1.6T_3.2T制程细节 | COUPE 1.6T/3.2T 製程差異，材料規格 |
| TSMC_CPO_完整工艺流程_IN1_to_上机 | Stage 0–7 完整工藝步驟，設備商對應 |
| 光源搭配方式_LPO_NPO_CPO_XPO | 各架構光源選型邏輯，功耗對比 |
| 光焱科技CPO產品與技術 | NightJar HSI 高光譜顯微成像，2026 量產設備路線 |
| 台灣CPO切磨拋原廠名錄 | 鐳射谷/京碼/正鉑/世極/中國砂輪等 15+ 廠商詳解 |
| 台股市場分析CPO與籌碼動態 | 2026/01/19 台股 31,639 歷史高點，CPO 板塊動態 |
| 泰瑞達矽光CPO投資分析 | 收購 Quantifi，雙面探針系統，Q2 2025 財務 |
| 泰瑞達與愛德萬CPO測試方案比較 | 雙面 vs 單面探針，IG-XL vs SmarTest 8 |
| 矽光子CPO2026商轉元年 | 2026 量產時間線，各 CSP 部署計畫 |
| 議題1_CPO光源與調製器完整框架 | MRM/MZM/TFLN/VCSEL/MicroLED 五路線 2026–2030 Roadmap |
| **CPO视频选题素材_光迅科技** | 光迅 CPO 三件套全解析，中國 NPO vs CPO 戰略，標準戰 OIF vs IPEC |
| **Taiwan_CPO_SiPh精密切磨拋報告** | 鐳射谷/京碼/世極/中國砂輪等台灣設備商深度分析，TGV 加工技術 |
| **LPO_NPO_CPO_XPO製程設備對照表** | Stage 1–8 各架構設備完整對照表（含 CPO 獨有設備標記）|

"""

TGV_KNOWLEDGE = """
# TGV（T
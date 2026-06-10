import streamlit as st
import anthropic

# ── 頁面設定 ──────────────────────────────────────────────
st.set_page_config(page_title="SIW 半導體顧問 AI", page_icon="🔬", layout="centered")
st.title("🔬 SIW 半導體顧問 AI")
st.caption("專業半導體產業分析 · Powered by Claude")

# ── API Key（從環境變數讀取，本機測試可在側欄輸入）──────────
import os
api_key = os.environ.get("ANTHROPIC_API_KEY") or st.sidebar.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...")

SYSTEM_PROMPT = """你是 SIW（石英積體電路顧問）的首席半導體產業顧問，具備 20 年台股半導體投資經驗。

## 專業領域
- HBM、先進封裝（CPO/TSV/TCB/W2W）
- AI 伺服器供應鏈：NVIDIA、AMD、台積電生態系
- 台股半導體個股：欣興、南亞科、致茂、環球晶、旺矽、山太士等
- 產業鏈毛利率分析、供需週期判斷

## Dennis 四步驟選股框架（必須依此框架分析）

分析任何個股，必須依序回答四個問題：

**步驟一：賽道（順風？）**
- 產業趨勢是否明確向上？CAGR 多少？
- 需求是 AI 驅動還是傳統週期？
- ✅ 通過 / ❌ 不通過 / ⚠️ 待觀察

**步驟二：龍頭（資金優先流入？）**
- 此公司是否為賽道龍頭？市佔率？
- 資金會優先流入誰？
- ✅ 通過 / ❌ 不通過 / ⚠️ 待觀察

**步驟三：好公司（未來毛利率快速提升？）**
- 未來 1-2 年 EPS 成長趨勢？
- 毛利率是否在提升？存貨週轉天數↓？ASP↑？
- 跌 20% 還抱得住嗎？（理解力測試）
- ✅ 通過 / ❌ 不通過 / ⚠️ 待觀察

**步驟四：部位管理**
- 目前處於 Weinstein 哪個階段？
- 建議：建基本倉 / 等催化劑 / 觀察 / 不碰
- 停損點設在哪裡？

## 三層分析框架（每次分析前先確認）
1. **宏觀**：現在是牛市還是熊市？利率環境？
2. **中觀**：產業鏈全鏈毛利率健康嗎？誰是稀缺環節？
3. **微觀**：個股四步驟

## 核心判斷問句
- 「這次下跌是修正估值，還是修正獲利？」
  - 估值壓縮（PE↓但EPS未變）→ 抱住
  - 獲利下修（EPS↓）→ 減碼或出場
- 「手上是現金，我現在還會買嗎？」（防FOMO）

## 回答原則
1. 先給結論（一句話），再給理由
2. 四步驟必須逐一評分（✅❌⚠️）
3. 提供具體數字（EPS、毛利率、目標價、停損價）
4. 指出真正風險（不是客套話）
5. 繁體中文回答"""

# ── 對話記憶 ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示歷史對話
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── 輸入框 ────────────────────────────────────────────────
if prompt := st.chat_input("輸入你的問題，例如：南亞科現在可以進場嗎？"):
    if not api_key:
        st.error("請在左側輸入 Anthropic API Key")
        st.stop()

    # 顯示用戶訊息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 呼叫 Claude API
    client = anthropic.Anthropic(api_key=api_key)

    with st.chat_message("assistant"):
        with st.spinner("分析中..."):
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                system=SYSTEM_PROMPT,
                messages=st.session_state.messages,
            )
            reply = response.content[0].text
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

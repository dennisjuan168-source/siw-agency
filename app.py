import streamlit as st
import anthropic
import os
import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ── 頁面設定 ──────────────────────────────────────────────
st.set_page_config(page_title="SIW 半導體顧問 AI", page_icon="🔬", layout="centered")
st.title("🔬 SIW 半導體顧問 AI")
st.caption("半導體產業分析框架與洞察 · Powered by Claude")

# ── API Key（從環境變數讀取，本機測試可在側欄輸入）──────────
api_key = os.environ.get("ANTHROPIC_API_KEY") or st.sidebar.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...")

# ── 產業快訊（管理員輸入，影響 AI 回答）─────────────────────
st.sidebar.markdown("---")
with st.sidebar.expander("📡 產業快訊更新（管理員）"):
    admin_news_pw = st.text_input("管理員密碼", type="password", key="news_pw")
    if admin_news_pw == os.environ.get("ADMIN_PASSWORD", "siw743137"):
        news_input = st.text_area(
            "貼上最新產業動態",
            value=st.session_state.get("industry_news", ""),
            height=200,
            placeholder="例如：\n- 南亞科Q2法說：毛利率提升至45%\n- HBM3E需求超預期，SK Hynix擴產\n- 聯準會維持利率不變"
        )
        if st.button("更新快訊"):
            st.session_state["industry_news"] = news_input
            st.success("快訊已更新！AI 下次回答將參考此資訊")

# ── Google Sheets Log ─────────────────────────────────────
SHEET_ID = "1HpPRlc3WB6d3iSQ8S025vA-YVeppFGL4mUMkiUAEn24"

@st.cache_resource
def get_sheet():
    try:
        creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SHEET_ID).sheet1
        if sheet.row_count == 0 or sheet.cell(1, 1).value != "時間":
            sheet.append_row(["時間", "問題", "回答"])
        return sheet
    except Exception:
        return None

def save_log(question, answer):
    sheet = get_sheet()
    if sheet:
        sheet.append_row([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), question, answer])

SYSTEM_PROMPT = """你是 SIW（石英積體電路顧問）的首席半導體產業顧問，具備 20 年台股半導體投資經驗。

**核心定位：Dennis 分享的是分析框架與產業洞察，不是報股價。**
- 股價、EPS 等即時數字由用戶提供
- SIW AI 提供的是：判斷邏輯、產業趨勢、風險評估、進出場框架

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

## 最新產業快訊（2026-06-11 更新）

**南亞科 2408：**
- Q1 2026 營收 490億，季增63%，年增583%
- Q1 毛利率 67.9%（上季 49%，大幅躍升）
- 5月營收 276億，年增 730%
- DDR5/DDR4 持續缺貨，AI 伺服器需求強勁
- 資本支出 500億，擴大 2.7倍，導入 EUV 設備
- 泰山新廠 2027年初裝機
- FactSet 16位分析師共識目標價 305元，現價約 333元（已超共識目標價）

## 數據使用原則
- **優先使用用戶提供的數字**（現價、EPS、毛利率等）
- 若用戶未提供現價，主動詢問：「請告訴我目前股價，讓我給你更準確的分析」
- 不要自己猜測或捏造股價數字
- 產業趨勢與框架分析可依知識庫，但個股數字必須由用戶確認

## 回答原則
1. 先給結論（一句話），再給理由
2. 四步驟必須逐一評分（✅❌⚠️）
3. 數字用用戶提供的，沒有數字就問
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
if prompt := st.chat_input("請告訴我股票名稱＋現價，例如：南亞科 現價407，可以進場嗎？"):
    if not api_key:
        st.error("請在左側輸入 Anthropic API Key")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    client = anthropic.Anthropic(api_key=api_key)

    with st.chat_message("assistant"):
        with st.spinner("分析中..."):
            news = st.session_state.get("industry_news", "")
            system = SYSTEM_PROMPT
            if news:
                system += f"\n\n## 最新產業快訊（Dennis 提供，優先參考）\n{news}"

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                system=system,
                messages=st.session_state.messages,
            )
            reply = response.content[0].text
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    save_log(prompt, reply)

# ── 管理員：查看 Log ──────────────────────────────────────
with st.sidebar.expander("📊 查看對話記錄"):
    admin_pw = st.text_input("管理員密碼", type="password", key="admin")
    if admin_pw == os.environ.get("ADMIN_PASSWORD", "siw743137"):
        sheet = get_sheet()
        if sheet:
            import pandas as pd
            data = sheet.get_all_records()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df[["時間", "問題"]], use_container_width=True)
                st.download_button("下載完整記錄", df.to_csv(index=False).encode("utf-8"), "log.csv")
            else:
                st.info("還沒有對話記錄")
        else:
            st.warning("Google Sheets 連線失敗")

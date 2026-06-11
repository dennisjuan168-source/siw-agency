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
    if admin_news_pw == st.secrets.get("ADMIN_PASSWORD", ""):
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

_base_prompt = st.secrets.get("SYSTEM_PROMPT", "你是 SIW 半導體顧問 AI，請用繁體中文回答半導體產業問題。")
_knowledge = st.secrets.get("KNOWLEDGE_BASE", "")
SYSTEM_PROMPT = _base_prompt + ("\n\n## Dennis 技術知識庫\n" + _knowledge if _knowledge else "")

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
    if admin_pw == st.secrets.get("ADMIN_PASSWORD", ""):
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

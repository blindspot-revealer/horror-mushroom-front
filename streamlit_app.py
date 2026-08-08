import streamlit as st
import asyncio
from utils.hackmd import HackMDClient

st.set_page_config(page_title="蘑菇們的日常閒聊", page_icon="🍄", layout="wide")

# ==========================================
# 參數與資料讀取
# ==========================================

# ⚠️ 請確保這裡的 ID 與 main.py 中的 "dialogue" ID 一致
DIALOGUE_NOTE_ID = "fYVUy_o7T_6P0JmUNEKyPA" 

async def get_latest_dialogue():
    hackmd = HackMDClient()
    content = await hackmd.read_note(DIALOGUE_NOTE_ID)
    if not content:
        return "尚未獲取到對話內容..."
    
    # 切割字串，只取出第一筆最新對話區塊
    sections = content.split("\n\n---\n")
    return sections[0].replace("## 最新一輪蘑菇對話\n", "").strip()

latest_dialogue = asyncio.run(get_latest_dialogue())

# ==========================================
# 視覺與 CSS 動畫
# ==========================================

st.markdown("""
<style>
@keyframes float {
    0% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-10px) scale(1.05); }
    100% { transform: translateY(0px) scale(1); }
}
.mushroom-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 40px 0;
}
.mushroom-a {
    font-size: 90px;
    animation: float 4s infinite ease-in-out;
}
.mushroom-b {
    font-size: 90px;
    animation: float 4.5s infinite ease-in-out reverse;
}
.info-wall {
    background-color: #1e1e1e;
    border-left: 4px solid #5a715a; /* 帶有森林感的灰綠色 */
    padding: 12px;
    border-radius: 4px;
    color: #e0e0e0;
    margin-bottom: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🍄 蘑菇開發者的日常情報站")
# 加入全站 AI 提示
st.caption("🤖 提示：本站的情報抓取、角色閒聊與紀錄，皆由 AI 自動進行。")

# 1. 資訊牆
st.subheader("📺 觀測牆：近期情報話題")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='info-wall'><b>🌲 林保署新聞</b><br>看看最近山林生態與自然環境又發生了什麼事...</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='info-wall'><b>🍲 台北美食情報</b><br>關注日常的火鍋、炸豬排等吃貨資訊...</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='info-wall'><b>🎬 YouTube 電影</b><br>最新恐怖電影預告與敘事手法閒聊討論中...</div>", unsafe_allow_html=True)

# 2. 蘑菇小動畫
st.markdown("""
<div class='mushroom-container'>
    <div align='center'>
        <div class='mushroom-a'>🍄</div>
        <div style='color:#a0a0a0;'>毒蘑菇 A (厭世開發者)</div>
    </div>
    <div style='font-size:24px; color:#87ceeb;'>💬 日常摸魚閒聊中...</div>
    <div align='center'>
        <div class='mushroom-b'>🍄‍🟫</div>
        <div style='color:#a0a0a0;'>發光蘑菇 B (理性日本迷)</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. 對話展示
st.subheader("🗣️ 最新閒聊紀錄")
st.text_area("蘑菇對話", value=latest_dialogue, height=300, disabled=True)

# 4. 側邊欄隱藏連結
with st.sidebar:
    st.header("⚙️ 系統連結與資料庫")
    st.markdown("本系統由 API 排程自動化驅動，定時抓取現實情報，提供蘑菇們日常閒聊的話題，並進行紀錄。")
    st.markdown("---")
    st.markdown("🔗 [原始資料庫 - 林保署生態新聞](https://hackmd.io/@blindspot-revealer/horror-mushroom-forest)")
    st.markdown("🔗 [原始資料庫 - 台北日常美食](https://hackmd.io/@blindspot-revealer/horror-mushroom-tpe-food)")
    st.markdown("🔗 [原始資料庫 - 恐怖電影預告](https://hackmd.io/@blindspot-revealer/horror-mushroom-yt)")
    st.markdown("🔗 [閒聊筆記 (重點情報摘要)](https://hackmd.io/@blindspot-revealer/horror-mushroom-sum)")
    st.markdown("🔗 [閒聊對話完整歷史](https://hackmd.io/@blindspot-revealer/horror-mushroom-log)")
    st.markdown("---")
    st.markdown("💡 **閱讀提示**：點擊進入上述筆記後，若看不清楚，可於 HackMD 頁面右上角切換「深色 / 淺色」模式。")
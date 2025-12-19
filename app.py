import streamlit as st
from datetime import datetime

st.set_page_config(page_title="IA Cockpit", layout="wide", page_icon="🚀")

# 1. STYLE CSS
st.markdown("""
<style>
.card {
    background: white; padding: 15px; border-radius: 12px;
    border: 1px solid #eee; text-align: center; height: 140px;
    transition: 0.3s; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.card:hover { border-color: #ff4b4b; transform: translateY(-3px); }
.icon { font-size: 30px; }
.title { font-size: 14px; font-weight: bold; color: #31333F; }
a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# 2. SIDEBAR
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state:
    st.session_state.list = []

new_t = st.sidebar.text_input("Ajouter tâche")
if st.sidebar.button("Ajouter"):
    if new_t:
        st.session_state.list.append(new_t)
        st.rerun()

for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")

if st.sidebar.button("Tout vider"):
    st.session_state.list = []
    st.rerun()

st.sidebar.text_area("Notes", height=150)

# 3. TITRE ET RECHERCHE
st.title("🚀 Sales Cockpit IA")

col_s1, col_s2 = st.columns(2)
with col_s1:
    s_goog = st.text_input("Rechercher sur Google")
    if s_goog:
        url_g = f"https://www.google.com/search?q={s_goog.replace(' ', '+')}"
        st.markdown(f'[🔎 Lancer Google]({url_g})')

with col_s2:
    s_li = st.text_input("Rechercher sur LinkedIn")
    if s_li:
        url_li = f"https://www.linkedin.com/search/results/all/?keywords={s_li.replace(' ', '%20')}"
        st.markdown(f'[👤 Voir sur LinkedIn]({url_li})')

st.divider()

# 4. GRILLE DES APPLIS (Remises bien en évidence)
u1 = "https://cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/"
u2 = "https://freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/"
u3 = "https://go-nogo-ao-guljf7vfdgd8gwbwk2czss.streamlit.app/"
u4 = "https://ia-discovery-tool-exipby6qyeqodoryc8p7kj.streamlit.app/"
u5 = "https://objection-crusher-eickr9egabodnbspah7zgh.streamlit.app/"
u6 = "https://sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy.streamlit.app/"
u7 = "https://simulateuria-4geraztakpppefxpsvfp5z.streamlit.app/"
u8 = "https://account-manager-ia-hwtkfcycxcxcgqtxrhyrez.streamlit.app/"

tools = [
    ("CV Optimizer", "🎯", u1), ("Marge/Rentab", "⚖️", u2),
    ("Go/No-Go AO", "🚦", u3), ("IA Tool", "🔍", u4),
    ("Objection", "🛡️", u5), ("KPI Tracker", "📈", u6),
    ("Simu IA", "🤖", u7), ("Account Mgr", "🤝", u8)
]

c = st.columns(4)
for i in range(8):
    with c[i%4]:
        st.markdown(f"""
        <a href="{tools[i][2]}" target="_blank">
            <div class="card">
                <div class="icon">{tools[i][1]}</div>
                <div class="title">{tools[i][0]}</div>
            </div>
        </a>
        """, unsafe_allow_html=True)
        st.write("")

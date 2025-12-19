import streamlit as st
from datetime import datetime

st.set_page_config(page_title="IA Cockpit", layout="wide", page_icon="🚀")

# Style CSS
st.markdown("""
<style>
.card {
    background: white; padding: 20px; border-radius: 12px;
    border: 1px solid #eee; text-align: center; height: 160px;
    transition: 0.3s; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.card:hover { border-color: #ff4b4b; transform: translateY(-3px); }
.icon { font-size: 35px; }
.title { font-size: 16px; font-weight: bold; color: #31333F; }
a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
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

# TITRE
st.title("🚀 Sales Cockpit IA")
st.divider()

# URLs DECOUPÉES (pour éviter les lignes trop longues)
url1 = "https://cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/"
url2 = "https://freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/"
url3 = "https://go-nogo-ao-guljf7vfdgd8gwbwk2czss.streamlit.app/"
url4 = "https://ia-discovery-tool-exipby6qyeqodoryc8p7kj.streamlit.app/"
url5 = "https://objection-crusher-eickr9egabodnbspah7zgh.streamlit.app/"
url6 = "https://sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy.streamlit.app/"
url7 = "https://simulateuria-4geraztakpppefxpsvfp5z.streamlit.app/"
url8 = "https://account-manager-ia-hwtkfcycxcxcgqtxrhyrez.streamlit.app/"

tools = [
    ("CV Optimizer", "🎯", url1),
    ("Marge/Rentab", "⚖️", url2),
    ("Go/No-Go AO", "🚦", url3),
    ("IA Tool", "🔍", url4),
    ("Objection", "🛡️", url5),
    ("KPI Tracker", "📈", url6),
    ("Simu IA", "🤖", url7),
    ("Account Mgr", "🤝", url8)
]

# GRILLE
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

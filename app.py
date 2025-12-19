import streamlit as st
from datetime import datetime

st.set_page_config(page_title="IA Cockpit", layout="wide")

# CSS Minimal
st.markdown("""<style>
.card{background:white;padding:15px;border-radius:10px;border:1px solid #eee;text-align:center;height:130px;transition:0.3s;}
.card:hover{border-color:red;transform:translateY(-3px);}
.icon{font-size:25px;}
.title{font-size:13px;font-weight:bold;}
a{text-decoration:none !important;color:black;}
</style>""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.list = []
new_t = st.sidebar.text_input("Tâche")
if st.sidebar.button("Ajouter"):
    if new_t:
        st.session_state.list.append(new_t)
        st.rerun()
for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")
if st.sidebar.button("Vider"):
    st.session_state.list = []
    st.rerun()

# RECHERCHE
st.title("🚀 Sales Cockpit")
c1, c2 = st.columns(2)
with c1:
    g = st.text_input("Google")
    if g:
        u_g = "https://www.google.com/search?q=" + g.replace(' ', '+')
        st.markdown(f"[🔎 Go]({u_g})")
with c2:
    l = st.text_input("LinkedIn")
    if l:
        u_l = "https://www.linkedin.com/search/results/all/?keywords=" + l.replace(' ', '%20')
        st.markdown(f"[👤 Go]({u_l})")

st.divider()

# APPLIS (Liens découpés pour éviter la coupure)
base = "https://"
u1 = base + "cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/"
u2 = base + "freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/"
u3 = base + "go-nogo-ao-guljf7vfdgd8gwbwk2czss.streamlit.app/"
u4 = base + "ia-discovery-tool-exipby6qyeqodoryc8p7kj.streamlit.app/"
u5 = base + "objection-crusher-eickr9egabodnbspah7zgh.streamlit.app/"
u6 = base + "sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy.streamlit.app/"
u7 = base + "simulateuria-4geraztakpppefxpsvfp5z.streamlit.app/"
u8 = base + "account-manager-ia-hwtkfcycxcxcgqtxrhyrez.streamlit.app/"

tools = [
    ("CV Optimizer", "🎯", u1), ("Marge/Rentab", "⚖️", u2),
    ("Go/No-Go AO", "🚦", u3), ("IA Discovery", "🔍", u4),
    ("Objection", "🛡️", u5), ("KPI Tracker", "📈", u6),
    ("Simu Salaire Staffing", "🤖", u7), ("Account Mgr", "🤝", u8)
]

# GRILLE
cols = st.columns(4)
for i in range(8):
    with cols[i%4]:

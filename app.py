import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# CSS
st.markdown("""<style>
.card{background:white;padding:10px;border-radius:10px;
border:1px solid #eee;text-align:center;height:120px;transition: 0.3s;}
.card:hover{border-color:red; transform: translateY(-5px); box-shadow: 0px 4px 10px rgba(0,0,0,0.1);}
.icon{font-size:25px;}
.title{font-size:12px;font-weight:bold;}
a{text-decoration:none!important;color:black;}
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

# APPLIS (MISE À JOUR DE L'URL CV OPTIMIZER)
b = "https://"
s = ".streamlit.app/"

# Ton nouveau lien pour le premier outil
u1 = b + "cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp" + s

# Les autres liens (inchangés)
u2 = b + "freelancevscollab-" + "tcjdkokhjktthqet9emwd2" + s
u3 = b + "go-nogo-ao-" + "guljf7vfdgd8gwbwk2czss" + s
u4 = b + "ia-discovery-tool-" + "exipby6qyeqodoryc8p7kj" + s
u5 = b + "objection-crusher-" + "eickr9egabodnbspah7zgh" + s
u6 = b + "sales-kpi-tracker-" + "gemm7zlpac7rv5hdkfyesy" + s
u7 = b + "simulateuria-" + "4geraztakpppefxpsvfp5z" + s
u8 = b + "account-manager-ia-" + "hwtkfcycxcxcgqtxrhyrez" + s

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
        st.markdown(f"""<a href="{tools[i][2]}" target="_blank">
        <div class="card">
        <div class="icon">{tools[i][1]}</div>
        <div class="title">{tools[i][0]}</div>
        </div></a>""", unsafe_allow_html=True)
        st.write("")

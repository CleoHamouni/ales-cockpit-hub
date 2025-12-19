import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="IA Sales", layout="wide")

# CSS
st.markdown("""
<style>
.card {
    background: white; padding: 20px; border-radius: 10px;
    border: 1px solid #ddd; text-align: center; height: 120px;
}
.card:hover { border-color: red; }
a { text-decoration: none; color: black; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state:
    st.session_state.list = []

# Ajout tâche
t = st.sidebar.text_input("Tâche")
if st.sidebar.button("Ajouter"):
    if t:
        st.session_state.list.append(t)
        st.rerun()

# Affichage
for x in st.session_state.list:
    st.sidebar.checkbox(x)

if st.sidebar.button("Vider"):
    st.session_state.list = []
    st.rerun()

st.sidebar.text_area("Notes")

# GRILLE
st.title("🚀 COCKPIT")
u = [
    ("CV Opti", "https://cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/"),
    ("Marge", "https://freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/"),
    ("AO Go", "https://go-nogo-ao-guljf7vfdgd8gwbwk2czss.streamlit.app/"),
    ("IA Tool", "https://ia-discovery-tool-exipby6qyeqodoryc8p7kj.streamlit.app/"),
    ("Objection", "https://objection-crusher-eickr9egabodnbspah7zgh.streamlit.app/"),
    ("KPI", "https://sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy.streamlit.app/"),
    ("Simu IA", "https://simulateuria-4geraztakpppefxpsvfp5z.streamlit.app/"),
    ("Acc. Mgr", "https://account-manager-ia-hwtkfcycxcxcgqtxrhyrez.streamlit.app/")
]

c = st.columns(4)
for i in range(8):
    with c[i%4]:
        st.markdown(f'<div class="card"><a href="{u[i][1]}" target="_blank">{u[i][0]}</a></div>', unsafe_allow_html=True)
        st.write("")

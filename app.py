import streamlit as st
from datetime import datetime

st.set_page_config(page_title="IA Cockpit", layout="wide", page_icon="🚀")

# 1. STYLE CSS AMÉLIORÉ
st.markdown("""
<style>
.card {
    background: white; padding: 15px; border-radius: 12px;
    border: 1px solid #eee; text-align: center; height: 150px;
    transition: 0.3s; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    display: flex; flex-direction: column; justify-content: center;
}
.card:hover { border-color: #ff4b4b; transform: translateY(-3px); }
.icon { font-size: 30px; margin-bottom: 5px; }
.title { font-size: 14px; font-weight: bold; color: #31333F; line-height: 1.2; }
a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# 2. SIDEBAR (To-Do & Notes)
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
        url_li = f"https://www

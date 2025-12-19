import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="IA Sales Cockpit", layout="wide", page_icon="🚀")

# DESIGN CSS
st.markdown("""
<style>
.card {
    background: white; padding: 25px; border-radius: 15px;
    border: 1px solid #eee; text-align: center; height: 170px;
    transition: 0.3s; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.card:hover { 
    border-color: #ff4b4b; transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.icon { font-size: 40px; margin-bottom: 10px; }
.title { font-size: 18px; font-weight: bold; color: #31333F; }
a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📝 MON BUREAU")
if 'list' not in st.session_state:
    st.session_state.list = []

# Ajouter une tâche
new_t = st.sidebar.text_input("Ajouter une tâche")
if st.sidebar.button("Ajouter"):
    if new_t:
        st.session_state.list.append(new_t)
        st.rerun()

# Affichage des tâches
for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"todo_{i}")

if st.sidebar.button("Tout vider"):
    st.session_state.list = []
    st.rerun()

st.sidebar.text_area("Pense-bête", height=150)

# GRILLE DES APPLIS
st.title("🚀 Business Developer IA - Cockpit")
st.divider()

# Données des 8 outils
u = [
    ("CV Optimizer", "🎯", "https://cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/"),
    ("Marge/Rentab", "⚖️", "https://freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/"),
    ("Go/No-Go AO", "🚦", "https://go

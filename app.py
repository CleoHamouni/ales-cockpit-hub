import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="IA Sales Cockpit", layout="wide", page_icon="🚀")

quotes = [
    "On ne perd jamais : soit on gagne, soit on apprend.",
    "Le succès, c'est d'aller d'échec en échec sans enthousiasme.",
    "Vendre, c'est aider quelqu'un à obtenir ce qu'il veut.",
    "La persévérance est la clé.",
    "La chance sourit aux audacieux."
]

st.markdown("""
    <style>
    .main-card {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border: 1px solid #eaeaea; text-align: center; height: 180px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .main-card:hover {
        border-color: #ff4b4b; transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .card-icon { font-size: 38px; }
    .card-title { font-size: 17px; font-weight: 700; color: #1E1E1E; }
    a { text-decoration: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("📝 Mon Bureau")
st.sidebar.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = [{"task": "Relancer AO", "done": False}]

with st.sidebar.form("add_todo", clear_on_submit=True):
    new_t = st.text_input("Nouvelle tâche")
    if st.form_submit_button("Ajouter"):
        if new_t:
            st.session_state.todo_list.append({"task": new_t, "done": False})
            st.rerun()

for i, item in enumerate(st.session_state.todo_list):
    st.session_state.todo_list[i]['done'] = st.sidebar.checkbox(item['task'], value=item['done'], key=f"c_{i}")

if st.sidebar.button("🗑️ V

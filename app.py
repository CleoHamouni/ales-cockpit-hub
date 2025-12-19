import streamlit as st
import random
from datetime import datetime

# 1. Configuration de la page
st.set_page_config(page_title="IA Sales Cockpit", layout="wide", page_icon="🚀")

# 2. Citations de motivation
quotes = [
    "On ne perd jamais : soit on gagne, soit on apprend.",
    "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme.",
    "Vendre, c'est aider quelqu'un à obtenir ce qu'il veut.",
    "La persévérance est la clé. Le 'Non' n'est qu'un 'Pas encore'.",
    "Fais de chaque client un partenaire, pas une transaction.",
    "La chance sourit aux audacieux."
]

# 3. Design CSS personnalisé (Vérifié sans erreur de fermeture)
st.markdown("""
    <style>
    .main-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #eaeaea;
        text-align: center;
        transition: all 0.3s ease;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .main-card:hover {
        border-color: #ff4b4b;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        background-color: #fffafa;
    }
    .card-icon { font-size: 38px; margin-bottom: 10px; }
    .card-title { font-size: 17px; font-weight: 700; color: #1E1E1E; margin-bottom: 5px; }
    .card-desc { font-size: 12px; color: #666666; line-height: 1.2; }
    a { text-decoration: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (To-Do dynamique & Pense-bête) ---
st.sidebar.title("📝 Mon Bureau")
st.sidebar.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")

st.sidebar.divider()
st.sidebar.subheader("📌 To-Do List")

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = [
        {"task": "Relancer les AO de la veille", "done": False},
        {"task": "Mettre à jour Salesforce", "done": False}
    ]

with st.sidebar.form("add_todo", clear_on_submit=True):
    new_task = st.text_input("Ajouter une tâche...", placeholder="Ex: Rappeler Marc")
    if st.form_submit_button("Ajouter"):
        if new_task:
            st.session_state.todo_list.append({"task": new_task, "done": False})
            st.rerun()

for i, item in enumerate(st.session_state.todo_list):
    st.session_state.todo_list[i]['done'] = st.sidebar.checkbox(
        item['task'], 
        value=item['done'], 
        key=f"check_{i}"
    )

if st.sidebar.button("🗑️ Vider la liste"):
    st.session_state.todo_list = []
    st.rerun()

st.sidebar.divider()
st.sidebar.subheader("💡 Pense-bête")
st.sidebar.text_area("Notes rapides...", height=200)

# --- CORPS DE L'APPLICATION (GRILLE 4x2) ---
st.title("🚀

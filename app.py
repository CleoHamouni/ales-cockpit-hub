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
    "La chance sourit aux audacieux (et à ceux qui relancent)."
]

# 3. Design CSS personnalisé
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

# --- SIDEBAR (To-Do & Pense-bête) ---
st.sidebar.title("📝 Mon Bureau")
st.sidebar.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")

st.sidebar.divider()
st.sidebar.subheader("📌 To-Do List")
st.sidebar.checkbox("Relancer les AO de la veille")
st.sidebar.checkbox("Qualifier 5 nouveaux profils")
st.sidebar.checkbox("Mettre à jour Salesforce")
st.sidebar.checkbox("Préparer les calls de demain")

st.sidebar.divider()
st.sidebar.subheader("💡 Pense-bête")
st.sidebar.text_area("Notes rapides (ex: Rappeler Marc à 14h...)", height=200)

# --- CORPS DE L'APPLICATION ---
st.title("🚀 Business Developer IA - Cockpit")
st.info(f"💡 **Motivation du jour :** {random.choice(quotes)}")
st.divider()

# Liste des 8 applications
apps = [
    {"title": "CV Optimizer Pro", "icon": "🎯", "url": "https://cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6.streamlit.app/", "desc": "Matching LinkedIn & Pitch candidat."},
    {"title": "Freelance vs Collab", "icon": "⚖️", "url": "https://freelancevscollab-tcjdkokhjktthqet9emwd2.streamlit.app/", "desc": "Calcul de marge et rentabilité."},
    {"title": "Go / No-Go AO", "icon": "🚦", "url": "https://go-nogo-ao-guljf7vfdgd8gwbwk2czss.streamlit.app/", "desc": "Qualification & rapport Salesforce."},
    {"title": "IA Discovery Tool", "icon": "🔍", "url": "https://ia-discovery-tool-exipby6qyeqodoryc8p7kj.streamlit.app/", "desc": "Explorer les opportunités IA."},
    {"title": "Objection Crusher", "icon": "🛡️", "url": "https://objection-crusher-eickr9egabodnbspah7zgh.streamlit.app/", "desc": "Réponses aux barrages clients."},
    {"title": "Sales KPI Tracker", "icon": "📈", "url": "https://sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy.streamlit.app/", "desc": "Suivi d'activité et rapport hebdo."},
    {"title": "Simulateur IA", "icon": "🤖", "url": "https://simulateuria-4geraztakpppefxpsvfp5z.streamlit.app/", "desc": "Projections financières."},
    {"title": "Account Manager IA", "icon": "🤝", "url": "https://account-manager-ia-hwtkfcycxcxcgqtxrhyrez.streamlit.app/", "desc": "Stratégie de compte client."}
]

# Affichage en grille 4x2
col_row1 = st.columns(4)
for i in range(4):
    with col_row1[i]:
        app = apps[i]
        st.markdown(f"""
            <a href="{app['url']}" target="_blank">
                <div class="main-card">
                    <div class="card-icon">{app['icon']}</div>
                    <div class="card-title">{app['title']}</div>
                    <div class="card-desc">{app['desc']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

st.write("") # Espace entre les lignes

col_row2 = st.columns(4)
for i in range(4):
    with col_row2[i]:
        app = apps[i+4]
        st.markdown(f"""
            <a href="{app['url']}" target="_blank">
                <div class="main-card">
                    <div class="card-icon">{app['icon']}</div>
                    <div class="card-title">{app['title']}</div>
                    <div class="card-desc">{app['desc']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

st.divider()
st.caption("Sales Cockpit v1.0 - Travaillez plus intelligemment, pas plus dur.")

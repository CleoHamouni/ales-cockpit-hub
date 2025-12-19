import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Sales Cockpit Hub", page_icon="💼", layout="wide")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { background-color: #007bff; color: white; border-radius: 8px; }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (NAVIGATION) ---
with st.sidebar:
    st.title("👨‍✈️ Menu Pilotage")
    st.subheader("Mes Outils")
    
    # BOUTON VERS TA NOUVELLE APPLI CV
    st.link_button("🎯 Ouvrir l'Analyseur de CV", "https://cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp.streamlit.app/")
    
    st.divider()
    st.caption("Sales Cockpit v2.0")

# --- CONTENU PRINCIPAL ---
st.title("💼 Sales Cockpit : Tableau de Bord")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="card">
        <h3>📈 Performance</h3>
        <p>Suivez vos KPIs de vente en temps réel.</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="card">
        <h3>🤝 CRM Quick Access</h3>
        <p>Accès rapide à vos derniers contacts.</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class="card">
        <h3>📄 Recrutement / Staffing</h3>
        <p>Utilisez l'IA pour matcher vos candidats.</p>
    </div>""", unsafe_allow_html=True)
    # Rappel du lien aussi ici pour plus de visibilité
    st.link_button("Lancer l'Analyseur CV", "https://cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp.streamlit.app/")

st.divider()

# Section Actualités ou Rappels
st.subheader("📅 Rappels du jour")
st.checkbox("Relancer le client de l'annonce CV")
st.checkbox("Vérifier les nouveaux crédits OpenAI")

import streamlit as st
import openai
import pdfplumber

# Configuration de la page
st.set_page_config(page_title="Cockpit CV Optimizer", page_icon="🚀", layout="wide")

# Design personnalisé
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stProgress > div > div > div > div { background-color: #ef4444; }
    .score-box { padding: 20px; border-radius: 10px; text-align: center; color: white; font-weight: bold; font-size: 24px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Cockpit d'Analyse CV Pro")
st.write("Optimisez le matching entre vos candidats et vos offres d'emploi.")

# Barre latérale pour la clé API
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Clé API OpenAI", type="password")
    st.info("Récupérez votre clé sur platform.openai.com")

# Zone de saisie
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 L'Offre d'Emploi")
    job_desc = st.text_area("Collez la fiche de poste ici :", height=250)

with col2:
    st.subheader("📄 Le CV du Candidat")
    uploaded_file = st.file_uploader("Chargez le CV (PDF)", type="pdf")

if st.button("📊 ANALYSER LE MATCHING"):
    if not api_key or not job_desc or not uploaded_file:
        st.error("Veuillez remplir tous les champs et ajouter votre clé API.")
    else:
        with st.spinner("Analyse en cours par l'IA..."):
            try:
                # 1. Extraction du texte
                with pdfplumber.open(uploaded_file) as pdf:
                    resume_text = "".join([page.extract_text() for page in pdf.pages])

                # 2. IA OpenAI
                client = openai.OpenAI(api_key=api_key)
                prompt = f"""
                Analyse le matching entre ce CV et cette offre.
                Offre : {job

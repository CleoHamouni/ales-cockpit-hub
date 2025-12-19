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

import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# CSS
st.markdown("""<style>
.card{background:white;padding:15px;border-radius:10px;
border:1px solid #eee;text-align:center;height:130px;}
.card:hover{border-color:red;}
.icon{font-size:25px;}
.title{font-size:13px;font-weight:bold;}
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

# APPLIS (Lignes très courtes pour éviter les bugs)
b = "https://"
s = ".streamlit.app/"

u1 = b + "cv-optimizer-pro-jjfrcz4bzexfn9y9puerq6" + s
u2 = b + "freelancevscollab-tcjdkokhjktthqet9emwd2" + s
u3 = b + "go-nogo-ao-guljf7vfdgd8gwbwk2czss" + s
u4 = b + "ia-discovery-tool-exipby6qyeqodoryc

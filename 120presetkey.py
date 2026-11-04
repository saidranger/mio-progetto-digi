import streamlit as st
from pathlib import Path
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

def main():
    if not st.session_state.get("user_logged_in"):
            st.error("Il contenuto è privato: effettua il login per accedere.")
            if st.button("Fai il login", icon="🔑", type="primary"):
                st.switch_page("login.py")
            return
    else:
        st.html(Path("./static/120/120.Assegnazione.Tasti.Funzione.html"), unsafe_allow_javascript=True)

main()

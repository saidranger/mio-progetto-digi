import streamlit as st

st.set_page_config(page_title="...Appunti...",initial_sidebar_state="collapsed")

pages = {
    "Login": [
        st.Page("login.py", title="🔑 Fai il Login"),],
    "Software": [
        st.Page("Home.py", title="📚 Installazione e Attivazione"),
        #st.Page("Approfondimento.py",title="Approfondimento sul Digiproject"),
        ],
    "Bilance Manuali": [
        st.Page("specifiche.py", title="📄 Specifiche Tecniche SM-6000"),
        st.Page("120presetkey.py", title="📄 Assegnazione tasti funzione SM-120"),
        st.Page("120manuale.py", title="📄 Manuale SM-120"),
        st.Page("120manualeservizio.py", title="📄 Manuale Servizio SM.120"),
        ],
    "Guide pratiche": [
        st.Page("120ShopName.py", title="📄 Stampa Nome Negozio"),
        st.Page("120CambioEtichetta.py", title="📄 Cambio Rapido Formato Etichetta"),
    ],
    "Video": [
        st.Page("webapplotti.py", title="📹 Video Caricamento Lotto")
    ]
}

pg = st.navigation(pages,position='top')
pg.run()
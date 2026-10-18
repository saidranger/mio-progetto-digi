import streamlit as st

pages = {
    "Pagine": [
        st.Page("login.py", title="Fai il Login"),
        st.Page("Home.py", title="Leggi la Documentazione"),
    ]
}

pg = st.navigation(pages)
pg.run()
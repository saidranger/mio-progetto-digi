import streamlit as st

st.set_page_config(page_title="...Appunti...",initial_sidebar_state="collapsed")

pages = {
    "Pagine": [
        st.Page("login.py", title="Fai il Login"),
        st.Page("Home.py", title="Leggi la Dovumantazione"),
    ]
}

pg = st.navigation(pages,position='top')
pg.run()
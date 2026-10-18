import streamlit as st
# import sys
# from pathlib import Path

# Quando Streamlit avvia una pagina da `pages/`, la cartella del progetto
# potrebbe non essere nel percorso di ricerca degli import.
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from contenuti import *

def main():
    col1, col2 = st.columns([1, 3])
    col1.image("./static/Logo.jpeg", width=150)
    col2.markdown(
        """
        <h1 style="
            margin: 0;
            color: #1f4e79;
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 4.6rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            text-shadow: 1px 2px 3px rgba(31, 78, 121, 0.18);
        ">...Appunti...</h1>
        """,
        unsafe_allow_html=True,
    )
    footer()
    body()

def body():
    @st.dialog("Dialog", width="large")
    def mostra_mio_dialog():        
        st.write(paragrafo3)
        st.image("./static/dbmaintanance.png", width="stretch")
        st.markdown("Una volta pulito possiamo copiarlo in **c:\programdata\digiproject** come visto in precedenza.")
        if st.button("Chiudi",type="primary"):
            st.rerun()
    st.header("DigiProject",anchor="digiproject")
    with st.container(border=True,vertical_alignment="center",autoscroll=True):
        st.markdown(paragrafo1)
        column1, column2 = st.columns(2)
        with open('./static/DIGIproject.Server.zip', 'rb') as f:
            column1.download_button(r'$\textsf{\large Download DIGIproject Server}$', f, file_name='DIGIproject.Server.zip',icon="⬇️",type="secondary")
        if column2.button(r'$\textsf{\large Pulire il DB}$',icon="📒",type="secondary"):
            mostra_mio_dialog()
    Attivazione()
    footer()

def Attivazione():
    @st.dialog("Attivazione Licenza",width="large")
    def showdialog():
        st.pdf("./static/Gestione_licenze_DIGIproject_Pagina_WEB - Installatore.pdf", height=600)

    st.header("Installazione & Attivazione Licenza",anchor="attivazione")
    with st.container(border=True,vertical_alignment="center",autoscroll=True):
        st.markdown(paragrafo2)
        column1, column2 = st.columns(2)
        column1.image("./static/primo.avvio.png", caption="Primo avvio password=admin", width="stretch")
        column2.image("./static/richiesta.licenza.png", caption="Attivazione Licenza", width="stretch")
        st.markdown('Per ottenere il codice di licenza fate riferimento alla piccola guida ufficiale di Digi.')
        if st.button(r'$\textsf{\large Guarda la guida}$',icon="👀"):
            showdialog()
        st.markdown('''Una volta attivata la licenza, vi verrà richiesto di creare l'utente amministratore, dovrete inserire:\n
   - username *admin*
   - password *teraoka*\n''')
        st.image("./static/creazione.admin.png", caption="**:red[NON CLICCATE SU] REQUIRE A UNIQUE CODE FOR EACH LOGIN ATTEMPT**", width="content")
        st.markdown('''Dopo aver creato l'utente admin, fate il primo ingresso nel Digiproject e poi chiudetelo.
        Arrestate il servizio di Windows **"DigiProject Server"** e copiate il file **digiproject.db** (recuperato da un'altra istallazione) nella cartella **C:\\ProgramData\\DIGI\\DIGIproject Server** rinominando quello esistente.
        Dopo averlo copiato, riavviate il servizio.''')

def footer():
    with st.container(border=True,horizontal=True,autoscroll=True):
        st.markdown("[:primary[DigiProject]](#digiproject)")
        st.markdown("[:primary[Attivazione Licenza]](#attivazione)")

if 'user_logged_in' in st.session_state and st.session_state.user_logged_in:
    main()
else:
    st.error(r"$\textsf{\Large Il contenuto è privato fai il login per accedere.}$")
    if st.button(label="**Fai il login**", icon="🔑",type='primary'):
        st.switch_page("app.py")

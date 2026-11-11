import streamlit as st

st.set_page_config(
    page_title="DigiWebApp",
    layout="wide"
)
def main():
    st.title("DigiWebApp", text_alignment="center",anchor=None)

    with st.container(border=True):
        st.markdown(""":red-background[Un breve video che mostra come caricare un lotto sulla digiWebApp.
        Molto importante, come si vede nel video, tutti i campi devono essere compilati, è obbligatorio!]
        :rainbow-background[Il peso è in kg, per i grammi si deve usare la "," non il "."]
        """)
        # carica il video
    video_file = './static/filmato.mp4'  # sostituisci con il percorso del tuo video

    st.video(video_file)

if 'user_logged_in' in st.session_state and st.session_state.user_logged_in:
    main()
else:
    st.error(r":gray[$\textsf{\Large Il contenuto è privato fai il login per accedere.}$]")
    if st.button(label="**Fai il login**", icon="🔑",type='primary'):
        st.switch_page("login.py")

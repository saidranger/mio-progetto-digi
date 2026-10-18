import streamlit as st
import csv

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

# Definiamo la funzione per leggere il file CSV e cercare l'utente
def user_exists(username, password):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                return True
        return False

# Creiamo un layout di Streamlit
st.title('Login Form')

# Creiamo un form di login
with st.form('login_form'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit_button = st.form_submit_button('Login')

# Verifichiamo se l'utente esiste
if submit_button:
    if user_exists(username, password):
        st.success('Login success')
        st.session_state.user_logged_in = True  # Impostiamo lo stato di login
        st.switch_page("Home.py")
        
    else:
        st.error('Username o Password Errati. Riprova.')

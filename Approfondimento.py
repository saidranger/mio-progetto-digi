import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

st.header("..ma il Digiproject cosa fa?",text_alignment="center")

c1=st.container(border=True)
c1.markdown('''Prima di passare al Digiproject è doveroso fare una breve parentesi sugli 
strumenti che si interfacciano con questo programma (Configuratore).

Tutti i dispositivi Digi si interfacciano con il Digiproject tramite connessioni a intervalli
regolari, che impostiamo nel Digiproject, per lo scambio di dati.

Dopo il login nel Digiproject troveremo una serie di pulsanti, esporeremo quelli fondamentali.
 - Parametri.
 - Negozi.
 - Back Office.
 - Librerie.
   - 1 Libr. Rapporti
   - 2 Libr. Colori
   - 3 Libr. iva
   - 4 Libr. tracciabilità
   - 5 Libr. plu
 - Bilance.
 - Manutenzione.
''')

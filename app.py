#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
from components.formSatisfaction import formsatisfaction
from components.boardStat import boardstat
from Airplane import df

# Titre de l'application
# st.title("Application de Réservation de Vols")
# st.dataframe(df.sort_values(by='id'))


# Menu de navigation latéral
selection = st.sidebar.radio("Sélectionnez une page", ["formulaire", "tableau de bord"])

if selection == "formulaire":
    formsatisfaction ()
    
elif selection == "tableau de bord":
    boardstat()





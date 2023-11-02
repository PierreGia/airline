#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
from components.formSatisfaction import formsatisfaction

from Airplane import df

# Titre de l'application
st.title("Application de Réservation de Vols")
st.dataframe(df)

#import de la fonction affichant le formulaire de satisfaction
formsatisfaction ()




import streamlit as st
from Airplane import df

# Titre de l'application
st.title("Application de Réservation de Vols")
st.dataframe(df)



#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st

def formsatisfaction():
    # Titre de l'application
    st.title("Application de Vols")

    # Formulaire pour le genre
    genre = st.radio("Genre:", ("Homme", "Femme"))

    # Formulaire pour le type de client loyal ou non 
    type = st.radio("type de client:", ("Loyal", "Non loyal"))

    # Afficher le genre et le type de client sélectionnés
    if genre:
        st.write(f"Genre: {genre}")

    if type:
        st.write(f"Type de client: {type}")
    
   
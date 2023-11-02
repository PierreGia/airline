
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


def formsatisfaction():
    '''
    formulaire pour permettre à l'utilisateur de rentrer des paramètres et utiliser le modèle sur ces variables.
    '''
    # Titre de l'application
    st.title("Application de Vols")

    # Formulaire pour le genre
    genre = st.selectbox("Genre:", ("Homme", "Femme"))

    # Formulaire pour le type de client loyal ou non 
    type_client = st.selectbox("Type de client:", ("Loyal", "Non loyal"))

    # Champ pour l'âge
    age = st.number_input("Âge", min_value=0, max_value=150, value=25)

    # Formulaire pour le type de trajet
    type_trajet = st.selectbox("Type de trajet:", ("personnel", "Business"))

    # Formulaire pour la classe
    classe = st.selectbox("Type de vol:", ("Eco", "Eco Plus", "Business"))

    # Champ pour la distance
    distance = st.number_input("Distance", min_value=0, max_value=10000, value=300)

    # Formulaire pour la qualité du wifi
    wifi = st.selectbox("Qualité du wifi:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour l'heure de départ/arrivée pratique
    heure_depart_arrivee = st.selectbox("Heure de départ/arrivée pratique:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour la facilité de réservation en ligne
    reservation = st.selectbox("Facilité de réservation en ligne:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour l'emplacement de la porte
    emplacement_porte = st.selectbox("Emplacement de la porte:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour la nourriture/boissons
    food_drink = st.selectbox("Nourriture/Boissons:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour l'embarquement en ligne
    embarquement_ligne = st.selectbox("Embarquement en ligne:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le confort d'assise
    comfort = st.selectbox("Confort d'assise:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le divertissement à bord
    divertissement = st.selectbox("Divertissement à bord:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le service à bord
    service = st.selectbox("Service à bord:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le service pour les jambes
    service_jambes = st.selectbox("Service pour les jambes:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour la manutention des bagages
    manutention_bagages = st.selectbox("Manutention des bagages:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le service d'enregistrement
    service_enregistrement = st.selectbox("Service d'enregistrement:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour le service en vol
    service_vole = st.selectbox("Service en vol:", ("0", "1", "2", "3", "4", "5"))

    # Formulaire pour la propreté
    proprete = st.selectbox("Propreté:", ("0", "1", "2", "3", "4", "5"))

    # Champ pour le retard du départ
    retard_depart = st.number_input("Retard de départ:", min_value=0, max_value=1900, value=60)

    # Champ pour le retard d'arrivée
    retard_arrivee = st.number_input("Retard d'arrivée:", min_value=0, max_value=1900, value=60)

    # Bouton pour soumettre le formulaire
    if st.button("Soumettre"):
        # Créez un dictionnaire contenant les données du formulaire
        data = {
            'Genre': [genre],
            'Type de client': [type_client],
            'Âge': [age],
            'Type de trajet': [type_trajet],
            'Classe': [classe],
            'Distance': [distance],
            'Qualité du wifi': [wifi],
            'Heure de départ/arrivée pratique': [heure_depart_arrivee],
            'Facilité de réservation en ligne': [reservation],
            'Emplacement de la porte': [emplacement_porte],
            'Nourriture/Boissons': [food_drink],
            'Embarquement en ligne': [embarquement_ligne],
            'Confort d\'assise': [comfort],
            'Divertissement à bord': [divertissement],
            'Service à bord': [service],
            'Service pour les jambes': [service_jambes],
            'Manutention des bagages': [manutention_bagages],
            'Service d\'enregistrement': [service_enregistrement],
            'Service en vol': [service_vole],
            'Propreté': [proprete],
            'Retard de départ': [retard_depart],
            'Retard d\'arrivée': [retard_arrivee]
        }

        # Créez un DataFrame à partir du dictionnaire
        df = pd.DataFrame(data)

        # Affichez le DataFrame
        st.write("Données du formulaire:", df)



        #st.title("resultats")
    
        
        
   
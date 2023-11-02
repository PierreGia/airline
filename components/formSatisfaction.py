
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


def formsatisfaction():
    
    '''
    formulaire pour permettre a l'utilisateur de rentréer des paramètres et utiliser le model sur ces variables.
    '''
    # Titre de l'application
    st.title("Application de Vols")

    # Formulaire pour le genre
    genre = st.radio("Genre:", ("Homme", "Femme"))

    # Formulaire pour le type de client loyal ou non 
    type_client = st.radio("type de client:", ("Loyal", "Non loyal"))

    # Champ pour l'âge
    age = st.number_input("Âge", min_value=0, max_value=150, value=25)

    # Formulaire pour le type de trajet
    type_trajet = st.radio("type de trajet :", ("personel", "Business"))

    # Formulaire pour la classe
    classe = st.radio("type de vole :", ("Eco","Eco Plus", "Business"))

    # Champ pour l'âge
    distance = st.number_input("Distance", min_value=0, max_value=10000, value=300)
    
    # Formulaire pour le wifi
    wifi = st.radio("Qualité du wifi :", ("0","1", "2","3","4","5"))

    # Formulaire pour l'Heure de départ/arrivée pratique
    heure_depart_arrivee = st.radio("Heure de départ/arrivée pratique :", ("0","1", "2","3","4","5"))

    
    # Formulaire pour la Facilité de réservation en ligne
    reservation = st.radio("Facilité de réservation en ligne :", ("0","1", "2","3","4","5"))
    

    
    # Formulaire pour l'Emplacement de la porte
    emplacemement_porte = st.radio("Emplacement de la porte :", ("0","1", "2","3","4","5"))
    
    
    # Formulaire pour la nourriture
    food_drink = st.radio("nourriture:", ("0","1", "2","3","4","5"))
    
    #formulaire Embarquement en ligne
    embarquement_ligne = st.radio("Embarquement en ligne:", ("0","1", "2","3","4","5"))
    
    #formulaire Confort d'assise
    comfort = st.radio("Confort d'assise:", ("0","1", "2","3","4","5"))
    
    #Divertissement à bord
    divertissement = st.radio("Divertissement à bord:", ("0","1", "2","3","4","5"))
    
    #formulaire Service à bord
    service = st.radio("Service à bord:", ("0","1", "2","3","4","5"))
    
    #Service de chambre pour les jambes
    service_jambes = st.radio("Service pour les jambes:", ("0","1", "2","3","4","5"))
    
    #formulaire pou La manutention des bagages
    manutention_bagages = st.radio("manutention des bagages:", ("0","1", "2","3","4","5"))
    
    #formulaire Service d'enregistrement
    service_enregistrement = st.radio("Service d'enregistrement:", ("0","1", "2","3","4","5"))
    
    #formulaire Service en vol
    service_vole = st.radio("Service en vole:", ("0","1", "2","3","4","5"))
    
    #formulaire propreté
    proprete = st.radio("Propreté:", ("0","1", "2","3","4","5"))
    
    
    # Champ pour le retard du depart
    retard_depart = st.number_input("Retard de départ:", min_value=0, max_value=1900, value=60)

    # Champ pour le retard d'arrivée
    retard_arrivee = st.number_input("Retard d'arrivée':", min_value=0, max_value=1900, value=60)



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
            'Emplacement de la porte': [emplacemement_porte],
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
    
        
        
   
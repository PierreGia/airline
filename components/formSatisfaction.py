
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib


def formsatisfaction():
    
    '''
    formulaire pour permettre a l'utilisateur de rentréer des paramètres et utiliser le model sur ces variables.
    '''
    # Titre de l'application
    st.title("Application de Vols")

    # # Formulaire pour le genre
    # genre = st.radio("Genre:", ("Homme", "Femme"))

    # Formulaire pour le type de client loyal ou non 
    type_client = st.radio("Customer Type:", ("Loyal Customer", "disloyal Customer"))

    # Champ pour l'âge
    age = st.number_input("Age", min_value=0, max_value=150, value=25)

    # Formulaire pour le type de trajet
    type_trajet = st.radio("Type of Travel :", ("Personal Travel", "Business travel"))

    # Formulaire pour la classe
    classe = st.radio("Class :", ("Eco","Eco Plus", "Business"))

    # Champ pour la distance
    distance = st.number_input("Flight Distance", min_value=0, max_value=10000, value=300)
    
    # Formulaire pour le wifi
    wifi = st.radio("Inflight wifi service :", ("0","1", "2","3","4","5"))

    # Formulaire pour l'Heure de départ/arrivée pratique
    heure_depart_arrivee = st.radio("Departure/Arrival time convenient :", ("0","1", "2","3","4","5"))

    # Formulaire pour la Facilité de réservation en ligne
    reservation = st.radio("Ease of Online booking :", ("0","1", "2","3","4","5"))
    
    # Formulaire pour l'Emplacement de la porte
    emplacemement_porte = st.radio("Gate location:", ("0","1", "2","3","4","5"))
    
    # # Formulaire pour la nourriture
    # food_drink = st.radio("nourriture:", ("0","1", "2","3","4","5"))
    
    #formulaire Embarquement en ligne
    embarquement_ligne = st.radio("Online boarding:", ("0","1", "2","3","4","5"))
    
    #formulaire Confort d'assise
    comfort = st.radio("Seat comfort:", ("0","1", "2","3","4","5"))
    
    # #Divertissement à bord
    # divertissement = st.radio("Divertissement à bord:", ("0","1", "2","3","4","5"))
    
    #formulaire Service à bord
    service = st.radio("On-board service:", ("0","1", "2","3","4","5"))
    
    # #Service de chambre pour les jambes
    # service_jambes = st.radio("Service pour les jambes:", ("0","1", "2","3","4","5"))
    
    #formulaire pou La manutention des bagages
    manutention_bagages = st.radio("Baggage handling:", ("0","1", "2","3","4","5"))
    
    #formulaire Service d'enregistrement
    service_enregistrement = st.radio("Checkin service:", ("0","1", "2","3","4","5"))
    
    # #formulaire Service en vol
    # service_vole = st.radio("Inflight entertainment:", ("0","1", "2","3","4","5"))
    
    #formulaire propreté
    proprete = st.radio("Cleanliness:", ("0","1", "2","3","4","5"))
    
    # # Champ pour le retard du depart
    # retard_depart = st.number_input("Retard de départ:", min_value=0, max_value=1900, value=60)

    # Champ pour le retard d'arrivée
    retard_arrivee = st.number_input("Arrival Delay in Minutes':", min_value=0, max_value=1900, value=60)

    # Bouton pour soumettre le formulaire
    if st.button("Soumettre"):
        # Création d'un dictionnaire contenant les données du formulaire
        data = {
            # 'Genre': [genre],
            'Customer Type': [type_client],
            'Age': [age],
            'Type of Travel': [type_trajet],
            'Class': [classe],
            'Flight Distance': [distance],
            'Inflight wifi service': [wifi],
            'Departure/Arrival time convenient': [heure_depart_arrivee],
            'Ease of Online booking': [reservation],
            'Gate location': [emplacemement_porte],
            # 'Nourriture/Boissons': [food_drink],
            'Online boarding': [embarquement_ligne],
            'Seat comfort': [comfort],
            # 'Divertissement à bord': [divertissement],
            'On-board service': [service],
            # 'Service pour les jambes': [service_jambes],
            'Baggage handling': [manutention_bagages],
            'Checkin service': [service_enregistrement],
            # 'Inflight entertainment': [service_vole],
            'Cleanliness': [proprete],
            # 'Retard de départ': [retard_depart],
            'Arrival Delay in Minutes': [retard_arrivee]
        }

        # Créez un DataFrame à partir du dictionnaire
        df = pd.DataFrame(data)

        # Affichez le DataFrame
        st.write("Données du formulaire:", df)

        # Conversion des données avec le préprocesseur
        preprocessor = joblib.load("ML/preprocessor.joblib")
        df = preprocessor.transform(df)

        # Chargement du modèle
        model = joblib.load("ML/RandomForestClassifier.joblib")

        # Prédiction du modèle 
        prediction = model.predict(df)

        # Affichez la prédiction et sa probabilite
        if prediction:
            satisfaction, mood, proba = "Satisfied", ":grin:", model.predict_proba(df)[0][1] 
        else:
            satisfaction, mood, proba = "Neutral or dissatisfied", ":angry:", (1 - model.predict_proba(df)[0][1])

        st.write("Prediction:", satisfaction, "with probability:", f"{proba*100:.2f} %", mood)


        #st.title("resultats")
    
        
        
   
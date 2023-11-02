
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st

def formsatisfaction():
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


    st.title("resultats")
    # Afficher les infos sélectionnés
    if genre:
        st.write(f"Genre: {genre}")

    if type_client:
        st.write(f"Type de client: {type_client}")
        
    if age:
        st.write(f"Âge: {age} ans")
        
    if type_trajet:
        st.write(f"Type de trajet: {type_trajet}")
    
    if classe:
        st.write(f"Type de vole: {classe}")
    
    if distance:
        st.write(f"Distance: {distance} km")
        
    if wifi:
        st.write(f"Qualité wifi: {wifi} ")
    
    if heure_depart_arrivee:
        st.write(f"Heure de départ/arrivée pratique: {heure_depart_arrivee} ")
    
    if reservation:
        st.write(f"Qualité reservation en ligne: {reservation} ")
        
      
    if emplacemement_porte:
        st.write(f"Emplacement de la porte : {emplacemement_porte} ")   
    
    if food_drink :
        st.write(f"nourriture : {food_drink} ")
    
    if embarquement_ligne :
        st.write(f"nourriture : {embarquement_ligne} ")
    
    if comfort :
        st.write(f"nourriture : {comfort} ")
    
    if divertissement :
        st.write(f"divertissement : {divertissement} ")
        
    if service :
        st.write(f"divertissement : {service} ")
        
    if service_jambes :
        st.write(f"service pour les jambes: {service_jambes} ")
    
    if manutention_bagages :
        st.write(f"service pour les jambes: {manutention_bagages} ")     
    
    if service_enregistrement :
        st.write(f"service pour les jambes: {service_enregistrement} ")   
    
    if service_vole :
        st.write(f"service en vole: {service_vole} ")
    
    if proprete :
        st.write(f"propreté: {proprete} ")

    if retard_depart:
        st.write(f"retart de départ: {retard_depart} ")
        
    if retard_arrivee:
        st.write(f"retart d'arrivée: {retard_arrivee} ")
        
        
   
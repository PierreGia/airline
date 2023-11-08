#dans app on appelle les différentes fonction des fichiers dans components
import streamlit as st
from components.formSatisfaction import formsatisfaction
from components.formInscription import formInscription
from components.formConnexion import formConnexion
from components.boardStat import boardstat
#from components.figure import plot_graph, curvroc, confmat, metric, features
from Airplane import df
import bcrypt
import mysql.connector
import streamlit_authenticator
import os, sys
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from components.useful_function import session

# Initialisation des variables de session
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = ''

if 'name' not in st.session_state:
    st.session_state['name'] = ''

if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = ''
    
# Titre de l'application
# st.title("Application de Réservation de Vols")
# st.dataframe(df.sort_values(by='id'))

# Chemins vers les images
confusion = "figures/confusion_matrix.png"
features = "figures/features.png"
metrics = "figures/metrics.png"
curve_roc = "figures/roc_curve.png"

# Menu de navigation latéral
selection = st.sidebar.radio("Sélectionnez une page", ["inscription", "connexion", "formulaire", "tableau de bord"])

# Affichage de la page correspondante
if selection == "formulaire":
    session(formsatisfaction)

elif selection == "tableau de bord":
    session(boardstat, confusion, features, metrics, curve_roc)

elif selection == "inscription":
    formInscription()

elif selection == "connexion":
    formConnexion()

    



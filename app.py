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



# Menu de navigation latéral
selection = st.sidebar.radio("Sélectionnez une page", ["inscription", "formulaire", "tableau de bord", "connexion"])

if selection == "inscription":
    formInscription()

elif selection == "formulaire":
    formsatisfaction ()
    
elif selection == "tableau de bord":
    st.title("Tableau de bord")
    #boardstat(confusion, features, metrics, roc_curve)


elif selection == "connexion":
    formConnexion()

    



import streamlit as st
import os, sys
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# On va dans le dossier parent
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from components.create_yaml_credentials import exec_yaml
from components.useful_function import session

def formConnexion():

    # On ajoute le nouvel utilisateur au fichier YAML
    exec_yaml()

    # On récupère le fichier YAML
    with open('databases/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
  
    # Récupération des informations du fichier YAML
    st.title("Formulaire de connexion")
    authenticator = stauth.Authenticate(config['credentials'],
                                        config["cookie"]["name"], 
                                        config["cookie"]["key"],
                                        config["cookie"]["expiry_days"],
                                        config["prehautorized"])
    
    # Lancement de l'authentification
    name, authentication_status, username = authenticator.login('Login', 'main')  

    # Récupération des informations de l'utilisateur pour la session
    st.session_state["authentication_status"] = authentication_status 
    st.session_state["name"] = name
    st.session_state["authenticator"] = authenticator

    # Lancement de la session
    session()
 
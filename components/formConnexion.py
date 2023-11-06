import streamlit as st
import os, sys
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from components.yaml_credentials import exec_yaml

def formConnexion():

    # On ajoute le nouvel utilisateur au fichier YAML
    exec_yaml()

    with open('databases/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
  
    st.title("Formulaire de connexion")
    authenticator = stauth.Authenticate(config['credentials'],
                                        config["cookie"]["name"], 
                                        config["cookie"]["key"],
                                        config["cookie"]["expiry_days"],
                                        config["prehautorized"])
    name, authentication_status, username = authenticator.login('Login', 'main')   

    # On affiche la session    
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Bienvenue *{name}*')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

    return authentication_status, authenticator, name
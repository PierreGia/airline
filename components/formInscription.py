import streamlit as st
from sqlalchemy.orm import sessionmaker
import os, sys
import streamlit_authenticator as stauth


from sqlalchemy import create_engine

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
print(parent_dir)
from databases import config
from databases.classes import Login_Mot_de_passe

def formInscription():

    # Connexion a la base de données

    # Importation des informations de connexion
    DATABASE_HOST = config.DATABASE_HOST
    DATABASE_NAME = config.DATABASE_NAME
    DATABASE_USERNAME = config.DATABASE_USERNAME
    DATABASE_PASSWORD = config.DATABASE_PASSWORD
    DATABASE_PORT = config.DATABASE_PORT

    # Création du moteur de base de données
    engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

    st.title("Formulaire d'inscription")

    login = st.text_input("Login")
    email = st.text_input("Email")
    name = st.text_input("Nom")
    password = st.text_input("Mot de passe", type="password")

    hashed_passwords = stauth.Hasher(passwords=[password]).generate()

    if st.button("S'enregistrer"):

        # Ajout dans la base de données

        # Création d'une session
        Session = sessionmaker(bind=engine)
        session = Session()

        if session.query(Login_Mot_de_passe).filter_by(login=name).first():
            st.error("Ce nom existe déjà. Veuillez en choisir un autre.")
            session.close()
        else:
            session.add(Login_Mot_de_passe(login=login, email=email, name=name, mot_de_passe=hashed_passwords[0]))
            session.commit()
            st.success("Inscription reussie")
            session.close()


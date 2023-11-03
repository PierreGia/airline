import streamlit as st
from sqlalchemy.orm import sessionmaker
import os, sys

from sqlalchemy import create_engine

parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from databases import config
from databases.classes import Client

st.title("Formulaire d'inscription")

name = st.text_input("Nom")
password = st.text_input("Mot de passe", type="password")

if st.button("S'enregistrer"):

    # Ajout dans la base de données

    # Connexion a la base de données

    # Importation des informations de connexion
    DATABASE_HOST = config.DATABASE_HOST
    DATABASE_NAME = config.DATABASE_NAME
    DATABASE_USERNAME = config.DATABASE_USERNAME
    DATABASE_PASSWORD = config.DATABASE_PASSWORD
    DATABASE_PORT = config.DATABASE_PORT

    # Création du moteur de base de données
    engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(Client).filter_by(name=name).first():
        st.error("Ce nom existe désormais")
        session.close()
    else:
        session.add(name, password)
        session.commit()
        session.close()

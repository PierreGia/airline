
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
import pandas as pd
import os, sys
from components.formConnexion import formConnexion


# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

def boardstat():

    authentication_status, authenticator, name = formConnexion()

    st.title("tableau de bord")
    df = pd.read_csv("data/airline_short.csv")
    st.dataframe(df)

#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
import pandas as pd

import os, sys

# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

def boardstat():
    
    st.title("tableau de bord")
    df = pd.read_csv("data/airline_short.csv")
    st.dataframe(df)
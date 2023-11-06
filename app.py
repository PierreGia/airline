#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st
from components.formSatisfaction import formsatisfaction
from components.formInscription import formInscription
from components.formConnexion import formConnexion
from components.boardStat import boardstat
from components.figure import plot_graph, curvroc, confmat, metric, features
from Airplane import df
import bcrypt
import mysql.connector

# Titre de l'application
# st.title("Application de Réservation de Vols")
# st.dataframe(df.sort_values(by='id'))

# Chemins vers les images
confusion = "figures/confusion_matrix.png"
features = "figures/features.png"
metrics = "figures/metrics.png"
roc_curve = "figures/roc_curve.png"


# Menu de navigation latéral
selection = st.sidebar.radio("Sélectionnez une page", ["formulaire", "tableau de bord", "graphe", "inscription", "connexion"])

if selection == "formulaire":
    formsatisfaction ()
    
elif selection == "tableau de bord":
    st.title("Tableau de bord")
    boardstat(confusion, features, metrics, roc_curve)

elif selection == "graphe":
    plot_graph(curvroc, confmat, metric, features)

elif selection == "inscription":
    formInscription()

elif selection == "connexion":
    formConnexion()

    



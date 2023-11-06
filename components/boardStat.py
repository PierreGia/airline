
#dans app on appelle les différentes fonction des fichiers dans components

import streamlit as st

import pandas as pd
import os, sys
from components.formConnexion import formConnexion


# Chemins vers les images
confusion = "figures/confusion_matrix.png"
features = "figures/features.png"
metrics = "figures/metrics.png"
roc_curve = "figures/roc_curve.png"


def boardstat(confusion, features, metrics, roc_curve):
    # Affichage des images
    st.image(open(confusion, 'rb').read(), use_column_width=True, caption="Matrice de confusion")
    st.image(open(features, 'rb').read(), use_column_width=True, caption="Caractéristiques")
    st.image(open(metrics, 'rb').read(), use_column_width=True, caption="Métriques")
    st.image(open(roc_curve, 'rb').read(), use_column_width=True, caption="Courbe ROC")
    authentication_status, authenticator, name = formConnexion()




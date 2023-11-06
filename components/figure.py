from sklearn.metrics import classification_report
import joblib
from components.create_model import X_test, y_test
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt
from components.useful_function import make_confusion_matrix, plot_features
import pandas as pd
import streamlit as st

from components.formConnexion import formConnexion

st.title("figure")
#Définissez une fonction pour générer la courbe ROC, la matrice de confusion et d'autres éléments.
#def generate_metrics_and_plots(model, X_test, y_test):
    
 # Chargement du modèle
model = joblib.load("ML/RandomForestClassifier.joblib")
y_pred = model.predict(X_test)

# Creation de la courbe ROC

curve_roc= RocCurveDisplay.from_estimator(model, X_test, y_test)

# Sauvegarde de la figure
plt.savefig('figures/roc_curve.png')

# Creation de la matrice de confusion et sauvegarde de la figure

confusion = make_confusion_matrix(y_test, y_pred)

# Creation du rapport de classification et sauvegarde du rapport
report = classification_report(y_test, y_pred)
with open('figures/classification_report.txt', 'w') as file:
    file.write(report)

# Recuperer les metriques
metrics = pd.read_csv('ML/metrics.csv')
metric = metrics.T.plot.bar(title="scores du model RandomForestClassifier")

# Sauvegarde de la figure
plt.savefig('figures/metrics.png')

# Creation du graphique des features et sauvegarde de la figure

features = plot_features(X_test.columns, model.feature_importances_)

plt.savefig('figures/features.png')

def plot_graph(curve_roc, confusion, metric, features):

    authentication_status, authenticator, name = formConnexion()

    st.pyplot(curve_roc.figure_)
    st.pyplot(confusion)
    st.pyplot(metric)
    st.pyplot(features)



from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import itertools
import string
import random
import streamlit as st

def test_model(X_train, X_test, y_train, y_test, models, param_grids):
  '''
  Cette fonction permet de tester les modèles en fonction des hyperparamètres
  Args: X_train: jeu d'entrainement des features
        X_test: jeu de test des features
        y_train: jeu d'entrainement de la target
        y_test: jeu de test de la target
        models: dictionnaire des models
        param_grids: dictionnaire des hyperparamètres
  Returns: un dataframe avec les scores des modèles
  '''
  metrics = {}
  for nom, model in models.items():
    # On sauvegarde les valeurs de X_train et X_test
    X_temp_train = X_train
    X_temp_test = X_test
    # Cas spécifique du model RBFSampler
    if nom == "RBFSampler":
      X_train = model.fit_transform(X_train)
      X_test = model.transform(X_test)
      model = models["SGDClassifier"]
    # Crééons un grid search cv
    grid_search = GridSearchCV(model(), param_grid=param_grids[model], cv=5, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)
    # Meilleurs hyperparamètres trouvés
    best_params = grid_search.best_params_
    best_model = model(**best_params)
    # Entrainement du model
    best_model.fit(X_train, y_train)
    # Enregistrement du model
    filename = f"ML/{nom}.joblib"
    joblib.dump(best_model, filename)
    # Prédiction
    y_pred = best_model.predict(X_test)
    # On récupère les valeures de X_train et X_test
    X_train = X_temp_train
    X_test = X_temp_test
    # Ajout des noms et des scores
    class_metrics = {}
    class_metrics["accuracy"] = accuracy_score(y_test, y_pred)
    class_metrics["precision"] = precision_score(y_test, y_pred, average="macro")
    class_metrics["recall"] = recall_score(y_test, y_pred, average="macro")
    class_metrics["f1-score"] = f1_score(y_test, y_pred, average="macro")
    metrics[nom] = class_metrics
  metrics = pd.DataFrame.from_dict(metrics, orient='index')
  print(metrics)
  # Enregistrement du dataframe
  metrics.to_csv("ML/metrics.csv", index=False)
  return metrics

def make_confusion_matrix(y_true, y_pred, classes=None, figsize=(10, 10), text_size=15, norm=False): 
  """Fait une matrice de confusion étiquetée comparant les prédictions aux étiquettes de vérité.
Si classes est passé, la matrice de confusion sera étiquetée, sinon, des valeurs de classe entières seront utilisées.

Arguments :
        y_true : Tableau des étiquettes de vérité (doit avoir la même forme que y_pred).
        y_pred : Tableau des étiquettes prédites (doit avoir la même forme que y_true).
        classes : Tableau des étiquettes de classe (par exemple, sous forme de chaînes de caractères). Si None, des étiquettes entières sont utilisées.
        figsize : Taille de la figure de sortie (par défaut : (10, 10)).
        text_size : Taille du texte de la figure de sortie (par défaut : 15).
        norm : Normaliser les valeurs ou non (par défaut : False).
        savefig : Enregistrer la matrice de confusion dans un fichier (par défaut : False).
Renvoie :
Une matrice de confusion étiquetée comparant y_true et y_pred.
  """  
  # Créez la matrice de confusion
  cm = confusion_matrix(y_true, y_pred)
  cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] # normalise
  n_classes = cm.shape[0] # determine le nombre de classes que la matrice de confusion contient

  # Trace la figure et la rend jolie
  fig, ax = plt.subplots(figsize=figsize)
  cax = ax.matshow(cm, cmap=plt.cm.Blues) # les couleurs indiquent à quel point la matrice de confusion correspond, le plus foncé est le mieux
  fig.colorbar(cax)

  # Y a t-il une liste de noms de classe ?
  if classes:
    labels = classes
  else:
    labels = np.arange(cm.shape[0])
  
  # Nommer les axes
  ax.set(title="Confusion Matrix",
         xlabel="Predicted label",
         ylabel="True label",
         xticks=np.arange(n_classes), # creer suffisament de slots pour chaque classe
         yticks=np.arange(n_classes), 
         xticklabels=labels, #  les axes sont etiquettés avec les noms de classe (s'il existent) ou des entiers
         yticklabels=labels)
  
  # Fais apparaitre les etiquettes de l'axe x en bas
  ax.xaxis.set_label_position("bottom")
  ax.xaxis.tick_bottom()

  #  Paramétrer le seuil pour differentes couleurs
  threshold = (cm.max() + cm.min()) / 2.

  # Tracer le texte dans chaque cellule
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    if norm:
      plt.text(j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
              horizontalalignment="center",
              color="white" if cm[i, j] > threshold else "black",
              size=text_size)
    else:
      plt.text(j, i, f"{cm[i, j]}",
              horizontalalignment="center",
              color="white" if cm[i, j] > threshold else "black",
              size=text_size)
      
  # Enregistrer la figure dans le dossier figures
  fig.savefig("figures/confusion_matrix.png")
  return fig

def plot_features(columns, importances, n=20):
  df = (pd.DataFrame({"features": columns,
                      "feature_importances": np.round(importances, 3)})
      .sort_values("feature_importances", ascending=False)
      .reset_index(drop=True))
  
  # Plot the dataframe
  fig, ax = plt.subplots()
  ax.barh(df["features"][:n], df["feature_importances"][:20])
  ax.set_ylabel("Features")
  ax.set_xlabel("Feature_importance")
  ax.invert_yaxis()
  return fig

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Caractères autorisés : lettres et chiffres
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def session(fonction=None, *args):
  # On affiche la session    
  if st.session_state["authentication_status"]:
    st.session_state["authenticator"].logout('Logout', 'main', key='unique_key')
    st.write(f'Bienvenue *{st.session_state["name"]}*')
    if fonction and args:
      fonction(*args)
    elif fonction:
      fonction()
  elif st.session_state["authentication_status"] is False:
      st.error('nom d’utilisateur ou mot de passe incorrect')
  elif st.session_state["authentication_status"] is None:
      st.warning('Veuillez entrer votre nom d’utilisateur et votre mot de passe')
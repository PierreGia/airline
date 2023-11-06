# Nettoyage des donnees

# import des libraries
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_selector
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
import os, sys
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.kernel_approximation import RBFSampler
from components.useful_function import test_model
from sklearn.ensemble import RandomForestClassifier

# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from Airplane import df

# Remplacer les valeurs à zeros par la moyenne car zero représente l'absence d'avis
df["Inflight wifi service"] = df["Inflight wifi service"].replace(0, df["Inflight wifi service"].mean())
df["Departure/Arrival time convenient"] = df["Departure/Arrival time convenient"].replace(0, df["Departure/Arrival time convenient"].mean())
df["Ease of Online booking"] = df["Ease of Online booking"].replace(0, df["Ease of Online booking"].mean())
df["Gate location"] = df["Gate location"].replace(0, df["Gate location"].mean())
df["Food and drink"] = df["Food and drink"].replace(0, df["Food and drink"].mean())
df["Online boarding"] = df["Online boarding"].replace(0, df["Online boarding"].mean())
df["Seat comfort"] = df["Seat comfort"].replace(0, df["Seat comfort"].mean())
df["Inflight entertainment"] = df["Inflight entertainment"].replace(0, df["Inflight entertainment"].mean())
df["On-board service"] = df["On-board service"].replace(0, df["On-board service"].mean())
df["Leg room service"] = df["Leg room service"].replace(0, df["Leg room service"].mean())
df["Checkin service"] = df["Checkin service"].replace(0, df["Checkin service"].mean())
df["Inflight service"] = df["Inflight service"].replace(0, df["Inflight service"].mean())
df["Cleanliness"] = df["Cleanliness"].replace(0, df["Cleanliness"].mean())

# Separation de la target et des features
X = df.drop(["Satisfaction","id", "Departure Delay in Minutes", "Gender", "Food and drink", "Inflight entertainment", "Leg room service"], axis=1)
y = df["Satisfaction"]

# Enregistrement du dataframe original avec les colonnes jugées inutiles pour la prédiction retirées
X.to_csv("data/airline_short.csv", index=False)

# Creation des colonnes numeriques et categorielles et conversion des variables entieres en flottants
numerical_features = make_column_selector(dtype_include=np.number)
categorical_features = make_column_selector(dtype_exclude=np.number)
X[numerical_features] = X[numerical_features].astype(float)

# On récupère les noms des colonnes numeriques et categorielles pour les ajouter à la fin
numeric_columns = X[numerical_features].columns
categorical_columns = pd.get_dummies(X[categorical_features]).columns

# Creation des pipelines
numerical_pipelines = make_pipeline(SimpleImputer(), MinMaxScaler()) # SimpleImputer pour remplacer les valeurs manquantes par la moyenne et MinMaxScaler pour normaliser
categorical_pipelines = make_pipeline(OneHotEncoder())
preprocessor = make_column_transformer((numerical_pipelines, numerical_features), (categorical_pipelines, categorical_features))
X_clean = pd.DataFrame(preprocessor.fit_transform(X))

# Enregistrement du preprocessor
filename = "ML/preprocessor.joblib"
joblib.dump(preprocessor, filename)

# On renomme les colonnes avec les noms des colonnes numeriques et categorielles
X_clean.columns = (numeric_columns.tolist() + categorical_columns.tolist())

# On enregistre le dataframe nettoye
X_clean.to_csv("data/airline_clean.csv", index=False)

# On remplace les valeurs categorielles par des valeurs numeriques dans la target
y = y.map({"neutral or dissatisfied": 0, "satisfied": 1})

# Séparation du jeu de données en un jeu d'entrainement et un jeu de test
X_train, X_test, y_train, y_test = train_test_split(X_clean, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# On définit les hyperparamètres des models
param_grid_model = {
    # SGDClassifier : {'loss': ['log_loss', 'squared_error'],
    # 'penalty': ['l1', 'elasticnet'],
    # 'learning_rate': ['constant', 'optimal'],
    # 'eta0': [0.01],
    # 'n_jobs': [-1]},
    RandomForestClassifier : {'n_jobs': [-1]}                                                          
}

# On definit les models
models = { #"SGDClassifier" : SGDClassifier,
          #"RBFSampler" : RBFSampler(gamma=1),
          "RandomForestClassifier" : RandomForestClassifier}

# Testons les modèles en fonction des hyperparamètres
test_model(X_train, X_test, y_train, y_test, models, param_grid_model)
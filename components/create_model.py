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
from useful_function import test_model
from sklearn.ensemble import RandomForestClassifier


# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from Airplane import df

# Separation de la target et des features
X = df.drop(["Satisfaction","id"], axis=1)
y = df["Satisfaction"]

# Creation des colonnes numeriques et categorielles et Conversion des variables numeriques en flottants
numerical_features = make_column_selector(dtype_include=np.number)
categorical_features = make_column_selector(dtype_exclude=np.number)
X[numerical_features] = X[numerical_features].astype(float)
X["Average delay in minutes"] = X[['Departure Delay in Minutes','Arrival Delay in Minutes']].mean(axis=1)
X.drop(['Departure Delay in Minutes','Arrival Delay in Minutes'], axis=1, inplace=True)

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
    SGDClassifier : {'loss': ['squared_hinge', 'log_loss', 'squared_error'],
    'penalty': ['l1', 'elasticnet'],
    'learning_rate': ['constant', 'optimal'],
    'eta0': [0.01]},
    RandomForestClassifier : {'n_estimators': [100],
    'max_depth': [3, 5, 8]},
}

# On definit les models
models = {"SGDClassifier" : SGDClassifier,
          "RBFSampler" : RBFSampler(gamma=1),
          "RandomForestClassifier" : RandomForestClassifier}

# Testons les modèles en fonction des hyperparamètres
test_model(X_train, X_test, y_train, y_test, models, param_grid_model)
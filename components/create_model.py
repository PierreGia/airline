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

# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from Airplane import df

# Creation des colonnes numeriques et categorielles et Conversion des variables numeriques en flottants
numerical_features = make_column_selector(dtype_include=np.number)
categorical_features = make_column_selector(dtype_exclude=np.number)
df[numerical_features] = df[numerical_features].astype(float)
df["Average delay in minutes"] = df[['Departure Delay in Minutes','Arrival Delay in Minutes']].mean(axis=1)
df.drop(['Departure Delay in Minutes','Arrival Delay in Minutes'], axis=1, inplace=True)

# Creation des pipelines
numerical_pipelines = make_pipeline(SimpleImputer(), MinMaxScaler()) # SimpleImputer pour remplacer les valeurs manquantes par la moyenne et MinMaxScaler pour normaliser
categorical_pipelines = make_pipeline(OneHotEncoder())
preprocessor = make_column_transformer((numerical_pipelines, numerical_features), (categorical_pipelines, categorical_features))
df_clean = pd.DataFrame(preprocessor.fit_transform(df))
print(df_clean)


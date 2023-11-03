from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import pandas as pd
from sklearn.linear_model import SGDClassifier

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
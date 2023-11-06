# Analyse des donnees
import os
import pandas as pd
import ydata_profiling

from ydata_profiling import ProfileReport # conda install -c conda-forge ydata-profiling
print(os.getcwd())
df = pd.read_csv('data/Airline_Dataset.csv')
profile = ProfileReport(df,title="HCC Profiling Report")
profile.to_notebook_iframe() 
profile.to_file("report.html") #(fichier à ouvrir avec navigateur)






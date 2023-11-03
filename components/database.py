from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
import sys, os
import pandas as pd
import csv

# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from databases.classes import Classes, Customer_types, Types_of_Travel, Flights, Evaluation, Customers, Base
from databases import config

# Importation des informations de connexion
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME
DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD
DATABASE_PORT = config.DATABASE_PORT

# Création du moteur de base de données
engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

# creation de la base de données si elle n'existe pas

if database_exists(engine.url):
    drop_database(engine.url)

create_database(engine.url)
print("is database existing?: ", database_exists(engine.url))

# Création des tables
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Récupération du dataframe
csv_file_path = "data/airline_short.csv"

# Lecture du fichier CSV et insertion des données dans la table
with open(csv_file_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    en_tetes = next(csv_reader)  # Enregistrer et ignorer la première ligne si elle contient les en-têtes
    csv_reader = list(csv_reader)

for row in csv_reader: 
    session.add(Customer_types(type=row[0]))
    session.add(Types_of_Travel(type=row[2]))
    session.add(Classes(type=row[3]))
    session.add(Customers(age=row[1]))
    session.add(Evaluation(inflight_wifi_service=row[5],
                           ease_of_online_booking=row[7],
                           gate_location=row[8],
                           online_boarding=row[9],
                           seat_comfort=row[10],
                           onboard_service=row[11],
                           baggage_handling=row[12],
                           checkin_service=row[13],
                           inflight_service=row[14],
                           cleanliness=row[15]))
    session.commit()
    session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()
for number,row in enumerate(csv_reader):
    customer_id = session.query(Customer_types).filter(Customer_types.type == row[0]).first().id
    type_of_travel_id = session.query(Types_of_Travel).filter(Types_of_Travel.type == row[2]).first().id
    class_id = session.query(Classes).filter(Classes.type == row[3]).first().id
    session.add(Flights( flight_distance=row[4],
                        departure_arrival_time_convenient=row[6],
                        arrival_delay_in_minutes=row[16],
                        customer_type_id=customer_id,
                        type_of_travel_id=type_of_travel_id,
                        class_id=class_id,
                        evaluation_id=number+1))
    session.commit()
    session.close()
                      
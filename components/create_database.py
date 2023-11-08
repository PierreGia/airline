from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
import sys, os
import pandas as pd
import csv

# On récupère les valeures uniques pour chaque colonne categorie du dataframe afin de les inserer plus tard dans les tables
df = pd.read_csv('data/Airline_Dataset.csv')
unique_satisfaction = df['Satisfaction'].unique()
unique_gender = df['Gender'].unique()
unique_customer_type = df['Customer Type'].unique()
unique_type_travel = df['Type of Travel'].unique()
unique_class_travel = df['Class'].unique()


# Comme le fichier "Airplane.py" est inclus dans le dossier parent du dossier actuel on revient deux fois en arrière
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
from databases.classes import Base, Satisfaction, Gender, Client, Customer_type, Flight, Type_Travel, Class_travel, Vol_Client
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
csv_file_path = "data/Airline_Dataset.csv"

# Lecture du fichier CSV et insertion des données dans la table
with open(csv_file_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    en_tetes = next(csv_reader)  # Enregistrer et ignorer la première ligne si elle contient les en-têtes
    csv_reader = list(csv_reader)

# Insertion des données
satisfaction = [
            Satisfaction(type=unique_satisfaction[0]),
            Satisfaction(type=unique_satisfaction[1])
]
session.add_all(satisfaction)

gender = [
            Gender(type=unique_gender[0]),
            Gender(type=unique_gender[1])
]
session.add_all(gender)

customer_type = [
            Customer_type(type=unique_customer_type[0]),
            Customer_type(type=unique_customer_type[1])
]
session.add_all(customer_type)

for row in csv_reader:
    flight = [
            Flight(flight_distance=row[6],
                   departure_delay=row[21],
                   arrival_delay=row[22])
    ]
    session.add_all(flight)

type_travel = [
            Type_Travel(type=unique_type_travel[0]),
            Type_Travel(type=unique_type_travel[1])
]
session.add_all(type_travel)

class_travel = [
            Class_travel(type=unique_class_travel[0]),
            Class_travel(type=unique_class_travel[1]),
            Class_travel(type=unique_class_travel[2])
]
session.add_all(class_travel)

session.commit()
session.close()


Session = sessionmaker(bind=engine)
session = Session()

for number,row in enumerate(csv_reader):
    customer_type_id = session.query(Customer_type).filter(Customer_type.type == row[2]).first().id
    gender_id = session.query(Gender).filter(Gender.type == row[1]).first().id
    session.add(Client( age=row[3],
                        gender_id=gender_id,
                        customer_type_id=customer_type_id))
    
    satisfaction_id = session.query(Satisfaction).filter(Satisfaction.type == row[23]).first().id
    type_travel_id = session.query(Type_Travel).filter(Type_Travel.type == row[4]).first().id
    class_travel_id = session.query(Class_travel).filter(Class_travel.type == row[5]).first().id
    session.add(Vol_Client(inflight_wifi_service=row[7],
                           departure_arrival_time_convenient=row[8],
                           ease_of_online_booking=row[9],
                           gate_location=row[10],
                           food_and_drink=row[11],
                           online_boarding=row[12],
                           seat_comfort=row[13],
                           inflight_entertainment=row[14],
                           on_board_service=row[15],
                           leg_room_service=row[16],
                           baggage_handling=row[17],
                           checkin_service=row[18],
                           inflight_service=row[19],
                           cleanliness=row[20],
                           satisfaction_id=satisfaction_id,
                           client_id=number+1,
                           flight_id=number+1,
                           type_travel_id=type_travel_id,
                           class_travel_id=class_travel_id
                           ))
    session.commit()
    session.close()
                      
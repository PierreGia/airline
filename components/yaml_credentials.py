from sqlalchemy.orm import sessionmaker
import os, sys
import yaml

from sqlalchemy import create_engine

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
print(parent_dir)
from databases import config
from databases.classes import Login_Mot_de_passe
from components.useful_function import generate_random_string

def exec_yaml():
    # Importation des informations de connexion
    DATABASE_HOST = config.DATABASE_HOST
    DATABASE_NAME = config.DATABASE_NAME
    DATABASE_USERNAME = config.DATABASE_USERNAME
    DATABASE_PASSWORD = config.DATABASE_PASSWORD
    DATABASE_PORT = config.DATABASE_PORT

    # Création du moteur de base de données
    engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

    Credentials = {}        

    Session = sessionmaker(bind=engine)
    session = Session()
    Credentials = {
    "credentials": {
        "usernames": {}
    },
    "cookie": {
        "expiry_days": 30,
        "key": generate_random_string(5),
        "name": generate_random_string(3)
    },
    "prehautorized": {
        "emails": "antonys@simplon.co"
                    }
    }
    for row in session.query(Login_Mot_de_passe).all():
        login = {row.login: 
                        {
                        "email": row.email,
                        "name": row.name,
                        "password": row.mot_de_passe         
                        }
                    }
        Credentials["credentials"]["usernames"].update(login)
    with open('databases/config.yaml', 'w') as yaml_file:
        yaml.dump(Credentials, yaml_file, default_flow_style=False)
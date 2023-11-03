from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Satisfaction(Base):
    __tablename__ = 'satisfaction'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Login_Mot_de_passe(Base):
    __tablename__ = 'login_mot_de_passe'
    id = Column(Integer, primary_key=True)
    login = Column(String(255), nullable=True)
    mot_de_passe = Column(String(255), nullable=True)

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    customer_type_id = Column(Integer, ForeignKey('customer_type.id'))
    login_mot_de_passe_id = Column(Integer, ForeignKey('login_mot_de_passe.id'))
    gender = relationship('Gender')
    customer_type = relationship('Customer_type')
    login_mot_de_passe = relationship('Login_Mot_de_passe')
    
    
class Customer_type(Base):
    __tablename__ = 'customer_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)
    

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    flight_distance = Column(Integer)
    departure_delay = Column(Integer)
    arrival_delay = Column(String(255))


class Type_Travel(Base):
    __tablename__ = 'type_travel'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Class_travel(Base):
    __tablename__ = 'class_travel'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)
 
    
class Vol_Client(Base):
    __tablename__ = 'vol_client'
    id = Column(Integer, primary_key=True)
    inflight_wifi_service = Column(Integer)
    departure_arrival_time_convenient = Column(Integer)
    ease_of_online_booking = Column(Integer)
    gate_location = Column(Integer)
    food_and_drink = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    inflight_entertainment = Column(Integer)
    on_board_service = Column(Integer)
    leg_room_service = Column(Integer)
    baggage_handling = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)
    satisfaction_id = Column(Integer, ForeignKey('satisfaction.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))
    type_travel_id = Column(Integer, ForeignKey('type_travel.id'))
    class_travel_id = Column(Integer, ForeignKey('class_travel.id'))
    satisfaction = relationship('Satisfaction')
    client = relationship('Client')
    flight = relationship('Flight')
    type_travel = relationship('Type_Travel')
    class_travel=relationship('Class_travel')


    
    

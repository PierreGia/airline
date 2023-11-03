from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True)
    gender = Column(String(255))

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    type_id = Column(Integer, ForeignKey('type.id'))
    gender = relationship('Gender')
    type = relationship('Type')
    
    
class Type_customer(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    customer_type = Column(String(255))
    

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    flight_distance = Column(Integer)
    departure_delay = Column(Integer)
    arrival_delay = Column(Integer)


class Type_Travel(Base):
    __tablename__ = 'type_travel'
    id = Column(Integer, primary_key=True)
    type_travel = Column(String(255))

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    class_travel = Column(String(255))
    
    
class Vole_Client(Base):
    __tablename__ = 'vole_client'
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
    satisfaction = Column(String(255))
    client_id = Column(Integer, ForeignKey('client.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    type_travel_id = Column(Integer, ForeignKey('type_travel.id'))
    client = relationship('Client')
    flight = relationship('Flight')
    class_travel=relationship('Class')
    type_travel = relationship('TypeTravel')
    
    

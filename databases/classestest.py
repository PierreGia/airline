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

    gender = Column(String(255), nullable=False)


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    type_id = Column(Integer, ForeignKey('type.id'))
    gender = relationship('Gender')
    type = relationship('Type')
    
    

class Customer_type(Base):
    __tablename__ = 'customer_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

    

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    flight_distance = Column(Integer)
    departure_delay = Column(Integer)
    arrival_delay = Column(Integer)


class Type_Travel(Base):
    __tablename__ = 'type_travel'
    id = Column(Integer, primary_key=True)

    type_travel = Column(String(255), nullable=False)


class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)

    class_travel = Column(String(255), nullable=False)
 

    
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
    class_id = Column(Integer, ForeignKey('class.id'))
    type_travel_id = Column(Integer, ForeignKey('type_travel.id'))
    satisfaction = relationship('Satisfaction')
    client = relationship('Client')
    flight = relationship('Flight')
    class_travel=relationship('Class')
    type_travel = relationship('TypeTravel')
    
    

#orm sqlalchemy definition des classes

# Import des modules SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Definition de la classe Base
Base = declarative_base()

class Customer_types(Base):
    __tablename__ = 'customer_types'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Types_of_Travel(Base):
    __tablename__ = 'types_of_travel'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Classes (Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Satisfaction(Base):
    __tablename__ = 'satisfaction'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    gender = relationship(Gender)
    Satisfaction_id = Column(Integer, ForeignKey('satisfaction.id'))
    Satisfaction = relationship(Satisfaction)

class Evaluation(Base):
    __tablename__ = 'evaluation'
    id = Column(Integer, primary_key=True)
    inflight_wifi_service = Column(Integer)
    ease_of_online_booking = Column(Integer)
    gate_location = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    onboard_service = Column(Integer)
    baggage_handling = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)

class Flights(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    flight_distance = Column(Integer)
    departure_delay_in_minutes = Column(Integer)
    departure_arrival_time_convenient = Column(Integer)
    arrival_delay_in_minutes = Column(Integer, nullable=True)
    customer_type_id = Column(Integer, ForeignKey('customer_types.id'))
    customer_type = relationship(Customer_types)
    type_of_travel_id = Column(Integer, ForeignKey('types_of_travel.id'))
    type_of_travel = relationship(Types_of_Travel)
    class_id = Column(Integer, ForeignKey('classes.id'))
    class_type = relationship(Classes)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customers)
    evaluation_id = Column(Integer, ForeignKey('evaluation.id'))
    evaluation = relationship(Evaluation)
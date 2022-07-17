from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    customer_address = Column(String, nullable=False)
    next_call_date = Column(DateTime, nullable=False)
    ts_inserted = Column(DateTime, nullable=False)

class Call(Base):
    __tablename__ = "call"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    start_time = Column(DateTime)
    next_call_date = Column(DateTime)
    end_time = Column(DateTime)
    call_outcome_id = Column(Integer)


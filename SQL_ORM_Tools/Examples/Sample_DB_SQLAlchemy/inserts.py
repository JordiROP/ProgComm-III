from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session
from models import Base, City, Employee, Customer, Call

engine = create_engine("postgresql://postgres:postgrespw@localhost:49153/example", echo=True, future=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()

Base.metadata.create_all(engine)

with Session(engine) as session:
    victor = Employee(first_name='Victor', last_name='Altés Gaspar')
    salma = Employee(first_name='Salma', last_name='Assiad Sebai')
    session.add_all([victor, salma])
    session.commit()

    lleida = City(name='Lleida')
    barcelona = City(name='Barcelona')
    murcia = City(name='Murcia')
    session.add_all([lleida, barcelona, murcia])
    session.commit()

    abraham = Customer(customer_name='Abraham Castro Criado', city_id=1, customer_address='Calle de la Piruleta', next_call_date='2022-12-01', ts_inserted='2022-12-01')
    pelayo = Customer(customer_name='Pelayo Cobos Rodriguez', city_id=1, customer_address='Salchichon', next_call_date='2022-05-01', ts_inserted='2022-05-01')
    artur = Customer(customer_name='Artur Cullerés Cervera', city_id=2, customer_address='Sanjacobo Street', next_call_date='2022-01-01', ts_inserted='2022-01-01')
    didac = Customer(customer_name='Didac Colominas Abalde', city_id=3, customer_address='Albacete Strassen', next_call_date='2022-08-01', ts_inserted='2022-08-01')
    eduard = Customer(customer_name='Eduard de La Arada Janoher', city_id=1, customer_address='Wala wala bing bong', next_call_date='2022-07-01', ts_inserted='2022-07-01')
    session.add_all([abraham, pelayo, artur, didac, eduard])
    session.commit()

    call1 = Call(employee_id=1, customer_id=1, start_time='2022-12-01 12:05:06', end_time='2022-12-01 12:06:06', call_outcome_id=0)
    call2 = Call(employee_id=1, customer_id=2, start_time='2022-05-01 17:11:06', end_time='2022-05-01 17:24:06', call_outcome_id=0)
    call3 = Call(employee_id=2, customer_id=3, start_time='2022-01-01 22:01:06', end_time='2022-01-01 22:01:45', call_outcome_id=0)
    call4 = Call(employee_id=2, customer_id=4, start_time='2022-08-01 11:43:06', end_time='2022-08-01 11:55:06', call_outcome_id=0)
    call5 = Call(employee_id=1, customer_id=5, start_time='2022-07-01 04:22:06', end_time='2022-07-01 05:22:06', call_outcome_id=0)

    session.add_all([call1, call2, call3, call4, call5])
    session.commit()
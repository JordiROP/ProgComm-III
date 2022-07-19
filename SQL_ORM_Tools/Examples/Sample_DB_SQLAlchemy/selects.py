from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Employee, Customer, Call

engine = create_engine("postgresql://<user>:<password>@<direction>:<port>/<database>", echo=True, future=True)
engine.connect()

with Session(engine) as session:
    print('------ SELECT ALL ------')
    employees = session.execute(select(Employee)).scalars().all()
    for employee in employees:
        print(employee.first_name)
    
    print('------ SELECT ONE ------')
    employee = session.execute(select(Employee)).scalar()
    print(employee.first_name)

    print('------ SELECT WITH FILTER ------')
    customers = session.execute(select(Customer).filter_by(city_id=1)).scalars().all()
    for customer in customers:
        print(customer.customer_name)

    print('------ SELECT WITH JOIN ------')
    calls = session.execute(select(Call).join(Customer, Call.customer_id==Customer.id).filter(Customer.city_id==1)).scalars().all()
    for call in calls:
        print(call.id)
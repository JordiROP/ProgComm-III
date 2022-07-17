from sqlalchemy import create_engine, select, update, delete
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

    print('------ UPDATE ------')
    updated_id = session.execute(update(Employee).where(Employee.id == 1).values(first_name="Paprika").returning(Employee.id)).scalar_one_or_none()
    session.commit()
    if updated_id is not None:
        employee = session.execute(select(Employee).filter_by(id=updated_id)).scalar()
        print(employee.first_name)

    print('------ DELETE ------')
    deleted_id = session.execute(delete(Call).where(Call.id == 1).returning(Call.id)).scalar_one_or_none()
    print(deleted_id)
    session.commit()
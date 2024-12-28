from sqlalchemy import create_engine, select
from sqlalchemy.orm import create_session
from models import Employee, Customer, Call

engine = create_engine("postgresql://<user>:<password>@<direction>:<port>/<database>", echo=True, future=True)
engine.connect()
Session = create_session(engine=engine)
with Session(engine) as session:
    # WITH EXECUTE
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
    calls = session.execute(select(Call).
                            join(Customer, Call.customer_id==Customer.id).
                            filter(Customer.city_id==1)).scalars().all()
    for call in calls:
        print(call.id)

    # WITH QUERY
    employees = session.query(Employee).all()
    for employee in employees:
        print(employee.first_name)

    employee = session.query(Employee).first()
    print(employee.first_name)

    # Fetch a specific user by ID
    employee = session.query(Employee).filter(Employee.id == 1).one()
    print(employee.first_name)

    employee = session.query(Employee).filter(Employee.first_name == "John Doe").all()
    for employee in employees:
        print(employee.first_name)
    
    employee = session.query(Employee).filter_by(first_name="John Doe").first()
    print(employee.first_name)
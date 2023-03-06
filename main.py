from sqlalchemy.orm import sessionmaker

from db_utils import setup_db_engine
from models import Income

engine = setup_db_engine()

Session = sessionmaker(bind=engine)
session = Session()


def get_income():
    income = session.query(Income).first()
    return income


def update_or_create_income(amount):
    if not session.query(Income).first():
        income = Income(amount=amount)
        session.add(income)
    else:
        current_income = session.query(Income).first()
        new_income = current_income.amount + amount
        session.query(Income).filter_by(id=1).update({"amount": new_income})
    session.commit()

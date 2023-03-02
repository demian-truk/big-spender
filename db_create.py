from sqlalchemy.orm import sessionmaker

from db_utils import create_database_if_not_exists, setup_db_engine
from models import Base, Category

if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine_obj=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """Example of adding expense categories"""
    category_1 = Category(name="Аренда")
    category_2 = Category(name="Развлечения")
    session.add_all([category_1, category_2])
    session.commit()
    session.close()

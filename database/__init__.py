from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


# Всё ещё изучаю, как работает async версия sqlalchemy (╥﹏╥)
engine = create_engine("sqlite:///orderDatabase.db", pool_size=10, max_overflow=20)
Session = sessionmaker(bind=engine)
session = Session()

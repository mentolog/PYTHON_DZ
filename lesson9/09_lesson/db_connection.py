#db_connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Параметры подключения к базе данных
DATABASE_URI = 'postgresql+psycopg2://testuser:testuser@localhost/QA'

def get_engine():
    """Создает и возвращает объект подключения к базе данных."""
    engine = create_engine(DATABASE_URI)
    return engine

def get_session():
    """Создает и возвращает новую сессию для работы с базой данных."""
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

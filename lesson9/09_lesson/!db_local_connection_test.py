from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Замените эти параметры на свои данные подключения
DATABASE_URI = 'postgresql+psycopg2://testuser:testuser@localhost/QA'

def get_engine():
    """Создает и возвращает объект подключения к базе данных."""
    try:
        print("Попытка подключения к базе данных...")
        engine = create_engine(DATABASE_URI)
        
        # Проверка успешности подключения
        connection = engine.connect()
        print("Подключение к базе данных успешно установлено.")
        connection.close()  # Закрываем соединение, так как оно больше не нужно
    except SQLAlchemyError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
    return engine

def get_session():
    """Создает и возвращает новую сессию для работы с базой данных."""
    engine = get_engine()
    if engine is None:
        print("Не удалось получить соединение с базой данных. Сессия не будет создана.")
        return None  # Возвращаем None, если подключение не удалось

    Session = sessionmaker(bind=engine)
    session = Session()
    print("Сессия успешно создана.")
    return session

# Для тестирования подключения можно добавить следующие строки:
if __name__ == "__main__":
    engine = get_engine()
    if engine:
        session = get_session()
        if session:
            print("Сессия активна.")
            session.close()  # Закрываем сессию после тестирования

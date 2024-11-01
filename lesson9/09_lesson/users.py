from sqlalchemy import text
from db_connection import get_session

class User:
    def __init__(self, user_email, subject_id):
        self.user_email = user_email
        self.subject_id = subject_id

def add_user(user_email, subject_id):
    session = get_session()
    new_user = User(user_email=user_email, subject_id=subject_id)
    try:
        session.execute(text("INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"),
                         {"email": new_user.user_email, "subject_id": new_user.subject_id})
        session.commit()
        print(f"Добавлен пользователь: {new_user.user_email}")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        session.rollback()
    finally:
        session.close()

def update_user(old_email, new_email):
    session = get_session()
    try:
        session.execute(text("UPDATE users SET user_email = :new_email WHERE user_email = :old_email"),
                         {"new_email": new_email, "old_email": old_email})
        session.commit()
        print(f"Обновлен пользователь: {old_email} на {new_email}")
    except Exception as e:
        print(f"Ошибка при обновлении пользователя: {e}")
        session.rollback()
    finally:
        session.close()

def delete_user(user_email):
    session = get_session()
    try:
        session.execute(text("DELETE FROM users WHERE user_email = :email"), {"email": user_email})
        session.commit()
        print(f"Удален пользователь: {user_email}")
    except Exception as e:
        print(f"Ошибка при удалении пользователя: {e}")
        session.rollback()
    finally:
        session.close()

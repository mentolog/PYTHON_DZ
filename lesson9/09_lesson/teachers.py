from sqlalchemy import text
from db_connection import get_session

class Teacher:
    def __init__(self, email, group_id):
        self.email = email
        self.group_id = group_id

def add_teacher(email, group_id):
    session = get_session()
    new_teacher = Teacher(email=email, group_id=group_id)
    try:
        session.execute(text("INSERT INTO teacher (email, group_id) VALUES (:email, :group_id)"),
                         {"email": new_teacher.email, "group_id": new_teacher.group_id})
        session.commit()
        print(f"Добавлен преподаватель: {new_teacher.email}")
    except Exception as e:
        print(f"Ошибка при добавлении преподавателя: {e}")
        session.rollback()
    finally:
        session.close()

def update_teacher(old_email, new_email):
    session = get_session()
    try:
        session.execute(text("UPDATE teacher SET email = :new_email WHERE email = :old_email"),
                         {"new_email": new_email, "old_email": old_email})
        session.commit()
        print(f"Обновлен преподаватель: {old_email} на {new_email}")
    except Exception as e:
        print(f"Ошибка при обновлении преподавателя: {e}")
        session.rollback()
    finally:
        session.close()

def delete_teacher(email):
    session = get_session()
    try:
        session.execute(text("DELETE FROM teacher WHERE email = :email"), {"email": email})
        session.commit()
        print(f"Удален преподаватель: {email}")
    except Exception as e:
        print(f"Ошибка при удалении преподавателя: {e}")
        session.rollback()
    finally:
        session.close()

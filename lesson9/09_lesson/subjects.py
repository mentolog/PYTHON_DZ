#subjects.py

from sqlalchemy import text
from db_connection import get_session

class Subject:
    def __init__(self, subject_title):
        self.subject_title = subject_title

def add_subject(subject_title):
    session = get_session()
    new_subject = Subject(subject_title=subject_title)
    try:
        session.execute(text("INSERT INTO subject (subject_title) VALUES (:subject_title)"),
                         {"subject_title": new_subject.subject_title})
        session.commit()
        print(f"Добавлен предмет: {new_subject.subject_title}")
    except Exception as e:
        print(f"Ошибка при добавлении предмета: {e}")
        session.rollback()
    finally:
        session.close()

def update_subject(old_subject_title, new_subject_title):
    session = get_session()
    try:
        session.execute(text("UPDATE subject SET subject_title = :new_subject_title WHERE subject_title = :old_subject_title"),
                         {"new_subject_title": new_subject_title, "old_subject_title": old_subject_title})
        session.commit()
        print(f"Обновлен предмет: {old_subject_title} на {new_subject_title}")
    except Exception as e:
        print(f"Ошибка при обновлении предмета: {e}")
        session.rollback()
    finally:
        session.close()

def delete_subject(subject_title):
    session = get_session()
    try:
        session.execute(text("DELETE FROM subject WHERE subject_title = :subject_title"), {"subject_title": subject_title})
        session.commit()
        print(f"Удален предмет: {subject_title}")
    except Exception as e:
        print(f"Ошибка при удалении предмета: {e}")
        session.rollback()
    finally:
        session.close()

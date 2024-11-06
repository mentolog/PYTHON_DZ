from sqlalchemy import text
from db_connection2 import get_session

class SubjectDatabase:
    def __init__(self):
        self.session = get_session()

    def add_subject(self, subject_id, subject_title):
        """Добавление новой записи предмета в базу данных."""
        query = text("INSERT INTO subject (subject_id, subject_title) VALUES (:subject_id, :subject_title)")
        self.session.execute(query, {'subject_id': subject_id, 'subject_title': subject_title})
        self.session.commit()

    def update_subject(self, subject_id, new_subject_title):
        """Обновление названия предмета по subject_id."""
        query = text("UPDATE subject SET subject_title = :subject_title WHERE subject_id = :subject_id")
        self.session.execute(query, {'subject_title': new_subject_title, 'subject_id': subject_id})
        self.session.commit()

    def delete_subject(self, subject_id):
        """Удаление записи предмета по subject_id."""
        query = text("DELETE FROM subject WHERE subject_id = :subject_id")
        self.session.execute(query, {'subject_id': subject_id})
        self.session.commit()

    def select_subject(self, subject_id):
        """Выбор записи предмета по subject_id."""
        query = text("SELECT * FROM subject WHERE subject_id = :subject_id")
        result = self.session.execute(query, {'subject_id': subject_id})
        return result.fetchall()  # Сохраняем кортежи

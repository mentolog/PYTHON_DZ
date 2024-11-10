from sqlalchemy import text
from db_connection2 import get_session

class TeacherDatabase:
    @staticmethod
    def add_teacher(teacher_id, email, group_id):
        """Добавляет преподавателя в базу данных."""
        session = get_session()
        try:
            session.execute(
                text("INSERT INTO teacher (teacher_id, email, group_id) VALUES (:teacher_id, :email, :group_id)"),
                {"teacher_id": teacher_id, "email": email, "group_id": group_id}
            )
            session.commit()
        except Exception as e:
            print(f"Ошибка при добавлении преподавателя: {e}")
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update_teacher(old_email, new_email):
        """Обновляет email преподавателя в базе данных."""
        session = get_session()
        try:
            session.execute(
                text("UPDATE teacher SET email = :new_email WHERE email = :old_email"),
                {"new_email": new_email, "old_email": old_email}
            )
            session.commit()
        except Exception as e:
            print(f"Ошибка при обновлении преподавателя: {e}")
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete_teacher(email):
        """Удаляет преподавателя из базы данных по email."""
        session = get_session()
        try:
            session.execute(
                text("DELETE FROM teacher WHERE email = :email"),
                {"email": email}
            )
            session.commit()
        except Exception as e:
            print(f"Ошибка при удалении преподавателя: {e}")
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def select_teacher(email):
        """Возвращает преподавателя из базы данных по email."""
        session = get_session()
        try:
            result = session.execute(
                text("SELECT * FROM teacher WHERE email = :email"),
                {"email": email}
            ).fetchone()
            return result
        finally:
            session.close()

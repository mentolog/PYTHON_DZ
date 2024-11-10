from sqlalchemy import text
from db_connection2 import get_session

class UserDatabase:
    @staticmethod
    def add_user(user_id, user_email, subject_id):
        """Добавляет пользователя в таблицу users."""
        with get_session() as session:
            session.execute(
                text(
                    "INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id)"
                ),
                {"user_id": user_id, "user_email": user_email, "subject_id": subject_id}
            )
            session.commit()

    @staticmethod
    def update_user(user_email, new_email):
        """Обновляет email пользователя в таблице users."""
        with get_session() as session:
            session.execute(
                text(
                    "UPDATE users SET user_email = :new_email WHERE user_email = :user_email"
                ),
                {"new_email": new_email, "user_email": user_email}
            )
            session.commit()

    @staticmethod
    def delete_user(user_id):
        """Удаляет пользователя из таблицы users по user_id."""
        with get_session() as session:
            session.execute(
                text(
                    "DELETE FROM users WHERE user_id = :user_id"
                ),
                {"user_id": user_id}
            )
            session.commit()

    @staticmethod
    def select_user(user_id):
        """Получает пользователя по user_id из таблицы users."""
        with get_session() as session:
            result = session.execute(
                text("SELECT * FROM users WHERE user_id = :user_id"),
                {"user_id": user_id}
            ).fetchall()
            return result

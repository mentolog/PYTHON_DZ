import pytest
from users2 import UserDatabase

class TestUserDatabase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Фикстура для подготовки и очистки данных перед и после каждого теста."""
        self.user_id = 9999
        self.user_email = 'unique_user@example.com'
        self.subject_id = 100

        # Очищаем таблицу перед каждым тестом
        UserDatabase.delete_user(self.user_id)
        yield
        # Очищаем таблицу после теста
        UserDatabase.delete_user(self.user_id)

    def test_add_user(self):
        """Тест на добавление пользователя в базу данных."""
        UserDatabase.add_user(self.user_id, self.user_email, self.subject_id)
        rows = UserDatabase.select_user(self.user_id)
        assert len(rows) > 0
        assert rows[-1][1] == self.user_email

    def test_update_user(self):
        """Тест на обновление email пользователя в базе данных."""
        UserDatabase.add_user(self.user_id, self.user_email, self.subject_id)
        new_email = 'updated_user@example.com'
        UserDatabase.update_user(self.user_email, new_email)
        rows = UserDatabase.select_user(self.user_id)
        assert len(rows) > 0
        assert rows[-1][1] == new_email

    def test_delete_user(self):
        """Тест на удаление пользователя из базы данных."""
        UserDatabase.add_user(self.user_id, self.user_email, self.subject_id)
        UserDatabase.delete_user(self.user_id)
        rows = UserDatabase.select_user(self.user_id)
        assert len(rows) == 0

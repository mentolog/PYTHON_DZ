import pytest
from users2 import UserDatabase

class TestUserDatabase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Фикстура для подготовки и очистки данных перед и после каждого теста."""
        self.user_id = 1234
        self.user_email = 'testuser@example.com'
        self.new_user_email = 'newemail@example.com'
        self.subject_id = 9999
        
        self.db = UserDatabase()

        # Очищаем таблицу перед каждым тестом
        self.db.delete_user(self.user_id)
        
        yield  # Тесты будут выполняться здесь
        
        # Очищаем таблицу после теста
        self.db.delete_user(self.user_id)

    def test_add_user(self):
        """Тест на добавление пользователя в базу данных."""
        self.db.add_user(self.user_id, self.user_email, self.subject_id)
        rows = self.db.select_user(self.user_id)
        assert len(rows) > 0
        assert rows[0][1] == self.user_email  # Индексация по числу, так как результат - кортеж

    def test_update_user(self):
        """Тест на обновление email пользователя в базе данных."""
        self.db.add_user(self.user_id, self.user_email, self.subject_id)
        self.db.update_user(self.user_email, self.new_user_email)
        rows = self.db.select_user(self.user_id)
        assert len(rows) > 0
        assert rows[0][1] == self.new_user_email  # Индексация по числу

    def test_delete_user(self):
        """Тест на удаление пользователя из базы данных."""
        self.db.add_user(self.user_id, self.user_email, self.subject_id)
        self.db.delete_user(self.user_id)
        rows = self.db.select_user(self.user_id)
        assert len(rows) == 0

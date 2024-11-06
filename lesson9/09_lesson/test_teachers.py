import pytest
from teachers2 import TeacherDatabase

class TestTeacherDatabase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Фикстура для подготовки и очистки данных перед и после каждого теста."""
        self.teacher_id = 1
        self.teacher_email = 'teacher@example.com'
        self.new_teacher_email = 'updated_teacher@example.com'
        self.group_id = 101

        self.db = TeacherDatabase()

        # Очищаем таблицу перед каждым тестом
        self.db.delete_teacher(self.teacher_email)

        yield  # Тесты будут выполняться здесь

        # Очищаем таблицу после теста
        self.db.delete_teacher(self.teacher_email)

    def test_add_teacher(self):
        """Тест на добавление преподавателя в базу данных."""
        self.db.add_teacher(self.teacher_id, self.teacher_email, self.group_id)
        result = self.db.select_teacher(self.teacher_email)
        assert result is not None
        assert result[1] == self.teacher_email  # Проверяем email преподавателя

    def test_update_teacher(self):
        """Тест на обновление email преподавателя в базе данных."""
        self.db.add_teacher(self.teacher_id, self.teacher_email, self.group_id)
        self.db.update_teacher(self.teacher_email, self.new_teacher_email)
        result = self.db.select_teacher(self.new_teacher_email)
        assert result is not None
        assert result[1] == self.new_teacher_email  # Проверяем новый email

    def test_delete_teacher(self):
        """Тест на удаление преподавателя из базы данных."""
        self.db.add_teacher(self.teacher_id, self.teacher_email, self.group_id)
        self.db.delete_teacher(self.teacher_email)
        result = self.db.select_teacher(self.teacher_email)
        assert result is None  # Убедимся, что преподаватель удалён

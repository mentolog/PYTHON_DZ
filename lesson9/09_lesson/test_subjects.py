import pytest
from subjects2 import SubjectDatabase

class TestSubjectDatabase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Фикстура для подготовки и очистки данных перед и после каждого теста."""
        self.subject_id = 9999
        self.subject_title = 'Mathematics'
        self.new_subject_title = 'Physics'
        
        self.db = SubjectDatabase()

        # Очищаем таблицу перед каждым тестом
        self.db.delete_subject(self.subject_id)
        
        yield  # Тесты будут выполняться здесь
        
        # Очищаем таблицу после теста
        self.db.delete_subject(self.subject_id)

    def test_add_subject(self):
        """Тест на добавление предмета в базу данных."""
        self.db.add_subject(self.subject_id, self.subject_title)
        rows = self.db.select_subject(self.subject_id)
        assert len(rows) > 0
        assert rows[0][1] == self.subject_title  # Индексация по числу, так как результат - кортеж

    def test_update_subject(self):
        """Тест на обновление предмета в базе данных."""
        self.db.add_subject(self.subject_id, self.subject_title)
        self.db.update_subject(self.subject_id, self.new_subject_title)
        rows = self.db.select_subject(self.subject_id)
        assert len(rows) > 0
        assert rows[0][1] == self.new_subject_title  # Индексация по числу

    def test_delete_subject(self):
        """Тест на удаление предмета из базы данных."""
        self.db.add_subject(self.subject_id, self.subject_title)
        self.db.delete_subject(self.subject_id)
        rows = self.db.select_subject(self.subject_id)
        assert len(rows) == 0

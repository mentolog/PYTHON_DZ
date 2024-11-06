import pytest
from teachers2 import TeacherDatabase

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Фикстура для подготовки и очистки данных перед и после каждого теста."""
    teacher_id = 55555
    email = 'unique_teacher@example.com'
    group_id = 55

    # Удаление тестового преподавателя перед каждым тестом
    TeacherDatabase.delete_teacher(email)
    yield teacher_id, email, group_id
    # Удаление тестового преподавателя после каждого теста
    TeacherDatabase.delete_teacher(email)


def test_add_teacher(setup_and_teardown):
    """Тест на добавление преподавателя в базу данных."""
    teacher_id, email, group_id = setup_and_teardown
    TeacherDatabase.add_teacher(teacher_id, email, group_id)
    result = TeacherDatabase.select_teacher(email)
    
    assert result is not None
    assert result[1] == email  # Используем индекс для email
    assert result[2] == group_id  # Используем индекс для group_id


def test_update_teacher(setup_and_teardown):
    """Тест на обновление email преподавателя в базе данных."""
    teacher_id, email, group_id = setup_and_teardown
    new_email = 'updated_teacher@example.com'
    
    # Добавляем и обновляем преподавателя
    TeacherDatabase.add_teacher(teacher_id, email, group_id)
    TeacherDatabase.update_teacher(email, new_email)
    
    # Проверяем, что преподаватель обновлен
    result = TeacherDatabase.select_teacher(new_email)
    assert result is not None
    assert result[1] == new_email  # Используем индекс для нового email


def test_delete_teacher(setup_and_teardown):
    """Тест на удаление преподавателя из базы данных."""
    teacher_id, email, group_id = setup_and_teardown

    # Добавляем и удаляем преподавателя
    TeacherDatabase.add_teacher(teacher_id, email, group_id)
    TeacherDatabase.delete_teacher(email)

    # Проверяем, что преподавателя больше нет
    result = TeacherDatabase.select_teacher(email)
    assert result is None

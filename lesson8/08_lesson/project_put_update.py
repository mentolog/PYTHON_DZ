# test_project_negative.py
import requests
from project_api import ProjectAPI

USER_ID = "5c956cf4-f2a2-4134-808b-46dfe0e7a305"  # ID пользователя с ролью admin

def get_projects():
    """ Получает и выводит список проектов """
    print("Получаем список проектов...")
    response = ProjectAPI.get_projects()
    print("Список проектов:")
    print(response.json())

def run_negative_tests():
    """ Запускает негативные тесты """
    test_create_project_without_title()
    test_get_project_with_invalid_id()
    test_delete_project_with_invalid_id()

def test_create_project_without_title():
    print("Тест 1: Создаем проект без указания названия...")
    payload = {
        "users": {
            USER_ID: "admin",
        }
    }
    response = ProjectAPI.create_project("", USER_ID)  # Передаем пустое название

    # Проверяем статус ответа
    assert response.status_code == 400, f"Ошибка при создании проекта без названия: {response.status_code} - {response.text}"
    print("Проект без названия не был создан, статус: 400.")

def test_get_project_with_invalid_id():
    invalid_project_id = "invalid-id"  # Неверный ID проекта
    print(f"Тест 2: Получаем проект с неверным ID: {invalid_project_id}...")
    response = ProjectAPI.get_project_by_id(invalid_project_id)

    # Проверяем статус ответа
    assert response.status_code == 404, f"Ошибка при получении проекта с неверным ID: {response.status_code} - {response.text}"
    print("Ошибка 404: проект не найден.")

def test_delete_project_with_invalid_id():
    invalid_project_id = "invalid-id"  # Неверный ID проекта
    print(f"Тест 3: Удаляем проект с неверным ID: {invalid_project_id}...")
    payload = {"deleted": True}
    response = ProjectAPI.delete_project(invalid_project_id, payload)

    # Проверяем статус ответа
    assert response.status_code == 404, f"Ошибка при удалении проекта с неверным ID: {response.status_code} - {response.text}"
    print("Ошибка 404: проект не найден для удаления.")

# Запускаем тесты
if __name__ == "__main__":
    get_projects()  # Получаем список проектов перед тестами
    run_negative_tests()  # Запускаем негативные тесты
    get_projects()  # Получаем список проектов после тестов

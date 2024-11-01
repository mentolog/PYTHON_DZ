# test_project_positive.py
import requests
from project_api import ProjectAPI

USER_ID = "5c956cf4-f2a2-4134-808b-46dfe0e7a305"  # ID пользователя с ролью admin

def test_create_and_manage_project():
    print("Шаг 1: Получаем список проектов...")
    initial_projects_response = ProjectAPI.get_projects()
    print("Список проектов до создания нового:")
    print(initial_projects_response.json())

    # Шаг 2: Создаем новый проект
    project_name = "Проект для автотеста"
    print(f"Шаг 2: Создаем проект: {project_name}")
    response = ProjectAPI.create_project(project_name, USER_ID)

    # Проверяем статус ответа
    assert response.status_code == 201, f"Ошибка при создании проекта: {response.status_code} - {response.text}"
    print("Проект успешно создан.")

    # Шаг 3: Получаем список проектов после создания нового
    print("Шаг 3: Получаем список проектов после создания нового...")
    updated_projects_response = ProjectAPI.get_projects()
    print("Список проектов после создания нового:")
    print(updated_projects_response.json())

    # Получаем ID созданного проекта
    project_id = response.json().get("id")
    print(f"ID созданного проекта: {project_id}")

    # Шаг 4: Изменяем имя проекта
    new_project_name = "Измененное имя проекта"
    print(f"Шаг 4: Изменяем имя проекта на: {new_project_name}")
    update_response = ProjectAPI.update_project(project_id, new_project_name)

    # Проверяем статус ответа
    assert update_response.status_code == 200, f"Ошибка при изменении имени проекта: {update_response.status_code} - {update_response.text}"
    print("Имя проекта успешно изменено.")

    # Шаг 5: Получаем список проектов после изменения имени
    print("Шаг 5: Получаем список проектов после изменения имени...")
    final_projects_response = ProjectAPI.get_projects()
    print("Список проектов после изменения имени:")
    print(final_projects_response.json())

    # Шаг 6: Удаляем созданный тестовый проект
    print(f"Шаг 6: Удаляем проект с ID: {project_id}")
    delete_payload = {"deleted": True}  # Передаем параметр deleted
    delete_response = ProjectAPI.delete_project(project_id, delete_payload)

    # Проверяем статус ответа
    assert delete_response.status_code == 200, f"Ошибка при удалении проекта: {delete_response.status_code} - {delete_response.text}"
    print("Проект успешно удален.")

    # Шаг 7: Проверяем, что проект был удален
    print("Шаг 7: Проверяем список проектов после удаления...")
    check_response = ProjectAPI.get_projects()
    print("Список проектов после удаления:")
    print(check_response.json())

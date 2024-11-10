# project_get_by_id.py

import requests
from auth_config import BASE_URL, HEADERS

def get_project(project_id):
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        project = response.json()
        print("Информация о проекте:")
        print(f"Название: {project.get('title')}")
        print(f"ID: {project.get('id')}")
        print(f"Дата создания: {project.get('timestamp')}")
        
        users = project.get("users", {})
        for user_id, role in users.items():
            print(f"Пользователь ID: {user_id}, Роль: {role}")
    
    elif response.status_code == 404:
        error_info = response.json()
        print(f"Ошибка: {error_info.get('statusCode')} - {error_info.get('message')}")
    
    else:
        print(f"Неизвестная ошибка: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Замените на ID проекта, который хотите получить
    project_id = "2a0bb94e-3144-4728-bb23-1f63ec8b0333"
    get_project(project_id)

import requests
import json
from auth_config import BASE_URL, HEADERS

def get_projects():
    url = f"{BASE_URL}/projects"
    
    response = requests.get(url, headers=HEADERS)

    # Проверка статуса ответа
    if response.status_code == 200:
        projects = response.json().get('content', [])
        print(f"Получено проектов: {len(projects)}")
        
        for project in projects:
            title = project.get('title', 'Нет названия')
            timestamp = project.get('timestamp', 'Нет времени')
            project_id = project.get('id', 'Нет ID')
            users = project.get('users', {})

            # Отображаем информацию о проекте
            print(f"ID: {project_id}, Название: {title}, Дата создания: {timestamp}")
            for user_id, role in users.items():
                print(f"  Пользователь ID: {user_id}, Роль: {role}")

    elif response.status_code == 404:
        print("Проекты не найдены (404).")
    else:
        print(f"Произошла ошибка: {response.status_code}")

if __name__ == "__main__":
    get_projects()

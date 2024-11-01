# project_api.py
import requests
import json
from auth_config import BASE_URL, HEADERS

class ProjectAPI:
    @staticmethod
    def create_project(title, user_id):
        url = f"{BASE_URL}/projects"
        payload = {
            "title": title,
            "users": {
                user_id: "admin",  # Используем ID пользователя с ролью admin
            }
        }
        response = requests.post(url, headers=HEADERS, json=payload)  # Используем json для автоматической сериализации
        return response

    @staticmethod
    def get_projects():
        url = f"{BASE_URL}/projects"
        response = requests.get(url, headers=HEADERS)
        return response

    @staticmethod
    def get_project_by_id(project_id):
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=HEADERS)
        return response

    @staticmethod
    def update_project(project_id, new_name):
        url = f"{BASE_URL}/projects/{project_id}"
        payload = json.dumps({"title": new_name})  # Обновлено на "title"
        response = requests.put(url, headers=HEADERS, data=payload)
        return response

    @staticmethod
    def delete_project(project_id, payload):
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.put(url, headers=HEADERS, data=json.dumps(payload))  # Используем PUT для передачи параметров
        return response

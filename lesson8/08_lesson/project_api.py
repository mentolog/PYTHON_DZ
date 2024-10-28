# project_api.py
import requests
import json
from auth_config import BASE_URL, HEADERS


class ProjectAPI:
    @staticmethod
    def create_project(data):
        url = f"{BASE_URL}/projects"
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_project(project_id):
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_project(project_id, data):
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.put(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_project(project_id):
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return response.status_code

# yougile_auth.py
import requests
import json
from yougile_config import BASE_URL, HEADERS


class YougileAPI:
    @staticmethod
    def get_projects():
        url = f"{BASE_URL}/projects"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raises an error for any unsuccessful status codes
        return response.json()


if __name__ == "__main__":
    # Пример вызова для проверки авторизации и получения списка проектов
    try:
        projects = YougileAPI.get_projects()
        print(json.dumps(projects, indent=2, ensure_ascii=False))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

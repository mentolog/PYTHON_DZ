import requests
import json
from auth_config import BASE_URL, HEADERS

def create_project():
    url = f"{BASE_URL}/projects"
    
    # Данные для создания проекта
    payload = {
        "title": "Вася Пупкин Жжот",
        "users": {
            "5c956cf4-f2a2-4134-808b-46dfe0e7a305": "admin",
            }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code == 201:
        print("Проект успешно создан.")
        print("ID созданного проекта:", response.json().get('id'))
    elif response.status_code == 400:
        error_response = response.json()
        print(f"Ошибка: {error_response['statusCode']}, Сообщение: {error_response['message']}")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_project()

import requests
import json

class AuthConfig:
    base_url = "https://ru.yougile.com/api-v2/auth"
    headers = {"Content-Type": "application/json"}

    @staticmethod
    def get_auth_token():
        # Запрашиваем токен с использованием логина и пароля
        payload = {
            "login": "rr21911@yandex.ru",
            "password": "yougile_ranger"
        }
        response = requests.post(AuthConfig.base_url, headers=AuthConfig.headers, json=payload)
        
        # Проверяем успешность авторизации
        if response.status_code == 200:
            token = response.json().get("token")
            if token:
                return token
            else:
                raise ValueError("Token not found in response.")
        else:
            raise Exception(f"Authentication failed with status code: {response.status_code}")

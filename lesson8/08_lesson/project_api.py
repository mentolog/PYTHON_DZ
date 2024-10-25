import requests
from auth_config import AuthConfig

class ProjectAPI:
    base_url = "https://ru.yougile.com/api-v2/projects"
    headers = {
        "Authorization": f"Bearer {AuthConfig.get_auth_token()}",
        "Content-Type": "application/json"
    }

    def create_project(self, payload):
        response = requests.post(self.base_url, headers=self.headers, json=payload)
        return response

    def get_projects(self):
        response = requests.get(self.base_url, headers=self.headers)
        return response

    def update_project(self, project_id, payload):
        response = requests.put(f"{self.base_url}/{project_id}", headers=self.headers, json=payload)
        return response

    def get_project_by_id(self, project_id):
        response = requests.get(f"{self.base_url}/{project_id}", headers=self.headers)
        return response

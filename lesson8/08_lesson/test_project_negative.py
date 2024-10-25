import pytest
from project_api import ProjectAPI

api = ProjectAPI()

def test_create_project_missing_name():
    payload = {
        "description": "A test project without name."
    }
    response = api.create_project(payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_create_project_missing_description():
    payload = {
        "name": "Project without description"
    }
    response = api.create_project(payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_update_project_missing_fields():
    payload = {
        "name": "Project for Missing Fields",
        "description": "Testing update with missing fields"
    }
    create_response = api.create_project(payload)
    project_id = create_response.json()["id"]

    update_payload = {}
    response = api.update_project(project_id, update_payload)
    assert response.status_code == 400
    assert "error" in response.json()

import pytest
from project_api import ProjectAPI

api = ProjectAPI()

def test_create_project():
    payload = {
        "name": "Test Project",
        "description": "A test project for positive testing."
    }
    response = api.create_project(payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_projects():
    response = api.get_projects()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_project():
    payload = {
        "name": "Project for Update",
        "description": "Initial description"
    }
    create_response = api.create_project(payload)
    project_id = create_response.json()["id"]

    update_payload = {
        "name": "Updated Project Name",
        "description": "Updated description"
    }
    update_response = api.update_project(project_id, update_payload)
    assert update_response.status_code == 200
    updated_project = api.get_project_by_id(project_id).json()
    assert updated_project["name"] == "Updated Project Name"

def test_get_project_by_id():
    payload = {
        "name": "Single Project Retrieval",
        "description": "Testing retrieval by ID"
    }
    create_response = api.create_project(payload)
    project_id = create_response.json()["id"]

    response = api.get_project_by_id(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

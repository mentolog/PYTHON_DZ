# test_project_positive.py
import pytest
from project_api import ProjectAPI


@pytest.fixture(scope="module")
def setup_project():
    data = {"name": "Test Project"}
    project = ProjectAPI.create_project(data)
    yield project
    ProjectAPI.delete_project(project["id"])


def test_create_project_positive(setup_project):
    project = setup_project
    assert project["name"] == "Test Project"
    assert "id" in project


def test_get_project_positive(setup_project):
    project = setup_project
    fetched_project = ProjectAPI.get_project(project["id"])
    assert fetched_project["id"] == project["id"]
    assert fetched_project["name"] == "Test Project"


def test_update_project_positive(setup_project):
    project = setup_project
    update_data = {"name": "Updated Test Project"}
    updated_project = ProjectAPI.update_project(project["id"], update_data)
    assert updated_project["name"] == "Updated Test Project"

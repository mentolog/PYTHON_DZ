# test_project_negative.py
import pytest
from project_api import ProjectAPI
import requests


def test_create_project_missing_name():
    data = {}
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        ProjectAPI.create_project(data)
    assert excinfo.value.response.status_code == 400


def test_get_nonexistent_project():
    nonexistent_id = "nonexistent_id"
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        ProjectAPI.get_project(nonexistent_id)
    assert excinfo.value.response.status_code == 404


def test_update_project_missing_name(setup_project):
    project = setup_project
    update_data = {}
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        ProjectAPI.update_project(project["id"], update_data)
    assert excinfo.value.response.status_code == 400

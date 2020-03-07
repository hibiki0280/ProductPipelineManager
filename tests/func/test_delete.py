import pytest

import projects
from projects import Project, Asset

list_entities = [
    Project("aws learning", "learning aws for fun","hsuzuki"),
    Project("Firm project", "Creating Short firm by myself","urata"),
    Project("VR_r&d", "testing virtual reality tools"),
    Project("ML", "Machine learning development","steve"),
    Asset("mokuri", "main character"),
    Asset("noinoi", "sub character","hsuzuki"),
    Asset("landscape_setA", "landscape set for sequence 01","urata"),
    Asset("hammer01A", "hammer for mokuri's prop")
]


@pytest.mark.parametrize("entity",list_entities)
def test_delete(entity):
    project_id = projects.add(entity)
    projects.delete(project_id)
    assert not Project.is_element(entity, projects.list_all())

def test_delete_all(db_with_3_projects):
    projects.delete_all()
    assert projects.count() == 0
    assert projects.list_all() == []


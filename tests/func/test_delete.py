import pytest

import entity_database
from entity_database import Project, Asset, Shot

list_entities = [
    Project("aws learning", "learning aws for fun","hsuzuki"),
    Project("Firm project", "Creating Short firm by myself","urata"),
    Project("VR_r&d", "testing virtual reality tools"),
    Project("ML", "Machine learning development","steve"),
    Asset("mokuri", "main character"),
    Asset("noinoi", "sub character","hsuzuki"),
    Asset("landscape_setA", "landscape set for sequence 01","urata"),
    Asset("hammer01A", "hammer for mokuri's prop"),
    Shot("S1C010"),
    Shot("S1C020"),
    Shot("S2C030"),
]


@pytest.mark.parametrize("entity",list_entities)
def test_delete(entity):
    project_id = entity_database.add(entity)
    entity_database.delete(project_id)
    assert not Project.is_element(entity, entity_database.list_all())

def test_delete_all(db_with_3_projects):
    entity_database.delete_all()
    assert entity_database.count() == 0
    assert entity_database.list_all() == []


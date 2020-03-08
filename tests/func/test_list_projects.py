import pytest

import entity_database
from entity_database import Project, Asset, Shot

def test_list_all_returns_valid_entity(db_with_1_prj_and_some_items):
    list_entities = entity_database.list_all()
    assert isinstance(list_entities, list)
    for entity in list_entities:
        assert isinstance(entity, (Project, Asset, Shot)) 
    
@pytest.mark.parametrize("ItemType",
    ["Asset", "Shot"]
)
def test_list_items_returns_valid_items(db_with_1_prj_and_some_items, ItemType):
    project_id = db_with_1_prj_and_some_items
    list_items = entity_database.list_items(project_id, ItemType)
    assert isinstance(list_items, list)
    for entity in list_items:
        assert isinstance(entity, (Asset, Shot)) 
    
        
def has_unique_ids(list_projects) -> bool:
    ids = []
    for prj in list_projects:
        prj_id = prj.id.value()
        if prj_id in ids:
            return False
        else:
            ids.append(prj_id)
            continue

    return True

def test_count_returns_valid_num(db_with_3_projects):
    assert isinstance(entity_database.count(), int)

def test_count_returns_correct_count(db_with_3_projects):
    added_projects = db_with_3_projects
    assert entity_database.count() == len(added_projects)


import pytest

import projects
from projects import Project, Asset

def test_list_all_returns_valid_entity(db_with_1_prj_9_asset):
    list_entities = projects.list_all()
    assert isinstance(list_entities, list)
    for entity in list_entities:
        assert isinstance(entity, (Project,Asset)) 
    
        
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
    assert isinstance(projects.count(), int)

def test_count_returns_correct_count(db_with_3_projects):
    added_projects = db_with_3_projects
    assert projects.count() == len(added_projects)


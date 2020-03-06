import pytest

import projects
from projects import ProjectEntity

def test_list_projects_returns_valid_projects(db_with_3_projects):
    list_projects = projects.list_projects()
    assert isinstance(list_projects, list)
    for prj in list_projects:
        assert isinstance(prj, ProjectEntity)

def test_list_projects_has_unique_ids(db_with_3_projects):
    list_projects = projects.list_projects()
    assert has_unique_ids(list_projects)
    
        
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


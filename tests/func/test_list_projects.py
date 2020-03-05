import pytest

import projects
from projects import Project

def test_list_projects_returns_valid_projects(db_with_3_projects):
    list_projects = projects.list_projects()
    assert isinstance(list_projects, list)
    for prj in list_projects:
        assert isinstance(prj, Project)

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


def equivalent(p1, p2) -> bool:
    p1_d = p2._asdict()
    p2_d = p2._asdict()

    for field in p1._fields:
        if field != "id":
            if p1_d[field] != p2_d[field]:
                return False
            else:
                continue

    return True
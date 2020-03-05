import pytest

import projects
from projects import Project

list_projects = [
    Project("aws learning", "learning aws for fun","hsuzuki"),
    Project("Firm project", "Creating Short firm by myself","urata"),
    Project("VR_r&d", "testing virtual reality tools"),
    Project("ML", "Machine learning development","steve")
]


@pytest.mark.parametrize("project",list_projects)
def test_delete(project):
    project_id = projects.add(project)
    projects.delete(project_id)
    assert not is_element(project, projects.list_projects())

def test_delete_all(db_with_3_projects):
    projects.delete_all()
    assert projects.count() == 0
    assert projects.list_projects() == []


def is_element(p1,list_projects) -> bool:
    for p2 in list_projects:
        if equivalent(p1,p2):
            return True
    else:
        return False

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
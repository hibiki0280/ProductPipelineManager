import pytest

import projects
from projects import ProjectEntity

list_projects = [
    ProjectEntity("aws learning", "learning aws for fun","hsuzuki"),
    ProjectEntity("Firm project", "Creating Short firm by myself","urata"),
    ProjectEntity("VR_r&d", "testing virtual reality tools"),
    ProjectEntity("ML", "Machine learning development","steve")
]


@pytest.mark.parametrize("project",list_projects)
def test_delete(project):
    project_id = projects.add(project)
    projects.delete(project_id)
    assert not ProjectEntity.is_element(project, projects.list_projects())

def test_delete_all(db_with_3_projects):
    projects.delete_all()
    assert projects.count() == 0
    assert projects.list_projects() == []


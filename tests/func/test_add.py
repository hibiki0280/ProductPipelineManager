import pytest

import projects
from projects import ProjectEntity


def test_add_returns_valid_id():
    project = ProjectEntity("alita", "project")
    prj_id = projects.add(project)
    print("Project id: %s", prj_id)
    assert isinstance(prj_id, int)

def test_added_project_has_id_set():
    project = ProjectEntity("alita", "project")
    prj_id = projects.add(project)

    resistered_project = projects.get(prj_id)

    print(resistered_project._asdict())

    assert resistered_project.id.value() == prj_id

@pytest.mark.parametrize("project",
    [ProjectEntity("VR_r&d", "testing virtual reality tools"),
    ProjectEntity("aws learning", "learning aws for fun","hsuzuki"),
    ProjectEntity("Firm project", "Creating Short firm by myself","urata"),
    ProjectEntity("ML", "Machine learning development","steve")]
)
def test_add(project):
    project_id = projects.add(project)
    project_resistered = projects.get(project_id)
    print("project_id= ", project_id)
    assert ProjectEntity.equivalent(project, project_resistered)



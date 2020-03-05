import pytest

import projects
from projects import Project


def test_add_returns_valid_id():
    project = Project("alita", "project")
    prj_id = projects.add(project)
    print("Project id: %s", prj_id)
    assert isinstance(prj_id, int)

def test_added_project_has_id_set():
    project = Project("alita", "project")
    prj_id = projects.add(project)

    resistered_project = projects.get(prj_id)

    print(resistered_project._asdict())

    assert resistered_project.id.value() == prj_id

@pytest.mark.parametrize("project",
    [Project("VR_r&d", "testing virtual reality tools"),
    Project("aws learning", "learning aws for fun","hsuzuki"),
    Project("Firm project", "Creating Short firm by myself"),
    Project("ML", "Machine learning development")]
)
def test_add(project):
    project_id = projects.add(project)
    project_resistered = projects.get(project_id)
    print("\r\n",project_resistered)
    print("\r\n",project)
    print("project_id= ", project_id)
    assert equivalent(project, project_resistered)



def equivalent(p1, p2):
    p1_d = p2._asdict()
    p2_d = p2._asdict()

    for field in p1._fields:
        if field != "id":
            if p1_d[field] != p2_d[field]:
                return False
            else:
                continue

    return True
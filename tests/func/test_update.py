import pytest

import projects
from projects import Project

@pytest.mark.parametrize(("project,project_updated"),
    [(Project("VR_r&d", "testing virual reality tools"), Project("VR_r&d", "testing virual reality tools")),
    (Project("aws learning", "learning aws for fun","hsuzuki"),Project("gcp learning", "learning gcp for fun","hsuzuki")),
    ]
)
def test_update(project, project_updated):
    project_id = projects.add(project)
    # project_resistered = projects.get(project_id)
    projects.update(project_id, project_updated)
    project_resistered = projects.get(project_id)
    assert equivalent(project_updated, project_resistered)


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
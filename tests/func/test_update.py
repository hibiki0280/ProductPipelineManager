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
    projects.update(project_id, project_updated)
    project_resistered = projects.get(project_id)
    assert Project.equivalent(project_updated, project_resistered)

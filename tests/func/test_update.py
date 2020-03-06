import pytest

import projects
from projects import ProjectEntity

@pytest.mark.parametrize(("project,project_updated"),
    [(ProjectEntity("VR_r&d", "testing virual reality tools"), ProjectEntity("VR_r&d", "testing virual reality tools")),
    (ProjectEntity("aws learning", "learning aws for fun","hsuzuki"),ProjectEntity("gcp learning", "learning gcp for fun","hsuzuki")),
    ]
)
def test_update(project, project_updated):
    project_id = projects.add(project)
    projects.update(project_id, project_updated)
    project_resistered = projects.get(project_id)
    assert ProjectEntity.equivalent(project_updated, project_resistered)

import pytest

import entity_database
from entity_database import Project, Asset, Shot

@pytest.mark.parametrize(("project,project_updated"),
    [(Project("VR_r&d", "testing virual reality tools"), Project("VR_r&d", "testing virual reality tools")),
    (Project("aws learning", "learning aws for fun","hsuzuki"), Project("gcp learning", "learning gcp for fun","hsuzuki")),
    (Asset("assetA", "", ""), Asset("assetA", "this is asset A", "hibiki suzuki")),
    (Shot("s01", "", ""), Shot("shot001", "this is shot 001", "hibiki suzuki")),
    ]
)
def test_update(project, project_updated):
    project_id = entity_database.add(project)
    entity_database.update(project_id, project_updated)
    project_resistered = entity_database.get(project_id)
    assert Project.equivalent(project_updated, project_resistered)
id
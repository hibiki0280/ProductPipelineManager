import pytest
from uuid import UUID
import projects
from projects import Project, Asset, Shot


def test_add_returns_valid_id():
    project = Project("alita", "project")
    prj_id = projects.add(project)
    assert isinstance(prj_id, str)

def test_added_project_has_id_set():
    project = Project("alita", "project")
    prj_id = projects.add(project)

    resistered_project = projects.get(prj_id)

    assert resistered_project.id.value() == prj_id

@pytest.mark.parametrize("project",
    [Project("VR_r&d", "testing virtual reality tools"),
    Project("aws learning", "learning aws for fun","hsuzuki"),
    Project("Firm project", "Creating Short firm by myself","urata"),
    Project("ML", "Machine learning development","steve")]
)
def test_add_project(project):
    project_id = projects.add(project)
    project_resistered = projects.get(project_id)
    assert Project.equivalent(project, project_resistered)


def test_add_to_project_returns_valid_id(single_project, single_asset):
    prj_id = projects.add(single_project)
    asset_id = projects.add_to_project(single_asset, prj_id)
    assert isinstance(asset_id, str)

def test_added_asset_has_id_and_project_id_set(single_project, single_asset):
    prj_id = projects.add(single_project)
    asset_id = projects.add_to_project(single_asset, prj_id)
    
    resistered_asset = projects.get(asset_id)

    assert resistered_asset.id.value() == asset_id
    assert resistered_asset.project_id.value() == prj_id

@pytest.mark.parametrize("asset",
    [Asset("mokuri", "main character"),
    Asset("noinoi", "sub character","hsuzuki"),
    Asset("landscape_setA", "landscape set for sequence 01","urata"),
    Asset("hammer01A", "hammer for mokuri's prop"),
    Shot("shotA","test shot"),
    Shot("shotB","test shot"),
    ]
)
def test_add_asset_or_shot_to_project(asset, single_project):
    project_id = projects.add(single_project)
    asset_id = projects.add_to_project(asset, project_id)
    
    resistered_asset = projects.get(asset_id)

    
    assert Asset.equivalent(asset, resistered_asset)

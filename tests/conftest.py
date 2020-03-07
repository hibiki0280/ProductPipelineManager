import pytest

import projects
from projects import Project, Asset


@pytest.fixture(autouse=True)
def initialized_database(tmpdir):
    projects.start_database(str(tmpdir))

    yield

    projects.stop_database()

@pytest.fixture()
def single_project():
    return Project("testproject", "this is a test project.", "testauthor")
    
@pytest.fixture()
def single_asset():
    return Asset("testassset", "this is a test asset.", "testauthor")

@pytest.fixture()
def setup_few_projects():
    return (
        Project("Capture Animals", "try to capture rare animals", "Jhonson"),
        Project("PUBG", "pvp shooting game in which up 100 players fight in a battle royale","Player Unknown"),
        Project("MineCraft","3d sandbox game which is one of the most popular game in the world", )
    )

@pytest.fixture
def db_with_3_projects(setup_few_projects):
    for prj in setup_few_projects:
        projects.add(prj)
    return setup_few_projects

@pytest.fixture()
def setup_few_assets():
    return (
        Asset("CharacterA"),
        Asset("CharacterB"),
        Asset("CharacterC"),
        Asset("PropD"),
        Asset("PropE"),
        Asset("PropF"),
        Asset("EnvironmentG"),
        Asset("EnvironmentH"),
        Asset("EnvironmentQ"),
    )

@pytest.fixture
def db_with_1_prj_9_asset(single_project, setup_few_assets):
    prj_id = projects.add(single_project)
    for asset in setup_few_assets:
        projects.add_to_project(asset, prj_id)
    

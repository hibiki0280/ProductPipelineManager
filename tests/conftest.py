import pytest

import projects
from projects import Project


@pytest.fixture(autouse=True)
def initialized_database(tmpdir_factory):
    projects.start_database(str(tmpdir_factory.getbasetemp()))

    yield

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
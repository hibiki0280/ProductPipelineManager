import pytest

import projects
from projects import ProjectEntity


@pytest.fixture(autouse=True)
def initialized_database(tmpdir):
    projects.start_database(str(tmpdir))

    yield

    projects.stop_database()

@pytest.fixture()
def setup_few_projects():
    return (
        ProjectEntity("Capture Animals", "try to capture rare animals", "Jhonson"),
        ProjectEntity("PUBG", "pvp shooting game in which up 100 players fight in a battle royale","Player Unknown"),
        ProjectEntity("MineCraft","3d sandbox game which is one of the most popular game in the world", )
    )

@pytest.fixture
def db_with_3_projects(setup_few_projects):
    for prj in setup_few_projects:
        projects.add(prj)
    return setup_few_projects
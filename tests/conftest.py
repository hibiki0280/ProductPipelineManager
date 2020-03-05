import pytest

import projects
from projects import Project


@pytest.fixture(autouse=True, scope="session")
def initialized_database(tmpdir_factory):
    projects.start_database(str(tmpdir_factory.getbasetemp()))

    yield

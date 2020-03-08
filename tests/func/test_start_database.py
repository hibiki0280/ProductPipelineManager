import os
import pytest

from entity_database import start_database

@pytest.fixture(scope="session")
def start_database_in_tempdir(tmpdir_factory):
    db_dir = tmpdir_factory.mktemp("db")
    start_database(str(db_dir))

    return db_dir

def test_database_file_exists(start_database_in_tempdir):
    db_dir = start_database_in_tempdir
    assert os.path.exists(os.path.join(db_dir, "entity_database.db"))

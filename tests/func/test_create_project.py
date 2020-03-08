import os

import entity_database
from entity_database import Project
import project_filesystem_handler as fs

def test_create_project(single_project, tmpdir):
    root_path = str(tmpdir.mkdir("projects"))
    id = fs.create_project(single_project, root_path)
    resistered_project = entity_database.get(id)

    assert isinstance(id, str)
    assert resistered_project.id.value() == id

    expect_dir = os.path.join(root_path, single_project.name.value())
    print(os.listdir(root_path))
    assert os.path.exists(expect_dir)

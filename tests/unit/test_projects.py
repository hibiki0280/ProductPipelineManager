from projects import Project

def test_asdict():
    prj = Project("test_project", "This is a test project.", id=12)
    dict = prj._asdict()
    expected = {
        "name": "test_project",
        "description": "This is a test project.",
        "id": 12
    }
    assert dict == expected

    
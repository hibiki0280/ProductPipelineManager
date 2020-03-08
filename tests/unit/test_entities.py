import pytest
from entity_database import Project, Asset, Shot

@pytest.mark.parametrize("entity, expected",[
    (Project("test_project", "This is a test project.", id=12),
    {
        "name": "test_project",
        "description": "This is a test project.",
        "id": 12
    }),
    (Asset("test_asset", "this is a test asset.", id=5),
    {
        "name": "test_asset",
        "description": "this is a test asset.",
        "id": 5
    }),
    (Shot("shot001", id=123),
    {
        "name": "shot001",
        "id": 123
    })
])
def test_asdict(entity, expected):
    dict = entity._asdict()
    assert dict == expected



    
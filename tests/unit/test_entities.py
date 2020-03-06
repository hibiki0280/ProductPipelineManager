import pytest
from projects import ProjectEntity, AssetEntity

@pytest.mark.parametrize("entity, expected",[
    (ProjectEntity("test_project", "This is a test project.", id=12),
    {
        "name": "test_project",
        "description": "This is a test project.",
        "id": 12
    }),
    (AssetEntity("test_asset", "this is a test asset.", id=5),
    {
        "name": "test_asset",
        "description": "this is a test asset.",
        "id": 5
    }

    )
])
def test_asdict(entity, expected):
    dict = entity._asdict()
    assert dict == expected



    
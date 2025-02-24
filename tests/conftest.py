import pytest
from models import Base

@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base

@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [("user", [
        {
            "id": 1,
            "name": "Kevin"
        },
        {
            "id": 2,
            "name": "Dwight"
        }
    ])]
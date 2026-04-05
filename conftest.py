import pytest
from services.user_service import UserService


@pytest.fixture(scope="session")
def user_service():
    return UserService()

import pytest
from example import User

@pytest.fixture
def user():
    """готовый пользователь с валидными данными"""
    user = User("Anna", "old@example.com")
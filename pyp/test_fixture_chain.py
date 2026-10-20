import pytest
from models.model import User

@pytest.fixture
def base_user():
    print(">>> 1. Создаём base_user")
    return User("Base", 20, "base@example.com")

@pytest.fixture
def adult_user(base_user):
    """Зависит от base_user"""
    print(">>> 2. Модифицируем base_user в adult_user")
    base_user.age=25
    return base_user

@pytest.fixture
def email_verified_user(adult_user):
    """Зависит от adult_user"""
    print(">>> 3. Модифицируем adult_user в email_verified_user")
    adult_user.change_email("verified@example.com")
    return adult_user

def test_chain(email_verified_user):
    assert email_verified_user.name == "Base"
    assert email_verified_user.age == 25
    assert email_verified_user.email == "verified@example.com"

import pytest

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_email(self, new_email):
        self.email = new_email
        return self.email
    
@pytest.fixture
def user():
    """готовый пользователь с валидными данными"""
    return User("Anna", "old@example.com")

@pytest.fixture
def user_factory():
    """фабрика создаёт пользователя с любыми данными"""
    def _make(name="test", email="email@email.com"):
        return User(name, email)
    return _make
    

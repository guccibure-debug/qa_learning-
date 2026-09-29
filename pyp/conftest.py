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

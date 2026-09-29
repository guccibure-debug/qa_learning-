import pytest
from models.model import User


def test_user_name(user):
    assert user.name == "Anna"

def test_user_email(user):
    assert user.email == "old@example.com"

def test_user_change_mail(user):
    user.change_email("new@example.com")
    assert user.email == "new@example.com"
    
@pytest.fixture
def user_with_log():
    print ("\n>>> создаём пользователя")
    user = User("Test", 25, "test@example.com")
    yield user
    print (">>> удаляем пользователя")

def test_with_teardown(user_with_log):
    assert user_with_log.name == "Test"
import pytest

@pytest.fixture
def user():
    """Создаёт тестового пользователя."""
    return User("Anna", "old@example.com")


def test_user_creation(user):        # 👈 имя аргумента = имя фикстуры
    assert user.name == "Anna"


def test_user_can_change_email(user):
    user.change_email("new@example.com")
    assert user.email == "new@example.com"
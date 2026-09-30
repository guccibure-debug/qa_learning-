import pytest
from example import add


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_add_mixed():
    with pytest.raises(TypeError):
        add(5, "2")


def test_change_email(user):                # 👈 фикстура из conftest.py
    with pytest.raises(ValueError):
        user.change_email("new@example.com")
        user.email == "new@example.com"


def test_change_email_invalid(user):        # 👈 фикстура
    with pytest.raises(ValueError):
        user.change_email("bad-email")


def test_user_creation(user):               # 👈 фикстура
    assert user.name == "Anna"
    assert user.email == "old@example.com"

def test_multiple_users(user_factory):
    u1 = user_factory("Alice", "alice@example.com")
    u2 = user_factory("Bob", "bob@example.com")
    assert u1.name == "Alice"
    assert u2.name == "Bob"
    assert u1.email != u2.email
import pytest

@pytest.fixture
def alice():
    return {"id":1, "name": "Alice", "mail": "alice@examle.com"}

def test_user_has_email(alice):
    assert "@" in alice["mail"]

def test_user_id_is_int(alice):
    assert isinstance(alice["id"], int)

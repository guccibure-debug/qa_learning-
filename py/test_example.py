import pytest
from example import add
from example import User

def test_add_positive ():
    assert add(1,2) == 3

def test_add_negative():
    assert add(-1,-2) == -3

def test_add_mixed():
    assert add(5,2) == 5

def test_add_string_and_number_raises():
    with pytest.raises(TypeError)   :
        add("a",1)

def test_user_can_change_email():
    # Arrange
    user = User("Anna", "old@example.com")

    # Act
    user.change_email("new@example.com")

    # Assert
    assert user.email == "new@example.com"


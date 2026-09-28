import pytest
from example import add

def test_add_positive ():
    assert add(1,2) == 3

def test_add_negative():
    assert add(-1,-2) == -3

def test_add_mixed():
    with pytest.raises(TypeError):
        add(5,"2") 

def test_change_email(user):
    user.change_email("kostya@mail.ru")
    assert user.email == "kostya@mail.ru"

def test_change_email_error(user):
    with pytest.raises(ValueError):
        user.change_email("kotya")

def test_add_string_and_number_raises():
    with pytest.raises(TypeError)   :
        add("a",1)

def test_user_can_change_email(user):

    # Act
    user.change_email("new@example.com")

    # Assert
    assert user.email == "new@example.com"


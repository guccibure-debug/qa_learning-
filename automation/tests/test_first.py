from basics.user import User
import pytest

def test_addition():
    assert 2+2==4

def test_substraction():
    assert 5-2==3

@pytest.mark.xfail(reason="демонстрация падения")
def test_will_fail():
    assert 5+3==1

def test_change_email_invalid_message():
    user = User("Иван", 25, "old@example.com")
    with pytest.raises(ValueError, match="некорректный"):
        user.change_email("bad-email")
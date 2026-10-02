import pytest
from models.model import User

@pytest.fixture
def user_from_param(request):
    """фикстура которая получает данные из параметра"""
    name, age, mail = request.param
    return User(name, age, mail)

@pytest.mark.parametrize(
    "user_from_param",
    [
        ("Anna", 25, "anna@example.com"),
        ("Bob", 17, "bob@example.com"),
        ("Charlez", 65, "charlez@example.com"),
    ],
    indirect=True
)

def test_user_adult_status(user_from_param):
    """проверяем is_adult для разных пользователей"""
    excepted = user_from_param.age >= 18
    assert (user_from_param.age>=18)==excepted
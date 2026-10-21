import pytest
from models.model import User

@pytest.fixture
def user(request):
    """фикстура которая берёт данные из параметра"""
    name, age, mail = request.param
    return User(name,age,mail)

@pytest.mark.parametrize(
    "user",
    [
        ("Anna", 17, "anna@example.com"),
        ("Bob", 18, "bob@example.com"),
        ("Charlie", 65, "charlie@example.com"),
    ], 
    indirect=True,
    ids=
    [
        "minor-anna",
        "boundary-bob",
        "senior-charlie",
    ],
)
def test_user_adult_status(user):
    expected = user.age >=18
    assert user.is_adult() == expected
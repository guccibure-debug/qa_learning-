import pytest
from models.model import User
from automation.basics.basics import multiply

@pytest.fixture
def user(request):
    """фикстура которая берёт данные из параметра"""
    name, age, mail = request.param
    return User(name,age,mail)

@pytest.mark.parametrize(
    "user",
    [
        ("Anna", 17, "anna@example.com"),
            pytest.param(
                ("Bob", 18, "bob@example.com"),
                marks=pytest.mark.xfail(reason="Известный баг"),
                id="known-bag-zero",
                ),
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


@pytest.mark.parametrize("age", [17,18,65])
@pytest.mark.parametrize("email_valid", [True, False])
def test_user(age, email_valid):
    """проверяем что пользователь проходит валидацию"""
    email = "user@example.com" if email_valid else "user@@bad"
    if email_valid and age >= 18:
        assert "@" in email and age >= 18
    else:
        with pytest.raises(AssertionError):
            assert email_valid and age >= 18

@pytest.fixture
def user_from_param(request):
    """фикстура берёт данные из параметра"""
    name, age, mail = request.param
    return User(name, age, mail)

@pytest.mark.parametrize(
    "user",
    [
        ("kostya", 21, "kostya@example.com"),
        ("masha", 21, "krasnova@example.com"),
    ],
    indirect=True,
    ids=["kostya-good", "masha-broke"],
)

def test_user_adult_status(user):
    expected = user.age >= 18
    assert user.is_adult() == expected


@pytest.mark.parametrize("a", [1,2,-3])
@pytest.mark.parametrize("b", [2,0,5])
def test_multiply_combinations(a,b):
    assert multiply(a,b)==b*a
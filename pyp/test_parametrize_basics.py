import pytest
from models.model import User

@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (0, False),
        (65, True)
    ],
    ids=[
        "minor-17",
        "boundary-18",
        "baby-0",
        "senior-65",
    ],
)
def test_is_adult(age,expected):
    user = User("Иван", age, "mail@mail.ru")
    assert user.is_adult() == expected
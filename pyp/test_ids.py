import pytest

@pytest.fixture
def age():
    return 25

@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (25, True),
        (65, True),
        (0, False)
    ],
    ids=[
        "17-minor",
        "18-boundary",
        "25-adult",
        "65-senior",
        "0-baby",
    ],
)
def test_is_adult(age, expected):
    """проверяет границы is_adult"""
    assert (age>=18) == expected
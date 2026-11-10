import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # адрес вашего API


@pytest.fixture(scope="session")
def api_client():
    """Сессия, переиспользуемая во всех API-тестах."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    session.base_url = BASE_URL          # удобный шорткат
    yield session
    session.close()


def test_get_user_status(api_client):
    response = api_client.get(
        f"{api_client.base_url}/users/1",
        timeout=10,
    )
    assert response.status_code == 200, response.text
    assert response.json()["id"] == 1
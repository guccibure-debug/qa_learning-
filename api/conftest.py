import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # адрес вашего API

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def api_client():
    """Сессия, переиспользуемая во всех API-тестах."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()


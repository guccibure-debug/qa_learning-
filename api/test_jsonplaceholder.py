import requests
import certifi
import pytest

print(certifi.where())

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_status():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

@pytest.mark.api
def test_get_user_body():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert data["id"] == 1  
    assert "name" in data
    assert "email" in data
    assert "@" in data["email"]

@pytest.mark.api
def test_get_user_content_type():
    response = requests.get(f"{BASE_URL}/users/1")
    assert "application/json" in response.headers["Content-Type"]

@pytest.mark.api
def test_get_user_response_time():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.elapsed.total_seconds() < 2 #не больше 2 секунд

@pytest.mark.api
def test_get_user_status(api_client, base_url):
    response = api_client.get(f"{base_url}/users/1", timeout=10)
    assert response.status_code == 200, response.text
    assert response.json()["id"] == 1
    assert response.status_code == 200, response.text
    assert response.json()["id"] == 1

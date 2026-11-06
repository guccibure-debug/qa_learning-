import requests
import certifi

print(certifi.where())

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_status():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_get_user_body():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
    assert "@" in data["email"]

def test_get_user_content_type():
    response = requests.get(f"{BASE_URL}/users/1")
    assert "application/json" in response.headers["Content-Type"]

def test_get_user_response_time():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.elapsed.total_seconds() < 2 #не больше 2 секунд


import pytest

from api.conftest import api_client

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def new_post_payload():
    return {
        "title": "мой тестовый пост",
        "body": "текст поста",
        "userID": "1",
    }

def test_create_post(api_client, new_post_payload):
    responce = api_client.post(f"{BASE_URL}/posts", json=new_post_payload)
    assert responce.status_code == 201   #проверка что создалось
    data = responce.json()
    assert data["title"] == new_post_payload["title"]
    assert "id" in data   #сервер выдал id

def test_get_post(api_client):
    responce = api_client.get(f"{BASE_URL}/posts/1")
    assert responce.status_code == 200
    assert responce.json()["id"] == 1

def test_update_post(api_client):
    payload = {"id": 1, "title": "обновленный", "body": "новый текст", "userId": 1}
    responce = api_client.put(f"{BASE_URL}/posts/1", json=payload)
    assert responce.status_code == 200
    assert responce.json()["title"] == "обновленный"

def test_delete_post(api_client):
    responce = api_client.delete(f"{BASE_URL}/posts/1")
    assert responce.status_code == 200

def test_get_nonexistent_post(api_client):
    responce = api_client.get(f"{BASE_URL}/posts/999999")
    assert responce.status_code == 404

@pytest.mark.parametrize(
    "user_id, expected_name",
    [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch"),
    ],
)

def test_user_names(api_client, user_id, expected_name):
    responce = api_client.get(f"{BASE_URL}/users/{user_id}")
    assert responce.status_code == 200
    assert responce.json()["name"] == expected_name

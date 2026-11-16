import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def new_post_payload():
    return {
        "title": "мой тестовый пост",
        "body": "текст поста",
        "userID": "1",
    }

def test_create_post(api_client, new_post_payload):
    response = api_client.post(f"{BASE_URL}/posts", json=new_post_payload)
    assert response.status_code == 201   #проверка что создалось
    data = response.json()
    assert data["title"] == new_post_payload["title"]
    assert "id" in data   #сервер выдал id

def test_get_post(api_client):
    response = api_client.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_post(api_client):
    payload = {"id": 1, "title": "обновленный", "body": "новый текст", "userId": 1}
    response = api_client.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "обновленный"

def test_delete_post(api_client):
    response = api_client.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_nonexistent_post(api_client):
    response = api_client.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404

@pytest.mark.parametrize(
    "user_id, expected_name",
    [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch"),
    ],
    ids=["user-1", "user-2", "user-3"],
)

def test_user_names(api_client, user_id, expected_name):
    response = api_client.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == expected_name

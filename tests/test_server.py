from src.aws_flask.server import app
import pytest

new_user = {
    "name": "Elai",
    "country": "Israel",
    "cat_amount": 2,
}


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client 

@pytest.fixture
def setup_db(client):
    client.get("/api/reset")
    yield
    client.get("/api/reset")


def test_get_latest_user(client, setup_db):
    response = client.get("/api/users?latest=true")
    assert response.status_code == 200
    assert response.json == {
        "name": "Marcin",
        "country": "Polska",
        "cat_amount": 3,
    }


def test_add_user(client, setup_db):
    response = client.post("/api/users", json=new_user)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json == {"response": "New User added successfully."}


def test_get_all_users(client, setup_db):
    response = client.post("/api/users", json=new_user)
    assert response.status_code == 200
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json == [
        {"cat_amount": 3, "country": "Polska", "name": "Marcin"},
        {"cat_amount": 2, "country": "Israel", "name": "Elai"},
    ]


def test_non_existant(client, setup_db):
    response = client.get("/api/non-existent")
    assert response.status_code == 404

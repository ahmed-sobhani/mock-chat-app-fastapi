from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_interaction():
    payload = { "title": "new test interaction" }
    response = client.post("/interactions/", json=payload)
    assert response.status_code == 200

def test_invalid_created_interaction():
    payload = { "title": None }
    response = client.post("/interactions/", json=payload)
    assert response.status_code == 422

def test_get_interaction():
    response = client.get("/interactions/")
    assert response.status_code == 200




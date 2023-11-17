from fastapi.testclient import TestClient
from app.main import app
from app.message.schemas import RoleEnum
client = TestClient(app)

def get_interaction_id():
    """Find/Create an interaction to retrieve interaction_id"""
    interaction_id = 0

    interactions = client.get("/interactions/")
    assert interactions.status_code == 200
    if interactions:
        interaction_id = interactions.json()[0]["id"]
    else:
        payload = { "title": "test interaction" }
        interaction = client.post("/interactions/", json=payload)
        assert interaction.status_code == 200
        interaction_id = interaction.json()["id"]
    
    return interaction_id

def test_create_message():

    interaction_id = get_interaction_id()
    
    """Test adding new message to an interactions"""
    payload = { "content": "new message content", "role": RoleEnum.humam }
    response = client.post(f"/interaction/{interaction_id}/messages", json=payload)
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["interaction_id"] == interaction_id
    assert response.json()[1]["interaction_id"] == interaction_id
    assert response.json()[0]["role"] == RoleEnum.humam
    assert response.json()[1]["role"] == RoleEnum.ai

def test_create_message_invalid_interaction():
    interaction_id = 0

    payload = { "content": "new message content", "role": RoleEnum.humam }
    response = client.post(f"/interaction/{interaction_id}/messages", json=payload)
    assert response.status_code == 404

def test_create_message_invalid_role():

    interaction_id = get_interaction_id()

    payload = { "content": "new message content", "role": "person" }
    response = client.post(f"/interaction/{interaction_id}/messages", json=payload)
    assert response.status_code == 422

def test_create_message_without_content():

    interaction_id = get_interaction_id()

    payload = { "role": "person" }
    response = client.post(f"/interaction/{interaction_id}/messages", json=payload)
    assert response.status_code == 422

def test_get_interaction_messages():
    interaction_id = get_interaction_id()

    response = client.get(f"/interaction/{interaction_id}/messages")
    assert response.status_code == 200

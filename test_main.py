from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat/", json={"prompt": "안녕"})
    assert response.status_code == 200
    print(response.json())

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def sample_payload():
    return {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }

def test_addition_endpoint(sample_payload):
    response = client.post("/api/v1/addition/add", json=sample_payload)
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["batchid"] == "id0101"
    assert response_data["response"] == [3, 7]
    assert response_data["status"] == "completed"
    assert "started_at" in response_data
    assert "completed_at" in response_data

def test_addition_endpoint_invalid_payload():
    invalid_payload = {
        "batchid": "id0102",
        "payload": [[1, 2], "invalid"]
    }
    response = client.post("/api/v1/addition/add", json=invalid_payload)
    assert response.status_code == 422

import pytest
from fastapi.testclient import TestClient
from app.main import Input_model, app

client = TestClient(app)

def test_addition_endpoint():

    valid_input = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition/", json=valid_input)
    assert response.status_code == 200
    assert response.json()["batchid"] == "id0101"
    assert response.json()["status"] == "complete"

    invalid_input = {
        "batchid": "id0101",
        "payload": "not_a_input_lists"
    }
    response = client.post("/addition/", json=invalid_input)
    assert response.status_code == 422
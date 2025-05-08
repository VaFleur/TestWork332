from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_delete_transactions():
    response = client.delete("/transactions/", headers={"Authorization": "ApiKey your_api_key"})
    assert response.status_code == 200
    assert response.json()["message"] == "Transactions deleted"
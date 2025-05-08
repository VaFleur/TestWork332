from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_statistics():
    response = client.get("/statistics/", headers={"Authorization": "ApiKey your_api_key"})
    assert response.status_code == 200
    data = response.json()
    assert "total_transactions" in data
    assert "average_transaction_amount" in data
    assert "top_transactions" in data
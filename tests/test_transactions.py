from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = TestClient(app)

def test_create_transaction():
    transaction_data = {
        "transaction_id": "test123",
        "user_id": "user_001",
        "amount": 100.0,
        "currency": "USD",
        "timestamp": "2024-12-12T12:00:00"
    }
    response = client.post("/transactions/", json=transaction_data, headers={"Authorization": f"{API_KEY}"})
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_duplicate_transaction():
    transaction_data = {
        "transaction_id": "test123",
        "user_id": "user_001",
        "amount": 100.0,
        "currency": "USD",
        "timestamp": "2024-12-12T12:00:00"
    }
    response = client.post("/transactions/", json=transaction_data, headers={"Authorization": f"{API_KEY}"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Transaction ID already exists"
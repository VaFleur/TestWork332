from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = TestClient(app)

def test_get_statistics():
    response = client.get("/statistics/", headers={"Authorization": f"{API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert "total_transactions" in data
    assert "average_transaction_amount" in data
    assert "top_transactions" in data
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = TestClient(app)

def test_delete_transactions():
    response = client.delete("/transactions/", headers={"Authorization": f"{API_KEY}"})
    assert response.status_code == 200
    assert response.json()["message"] == "Transactions deleted"
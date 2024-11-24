import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_process_receipt(client):
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            { "shortDescription": "Mountain Dew 12PK", "price": "6.49" }
        ],
        "total": "6.49"
    }
    response = client.post('/receipts/process', json=receipt)
    assert response.status_code == 200
    assert "id" in response.json

def test_get_points(client):
    receipt_id = "nonexistent-id"
    response = client.get(f'/receipts/{receipt_id}/points')
    assert response.status_code == 404

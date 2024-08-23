# tests/test_dbapi.py

import pytest
from src.dbapi import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_data(client):
    """Test GET request to the /data endpoint."""
    response = client.get('/data')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Assuming the response is a list of records


def test_post_data(client):
    """Test POST request to the /data endpoint."""
    new_data = {
        "id": 129,
        "company": "Green Valley Electronics",
        "last_name": "Schneider",
        "first_name": "Anna",
        "phone": "+49 30 44 68 1122",
        "address": "Kurfürstendamm 26",
        "city_and_state": "Berlin",
        "postal_code": "10719",
        "country": "Germany"
    }
    response = client.post('/data', json=new_data)
    assert response.status_code == 201
    assert response.json['message'] == "Data added successfully"

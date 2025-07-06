import pytest
from app import app  # import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"making my hands dirty on cicd with docker and k8s" in response.data

def test_healthz(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {"status": "ok"}

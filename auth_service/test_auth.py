import pytest
from app import app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
def test_login_success(client):
    response = client.post('/login', json={'username': 'user1', 'password': 'password123'})
    assert response.status_code == 200
    assert 'token' in response.json
def test_login_failure(client):
    response = client.post('/login', json={'username': 'user1', 'password': 'wrongpass'})
    assert response.status_code == 401
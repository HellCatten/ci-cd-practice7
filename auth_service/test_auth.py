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
    
    # 1. Успешный вход второго зарегистрированного пользователя
def test_login_user2_success(client):
    response = client.post('/login', json={'username': 'user2', 'password': 'securepass'})
    assert response.status_code == 200
    assert response.json.get('token') == 'fake-jwt-token'

# 2. Отправка запроса с отсутствующим полем пароля (проверка на неполные данные)
def test_login_missing_password(client):
    response = client.post('/login', json={'username': 'user1'})
    assert response.status_code == 401
    assert response.json.get('message') == 'Invalid credentials'

# 3. Проверка запрета GET-запроса на эндпоинт авторизации (должен вернуть 405)
def test_login_get_method_not_allowed(client):
    response = client.get('/login')
    assert response.status_code == 405
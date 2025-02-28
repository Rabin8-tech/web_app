# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login(client):
    """Test if login works"""
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert b"Invalid email or password" not in response.data

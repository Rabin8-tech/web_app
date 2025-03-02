# tests/test_app.py
import pytest
from app import app, mysql

@pytest.fixture
def client():
    """Fixture to set up the Flask test client"""
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_db():
    """Fixture to initialize the database (mock or real)"""
    cursor = mysql.connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), email VARCHAR(100), password VARCHAR(100));")
    yield cursor
    cursor.execute("DROP TABLE IF EXISTS user;")
    mysql.connection.commit()

# Unit Test for the Login route
def test_login_page(client, init_db):
    """Test that the login page returns a 200 status"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_login_valid(client, init_db):
    """Test valid login"""
    # Add a test user
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", ('Test User', 'test@example.com', 'testpassword'))
    mysql.connection.commit()

    # Test login with valid credentials
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'testpassword'})
    assert response.status_code == 302  # Should redirect to dashboard after successful login
    assert b"Login successful" in response.data

import pytest
from config.api import app

@pytest.fixture()
def client():
    return app.test_client()

def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json['hello'] == 'world'
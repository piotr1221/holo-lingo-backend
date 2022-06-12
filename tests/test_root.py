from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    res = client.get('/')
    assert res.status_code  == 200
    assert res.json() == {'api_version': 'v1'}
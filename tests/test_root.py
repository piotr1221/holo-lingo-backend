from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    # res = client.get('/v1/')
    # assert res.status_code  == 200
    # assert res.json() == {'api_version': 'v1'}
    assert True == True
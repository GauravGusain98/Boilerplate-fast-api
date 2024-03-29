from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from FastAPI in Docker!"}

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_returns_greeting():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from my DevOps pet project!"
    }


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

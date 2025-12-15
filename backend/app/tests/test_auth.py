from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post(
        "/auth/login",
        params={
            "username": "admin",
            "password": "adminpass",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password():
    response = client.post(
        "/auth/login",
        params={
            "username": "admin",
            "password": "wrongpass",
        },
    )

    assert response.status_code == 401


def test_login_invalid_username():
    response = client.post(
        "/auth/login",
        params={
            "username": "unknown",
            "password": "adminpass",
        },
    )

    assert response.status_code == 401

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_protected_no_token():
    response = client.get("/protected")
    assert response.status_code == 401

def test_protected_with_token():
    login = client.post(
        "/auth/login",
        params={"username": "admin", "password": "adminpass"},
    )
    token = login.json()["access_token"]

    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["user"] == "admin"

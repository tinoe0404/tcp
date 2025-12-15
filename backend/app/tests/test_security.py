from app.core.security import hash_password, verify_password


def test_password_verification():
    password = "secret123"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False

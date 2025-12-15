from app.core.security import hash_password, verify_password
from app.models.user import User


def test_password_hashing():
    password = "secret123"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True


def test_user_fields():
    user = User(
        username="admin",
        full_name="System Admin",
        hashed_password=hash_password("adminpass"),
        is_admin=True,
    )

    assert user.username == "admin"
    assert user.is_admin is True
    assert user.is_active is True

from app.core.roles import UserRole


def test_user_roles_exist():
    assert UserRole.ADMIN.value == "admin"
    assert UserRole.STAFF.value == "staff"

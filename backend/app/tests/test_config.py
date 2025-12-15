from app.core.config import get_settings


def test_default_settings():
    settings = get_settings()
    assert settings.app_name == "TCP POS Backend"
    assert settings.env == "development"
    assert settings.debug is True

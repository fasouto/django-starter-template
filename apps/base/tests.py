from unittest.mock import patch

import pytest
from django.core.exceptions import ImproperlyConfigured

from config.startup import PLACEHOLDER_SECRET_KEYS, require_real_secret_key


@pytest.mark.django_db
def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_200(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_health_check_hides_database_error_details(client):
    with patch("django.db.connection.cursor", side_effect=Exception("secret-db-host.internal refused")):
        response = client.get("/health/")
    assert response.status_code == 500
    assert response.json() == {"status": "error", "database": "error"}
    assert "secret-db-host" not in response.content.decode()


@pytest.mark.parametrize("key", sorted(PLACEHOLDER_SECRET_KEYS))
def test_placeholder_secret_key_is_refused_in_production(settings, key):
    settings.DEBUG = False
    settings.SECRET_KEY = key
    with pytest.raises(ImproperlyConfigured, match="openssl rand -hex 32"):
        require_real_secret_key()


def test_real_secret_key_is_accepted_in_production(settings):
    settings.DEBUG = False
    settings.SECRET_KEY = "a-long-random-value-0123456789abcdef"  # noqa: S105
    require_real_secret_key()


@pytest.mark.parametrize("key", sorted(PLACEHOLDER_SECRET_KEYS))
def test_placeholder_secret_key_is_allowed_in_debug(settings, key):
    settings.DEBUG = True
    settings.SECRET_KEY = key
    require_real_secret_key()

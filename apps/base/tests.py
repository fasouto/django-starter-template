import pytest


@pytest.mark.django_db
def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_200(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


from app import app


def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"ShopSphere" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_products():
    response = app.test_client().get("/api/products")
    assert response.status_code == 200
    assert len(response.json) == 3


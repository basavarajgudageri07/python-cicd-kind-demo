
from app.main import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Welcome to Python CI/CD Demo!"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_info():
    client = app.test_client()

    response = client.get("/info")

    assert response.status_code == 200
    assert response.json["application"] == "python-cicd-kind-demo"


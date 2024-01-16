import pytest
from flask import Flask, make_response
from src.app_blueprint import app_blueprint

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)

    return app.test_client()

def test_get_flag(client):
    response = client.get("/flag")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Contenu du drapeau"

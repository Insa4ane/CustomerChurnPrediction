from unittest.mock import patch
from fastapi.testclient import TestClient
import numpy as np
import pytest
from api.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "status": "sukces",
        "wiadomosc": "API dziala w nowym folderze!"
    }


def test_columns_endpoint(client):
    response = client.post("/columns")

    assert response.status_code == 200
    assert response.json() == {"status": "sukces"}


@patch('api.server.PIPELINE_MODEL')
def test_predict_churn_success(mock_model, client):
    mock_model.predict.return_value = np.array([1])

    payload = {"age": 30, "tenure_months": 12, "plan": "premium"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "sukces"
    assert body["result"] == "1"

    called_df = mock_model.predict.call_args[0][0]
    assert len(called_df) == 1
    assert called_df.iloc[0]["plan"] == "premium"


@patch('api.server.PIPELINE_MODEL')
def test_predict_churn_returns_zero(mock_model, client):
    mock_model.predict.return_value = np.array([0])

    response = client.post("/predict", json={"age": 45})

    assert response.status_code == 200
    assert response.json()["result"] == "0"


@patch('api.server.PIPELINE_MODEL')
def test_predict_churn_model_error(mock_model, client):
    mock_model.predict.side_effect = ValueError("bad input data")

    response = client.post("/predict", json={"foo": "bar"})

    assert response.status_code == 400
    assert "bad input data" in response.json()["detail"]
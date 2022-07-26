from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_calculator_root():
    response = client.get("/calculator/")
    assert response.status_code == 200
    assert response.json() == {"Location": "The Calculation Router"}


def test_get_calculator_assessmentQuick_decline():
    arv = 100000
    pp = 50000
    rc = 25000

    response = client.get(f"/calculator/assessmentQuick?arv={arv}&pp={pp}&rc={rc}")
    assert response.status_code == 200
    assert response.json() == {
        "arv": arv,
        "pp": pp,
        "rc": rc,
        "max_amount": 45000,
        "max_request": 70000,
        "pre_approved": False,
        "max_amount_ratio": 0.45,
        "max_request_ratio": 0.7,
    }


def test_get_calculator_assessmentQuick_approve():
    arv = 200000
    pp = 50000
    rc = 25000

    response = client.get(f"/calculator/assessmentQuick?arv={arv}&pp={pp}&rc={rc}")
    assert response.status_code == 200
    assert response.json() == {
        "arv": arv,
        "pp": pp,
        "rc": rc,
        "max_amount": 115000,
        "max_request": 70000,
        "pre_approved": True,
        "max_amount_ratio": 0.575,
        "max_request_ratio": 0.35,
    }

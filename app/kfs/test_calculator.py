# python -m pytest -v --cov

import pytest
from .calculator import max_loan_amount, max_loan_request, calc_assessment_quick

# Test max_loan_amount
def test_max_loan_amount_default_modifier():
    arv = 100000
    repairCosts = 25000
    value = max_loan_amount(arv, repairCosts)
    assert value == 45000


# test max_loan_amount with a different arv modifier
def test_max_loan_amount_passed_in_modifier():
    arv = 100000
    repairCosts = 25000
    value = max_loan_amount(arv, repairCosts, 0.9)
    assert value == 65000


# Test max_loan_amount
def test_max_loan_request_default_modifier():
    purchasePrice = 100000
    repairCosts = 25000
    value = max_loan_request(purchasePrice, repairCosts)
    assert value == 115000


# test max_loan_amount with a different arv modifier
def test_max_loan_request_passed_in_modifier():
    purchasePrice = 100000
    repairCosts = 25000
    value = max_loan_request(purchasePrice, repairCosts, 0.8)
    assert value == 105000


def test_calc_assessment_quick_decline():
    arv = 100000
    pp = 50000
    rc = 25000
    result = calc_assessment_quick(arv, pp, rc)
    assert result["max_amount"] == 45000
    assert result["max_request"] == 70000
    assert result["pre_approved"] == False
    assert result["max_amount_ratio"] == 0.45
    assert result["max_request_ratio"] == 0.7


def test_calc_assessment_quick_approve():
    arv = 200000
    pp = 50000
    rc = 25000
    result = calc_assessment_quick(arv, pp, rc)
    assert result["max_amount"] == 115000
    assert result["max_request"] == 70000
    assert result["pre_approved"] == True
    assert result["max_amount_ratio"] == 0.575
    assert result["max_request_ratio"] == 0.35

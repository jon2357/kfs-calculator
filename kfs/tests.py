# python -m pytest -v --cov

import pytest
from .calculator import max_loan_amount, max_loan_request

#Test max_loan_amount
def test_max_loan_amount_default_modifier():
    arv = 100000
    repairCosts = 25000
    value = max_loan_amount(arv, repairCosts)
    assert value == 45000

# test max_loan_amount with a different arv modifier 
def test_max_loan_amount_passed_in_modifier():
    arv = 100000
    repairCosts = 25000
    value = max_loan_amount(arv, repairCosts,.9)
    assert value == 65000
    
    


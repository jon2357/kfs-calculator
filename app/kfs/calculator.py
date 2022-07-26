def max_loan_amount(arv: float, repairCosts: float, arvProportionModifier: float = 0.7):
    """
    Quick calculation for determining the max amount we will fund on a deal.
    arv = After Repair Value in USD.
    arvProportionModifier = what proportion of the ARV will we fund up to (default is .7).
    repairCosts = How much is the rehab in USD.
    """
    return (arv * arvProportionModifier) - repairCosts


def max_loan_request(
    purchasePrice: float, repairCosts: float, purchasePriceModifier: float = 0.9
):
    """
    Quick calculation for determining the max amount that can be requested for funding .
    purchasePrice = How much the property can be acquired for.
    purchasePriceModifier = what proportion of the purchase price we are willing to loan on (default is .9).
    repairCosts = How much is the rehab in USD.
    """
    return (purchasePrice * purchasePriceModifier) + repairCosts


def calc_assessment_quick(arv: float, pp: float, rc: float):
    """
    Quick calculation for determining the max amount that can be requested for funding .
    arv = After Repair Value
    pp = Purchase Price
    rc = Repair Costs (Estimated Rehab Costs )
    """
    pre_approved = False  # Default to a False Pre-approval
    max_amount = max_loan_amount(arv, rc, 0.7)  # use ARV modified of 70%
    max_amount_ratio = max_amount / arv
    max_request = max_loan_request(pp, rc, 0.9)  # use Purchase Price Modified of 90%
    max_request_ratio = max_request / arv
    if max_amount >= max_request:
        pre_approved = True

    return {
        "max_amount": max_amount,
        "max_amount_ratio": max_amount_ratio,
        "max_request": max_request,
        "max_request_ratio": max_request_ratio,
        "pre_approved": pre_approved,
    }

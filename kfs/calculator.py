
def max_loan_amount(arv: float, repairCosts: float, arvProportionModifier: float = .7):
    '''
    Quick calculation for determining the max amount we will fund on a deal.
    arv = After Repair Value in USD.
    arvProportionModifier = what proportion of the ARV will we fund up to (default is .7).
    repairCosts = How much is the rehab in USD.
    '''
    return (arv*arvProportionModifier) - repairCosts



def max_loan_request(purchasePrice:float, repairCosts: float, purchasePriceModifier: float = .9):
    '''
    Quick calculation for determining the max amount that can be requested for funding .
    purchasePrice = How much the property can be acquired for.
    purchasePriceModifier = what proportion of the purchase price we are willing to loan on (default is .9).
    repairCosts = How much is the rehab in USD.
    '''
    return (purchasePrice * purchasePriceModifier) + repairCosts
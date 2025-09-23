import math
def firstBracket(amt):
    '''
    firstBracket calculates the amount of tax owed
    on amt in the first federal tax bracket

    amt - Positive float
    Returns - a positive float

    Examples
    firstBracket(60000) -> 8319.375
    firstBracket(57375) -> 8319.375
    firstBracket(40000) -> 5800
    '''
    if amt > 57375:
        return 57375*.145
    else:
        return amt*.145

def secondBracket(amt):
    taxable = amt - 57375
    if taxable < 0:
        return 0
    if taxable >= 57375:
        return 57375*.205
    return taxable*.205

def thirdBracket(amt):
    taxable = amt - 57375 - 57375
    if taxable < 0:
        return 0
    if taxable >= 63132:
        return 63132*0.26
    return taxable*.26

def fourthBracket(amt):
    taxable = amt - 57375 - 57375 - 63132
    if taxable < 0:
        return 0
    if taxable >= 75532:
        return 75532*.29
    return taxable*.29

def fifthBracket(amt):
    taxable = amt - 253414
    if taxable < 0:
        return 0
    return taxable*.33

def bracket(amt, size, deductions, rate):
    '''
    bracket calculates the amount of tax owed given a Canadian
            citizen earned $amt, the size of this bracket is size,
            the sum of the brackets smaller than this is deductions
            and the taxrate of this bracket is rate

    amt - a positive number
    size - a positive number
    deductions - a positive number
    rate - a float between 0 and 1

    Examples
        bracket(40000, 57375, 0, 0.145) -> 5800
        bracket(163000, 63132, 114750, 0.26) -> 12545
        bracket(400000,math.inf, 253414, 0.33) -> 48373.38
    '''
    taxable = amt - deductions
    if taxable < 0:
        return 0
    if taxable >= size:
        return size*rate
    return taxable*rate

def incomeTax(amt):
    '''
    incomeTax calculates the total amount of federal income
              tax owed by a Canadian citizen who made amt
              gross taxable CAD in this year

    amt - a positive number
    returns - a positive number

    Examples:
        incomeTax(40000) -> 5800.00
        incomeTax(163000) -> 32626.25
        incomeTax(60000) -> 8857.5
    '''
    return (firstBracket(amt) + secondBracket(amt) +
            thirdBracket(amt) + fourthBracket(amt) +
            fifthBracket(amt)) 

def incomeTax2(amt):
    return (bracket(amt, 57375, 0, 0.145) +
            bracket(amt, 57375, 57375, 0.205) +
            bracket(amt, 63132 , 114750, 0.26) +
            bracket(amt, 75532, 177882, 0.29) +
            bracket(amt, math.inf, 253414, 0.33))

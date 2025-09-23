
def logFloor(n):
    '''
    logFloor returns the floor(log_10(n))

    n - a number >= 1
    returns - an integer
    '''
    assert n >= 1
    if n < 10:
        return 0
    return 1 + logFloor(n/10)

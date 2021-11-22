def sum2(a):
    """
    Sum 2 to any input
    a: integer
    returns: integer
    """
    if a < 0:
        raise ValueError('a is negative')
    return a + 2

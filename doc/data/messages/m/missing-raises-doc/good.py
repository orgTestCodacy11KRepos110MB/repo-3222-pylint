def integer_sum(a: int, b: int):
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    :raises ValueError: One of the parameters is not an integer.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Function supports only integer parameters.')
    return a + b

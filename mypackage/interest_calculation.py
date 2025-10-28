""" module for interest calculations"""

def simple_interest(prin, ny, roi):
    """
    calculating simple interest
    :param prin: principal amount
    :param ny: numbers of years
    :param roi: rate of interest
    :return: SI,total amount"""
    si = prin * ny * roi/100
    amount = prin + si
    return  si,amount
def compound_interest(prin, t, roi):
    """

    calculating simple interest
    :param prin: principal amount
    :param ny: numbers of years
    :param roi: rate of interest
    :return: total amount"""
    amount = prin * ((1+(roi/100)) ** t)
    return amount

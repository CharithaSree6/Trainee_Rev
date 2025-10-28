""" Area circumference of SQ, RECT,CIRCLE"""
from math import pi

def area_of_square(side):
    """

    :param side: side of square
    :return: area
    """
    return side * side


def area_of_circle(rad):
    return pi * rad* rad


def area_of_rect(len, brd):
    return len * brd

def cir_of_circle(rad):
    return 2 * pi * rad

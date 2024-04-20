"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-04-18"
-------------------------------------------------------
"""
from functions import square_pyramid

base = float(input("Enter length of the base of the pyramid: "))
height = float(input("Enter perpendicular height of the pyramid: "))

calc = square_pyramid(base, height)

print(f"height, area, and volume of a square pyramid: {calc}")


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """

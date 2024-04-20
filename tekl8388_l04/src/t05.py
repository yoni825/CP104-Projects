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
from functions import right_triangle

adj = float(input("Enter adjacent length: "))
opp = float(input("Enter length of opposite: "))

calc = right_triangle(adj, opp)
# since the results are in a list of more than 2 values we need to format it
formatted_calc = tuple(float(f"{x:.2f}") for x in calc)
print(
    f"The hypotenuse, perimeter, and area of a right triangle: {formatted_calc}")


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

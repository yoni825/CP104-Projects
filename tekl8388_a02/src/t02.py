"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-03-13"
-------------------------------------------------------
"""
prod = int(input("Enter a positive digit number: "))

first = prod//10  # so you would only get the first value
second = prod % 10  # so you would only get the second value

calc = first * second

print(f"The product of the digits of {prod} is {calc}")


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

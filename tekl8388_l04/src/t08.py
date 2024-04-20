"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-04-19"
-------------------------------------------------------
"""
from functions import computer_costs

test = computer_costs(1399, 87, 8.5)

# Format each value in the tuple to two significant digits
formatted_test = tuple(f"{value:.2f}" for value in test)

print(formatted_test)


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

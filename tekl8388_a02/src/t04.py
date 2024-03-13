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

cake = int(input("Number of pieces of cake: "))
goers = int(input("Number of party-goers: "))

calc1 = cake//goers
calc2 = cake % goers

print("Pieces of cake per party-goers: ", calc1)
print("Pieces of cake left over: ", calc2)


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

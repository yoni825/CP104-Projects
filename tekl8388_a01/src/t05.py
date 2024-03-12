"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-03-12"
-------------------------------------------------------
"""
prince = float(input("Principal: $"))
interest = float(input("Interest (%): "))
years = int(input("Number of years: "))
times = int(input("Number of times interest compounded per year: "))

interest_rate = 1 + ((interest/100)/times)

amount = prince * (interest_rate**(years*times))

print(f"Balance = ${amount}")


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

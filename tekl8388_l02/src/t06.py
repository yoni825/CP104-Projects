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
prince = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
int1 = int(input("Yearly interest rate (%): "))

rate = int1/100  # interest converted from percentage
months = years * 12

monthly_rate = rate/12

calc1 = monthly_rate*(1+monthly_rate) ** months
calc2 = (1+monthly_rate)**months - 1
calc3 = prince * (calc1/calc2)

print(f"The monthly payments are: $ {calc3}")


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

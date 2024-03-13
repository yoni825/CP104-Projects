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
food = float(input("Food Charge: $"))
sale = float(input("Sales Tax in (%): "))
tip = float(input("Tip in (%): "))

tip1 = tip/100 * food
sale1 = sale/100 * food
calc = food + tip1 + sale1
print(
    f"""
Cost of meal: 
Subtotal : $ {food}
     Tax : $ {sale1}
     Tip : $ {tip1}
-------------------      
    Total : {calc}

""")


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

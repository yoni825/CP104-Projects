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
ANNUAL_TAX = 18.50

sale = int(input("Enter the total sales: $"))

calc = (ANNUAL_TAX/100) * sale

print(f"""  
Projected Tax Report
------------------------------
Total sales:   $ {sale:.2f}
Annual tax:    % {ANNUAL_TAX}
------------------------------
Tax:           $ {calc:.2f}
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

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
date = int(input("Enter a date in the format DDMMYYYY: "))

year = date % 10000
month1 = (date // 10000)
month2 = (month1 % 100)
date = date // 1000000

print(f"The reformed date: {year}/{month2}/{date}")


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

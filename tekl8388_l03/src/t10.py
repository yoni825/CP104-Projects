"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))


print(f"The date: {year}/{month:02d}/{day:02d}")
# the :02d is a fill the 0 represents what will fill the empty space if condition is not met
# the 2 is the amount of values there should be (if you don't want zero to fill up space)
# the d indicates this format applies to integers


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

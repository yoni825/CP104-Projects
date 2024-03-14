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
total_minutes = int(input("Enter number of minutes: "))

days = total_minutes // (60 * 24)
remaining_minutes = total_minutes % (60 * 24)
hours = remaining_minutes // 60
minutes = remaining_minutes % 60

print(
    f"There are {days} days, {hours} hours, and {minutes} minutes in {total_minutes} minutes")


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

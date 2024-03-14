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

sec = int(input("Enter number of seconds: "))

hours = sec // 3600
remaining_seconds = sec % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(
    f"There are {hours} hours, {minutes} minutes, and {seconds} seconds in {sec} seconds")


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

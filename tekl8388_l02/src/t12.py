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

total_seconds = int(input("Number of seconds: "))

SECONDS_IN_AN_MINUTE = 60
seconds_in_an_hour = SECONDS_IN_AN_MINUTE * 60
seconds_in_a_day = seconds_in_an_hour * 24

days = total_seconds // seconds_in_a_day
remaining_seconds = total_seconds % seconds_in_a_day

hours = remaining_seconds // seconds_in_an_hour
remaining_seconds = remaining_seconds % seconds_in_an_hour

minutes = remaining_seconds // SECONDS_IN_AN_MINUTE
seconds = remaining_seconds % SECONDS_IN_AN_MINUTE

print(f"Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}")


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

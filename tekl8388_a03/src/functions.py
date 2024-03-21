"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-03-21"
-------------------------------------------------------
"""
ACRE = 43560
GRAVITY = 9.8


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = 0

    if (square_feet >= 0):
        acres = square_feet / ACRE

    else:
        acres

    return acres


def lawn_mowing(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mowing(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    time_minutes = (length * width) / speed

    return time_minutes


def date_extraction(date_number_format):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extraction(date_number_format)
    -------------------------------------------------------
    Parameters:
        date_number_format - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number_format % 10000
    month_day = date_number_format // 10000
    month = month_day // 100
    day = month_day % 100

    return year, month, day


def fraction_multiplier(number1, denom1, number2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: num, denom, product = fraction_multiplier(number1, denom1, number2, denom2)
    -------------------------------------------------------
    Parameters:
        number1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        number2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        num - numerator of the resulting fraction (int)
        denom - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    num = number1 * number2
    den = denom1 * denom2
    product = num / den

    return num, den, product


GRAVITY = 9.8
# formula distance = 1/2gt^2


def falling_distance(time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    distance = (GRAVITY * (time**2)) * 0.5

    return distance

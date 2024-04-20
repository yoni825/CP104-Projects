"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yonathan Tekle
ID:      169068388
Email:  tekl8388@mylaurier.ca
__updated__ = "2024-04-19"
-------------------------------------------------------
"""
import math  # we used this so we cant get the complete value of pi
# we set things to zero so if the function returns a weird value it will print out 0 instead of that weird number


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    diam = 0

    if (radius >= 0):
        diam = 2 * radius

    return diam


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    circ = 0

    if (radius >= 0):
        # the math.pi is the same as 3.14 except it uses all the values of pi
        circ = 2 * math.pi * radius

    return circ


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    ar = 0

    if (radius >= 0):
        ar = math.pi * radius ** 2
    return ar


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh = math.sqrt((base/2)**2 + height**2)
    area = (base ** 2) + 2 * base * math.sqrt((base**2)/4 + height**2)
    vol = (base ** 2) * (height/3)

    return sh, area, vol


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp = 0
    per = 0
    area = 0

    if (adjacent > 0, opposite > 0):
        hyp = math.sqrt(adjacent**2 + opposite**2)
        per = adjacent + opposite + math.sqrt(adjacent**2+opposite**2)
        area = (adjacent * opposite) * 0.5

    return hyp, per, area


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    radius = math.sqrt(s1**2 + s2**2)

    diam = 2 * radius

    circ = 2 * math.pi * radius

    area = math.pi * radius**2

    return radius, diam, circ, area


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00

    total = (NICKEL * nickels) + (DIME * dimes) + (QUARTER *
                                                   quarters) + (LOONIE * loonies) + (TOONIE * toonies)

    return total


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    pre_commission_cost = computer_cost * computers_bought
    commission = (commission_percent / 100)
    total_cost = pre_commission_cost * (1 + commission)

    # output
    return pre_commission_cost, total_cost


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    num = num1 * num2
    den = den1 * den2
    product = num / den
    return num, den, product


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    x = x2-x1
    y = y2-y1
    slp = y/x
    return slp


FREEZING_POINT = 32


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    if (celsius >= -273):
        fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


FREEZING_POINT = 32


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    if (fahrenheit >= -459):
        celsius = (fahrenheit - 32) * 5/9
    return celsius


SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    DAY = 86400
    HOUR = 3600
    MINUTE = 60

    days = 0
    hours = 0
    minutes = 0

    if (seconds < 3600) & (seconds > 0):
        minutes = seconds // MINUTE
        days = 0
        hours = 0

    elif (seconds == 3600):
        days = 0
        hours = 1
        minutes = 60

    elif (seconds < 86400):
        hours = seconds // HOUR
        minutes = seconds // MINUTE
        days = 0

    elif (seconds == 86400):
        days = 1
        hours = 24
        minutes = 1440

    else:
        days = seconds // DAY
        hours = seconds // HOUR
        minutes = seconds // MINUTE

    return days, hours, minutes


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    # constants
    MIN_TO_SEC = 60
    HOUR_TO_SEC = 60 * 60
    # calc
    days = initial_seconds // (24 * HOUR_TO_SEC)
    remaining_seconds = initial_seconds % (24 * HOUR_TO_SEC)
    hours = remaining_seconds // HOUR_TO_SEC
    remaining_seconds %= HOUR_TO_SEC
    minutes = remaining_seconds // MIN_TO_SEC
    seconds = remaining_seconds % MIN_TO_SEC

    return days, hours, minutes, seconds

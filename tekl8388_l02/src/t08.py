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

height = float(input("Enter your height (m): "))
mass = float(input("Enter your weight (kg): "))
upperBMILimit = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

bmi = mass / (height**2)

bmiPrime = bmi / upperBMILimit

print("Body Mass Index (kg/m^2) = ", bmi)
print("BMI Prime = ", bmiPrime)


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

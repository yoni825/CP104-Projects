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
PI = 3.14

diameter = float(input("Diameter of container base (cm): "))
height = float(input("Height of container (cm): "))
costOfMaterial = float(input("Cost of material ($/cm^2): "))
amount = int(input("Number of containers: "))

radius = diameter / 2

areaOfSides = 2 * PI * radius * height
areaOfBase = PI * (radius**2)

totalSurfaceArea = areaOfBase + areaOfBase + areaOfBase


costOfOne = totalSurfaceArea / costOfMaterial
costOfAmount = costOfOne * amount

print("The total cost of one container is $", costOfOne)
print("The total cost of all container is $", costOfAmount)


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

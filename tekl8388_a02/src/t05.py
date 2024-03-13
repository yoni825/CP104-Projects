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

lenght = float(input("Foundation lenght (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall = float(input("Wall height (m): "))
cost_concrete = float(input("Cost of concrete ($/m^3): "))
cost_bricks = float(input("Cost of bricks ($/m^2): "))

concrete_need = lenght * width * height

cost_of_conrete = concrete_need * cost_concrete

bricks_need = ((width * wall)*2) + ((lenght * wall)*2)

cost_of_bricks = bricks_need * cost_bricks

total = cost_of_bricks + cost_of_conrete


print(f"Concrete needed for foundation (m^3): {concrete_need:.2f}")
print(f"Cost of concrete: ${cost_of_conrete:.2f}")
print(f"Bricks needed for walls (m^2): {bricks_need:.2f}")
print(f"Cost of bricks: ${cost_of_bricks:.2f}")
print(f"Total cost: ${total:.2f}")


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

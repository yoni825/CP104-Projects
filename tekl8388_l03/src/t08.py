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
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

calc = dirt + gravel + sand

print(f'''
Material      Cubic Metres
Dirt           {dirt:7.1f}
Gravel         {gravel:7.1f}
Sand           {sand:7.1f}
Total          {calc:7.1f}

''')


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

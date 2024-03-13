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
MILK_FOR_SIX = 4  # cups
BUTTER_FOR_SIX = 8  # tablespoons
FLOUR_FOR_SIX = 0.5  # cups
SALT_FOR_SIX = 2  # teaspoons

# Ask the user for the number of servings
servings_wanted = int(input("Enter servings of Mac & Cheese: "))

# Calculate the ingredients needed for the desired number of servings
milk_needed = (MILK_FOR_SIX / 6) * servings_wanted
butter_needed = (BUTTER_FOR_SIX / 6) * servings_wanted
flour_needed = (FLOUR_FOR_SIX / 6) * servings_wanted
salt_needed = (SALT_FOR_SIX / 6) * servings_wanted

# Print the ingredients list
print(f"\n{servings_wanted} servings of Mac & Cheese requires:")
print(f"milk (cups): {milk_needed:.2f}")
print(f"butter (tablespoons): {butter_needed:.2f}")
print(f"flour (cups): {flour_needed:.2f}")
print(f"salt (teaspoons): {salt_needed:.2f}")


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

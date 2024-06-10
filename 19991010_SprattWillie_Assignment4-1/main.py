"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
numChars = 8
color = "gold"
woodType = "oak"



# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

# Write assignment and if statements here as appropriate.

numCharsQuestion = int(input("How many characters would there be: "))
woodTypeQuestion = input("Would you like oak or pine: ")
colorQuestion = input("What color would you like: ")

def woodShop(numCharsQuestion, woodTypeQuestion, colorQuestion):
    charge = 35.00

    if numCharsQuestion > 5:
        charge = charge + (numCharsQuestion - 5) * 4

    if woodTypeQuestion != "pine":
        charge = charge + 20

    if colorQuestion == "black" or colorQuestion == "white":
        charge = charge
    else:
        charge += 15

    # Output Charge for this sign.
    return "The charge for this sign is $" + str(charge)


print(woodShop(numCharsQuestion, woodTypeQuestion, colorQuestion))
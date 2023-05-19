"""
First, provide a docstring to include your name and the date and whatever remarks you think are useful and appropriate to describe your module

Inga Miller May 19, 2023
Project 2: Travel to Latvia (explore capital city Riga old town (which was built in 12 century) while there)


"""

import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# define some functions

def get_area_of_Riga_Old_Town(length, width):
    """
    Return area of a Old Town in the capital city of Latvia Riga given the length and width of the lot.


    """

    # Use a try / except / finally block when something 
    
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
get_area_of_Riga_Old_Town(2, 3)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print("your code here")

def get_area_of_Riga_Old_town(length, width):
    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None
print(f"Riga Old Town area: {get_area_of_Riga_Old_Town(2, 3)}")

def Riga_Old_Town_area(length, width):
    area = length * width
    print(f"Riga Old Town area: {area}")
Riga_Old_Town_area(2,3)

#sq miles in Old Town Riga to explore
def Riga_Old_Town_area_per_day(area,numdays):
    Riga_Old_Town_area = area * numdays
    print(f"You have 2 days: {get_area_of_Riga_Old_Town} sq mi")
Riga_Old_Town_area(2,3)

def Riga_Old_Town_area_round(radius):
    area_round = math.pi * (radius ** 2)
    print(f"Round Riga Old Town area: {area_round}")
Riga_Old_Town_area_round(10)

#Permutations and combinations
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")



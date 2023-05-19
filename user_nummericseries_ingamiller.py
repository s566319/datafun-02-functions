"""
First, provide a docstring to include your name and the date and whatever remarks you think are useful and appropriate to describe your module

Inga Miller May 19, 2023
Project 2: Practice working with classes using OOP- Buildings to visit while in Old Town Riga, Latvia

"""

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)
class building:

    # class attribute
    name = ""
    age = 0

# create building1 object
building1 = building()
building1.name = "St Peters Church"
building1.age = 814

# create another object building2
building2 = building()
building2.name = "Powder Tower"
building2.age = 1475

# access attributes
print(f"{building1.name} is {building1.age} years old")
print(f"{building2.name} is {building2.age} years old")
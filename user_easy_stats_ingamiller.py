"""
First, provide a docstring to include your name and the date and whatever remarks you think are useful and appropriate to describe your module

Inga Miller May 19, 2023
Project 2: High temperatures in Riga, Latvia for the month of June


"""

import statistics

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# define a variable with some univariant data 
# (one varabile, many readings)
y_temps = [
    65,
    62,
    63,
    69,
    69,
    65,
    68,
    61,
    65,
    65,
    67,
    68,
    72,
    72,
    75,
    74,
    73,
    69,
    69,
    67,
    62,
    63,
    69,
    70,
    70,
    72,
    74,
    71,
    69,
    70,
    74,
    75,
    
]


# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. high temperature each day)
x_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
y_temps = [65, 62, 63, 69, 69, 65, 68, 61, 65, 65, 67, 68, 72, 72, 75, 74, 73, 69, 69, 67, 62, 63, 69, 70, 70, 72, 74, 71, 69, 70, 74, 75]

#Calculate the high temperatures
mode= statistics.mode(y_temps)
mean= statistics.mean(y_temps)
median= statistics.median(y_temps)
variance= statistics.variance(y_temps)
standard_deviation=statistics.stdev(y_temps)

print(f"The mode of the high temps is {mode}.")
print(f"The mean of the high temps is {mean}.")
print(f"The median of the high temps is {median}.")
print(f"The variance of the high temps is {variance:.2f}. ")
print(f"The standard deviation of the high temps is {standard_deviation:.2f}. ")

slope, intercept = statistics.linear_regression(x_days, y_temps)

print(f"""The best fit line has a slope of {round(slope,2)} and intercept of {round(intercept, 2)}.""")

#Slope and intercept- predicting the temp
future_x=13
future_y= slope*future_x+intercept
print(f"""The high temp tomorrow will be {round(future_y,0)} degrees.""")
print (f'3.  the MEAN of values = { mean:0.2f}')
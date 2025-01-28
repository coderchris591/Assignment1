# Title: Fermat’s Last Theorem
# File name: main.py
# Necessary external files:  N/a
# Eexternal files your program creates plus an explanation for each file: N/a
# Programmer Names: Chris Martinez, Zachariah Kennedy
# Programmer Emails: chrisrmartinez@lewisu.edu, zachariahckennedy@lewisu.edu
# Course number and section number:SP25-CPSC-44000-LT1
# Date submitted: 
# What the program does: 
# Resources used: 


# SUDO CODE 
# Start

# EQUATION: x^n + y^n = z^n
# CONSTRAINTS: n is a natural number greater than 2, k is greater than or equal to 10

# Initalize variables: x, y, z, n, k, smallest_miss, current_miss


# INPUT: Ask the user for n (the power to use in the equation) 
# INPUT: Ask the user of k (which limits the range of x and y possibilities to test). 
# Check every combination of x and y from 10 to k.
#   For each combination, check if z^n < x^n + y^n < (z+1)^n
#       If it is, then:
#           Find which one is closer to x^n + y^n (either z or z+1)
#           Determine the size of the miss by subtracting x^n + y^n from the closer one (z or z+1)
#           Divide the miss by x^n + y^n to get the percentage of the miss and set current_miss
#           Print the combination of x, y, z, and the current_miss
#           If current_miss is less than smallest_miss
#               Set smallest_miss 
#       ELse:
#           Skip comboination
# OUTPUT: Print the smallest miss and the combination of x, y, z that produced it
# OUTPUT: Print the time it took to run the program
# End


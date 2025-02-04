# Title: Fermat’s Last Theorem
# File name: main.py
# Necessary external files:  N/a
# External files your program creates plus an explanation for each file: N/a
# Programmer Names: Chris Martinez, Zachariah Kennedy
# Programmer Emails: chrisrmartinez@lewisu.edu, zachariahckennedy@lewisu.edu
# Course number and section number:SP25-CPSC-44000-LT1
# Date submitted: 
# What the program does: 
# Resources used: 


# SUDO CODE 
# Start

# Print Welcome Message
print("Fermat's Last Theorem: x^n + y^n = z^n")
print("This program will find the smallest miss in the equation x^n + y^n = z^n")

# VARIABLES:
smallest_miss = 0.0
current_miss = 0.0
start = 10
x = start
y = start
n = 0
k = 0

# n must be a natural number greater than 2
while n <= 2 or n >= 12:
    # INPUT: Ask the user for n (the power to use in the equation)
    n = int(input("Please enter a natural number greater than 2 and less than 12: "))

# k must be greater than or equal to 10
while k < 10:
    # INPUT: Ask the user of k (which limits the range of x and y possibilities to test).
    k = int(input("Please enter a number greater than or equal to 10: ")) 

# Calculate the count of numbers between 10 and k
total_numbers = k - start + 1
# Calculate number of possible combinations 
possible_combinations = total_numbers ** 2

# Loop through all possible combinations of x and y
for i in range(0, total_numbers):
    iteration = i
    print("")
    for j in range(start + i, k+1):
        x = start + i
        y = start + iteration
        print("{}^{} + {}^{} = z^{}".format(x, n, y, n, n))
        iteration += 1
        # Calculate x^n + y^n
        # Find whole numbers z and z + 1 that “bracket” (x^n + y^n), so that z^n < (x^n + y^n) < (z+1)^n
        # Find out which one (either z^n or (z+1)^n) is closer to (x^n + y^n)
        # Determine the size of the miss by subtracting x^n + y^n from the closer one (z or z+1)
        # Divide the miss by x^n + y^n to get the percentage of the miss and set current_miss
        # If current_miss is less than smallest_miss, set smallest_miss to current_miss
        # Print the combination of x, y, z, and the smallest_miss
# End


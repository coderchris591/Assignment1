# Title: Fermat’s Last Theorem
# File name: main.py
# Necessary external files:  N/a
# External files your program creates plus an explanation for each file: N/a
# Programmer Names: Chris Martinez, Zachariah Kennedy
# Programmer Emails: chrisrmartinez@lewisu.edu, zachariahckennedy@lewisu.edu
# Course number and section number:SP25-CPSC-44000-LT1
# Date submitted: XX/XX/XXXX
# What the program does: This program searches for near misses in Fermat’s Last Theorem of the form x^n + y^n ≈ z^n. Essentially, the program is a tool that can be used for finding instances
#                        where x^2 + y^2 almost equals another perfect power z^n, highlighting those specific instances.
# Resources used: N/A


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
sum_val = x**n + y**n

# Find whole numbers z and z + 1 that “bracket” (x^n + y^n), so that z^n < (x^n + y^n) < (z+1)^n
z = int(sum_val ** (1.0/n))
if z**n >= sum_val:
            z -= 1
while (z+1)**n <= sum_val:
            z += 1

# Find out which one (either z^n or (z+1)^n) is closer to (x^n + y^n)
lower_diff = sum_val - z**n
upper_diff = (z+1)**n - sum_val

# Determine the size of the miss by subtracting x^n + y^n from the closer one (z or z+1)
if lower_diff <= upper_diff:
            miss = lower_diff
            candidate_z = z
else:
    miss = upper_diff
    candidate_z = z + 1

# Divide the miss by x^n + y^n to get the percentage of the miss and set current_miss
current_miss = miss / sum_val

# If current_miss is less than smallest_miss, set smallest_miss to current_miss
if current_miss < smallest_miss:
       smallest_miss = current_miss

# Print the combination of x, y, z, and the smallest_miss
print("New best near miss found:")
print("  x = {}, y = {}, z = {}".format(x, y, candidate_z))
print("  {}^{} + {}^{} = {}".format(x, n, y, n, sum_val))
print("  {}^{} = {}".format(candidate_z, n, candidate_z**n))
print("  Absolute miss = {}".format(miss))
print("  Relative miss = {:.10f}".format(current_miss))

# Testing
iteration += 1

# End


# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5

import math
num=int(input("Factorial of: "))
print(math.factorial(num))


# i=1
fact=1
# while i<=num:
#         fact*=i
#         i+=1
# print(fact)


# using for loop
for i in range(1,num+1):
        fact*=i
print(fact)

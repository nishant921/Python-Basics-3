# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
# HCF is the largest number that divides two or more numbers exactly.
# Example:
# Find HCF of 12 and 18
# Factors:
# 12 → 1, 2, 3, 4, 6, 12
# 18 → 1, 2, 3, 6, 9, 18
# 👉 Common factors = 1, 2, 3, 6
# 👉 Highest = 6
# ✔ HCF = 6

# LCM is the smallest number that is divisible by both numbers.
# 🧠 Example:
# Find LCM of 12 and 18
# Multiples:
# 12 → 12, 24, 36, 48...
# 18 → 18, 36, 54...
# just multiple the common factors
# 👉 First common multiple = 36
# ✔ LCM = 36
# lcm = (num1 * num2) // hcf

import math

num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

print(math.lcm(num1,num2))
print(math.gcd(num1,num2))




# Input two numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# -------- HCF (GCD) --------
a = num1
b = num2

while b != 0:
    a, b = b, a % b

hcf = a

# -------- LCM --------
lcm = (num1 * num2) // hcf

# Output
print("HCF is:", hcf)
print("LCM is:", lcm)


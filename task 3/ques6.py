# `Problem 6`: The natural logarithm can be approximated by the following series.
# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.
# (x-1)/x + (1/2)((x-1)/x)^2 + (1/2)((x-1)/x)^3 + (1/2)((x-1)/x)^4 + ...
    

x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

if x == 0:
    print("Undefined! x cannot be 0")

else:
    total = 0

    for i in range(1, n + 1):

        if i == 1:
            term = (x - 1) / x
        else:
            term = (1/2) * (((x - 1) / x) ** i)

        total += term

    print("Sum of series =", total)
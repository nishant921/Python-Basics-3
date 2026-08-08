# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

x=int(input("Enter the Value of X: "))
n=int(input("Enter the Value of n: "))
total=1
for i in range(2,n+1):
    total+=(x**i)/i
print(total)
# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
'''Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34'''

# f(n)=f(n-1)+f(n-2)

n=int(input("Enter Number of fibonacci series : "))
a=0
b=1
count=1

while  count<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1

print()
#using for loop
a=int(input("first term: "))
b=int(input("second term: "))

print("------FIBONACCI SERIES-----")
for i in range(int(input("NO. OF SERIES: "))):
    print(a,end=",")
    c=a+b
    a=b
    b=c



# Problem 7 - Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.
# Example:
# Input: 5
# Output: 2+22+222+2222+22222
# Sum of above series is: 24690

n = int(input("Enter the value of N: "))
value = input("Enter value for series: ")

term = ""
total = 0

for i in range(1, n + 1):
    term += value
    total += int(term)

    if i < n:
        print(term, end="+")
    else:
        print(term)

print("Sum of above series is:", total)



# another way
n = int(input('Enter the nth term: '))
a = int(input('Enter the a term: '))
total = 0
temp = 0
for i in range(n):
    temp=temp*10+a
    total+=temp
print('Sum of series: ', total)
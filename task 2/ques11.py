# Problem 11: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line


# using flag [even = True]
for i in range(1000,3000+1):
    even=True
    temp=i
    while temp>0:
        digit= temp % 10
        if digit % 2 != 0:
            even = False
            break
        temp=temp//10
    if even:
         print(i,end=" ")


# using all() function and list
for i in range(10,30):
    digits=[]
    temp=i

    while temp>0:
        digits.append(temp % 10)
        temp=temp//10

    if all(digit % 2 == 0 for digit in digits):
        print(i, end=" ")
    
    digits.clear()




# using all() and converting in str
# short and concise way
for i in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(i)):
        print(i, end=" ")
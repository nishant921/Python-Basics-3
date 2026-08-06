# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number.
num=int(input("Enter Decimal Number: "))
binary=""
if num==0:
    print(0000)

else:

    temp=num
    while temp>0:
        binary = str(temp % 2) + binary  # prepend instead of append
        temp=temp//2
    print(binary)

print(bin(num))
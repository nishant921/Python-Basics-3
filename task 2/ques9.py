# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

Nsum=0
count=0
while True:
    N=int(input("Enter a Number: "))
    if  N==0:
       break
    Nsum+=N
    count+=1
avg=Nsum/count
print("sum of the numbers: ",Nsum)
print("Average of above numbers: ",avg)

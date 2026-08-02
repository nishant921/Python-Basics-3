# Problem 13`:Write a program to print whether a given number is a prime number or not

print("Check If the Given Number is Prime or Not")
num=int(input("Enter the number: "))

if num<=1:
    print("Not a Prime Number!")
else: 
    prime=True
    
    for i in range(2,num):
        if num%i==0:
            prime=False
            break

    if prime:
        print(num,"is a Prime Number! ")     
    else:
        print(num,"is not a Prime Number! ")


# using two loops to find prime number between range

start=int(input("Enter starting range: "))
end=int(input("Enter end range: "))
for num in range(start,end):    
    if num<=1:
       print("Not a Prime Number!")
    else: 
       prime=True
       for i in range(2,num):
          if num%i==0:
            prime=False
            break
    if prime:
        print(num,"is a Prime Number! ")     
        
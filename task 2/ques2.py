# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not. 

#  sum of each three angle must be 180 to form a traingle 
# Each angle must be greater than 0°


angle_1=float(input("Enter first angle: "))
angle_2=float(input("Enter second angle: "))
angle_3=float(input("Enter third angle: "))

total=angle_1+angle_2+angle_3

if angle_1>0 and angle_2>0 and angle_3>0 and total==180:
    print("Angle_1: ",angle_1,"Angle_2: ",angle_2,"Angle_3: ",angle_3,"CAN FORM A TRIANGLE!!")
else:
    print("Angle_1: ",angle_1,"Angle_2: ",angle_2,"Angle_3: ",angle_3,"CANNOT FORM A TRIANGLE!!")
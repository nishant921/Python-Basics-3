# Problem 14:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong Number: An Armstrong number is a number in which:
# Sum of each digit raised to the power of total number of digits equals the original number.

# Example:153
# Number of digits = 3

# Calculation: 1^3+5^3+3^3=153 So, 153 is an Armstrong number.

start=int(input("Enter Starting range: ")) 
end=int(input("Enter End Range: ")) 
# num3=int(input("Enter Skip Step: ")) 
digit=0
for i in range(start,end+1):
    count=0
    total_sum=0
    temp = i
    while temp!=0:
        # digit = temp%10
        count+=1
        temp = temp//10
    temp=i
    while temp!=0:
        digit = temp%10
        temp = temp//10
        total_sum=total_sum+pow(digit,count)
    if total_sum==i:
        print(i)

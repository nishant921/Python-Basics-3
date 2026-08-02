# - Reverse a given integer number.
# Example:
# Input:76542
# Output:24567


print("REVERSE OF A GIVEN INTEGER")
num=int(input("Enter Number: "))
rev=0

while num!=0:
    digits=num%10
    num=num//10
    rev=rev*10+digits

print(rev)

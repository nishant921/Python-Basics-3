# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:
# Input
# khokho
# Output
# The entered string is symmetrical

string=input("Enter String: ")
mid=len(string)//2
n=len(string)
# [:mid]
# for i in range(len(string)):
if string[:mid]==string[mid+(n%2):]:
    print("The Entered String is Symmetrical")
else:
    print("The Entered String is NOT Symmetrical")
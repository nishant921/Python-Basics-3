# Write a program which can remove a particular character from a string.

string=input("Enter the string: ")
rem=input("Enter which character to remove: ")


# only one character should be entered
new_str=""
for i in string:
    if i !=rem:
        new_str+=i

print(new_str)


# using string function
string = input("Enter string: ")
rem = input("Enter character: ")

print(string.replace(rem, ""))
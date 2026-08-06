# Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive
# Expected Output:
# yaivePNT


str1 = "PyNaTive"
result=""
for i in str1:
    if i.islower():
        result+=i
for i in str1:
    if i.isupper():
        result+=i
print(result)
        
result = "".join([i for i in str1 if i.islower()] + [i for i in str1 if i.isupper()])
print(result)

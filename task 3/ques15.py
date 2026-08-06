# Problem 15: Removal of all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
# 2510

str1 = input("Enter String: ")
temp=''

for i in str1:
    if i.isdigit():
        temp+=i
print(temp)

print("".join(i for i in str1 if i.isdigit()))
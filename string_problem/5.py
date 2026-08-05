# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

string=input("Enter the string: ")
# check=string[::-1]
# if string==check:
#     print("Entered string is palindrome")
# else:
#     print("Entered string is not a palindrome")


# for interview
flag=True
for i in range(0,len(string)//2): 
    # print(string[len(string)-i-1]) for understanding
    if string[i]!=string[len(string)-i-1]:
        flag=False
        break
if flag:
    print("Entered string is palindrome")
else:
    print("Entered string is not a palindrome")

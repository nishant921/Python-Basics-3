# Problem 11: Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.
# Example:
# Input:
# Data science mentorship program
# Output: DSMP

string=input("Enter String: ")
temp=string.split()
# split logic manually
# l=[]
# temp=""
# for j in string:
#     if j!=" ":
#         temp+=j
#     else:
#         if temp!="":
#             l.append(temp)
#             temp=""
# if temp!="":
#     l.append(temp)
# print(l)
short=""
for i in range(len(temp)):
    short+=temp[i][0].upper()
print(short)
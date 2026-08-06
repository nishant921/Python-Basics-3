# roblem 12: Append second string in the middle of first string
# Input: campusx
# data
# Output:
# camdatapusx

str1=input("Enter 1st String: ")
str2=input("Enter 2nd String: ")
mid=len(str1)//2
l=[]
for i in range(len(str1)):
    if i==mid:
        l.append(str2)
    l.append(str1[i])
print("".join(l))

    
str1 = input("Enter 1st String: ")
str2 = input("Enter 2nd String: ")
mid = len(str1) // 2
result = str1[:mid] + str2 + str1[mid:]

print(result)
# Write a python program to convert a string to title case without using the title()


string=input("Enter the String: ")
l=[]
for i in string.split():
        l.append(i[0].upper() + i[1:].lower())

print(l)
print("".join(l))  #converting back to string
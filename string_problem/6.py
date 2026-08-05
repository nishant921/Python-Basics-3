# Write a program to count the number of words in a string without split()
#  * words not character

# split function logic 
string=input("Enter the String: ")
l=[]
temp=''
for i in string:
    if i!=" ":
        temp=temp+i
    else:
         if temp != '':   # avoid empty spaces/words
             l.append(temp)
             temp=''

if temp!="":
    l.append(temp)
print(l)

print(f"Number of Words in {string}: {len(l)}")
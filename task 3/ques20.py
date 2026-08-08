# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

string=input("Enter Sentence: ")
# l=string.split()
l=""
for i in string:
    if i not in l:
        # l.append(i)
        l+=i
print(l)
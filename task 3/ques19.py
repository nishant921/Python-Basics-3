# Problem 19: Word location in String.
# Statement: Find a location of a word in a given sentence.

# Example 1:
# Input:
# Sentence: We can learn data science through campusx mentorship program.
# word: campusx
# Output:

# Location of the word is 7.
# Note- Don't use index/find functions

string=input("Enter Sentence: ") 
word=input("Enter Word: ")
temp=string.split()  
count=0
flag=False

for i in temp:
    count+=1
    if i==word:
        flag=True
        break
if flag:
    print(f"The Location of {word}: {count}")
else:
    print("Word Not Found")



# another way
string = input("Enter Sentence: ")
word = input("Enter Word: ")

temp = string.split()

for i in range(len(temp)):
    if temp[i] == word:
        print(f"The Location of {word}: {i+1}")
        break
else:
    print("Word not found")
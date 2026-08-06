# Problem 17: Reverse words in a given String
# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:
# Input:
# geeks quiz practice code
# Output:
# code practice quiz geeks
# Example 2:
# Input:
# my name is laxmi
# Output:
# laxmi is name my

string=input("Enter String: ")
temp=string.split()
print(" ".join(temp[::-1]))




# using loop
string = input("Enter String: ")
words = string.split()
result = ""
for i in range(len(words)-1, -1, -1):
    result += words[i] + " "

print(result.strip())
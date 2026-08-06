# Problem 18: Find uncommon words from two Strings.
# Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words.
#  A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

# Example 1:
# Input:
# A = "apple banana mango" 
# B = "banana fruits mango"
# Output:
# ['apple', 'fruits']

A = "apple banana mango" 
B = "banana fruits mango"
temp = A.split()
print(temp)
temp2 = B.split()
l=[]
for i in temp:
    if i not in temp2:
        l.append(i)       
for j in temp2:
    if j not in temp:
        l.append(j)       

print(" ".join(l))



A = "apple banana mango"
B = "banana fruits mango"

words = A.split() + B.split()

result = [w for w in words if words.count(w) == 1]

print(''.join(result))
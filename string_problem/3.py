# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2

# Limitation: count() can also count substrings:
# "hello".count("ll")
# Output:1
# So it's not strictly character-only.

string=input("enter string: ")
find=input("what would like to search for: ")

print(string.count(find))


# without string function (better way)
count=0
for i in string:
    if i==find:
        count+=1

print(f"Frequency of {find} is: {count}")

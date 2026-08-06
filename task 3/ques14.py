# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:
# hel123O4every093
# Output:
# Sum: 22
# Avg: 2.75

string=input("Enter AlphaNumeric String: ")
total=0
count=0
for i in string:
    if i.isdigit():
        total+=int(i)
        count+=1

Avge=total/count
print(total)
print(Avge)



# digits = [int(i) for i in string if i.isdigit()]

# total = sum(digits)
# avg = total / len(digits)

# print(total)
# print(avg)
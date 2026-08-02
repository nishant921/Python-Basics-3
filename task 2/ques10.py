# Problem 10: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

print("numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200: ")
for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        print(i,sep='',end=",")




#converting outputs in strings for cleaner version
# list used, string functions used 
print()
result = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))

print(",".join(result))

# Here:
# numbers are stored in a list
# " ,".join() prints proper comma-separated output without extra comma at end.
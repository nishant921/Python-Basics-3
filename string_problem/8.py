# Write a program that can convert an integer to string.

num=int(input("Enter a Number: "))
# st=str(num)  using built in function

# manual
digit='0123456789'
result=''
 

if num==0:
  result+=digit[0]
while num!=0:
    result=digit[num % 10] + result
    num = num // 10

print("String: ",result)
print(type(result))
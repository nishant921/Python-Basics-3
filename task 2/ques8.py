# Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
# Example 1:
# Input:30
# Output:276
# If you want the output exactly 276, then the condition should be: “stop BEFORE adding a number that makes sum exceed 300”.
# if nsum+i>300:break

N=int(input("Enter N:"))
Nsum=0
i=1
while i<=N :
   if i%5==0:
      i+=1
      continue
   if Nsum+i>=300:
      break
   Nsum=Nsum+i
   i+=1
print(Nsum)


n=int(input("Enter the N: "))
total=0

for i in range(1,n+1):
    if total+i>=300:
          break
    if i%5==0:
       continue
    
    total+=i
print(total)
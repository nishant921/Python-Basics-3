# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
# Output:
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# ....so on

for i in range(1,5):
    for j in range(1,5):
       for k in range(1,5):
         for m in range(1,5):
           if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
             print(i,j,k,m)
   
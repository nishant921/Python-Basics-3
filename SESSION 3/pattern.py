# asterik
row=int(input("Enter no. rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
     print("*",end="")
    print() 


# number pattern: 1,121,12321,1234321
row=int(input("Enter no. of rows: "))
for i in range(1,row+1):
   for j in range(1,i+1):
      print(j,end="")
   for k in range(i-1,0,-1):
      print(k,end="")
   print()

# for printing : 54321,4321,321,21,2
row=int(input("Enter no. of rows: "))
for i in range(row,0,-1):
   for j in range(i,0,-1):
    print(j,end="")
   print()



# upper + lower triangle
for i in range(1,row+1):
   for j in range(1,i+1):
      print("*",end="")
   print()
for i in range(row,1,-1):
   for j in range(i-1,0,-1):
      print("*",end="")
   print()


# another way
row = 5
# Upper triangle
for i in range(1, row + 1):
    print("* " * i)
# Lower triangle
for i in range(row - 1, 0, -1):
    print("* " * i)

# another way
row = 5
for i in range(1, row + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(row - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# Problem 3:Write a program to pring the following pattern
#     *
#   * * *
# * * * * *

row=5
for i in range(1,row+1,2):
     # spaces
    for j in range((row - i) // 2):
        print(" ", end=" ")
    for k in range(i):
        print("* ",end="")
    print()




row = 5

for i in range(1, row + 1):

    # Print spaces
    for j in range(row - i):
        print(" ", end=" ")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
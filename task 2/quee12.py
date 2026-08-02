# Problem 12: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# The numbers after the direction are steps.
# ! means robot stop there.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example:
# Input:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# Output:2

import math

print("Enter the Direction in which you want to move the Robot")
print("DIRECTION: UP, DOWN, RIGHT, LEFT")
print("Enter ! to Stop")

x=0
y=0
print("Robot initial points: ",x,y)

while True:
    direction=input("Enter Direction in Capital: ")
    if direction == "!":
        break
    move=int(input("Enter Steps: "))
    if direction == "UP":
        y+=move
    elif direction == "DOWN":
        y-=move
    elif direction == "RIGHT":
        x-=move
    elif direction == "LEFT":
        x+=move
    else:
        print("INVALID OPTION!!")
distance=math.sqrt((pow(x,2)+pow(y,2)))
print("Robot current point: ",round(distance))

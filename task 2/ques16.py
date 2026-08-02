# Problem 15:Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
# Note: It may be assumed that the rectangles are parallel to the coordinate axis.

# l1(x1,y1), R1(x2,y2)
# l2(x3,y3), R2(x4,y4)

# beginner way
# Rectangle 1
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Rectangle 2
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
x4 = int(input("Enter x4: "))
y4 = int(input("Enter y4: "))

# Check overlap
if x2 < x3 or x4 < x1 or y2 > y3 or y4 > y1:
    print("Rectangles do NOT overlap")
else:
    print("Rectangles overlap")


# advance way

def overlap(l1, r1, l2, r2):

    # One rectangle is left of other
    if r1[0] < l2[0] or r2[0] < l1[0]:
        return False

    # One rectangle is above other
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False

    return True

# Rectangle 1
l1 = tuple(map(int, input("Enter l1 (x y): ").split()))
r1 = tuple(map(int, input("Enter r1 (x y): ").split()))

# Rectangle 2
l2 = tuple(map(int, input("Enter l2 (x y): ").split()))
r2 = tuple(map(int, input("Enter r2 (x y): ").split()))


if overlap(l1, r1, l2, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Do Not Overlap")
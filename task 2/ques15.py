# Problem 15:Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

# Input: H = 9 , M = 0
# Output: 90
# Explanation:
# The minimum angle between hour and minute hand when the time is 9 is 90 degress.

# 1 hour = 30 degree 
#  hour hand also moves 0.5 degree every minute(30/60(minute))
# so, hour hand angle =  30*hour+ 0.5*minute
# minute hand angle = 360/60 = 6*minute
# # angle = abs(hour_angle - minute_angle)
# because we always take the absolute difference.positive
# final formula for above 180  = 360 - [30*hour + o.5*minute]-6*minute

hour=int(input("Enter Hour Hand: "))
minute=int(input("Enter Minute Hand: "))
hour_angle =  30*hour+ 0.5*minute
minute_angle = 6*minute
angle=abs(hour_angle-minute_angle)

if angle>180:
    angle=360-angle
print("Minimum Angle between Hour hand and Minute hand: ", int(angle))
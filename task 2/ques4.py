#  Problem 4: Write a menu-driven program -
# cm to ft    1 cm=0.0328 ft
# km to miles  1 km=0.621 miles
# USD to INR   $1 = 95.44
# exit

while True:

    menu = input("""
    Conversion Calculator:
    1. CM TO FEET
    2. KM TO MILES       
    3. USD TO INR
    4. EXIT 
    ENTER YOUR CHOICES[1,2,3,4]: """)

    if menu=='1':
       print("CENTIMTERE TO FEET")
       cm=float(input("Enter the centimetre measurement: "))
       feet=cm*0.0328
       print("Feet : ", feet)
    elif menu=='2':
       print("KILOMETRE TO MILES")
       km=float(input("Enter the kilometre measurement: "))
       miles=km*0.621
       print("MILES : ", miles)
    elif menu=='3':
       print("USD(DOLLAR) TO INR(RUPEES)")
       usd=float(input("Enter the Amount of Dollar: "))
       inr=usd*95.44
       print("INR : ", inr)
    elif menu=='4':
       print("program existed!!")
       break
    else:
       print("INVALID OPTION!!")

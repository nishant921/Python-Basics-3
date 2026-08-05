# Extract username from a given email. 
# Eg if the email is nishantgaming120@gmail.com 
# then the username should be nishantgaming120


email=input("Enter Your Email: ")

pos=email.index("@")  #works for every mail
username=email[0:pos]
print("username: ",username)



# This works only for Gmail addresses.
# username="".join(email.split("@gmail.com"))
# print(username)


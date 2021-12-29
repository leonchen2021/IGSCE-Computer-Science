#data validation -
admin_password =  input("enter your new passowrd")
admin_password_length = len(admin_password)

if(admin_password_length >= 6 and admin_password_length <= 12):
    print("password is updated")
else:
    print("password must be 6 - 12 characters")

name = input("inter your name")

#check if user enters an empty string

name_length = len(name)

if(name_length == 0):
    print("You cannot enter an empty name")
elif(name_length < 3):
    print("Name must be more than three letters")
elif(name_length > 25):
    print("name must be less than 25 characters")
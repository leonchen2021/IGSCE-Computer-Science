#user input error - this throws an exception if a string is given by user
age = int(input("Enter your age:"))


#try-catch block
try:
    age = int(input("Enter your age:"))
except ValueError:
    print("please enter number only")
else:
    print("no exceptions were thrown, excute this")


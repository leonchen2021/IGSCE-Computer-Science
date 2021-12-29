#ask user to enter a number (integer)
#enter a number by casting it to an int type
user_input = int(input("Enter a number:10"))

#defining a new function called "get_square"
#it takes one value and returns value * value (square)
def get_square (number):
    return number * number

#call the get_square function, pass "number" as argument
#save the result in a varible called "square"
#call function, pass user input, print output
square = get_square(user_input)
print(square)
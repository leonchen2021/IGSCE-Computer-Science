#write a boolean varible is_present, set to True
is_present = True

#write an integer variable for my_grade, set to 99
my_grade = 99

#write a floating point variable for height, set it to 54.55
height = 54.55

#declare a string variable called my_mantra, set it to "I am a great student"
my_mantra = "I am a great student"

#Arithmetic Operations
cows = 5000
chicken = 2000
sheep = 188
total = cows + chicken + sheep 
print("result", total)

cows = 4770
chicken = 2000
sheep = 110
total = cows + chicken + sheep
print("result", total)

#User Input
#write the code to ask for the user name
#print the message goodmorning + that person's name
#output the message on the screen

def greeting(name):
    return "good morning" + name
greeting = greeting("my_neighbor")
print(greeting)

# Write a For Loop 
for i in range(10):
    print("I am getting smarter and smarter every day in every way")

# Write a While Loop 
number = 0
while(number < 7):
    print("I know what I’m talking about", number)
    number = number + 1

#Conditional Operators and Control Flow
the_dollars_in_my_wallet_has = 77
if the_dollars_in_my_wallet_has > 90 and the_dollars_in_my_wallet_has <= 100:
    print("you can buy a snack that’s between 90-100 dollars")
elif the_dollars_in_my_wallet_has > 80 and the_dollars_in_my_wallet_has <= 90:
    print("you can buy a snack that’s between 80-90 dollars")
elif the_dollars_in_my_wallet_has > 70 and the_dollars_in_my_wallet_has <= 80:
    print("you can buy a snack that’s between 70-80 dollars")
else:
    print("only buy a snack less than 70 dollars")
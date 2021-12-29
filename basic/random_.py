import random

random_number = random.randint(1, 100)
print(random_number)

def main():
    number = get_random(1, 100)
    print(number)

#main function 
def main_function():
    first_number = get_random(1, 100)
    second_number = get_random(101, 200)
    result = add(first_number, second_number)
    print(result)
    
#call our main function to start the program
main_function

#helper function
def get_random(start, end):
    random_number = random.randint(start, end)
    return random_number

#helper function #2 (dubroutine)
def add(number, another_number):
    return number + another_number
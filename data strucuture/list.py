#intialize a list (linked list)
student_names = ["Mike", "Amy", "charlie", "Marco", "David", "Leon", "Rain"]

#add the name to our list
student_names.append("Mars")
student_names.insert(0, "Mr. Amini") #insert at index (0) first position

#delete a name
student_names.remove("charlie")

#interate over our list
for name in student_names:
    print(name)

#Create a new list to represent class letter grades
#Character (letter) list
letter_grades = ["A", "A-", "A", "B", "B", "C", "C-", "A-", "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")

#count number of people with grade A
number_of_A_grades = letter_grades.count("B")
print("number of grades:",  number_of_A_grades)

#integer list
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#integer list
numbers = [0, 0, 1, 0, 2, 0, 3, 4, 0, 1, 1, 0, 2, 5, 4, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#sort list 
numbers.sort() #or use the .reserve()

#print each item in list (iteration)
for number in numbers:
    print(number)

#boolean list
has_completed_homework = [True, True, False, True, False, False, True]
number_of_completed_homeworks = has_completed_homework.count(True)
print("Number of people who did homework", number_of_completed_homeworks)

#combine two lists
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
combined_list = letters + numbers
print(combined_list)

#create a list of boolean balues to represent students who have done their homework 
have_done_homework = [True, False, True]
print(have_done_homework)
have_done_homework.sort()
print(have_done_homework)

#how many false values are in this data structure?
number_Falses = have_done_homework.count(False)
print(number_Falses)

#interate (traverse the data structuere)
for student in have_done_homework:
    print(number_Falses)

#make a list that stores student the amount of money each student has in their pocket
money_in_pocket = [50, 54, 100, 789, 1000, 5618, 154, 687, 524]
money_in_pocket.sort()
print(money_in_pocket)

#add 
money_in_pocket.append(34)
money_in_pocket.sort()
print(money_in_pocket)

#create a list of strings
student_names = ["Adrian", "Mike", "Charlie", "Hanson"]
student_names.sort()
print(student_names)

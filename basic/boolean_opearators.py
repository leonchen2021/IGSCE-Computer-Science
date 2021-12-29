is_computer_science_student = True
is_chang_jung_student = False

#and - both values must be true for the expression to be true
is_enrolled_CS = is_computer_science_student and is_chang_jung_student
print('the value of our AND statement',is_enrolled_CS)

#or - one of the values must be true for the expression to be true
is_enrolled_or = is_computer_science_student or is_chang_jung_student
print('the value of our OR statement', is_enrolled_or)

if(is_chang_jung_student and is_computer_science_student):
    print("You are enrolled in my computer science class")
elif(not is_computer_science_student and is_chang_jung_student):
    print("You are not in my computer science class")

#question for homework
student_age = 18
is_computer_science_student = True

if(student_age < 15 and is_computer_science_student):
    print("True")
elif(student_age > 15 and is_computer_science_student):
    print("False")

student_age = 16
is_computer_science_student = True
if(student_age < 15 or is_computer_science_student):
    print("True")
elif(student_age > 15 or is_computer_science_student):
    print("False")
    


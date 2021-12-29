#variables -
    #a) Write a boolean to represent whether or not you wil pass the exam
passed_exam = True

#b) Write an integer variable to represent your score on the exam
my_score_on_the_exam = 100

#c) Write a floating point variable to represent the class average on the exam
the_class_average_on_the_exam = 99.9    

#d) Write a string variable to represent something you'd say yo your friend in the morning
message = "Good morning"

#2 interations - for loops
#a) write a for loop that prints "I am a polite and kind person" 10x
for a in range(10):
    print("I am a polite and kind person", a)

#control flow - write a simple if-elif statement to describe this..
#a) if sudent has a grade of 90-100 print "you rock"
#b) elif student has a grade of 80-90 pint "you are great"
#c) elif sudent has a grade of 70-80 print "not bad, keep working"
#d) else if student has a grade of less than 70 print "keep working champ"

student_grade = 100
if student_grade > 90 and student_grade <= 100:
    print("you rock")
elif student_grade > 80 and student_grade <=90:
    print("you are great")
elif student_grade > 70 and student_grade <=80:
    print("not bad, keep working")
else:
    print("you can always do more and become more, growth mindest")

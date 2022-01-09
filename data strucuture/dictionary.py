#create a dictionary (key-value-pairs) aka "HashMap, Map, HashTable"
assignment_scores = {"Mars": 90, "Amy": 93, "Rain": 98, "Charlie": 98 }
amy_assignment_score = assignment_scores.get("Amy")
print("Amy assignment score", amy_assignment_score)


#creat a dictionary using built in dict function (same thing, different)
exam_scores = dict(Mars=90, Amy=93, Rain=98, Charlie=98)
mars_score = exam_scores.get("Mars")
print("Mars exam score", mars_score)

#key - student name l value - boolean (True / False) represents whether or not the student
has_pets = {"Henrt": False, "Mars": False, "Barbie": True, "Adrian": True, "Angelina": False}

#data structure operations - add, delete, search. sort
student_has_pet = has_pets.get("Barbie")
print("The student has a pet: ", student_has_pet)

#traverse the dictionary
for student in has_pets:
    print(student, "has a pet:", has_pets.get(student))

#remove method - pop()
student_removed = has_pets.pop("Adrian")
print(student_removed)
print(has_pets)

#create a dictionary (key-value pair)
#key = student name
#value = list of scores (numbers)

student_scores = {"Adrain": [90, 91, 88], "Charlie": [88, 99, 100], "Mandy": [90, 95, 99], "Yujing": [100, 95, 99], "Angelina": [99, 98, 99], "Mr. Amini": [50, 99, 99]}
student_scores = student_scores.get("Adrain")
for score in student_scores:
    print(score)

#dictionary to represent sibling names of students
student_siblings = {"Howard": ["Barbie", "Anthony", "Annie"], "Barbie": ["Howard", "Anthony", "Annie"], "Mike": ["Angel"], "Yujing": ["Jimmy"]}
student_siblings = student_siblings.get("Howard")
student_siblings.sort()
for siblings in student_siblings:
    print(siblings)


student_pets = {
    "Adrian": ["pet 1", "pet 2", "pet 3"],
    "mars": ["pet 1", "pet 2", "pet 3"]
}

student_pet_names = dict(
    Adrian=["pet 1 , pet 2, pet3"], 
    Charlie=["pet1, pet2, pet3"]
    )
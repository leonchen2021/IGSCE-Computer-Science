#the exam coding for list
has_participated = [True, True, False, True, False, False, True]
has_participated.sort()
has_participated.reverse()
print (has_participated)
number_of_participation = has_participated.count(True)
print("Number of people who participated", number_of_participation)

#the exam coding for dictionaries
student_scores = dict(Amy=89, Leon=88, Mike=85, Charlie=86, Amini=100)
print (student_scores)
student_scores.get("Amini")
print ("Mr. Amini", student_scores)
#create the dictionary that stores the students names and their pet's names
student_pets = dict(Adrain=["pet1", "pet2", "pet3"], Leon=["pet1", "pet2", "pet3"], Amini=["pet1", "pet2", "pet3"])
student_pets.get("Amini")
for pets in student_pets:
    print(pets)
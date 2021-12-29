
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

from array import array
#create a new array using built in array method 
test_scores = array("i", [90, 70, 40, 60, 98, 97, 93])

#add another test scores to end of our array (append = add)
test_scores.append(100)
print(test_scores[1])

#iterate over the array
for score in test_scores:
    print(score)

#get length of the array
length = len(test_scores)
print("length of the array(number of scores): ", length)

#sort list using built in list method .sort
student_names.sort()
for name in student_names:
    print(name)


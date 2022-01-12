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
score = student_scores.get("Amini")
print ("Mr. Amini", score)

#create the dictionary that stores the students names and their pet's names
student_pets = dict(Adrain=["pet2", "pet1", "pet3"], Leon=["pet1", "pet2", "pet3"], Amini=["pet1", "pet2", "pet3"])
pet_name = student_pets.get("Amini")
pet_name.sort()
print (pet_name)

#Example: 0(n) time
# where n is the number of items in list 
list = [1, 5, 7, 56, 14, 22]
#this runs in 0(n) time - proportional to the input (n)
for bocket in list:
    print (bocket)

#Example: 0(n^2) time 
list_two = [[5,7,9], [5,4,7], [9,7,3]]
#this runs in 0(n^2) time because for each input
#there is a nested operation 
for new_bocket in list_two:
    for result in new_bocket:
        print (result)


#working for binary search 
sorted_list = [1, 3, 5, 7, 9, 8, 10]
target = 5
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list)-1
    print(right_idx)

    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2)
        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(sorted_list[middle_idx] > target):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return - 1

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)


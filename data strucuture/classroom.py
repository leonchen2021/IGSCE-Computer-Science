#lists - create a list of integers to represent the daily temperature of 
#temperture in celsius

temperture = [13, 40, 30, 20, 41, 10, -13]
print(temperture)
#Add - the temperture 23 to the list(add to the end)
temperture.append(23)
print(temperture)

#Find - the index of value 30 in the list
index = temperture.index(30)
print(index)

#Delete - the value 22 from the list
temperture.remove(41)
print(temperture)

#Access value by index
Sunday_temp = temperture[0]
print(Sunday_temp)

#Sort the temperture 
temperture.sort()

#Get and print the highest temperture
highest_temp = temperture.pop()
print(highest_temp)

#create a dictionary to store the student in 
#IGCSE and whether or not they've been 
#naughty = False, nice = True
#to show which students are getting gifts

has_been_nice = {"Mr. Amini":False, "Mike": True, "Adraian": False, "Henry": False}
gets_a_gift = has_been_nice.get("Mr. Amini")
print("This person has a gift:", gets_a_gift)

#create a dictionary to represent Secret Santa
secret_santa = {"Mr. Amini": "Peter", "Ms. Jen": "Ms. Ana" }
recipient = secret_santa.get("Mr. Amini")
print(recipient)
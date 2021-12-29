class_name = {"Harward": ["Chemistry", "Computer Science", "Math"], "Leon": ["Computer Science","Physic", "Chemistry"], "Henry": ["IGCSE", "Computer Science", "Math"]}
class_name = class_name.get("Leon")
class_name.sort()
for name in class_name:
    print(name)


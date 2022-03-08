character = input("enter a single character:")
if len(character)>1:
    character = character[0]
print("the character", character)
print("has the ASCII value", ord(character))
#write a program using if-elif-else that....
#looks at a variable for temperature = 20C
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, and it;s above 5C, print it's cold 
#else print "bring an umbrella just in case"

temperature = 20

if temperature > 30:
    print("it's hot")
elif temperature < 30 and temperature > 10:
    print("it's warm")
elif temperature < 10 and temperature > 5:
    print("it's cold")
else:
    print("bring an umbrella just in case")
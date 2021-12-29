#write a if-elif-else function 
#the temperature is 20
#if the temperature > 30, print it's hot
#if the temperature < 30 and > 18, print it's warm
#if the temperature < 10 and > 5, print it's cold
#else print bring an umbrella just in cass

temperature = 20

if temperature > 30:
    print("it's hot")
elif temperature < 30 and temperature > 10:
    print("it's warm")
elif temperature < 10 and temperature > 5:
    print("it's cold")
else:
    print("bring an umbrella just in case")
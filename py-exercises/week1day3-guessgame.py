#bonus String Exercises: Guess Game 2
import random

a = 0
b = 100

counter = 0

x = random.randint(a,b)
print (x)
check = str(input("high/low/it? "))

while check != "it":
    if check == "high":
        b = x
        x = random.randint(a,b)
        print(x)
    if check == "low":
        a = x
        x = random.randint(a,b)
        print(x)
    counter = counter + 1
    check = str(input("high/low/it?"))

print ("Yay! I got it! Tries:", counter)

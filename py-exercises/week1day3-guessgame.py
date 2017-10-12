#bonus String Exercises: Guess Game 2
import random
import time

def pause():
    time.sleep(1.5)

print("""\n\n Guessing Game: Think of any number from 1 to 100 and I will try to guess it!\n\n""")
pause()

a = 0
b = 100

counter = 0

print("""My guess is""")
for i in range(4):
    time.sleep(0.3)
    print("\r" + ". " * i, end="")
    time.sleep(0.3)

x = random.randint(a,b)
print (x)

print("high/low/it?")
check = input('> ')

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
    print("high/low/it?")
    check = input('> ')

if counter <= 1:
    print("Yay! I got it! It took me 1 try!")
else:
    print ("Yay! I got it! It took me {} tries!".format(counter))

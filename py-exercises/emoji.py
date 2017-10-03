#play with emoji unicode
# website: http://www.fileformat.info/info/emoji/list.htm

palm = u"\U0001F334"
ok = u"\U0001F44C"
flower = u"\U0001F33A"
monkey = u"\U0001F412"
dog = u"\U0001F436"
poop = 	u"\U0001F4A9"
fire = u"\U0001F525"
lol = u"\U0001F602"
hearteyes = u"\U0001F60D"
okgirl = u"\U0001F646"
bike = u"\U0001F6B2"
van = 	u"\U0001F68C"
yay = u"\U0001F64C"
monkeycute = u"\U0001F649"

emojilist = [palm, ok, flower, monkey, dog, poop, fire, lol, hearteyes, okgirl, bike, van, yay, monkeycute]

def emoji():
    ans = str(input("Which emoji do you want? Any number 1 - 13, palm/ok/flower, or type 'quit' to stop playing   "))
    while ans != "quit":
        if ans == "palm":
            print (palm)
        if ans == "ok":
            print(ok)
        if ans =="flower":
            print(flower)
        else:
            try:
                val = int(ans)
                print(emojilist[val])
            except ValueError:
                print("That's not a valid input!")
        ans = str(input("Which emoji do you want? Any number 1 - 13, palm/ok/flower, or type 'quit' to stop playing   "))
    print("bye")

# emoji()

#random emoji function
import random
def randomemoji():
    ans = str(input("type j for a random emoji. q to quit. "))
    while ans != "q":
        if ans == "j":
            x = random.randint(0, len(emojilist)-1)
            print(emojilist[x])
        ans = str(input("type j for a random emoji. q to quit. "))
    print("bye")
# randomemoji()

def randomemojibanner(n):
    randomemojis = []
    for i in range(n):
        x = random.randint(0, len(emojilist)-1)
        randomemojis.append(emojilist[x])
    randomemojis = "".join(randomemojis)
    print (randomemojis)
# randomemojibanner(500)

#emoji banner
def emojibanner():
    sentence = str(input("EMOJI BORDER|| Enter a string:  "))
    width = len(sentence) + 2
    for i in range(3):
        if i == 0 or i == 2:
            randomemojibanner(width)
        else:
            x = random.randint(0, len(emojilist)-1)
            print(emojilist[x]+sentence+emojilist[x])
# emojibanner()

def emojitriangle(n):
    counter = 1
    for i in range(1,n+1):
        x = random.randint(0, len(emojilist)-1)
        print((emojilist[x]*counter).center(n*3, ' '))
        counter = counter + 2
# emojitriangle(10)

#infinite loop of emojis! Beware!
def infiniteemoji():
    ans = str(input("type j for a random emoji. q to quit. "))
    infiniteemojilist = []
    while ans != "q":
        if ans == "j":
            x = random.randint(0, len(emojilist)-1)
            infiniteemojilist.append(emojilist[x])
            print (infiniteemojilist)
# infiniteemoji()

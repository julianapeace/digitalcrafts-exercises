name = "juliana"
#uppercase a string
def upperAstring(n):
    print (n.upper())

#capitalize a string
def capitalizeAstring(n):
    print(n.capitalize())

#reverse a string
def reverseAstring(n):
    print(n[::-1])

#leetspeak
def leetspeak(n):
    n = n.upper()
    newstr = []

    for i in n:
        if i == "A":
            i = 4
        elif i =="E":
            i = 3
        elif i =="G":
            i = 6
        elif i =="I":
            i = 1
        elif i =="O":
            i = 0
        elif i =="S":
            i = 5
        elif i =="T":
            i = 7
        newstr.append(i)
    newstr = "".join(map(str,newstr))
    print(newstr)
test = "What is the longest word in Alice in Wonderland? How many characters does it have?"
leetspeak(test)

#long-long vowels
def longvowels(n):
    vowels = ["a","e","i","o","u"]
    counter = 0
    newstr = []

    for i in n:
        if i in vowels:
            counter = counter + 1
        if counter > 1:
            counter = 0
            newstr.append(i*3)
        newstr.append(i)
    newstr = "".join(newstr)
    print (newstr)
# word = "spoon"
# longvowels(word)

def ceasarcipher(n):
    plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '?']
    cipher = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',' ', '?']
    newstr = []
    for i in n:
        newstr.append(cipher[plain.index(i)])
    newstr = "".join(newstr)
    print(newstr)
#use these test sentences
# sentence = "What is the longest word in Alice in Wonderland? How many characters does it have?".lower()
# sentence = "lbh zhfg hayrnea jung lbh unir yrnearq"
# ceasarcipher(sentence)

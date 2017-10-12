"""
Exercise3 is a speech parser. Prints top 50 words used in obama's inauguration speech.
"""
def exercise1():
    print('Write a program that prompts the user to enter a file name, reads the contents of the file and prints it to the screen.')
    fh = (input("Let's read an existing file. Enter a file name: "))
    with open(fh, 'r') as fh:
        contents = fh.read()
    print(contents)
# exercise1()

def exercise2():
    print('Write a program that prompts the user to enter a file name, then prompts the user to enter the contents of the file, and then saves the content to the file.')

    filename = input("Let's create a new file. Enter a file name: ")

    fh = open(filename, 'w')
    contents = (input("Type some stuff."))
    fh.write(contents)
    fh.close()

    fh = open(filename, 'r')
    contents = fh.read()
    fh.close()
    print(contents)


# exercise2() #use the file name: test.txt

def exercise3():
    print('Write a program that prompts the user to enter a file name, then prints the letter histogram and the word histogram of the contents of the file.')

    filename = input("Open an existing file. Enter a file name: ")
    # fh = open(filename, 'r')
    # contents = fh.readlines()
    # fh.close()

    with open(filename, 'r') as fh:
        contents = fh.readlines()
#break down speech, line by line
    wordspeech = []
    for i in contents:
        parts = i.lower().strip().split()
        wordspeech.append(parts)
    # print(wordspeech[0:3]

#break down speech, word by word
    wordlist  = []
    for i in range(len(wordspeech)):
        for j in wordspeech[i]:
            wordlist.append(j)
    # print (wordlist)

#create word histogram
    word_dict = {}
    for i in wordlist:
        word_dict[i] = 0

    for i in wordlist:
        word_dict[i] = word_dict[i] + 1

    # print (word_dict)

    order = sorted(word_dict, key = word_dict.get, reverse=True)#sorts the values from high to low, stores the key
    values = [word_dict[key] for key in order] #stores the values for each key in the list "order"

    #prints the top 50 most used words
    for i in range(50):
        print(order[i], ":",values[i])

#create letter histogram
    letter_dict = {}
    for i in range(len(wordlist)):
        for j in wordlist[i]:
            letter_dict[j] = 0
    for i in range(len(wordlist)):
        for j in wordlist[i]:
            letter_dict[j] = letter_dict[j] + 1
    # print(letter_dict)

# exercise3() # use test.txt

import json
import matplotlib.pyplot as plot

def exercise4():
    print('Write program that takes a JSON file name as input and plots the X,Y data. Exchange JSON data with others to test your program more thoroughly.')
#use test.json
    data = {'data': [
        [1, 7],
        [2, 3],
        [3, 5],
        [4, 9]
      ]
    }
    with open('test.json', 'w') as fh:
        json.dump(data, fh)
    with open('test.json', 'r') as fh:
        contents = json.load(fh)
        # print(contents['data'])

    x_list = []
    y_list = []
    for i in contents['data']:
        x_list.append(i[0])
        y_list.append(i[1])

    plot.plot(x_list, y_list)
    plot.show()
# exercise4()

import io
def bonus():
    print('Bonus: Crash Test - Write a program that writes to an in memory file and keeps track of how many characters/bytes were added and prints that information to the screen. Continue adding characters until your program dies.(1)At what count did your computer crash? (2) What kind of error did you get? (3)Did your program crash earlier or later than expected? Why do you think?')
    fh = io.StringIO()
    fh.write("Some more stuff")
    contents = fh.getvalue()

# bonus()

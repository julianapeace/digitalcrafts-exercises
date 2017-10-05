def exercise1():
    fh = (input("Let's read an existing file. Enter a file name: "))
    with open(fh, 'r') as fh:
        contents = fh.read()
    print(contents)
# exercise1()

def exercise2():
    filename = input("Let's create a new file. Enter a file name: ")

    fh = open(filename, 'w')
    contents = (input("Type some stuff."))
    fh.write(contents)
    fh.close()

    fh = open(filename, 'r')
    contents = fh.read()
    fh.close()
    print(contents)

#use the file name: test.txt
# exercise2()

def exercise3():
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

# exercise3()

import json
import matplotlib.pyplot as plot

def exercise4():
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
    fh = io.StringIO()
    fh.write("Some more stuff")
    contents = fh.getvalue()

# bonus()

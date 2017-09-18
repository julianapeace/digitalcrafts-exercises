def exercise1():
    phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
    print ('Elizabeth', ':',phonebook_dict['Elizabeth'])
    phonebook_dict['Kareem'] = '938-489-1234'
    del phonebook_dict['Alice']
    phonebook_dict['Bob'] = '968-345-2345'
    print (phonebook_dict)
# exercise1()

def nesteddictionaries():
    ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
    print('Ramit',':',ramit.get('email'))
    print("Ramit's first interest is", ramit.get('interests')[0])
    print("Ramit's friend: Jasmine's email address is", ramit.get('friends')[0]['email'])
    print("Ramit's friend: Jan's second interest is:", ramit.get('friends')[1]['interests'][1])
# nesteddictionaries()

def lettersummary():
    word = str(input("Enter a word: ")).lower()
    letters = {}
    for i in word:
        letters[i] = 0
    for i in word:
        letters [i] = letters[i] + 1
    print(letters)
# lettersummary()

def wordsummary():
    phrase = str(input("Enter a paragraph of text: ")).lower()
    word_list = phrase.split()
    word_dict = {}
    for i in word_list:
        word_dict[i] = 0
    for i in word_list:
        word_dict[i] = word_dict[i] + 1
    print (word_dict)
# wordsummary()

#bonus challenge: print 3 most used words
def bonus():
    phrase = str(input("Enter a paragraph of text: ")).lower()
    word_list = phrase.split()
    word_dict = {}
    for i in word_list:
        word_dict[i] = 0
    for i in word_list:
        word_dict[i] = word_dict[i] + 1
    # ordernum =sorted(word_dict.values(),reverse=True)
    #above line sorts the value
    order = sorted(word_dict, key = word_dict.get, reverse=True)
    values = [word_dict[key] for key in order]
    for i in range(3):
        print (order[i], ":", values[i])
bonus()

def diff(a,b):
    lista = []
    listb = []
    for i in a:
        lista.append(i)
    for i in b:
        listb.append(i)
    print(list(set(listb)- set(lista)))

# diff('abcd', 'abcde')
# diff('aaabbcdd', 'abdbacade')

def algo3(str1, str2):
    for char in str2:
        try:
            list(str1).index(char) == -1
        except ValueError:
            print(char)
algo3('aaabbcdd', 'abdbacade')

def py(i,j,k):
    if i**2 + j**2 == k**2:
        print('yes')
        return True
    else:
        print('no')
        return False

from math import *
def pytrip():

    for i in range(int(sqrt(1000)),500):
        for j in range(int(sqrt(1000)),500):
            for k in range(int(sqrt(1000)),500):
                if i<j and j<k :
                    if i**2 + j**2 == k**2:
                        if i + j + k == 1000:
                            print(i,j,k)

# pytrip()
# py(9,12,17)
# print(int(sqrt(1000)))

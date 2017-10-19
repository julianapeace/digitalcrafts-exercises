"""
Challenge 2

Given an API which returns an array of chemical names and an array of chemical symbols, display the chemical names with their symbol surrounded by square brackets:

Ex:
Chemicals array: ['Amazon', 'Microsoft', 'Google']
Symbols: ['I', 'Am', 'cro', 'Na', 'le', 'abc']


Output:
[Am]azon, Mi[cro]soft, Goog[le]

If the chemical string matches more than one symbol, then choose the one with longest length. (ex. 'Microsoft' matches 'i' and 'cro')
"""

chemicals = ['Amazon', 'Microsoft', 'Google']
symbols = ['I', 'Am', 'cro', 'Na', 'le', 'abc']
new = []
def challenge2():
    for i in chemicals:
        for j in symbols:
            if j in i:
                print(i.replace(i,j))

challenge2()

#Day 2 exercises - python lists and tuples
grades = [7, 6, 5, -7, -6, -5]
print (grades)
def sumnum(n):
    count = 0
    for i in n:
        count = count + i
    print(count)
# sumnum(grades)

#print the largest of the numbers
def largest(n):
    print (max(n))
# largest(grades)

def smallest(n):
    print (min(n))
# smallest(grades)

def evennum(n):
    for i in n:
        if i % 2 == 0:
            print (i)
# evennum(grades)

def positivenum(n):
    for i in n:
        if i > 0:
            print (i)
# positivenum(grades)

def positivenumlist(n):
    posnum = []
    for i in n:
        if i > 0:
            posnum.append(i)
    print (posnum)
# positivenumlist(grades)

def multiplelist(n):
    factor = 3
    newlist = []
    for i in n:
        newlist.append(factor * i)
    print (newlist)
# multiplelist(grades)

#multiplication vectors
def multiplicatiovectors(n):
    anotherlist = [1,2,3,4,5,6]
    for i in range(0,len(n)):
        print (n[i] * anotherlist[i])
# multiplicatiovectors(grades)

#additionmatrix that works for any pair of matrices of any size, as long as they have the same size
def additionmatrix(x,y):
    matrix3 = [None]*(len(x)) # I am generated an empty list exactly like matrix1
    for i in range(len(matrix3)):
        matrix3[i] = [None] * (len(x[i])) #EXACTLY like matrix1
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    print (matrix3)

matrix1 = [[2,-2],[5,3]]
matrix2 = [[6,5], [4,3]]
additionmatrix(matrix1, matrix2)

#de-dup, remove duplicates from a lists
def dedup(n):
    unique = []
    for i in n:
        if i not in unique:
            unique.append(i)
    print (unique)
numbers = [1,2,3,3,2,2,1,5]
# dedup(numbers)

#bonus: matrix multiplication
for i in range(2):
    for j in range(2):
        print (matrix1[i][j], matrix2[i][j])








print("ahmer is awesome")

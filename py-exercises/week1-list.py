#Day 2 exercises - python lists and tuples

def sumnum(n):
    count = 0
    for i in n:
        count = count + i
    return count

grades = [7, 6, 5, -7, -6, -5]
#print(sumnum(grades))

#print the largest of the numbers
def largest(n):
    print (max(n))

def smallest(n):
    print (min(n))

def evennum(n):
    for i in n:
        if i % 2 == 0:
            print (i)

def positivenum(n):
    for i in n:
        if i > 0:
            print (i)

def positivenumlist(n):
    posnum = []
    for i in n:
        if i > 0:
            posnum.append(i)
    print posnum

def multiplelist(n):
    factor = 3
    newlist = []
    for i in grades:
        newlist.append(factor * i)
    print (newlist)

#multiplication vectors
def multiplicatiovectors(n):
    anotherlist = [1,2,3,4,5,6]
    for i in range(0,len(n)):
        print (n[i] * anotherlist[i])

#additionmatrix that works for any pair of matrices of any size, as long as they have the same size
def additionmatrix(x,y):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            print(matrix1[i][j] + matrix2[i][j])
matrix1 = [[2,-2],[5,3]]
matrix2 = [[6,5], [4,3]]

#de-dup, remove duplicates from a lists
def dedup(n):
    unique = []
    for i in n:
        if i not in unique:
            unique.append(i)
    print (unique)
numbers = [1,2,3,3,2,2,1,5]

#bonus: matrix multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):

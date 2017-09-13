#1 to 10
def oneten():
    for i in range(1,11):
        print (i)
# oneten()

#n to m
def onetennm():
    n = int(input("Start from: "))
    m = int(input("End on: "))
    m = m + 1
    for i in range(n,m):
        print (i)
# onetennm()

#odd numbers
def oddnum():
    for i in range(1,11):
        if i % 2 == 1:
            print (i)
# oddnum()

#print a square
def squareit():
    for i in range(5):
        print ("*"*5)
# squareit()

def squareitnum():
    n = int(input("How big is the square?"))
    for i in range(n):
        print("*" *n)
# squareitnum()

#print a box
def box():
    width = int(input("Width?"))
    height = int(input("Height?"))
    for i in range(height):
        if i == 0 or i == height-1:
            print ("*"*width)
        else:
            print("*"," "*(width-4),"*")
# box()

#print a triangle
def triangle():
    # for i in range(1,11):
    #     if i % 2 == 1:
    #         print (i)
    oddnum = [1,3,5,7]
    for i in oddnum:
        print (("*"*i).center(10, ' '))
# triangle()

#print a triangle II
def triangle2(n):
    counter = 1
    for i in range(1,n+1):
        print(("*"*counter).center(n*3, ' '))
        counter = counter + 2
# triangle2(4)

#multiplication table
def multiplicationtable():
    for i in range(1,11):
        for j in range(1,11):
            print (i," x ",j," = ", i*j)
# multiplicationtable()

#Bonus: print a banner
def banner():
    sentence = str(input("Enter a string"))
    width = len(sentence) + 2
    for i in range(3):
        if i == 0 or i == 2:
            print ("*"*width)
        else:
            print("*"+sentence+"*")
banner()

#Bonus: Triangle numbers
def trianglenum():
    for i in range(100):
        n = int(((i+1)*i)/2)
        print (n)
# trianglenum()

#Bonus: Factor a numbers
def factor(num):
    for i in range(1,1000):
        if num % i == 0:
            print(i)
# factor (120)

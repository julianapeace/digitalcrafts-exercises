#week2 Friday Challenges

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        elif n % 2 == 1:
            n = n*3 +1
        print('Collatz Sequence: {} \n'.format(n))
# collatz(200)

def isPal(n):
    n = str(n)
    if n[:] == n[::-1]:
        return True

def palnum():#could be solved with math or programming way by manipulating strings
    pallist = []
    pallistx = []
    pallisty = []
    for i in range(1000):
        for j in range (1000):
            ans = i * j
            if isPal(ans):
                pallist.append(ans)
                pallistx.append(i)
                pallisty.append(j)
    maxindex = pallist.index(max(pallist))
    print (pallistx[maxindex],"x", pallisty[maxindex],"=", max(pallist))
# palnum()

def holygrail(x):
    for i in range (11,21): #any num divisible by 1-10, is also divisible by 11-20
        if x % i != 0:
            return False
    return True

def challenge3():
    grail = []
    counter = 2520
    while counter != 999999999:
        if holygrail(counter) == True:
            grail.append(counter)
        counter += 2520 #If num is divisible by 20, it must be even. If 2520 is divisible 1-10, then we can move in increments of 2520.
    print(grail)

challenge3()

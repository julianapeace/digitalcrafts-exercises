import matplotlib.pyplot as plot

def hello(name):
    print("Hello", name)
# hello('julie')

def func1(x):
    return (x + 1)
# xfunc1 = list(range(-3,4))
# yfunc1 = []
# for x in xfunc1:
#     yfunc1.append(func1(x))
# plot.plot(xfunc1, yfunc1)

def func2(x):
    return (x**2)
# xfunc2 = list(range(-100, 101))
# yfunc2 = []
# for x in xfunc2:
#     yfunc2.append(func2(x))
# plot.plot(xfunc2, yfunc2)


def func3(x):
    if x % 2 == 0:
        return -1
    else:
        return 1
# xfunc3 = list(range(-5, 6))
# yfunc3 = []
# for x in xfunc3:
#     yfunc3.append(func3(x))
# plot.bar(xfunc3, yfunc3)

import math
def sine(x):
    return math.sin(x)
# xs = list(range(-5,6))
# ys = []
# for x in xs:
#     ys.append(sine(x))
# plot.plot(xs, ys)

from numpy import arange

def sine2(x):
    return math.sin(x)
# xs = arange(-5,6,0.1)
# ys = []
# for x in xs:
#     ys.append(sine(x))
# plot.plot(xs, ys)

def cel2fah(cel):
    return (cel*(9/5)) + 32
# xs = arange(-5,6,0.1)
# ys = []
# for x in xs:
#     ys.append(cel2fah(x))
# plot.plot(xs, ys)

def playagain():
    x = str(input("Do you want to play again(Y or N)?")).upper()
    if x == "Y":
        return True
    elif x == "N":
        return False
# playagain()

def playagain2():
    x = str(input("Do you want to play again(Y or N)?")).upper()
    if x == "Y":
        return True
    elif x == "N":
        return False
    else:
        print("Invalid input. Try again")
        playagain2()
# playagain2()

plot.show()

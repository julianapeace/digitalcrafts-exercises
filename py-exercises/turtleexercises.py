from turtle import *
import random
speed("fastest")

def drawstar(x):
    color('white')
    begin_fill()
    for i in range(5):
        forward(x)
        right(144)
    end_fill()

def nightsky():
    bgcolor('#000080')
    for i in range(20):
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        size = random.randint(10,50)
        up()
        goto(x,y)
        down()
        drawstar(size)
nightsky()

mainloop()

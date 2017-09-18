from turtle import *
import random
speed("fastest")
hideturtle()
title('Night Sky')

def drawstar(x):
    color('white')
    begin_fill()
    for i in range(5):
        forward(x)
        right(144)
    end_fill()

def nightsky():
    bgcolor('#000080')
    bgpic("1.jpg")
    for i in range(20):
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        size = random.randint(10,50)
        up()
        goto(x,y)
        down()
        drawstar(size)
# nightsky()

def diamond(x):
    color('white')
    pencolor('gray')
    begin_fill()
    seth(45)
    for i in range(4):
        forward(x)
        right(90)
    end_fill()
# diamond(50)

def nightsky2():
    bgcolor('black')
    for i in range(40):
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        size = random.randint(5,25)
        up()
        goto(x,y)
        down()
        diamond(size)

nightsky2()
exitonclick()
mainloop()

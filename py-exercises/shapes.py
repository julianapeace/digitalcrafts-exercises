from turtle import *

def equilateraltriangle():
    for i in range(3):
        forward(100)
        right(120)
# equilateraltriangle()

def drawsquare():
    for i in range(4):
        forward(100)
        right(90)
# drawsquare()

def drawpent():
    color('red')
    begin_fill()
    for i in range(5):
        forward(100)
        right(72)
    end_fill()
drawpent()

def drawhex():
    for i in range(6):
        pensize(5) #line weight
        forward(100)
        right(60)
# drawhex()

def drawoct():
    for i in range(8):
        turtlesize(5) #makes a giant fucking turtle lol
        forward(100)
        right(45)
# drawoct()

def drawstar():
    for i in range(5):
        fillcolor('red') #fillcolor affects the turtles lol, not the shape
        forward(100)
        right(144)
# drawstar()

def drawcircle():
    color('red') #pencolor
    circle(100)
# drawcircle()

mainloop()

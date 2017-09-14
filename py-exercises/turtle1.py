from turtle import *

# move into position
up()
forward(50)
left(90)
forward(50)
left(90)
down()

def draw_square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def draw_circle():
    pencolor('orange')
    width(10)
    circle(180)

def draw_star():
    for i in range(5):
        forward(100)
        right(144)
draw_star()

mainloop()

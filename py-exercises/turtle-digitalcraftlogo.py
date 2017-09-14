from turtle import *

speed("fastest")
up()
goto(-300,-300)
down()

def trapezoid():
    forward(150)
    left(60)
    forward(85)
    left(120)
    forward(235)
    left(120)
    forward(85)
    left(60)

color('#1F8CCD')
begin_fill()
trapezoid()

forward(150)
left(60)
trapezoid()
end_fill()

forward(150)
left(60)

color('#7EC045')
begin_fill()
trapezoid()

forward(150)
left(60)
trapezoid()
end_fill()

up()
goto(300, -300)
down()

def trapezoid_mirror():
    forward(150)
    right(60)
    forward(85)
    right(120)
    forward(235)
    right(120)
    forward(85)
    right(60)

color('#FA9E23')
begin_fill()
trapezoid_mirror()

forward(150)
right(60)
trapezoid_mirror()
end_fill()

forward(150)
color('#BCBDBF')
begin_fill()
right(60)
trapezoid_mirror()

forward(150)
right(60)
trapezoid_mirror()
end_fill()

def rhombus():
    for i in range(2):
        forward(85)
        right(120)
        forward(85)
        right(60)
color('#A6AAAB')
begin_fill()
rhombus()
end_fill()

position()
mainloop()

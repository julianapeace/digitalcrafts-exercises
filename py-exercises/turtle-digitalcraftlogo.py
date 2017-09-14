from turtle import *

speed("fastest")
up()
goto(-300,-300)
down()

x = 87

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
goto(240, -300)
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

up()
sety(-300)
down()

def rhombus_mirror():
    for i in range(2):
        forward(85)
        left(120)
        forward(85)
        left(60)

color('#F47820')
begin_fill()
rhombus_mirror()
end_fill()

up()
goto(-192,-225)
down()

color('#106DB7')
begin_fill()
rhombus()
end_fill()

up()
sety(-115)
down()

color('#5B893E')
begin_fill()
rhombus_mirror()
end_fill()

def triangle(y):
    for i in range(3):
        forward(y)
        left(120)
def triangle_mirror(y):
    for i in range(3):
        forward(y)
        right(120)

right(60)
up()
forward(60)
down()

color('#1466A2')
begin_fill()
triangle(x)
end_fill()

left(60)

color('#447764')
begin_fill()
triangle(x)
end_fill()

left(60)
up()
forward(x)
down()
right(60)

color('#1682B3')
begin_fill()
triangle_mirror(x)
end_fill()

forward(x)
right(60)
color('#1C8ECD')
begin_fill()
triangle_mirror(70)
end_fill()

up()
sety(-250)
down()
left(120)
color('#A8A9AB')
begin_fill()
triangle(70)
end_fill()

right(60)
color('#6E6D72')
begin_fill()
triangle(x)
end_fill()

up()
forward(x)
down()

left(60)
color('#C28254')
begin_fill()
triangle(x)
end_fill()

up()
forward(x)
down()
left(60)
color('#949597')
begin_fill()
triangle(x)
end_fill()

mainloop()

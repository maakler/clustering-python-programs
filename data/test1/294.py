from turtle import *
from math import cos, radians


pikkus = 200
laius = 50


penup()
setposition(-250,-200)
pendown()

fillcolor("brown")
begin_fill()
forward(pikkus)
left(60)
forward(laius)
left(120)
forward(2*cos(radians(60))*laius + pikkus)
left(120)
forward(laius)
left(60)
end_fill()

penup()
setposition(-150, -157)
pendown()

fillcolor("yellow")
left(90)
forward(150)
begin_fill()
right(120)
forward(40)
right(120)
forward(40)
end_fill()
right(120)
forward(40)

exitonclick()
from turtle import *
from math import *

a1 = 200
a2 = 260
b = 60

forward(a1)
left(60)
forward(b)
left(120)
forward(a2)
left(120)
forward(b)
left(60)

up()
c = a1/2
h = sqrt(pow(b,2) - pow((a2 - a1)/2,2))
forward(c-2)
left(90)
forward(h)

down()
forward(230)
right(120)
forward(65)
right(120)
forward(65)
left(120)
forward(120)
right(120)
forward(120)

exitonclick()
from turtle import *
from math import sqrt
from math import pi
import math

forward(240)
left(45)
forward(sqrt(3200))
left(135)
forward(40)
right(45)
forward(sqrt(3200))
left(45)
forward(80)
x=360/(2*pi)
a = math.atan(2/1.5)*x
right(a)
forward(sqrt(2500))
left(a)
forward(30)
b = math.atan(2)*x
left (b)
forward(sqrt(2000))
left (180-b)
forward(80)
right(180)
up()
forward(80)
down()
forward(40)
left(b)
forward(sqrt(2000))
left(180-b)
forward(260)
right(180)
up()
forward(260)
left(180-b)
down()
forward(sqrt(2000))

exitonclick()
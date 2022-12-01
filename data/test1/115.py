from turtle import *
from math import *
speed(10)
delay(0)
pikkus= 200      #põhja pikkus
korgus= 100
nurk=60
rnurk=radians(nurk)
ots=korgus/sin(rnurk)
juurde=korgus/tan(rnurk)

forward(pikkus)

left(nurk)
forward(ots)

left(180-nurk)
forward(pikkus+2*juurde)

left(180-nurk)
forward(ots)

up()

left(nurk)
forward(30)

left(90)
a=korgus
forward(a)

down()

for i in range(3):
    forward(50)
    right(90)

forward(50)

left(90)

up()
forward(40)

down()

for j in range(3):
    for i in range(90):
        forward(1)
        right(4)
    left(90)
    up()
    forward(80)
    down()
    right(90)

exitonclick()
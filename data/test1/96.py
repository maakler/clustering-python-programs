from turtle import *
from math import radians, degrees, sin, cos, tan, asin, acos, atan

alus1 = 300
alus2 = 350
haar = (350 - 300) / 2 / cos(radians(60))

#põhi
color("grey")
begin_fill()
forward(300)
left(60)
forward(haar)
left(120)
forward(350)
left(120)
forward(haar)
#liikumine ülemise osa joonistamiseks
up()
left(120)
forward(haar)
down()
end_fill()

#laeva ülemine osa
pensize(5)
pencolor("red")
fillcolor("#6C6161")
begin_fill()
left(20)
forward(100)
right(80)
forward(200)
right(80)
forward(100)

#korrused
right(180)
up()
forward(20)
left(80)
down()
forward(230)
right(100)
up()
forward(30)
down()
right(80)
forward(225)
left(120)
up()
forward(20)
down()
left(60)
forward(210)
end_fill()

exitonclick()
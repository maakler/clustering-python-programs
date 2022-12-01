from turtle import *
speed(0)
bgcolor('blue')
up()
right(90)
forward(400)
down()
pensize(8.5)
color('green')
left(180)
circle(1000, 25)

up()
goto(0, 0)

circle(350, 22.5)
down()
pensize(5)
color('orange')
begin_fill()
fillcolor('yellow')
circle(350, 22.5)
left(120)
for i in range(10):
    circle(350, 45)
    left(120)
circle(350, 22.5)
end_fill()
up()
left(90)
forward(45)
down()
dot(90, 'black')
up()
goto(300, 230)
down()
dot(150, 'yellow')
pensize(6)
color('yellow')
for i in range(6):
    forward(230)
    right(180)
    forward(230)
    left(180 + 60)
left(15)
for i in range(6):
    forward(270)
    right(180)
    forward(270)
    left(180 + 60)
left(15)
for i in range(6):
    forward(200)
    right(180)
    forward(200)
    left(180 + 60)
left(15)
for i in range(6):
    forward(210)
    right(180)
    forward(210)
    left(180 + 60)
    




exitonclick()


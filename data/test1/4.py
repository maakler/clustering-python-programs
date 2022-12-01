from turtle import *

setup(1200,800)
speed(0)

bgcolor("lightskyblue2")

penup()
goto(-500,-300)
pendown()

color("gray32")
begin_fill()
forward(1000)
left(60)
forward(100)
left(120)
forward(1100)
left(120)
forward(100)
left(60)
end_fill()

penup()
goto(-350,-212)
pendown()
color("white")
begin_fill()
forward(700)
left(90)
forward(50)
left(90)
forward(700)
left(90)
forward(50)
left(90)
end_fill()

a = -300
for i in range(0, 4):
    penup()
    goto(a,-161)
    pendown()
    color("darkgoldenrod1")
    begin_fill()
    forward(50)
    left(80)
    forward(120)
    left(90)
    forward(50)
    left(90)
    forward(130)
    left(100)
    end_fill()
    a+=150

hideturtle()
exitonclick()
from turtle import *

def draw(angle, distance):
    if(angle <= 180):
        right(angle)
    elif(angle > 180):
        left(360 - angle)
    forward(distance)

draw(315, 200)

pencolor("red")
draw(90, 50)
draw(230, 75)
draw(220, 60)

pencolor("black")
up()
draw(0, 200)
down()
draw(270, 300)

draw(90, 150)

draw(90, 550)

pencolor("cyan")
draw(225, 100)
draw(225, 80)
draw(135, 150)
draw(225, 115)
draw(135, 200)

pencolor("blue")
draw(270, 620)
draw(180, 960)

pencolor("cyan")
draw(115, 225)
draw(20, 155)

pencolor("black")
draw(315, 210)

draw(135, 100)
draw(270, 150)
draw(90, 40)
draw(90, 150)
draw(270, 30)
draw(270, 150)
draw(90, 40)
draw(90, 150)
draw(270, 30)
draw(270, 150)
draw(90, 40)
draw(90, 150)
draw(270, 120)

exitonclick()
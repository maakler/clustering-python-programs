from turtle import *

down()
startY = ycor()
left(45)
circle(60,90)
left(135)
lineLen = ycor() - startY
forward(lineLen)
left(90)
circle(lineLen/2, 180)
left(60)
forward(lineLen)
left(90)
circle(lineLen, 70)
right(145)
forward(50)
right(75)
forward(75)
right(75)
forward(45)

up()
exitonclick()
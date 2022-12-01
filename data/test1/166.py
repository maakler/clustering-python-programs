from turtle import *
import random

colormode(255)
#forward
#left
#rigth
#penup
#pendown
#fill

#Alus
forward(100)
left(45)
forward(50)
left(135)
forward(170)
left(135)
forward(50)
left(45)

#Mast
penup()
forward(50)
left(90)
forward(35)
pendown()
pensize(4)
pencolor("brown")
forward(120)

#Lipp
pensize(1)
R=random.randrange(0,255)
G=random.randrange(0,255)
B=random.randrange(0,255)
begin_fill()
fillcolor((R,G,B))
pencolor((R,G,B))
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()
backward(3)

#Puri
A=random.randrange(0,255)
B1=random.randrange(0,255)
C=random.randrange(0,255)
begin_fill()
fillcolor((A,B1,C))
pencolor((A,B1,C))
left(130)
forward(100)
right(130)
forward(65)
right(90)
forward(76)
end_fill()


exitonclick ()
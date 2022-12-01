#Ehita kilpkonnaga lihtne külgvaates paat

from turtle import *
#Õigesse kohta
up()
left(180)
forward(200)
left(180)
down()

#Leava alus
color("#823c11")
begin_fill()
forward(500)
left(45)
forward(100)
left(135)
forward(640)
left(135)
forward(100)
end_fill()

#lipumast
width(6)
pencolor("black")
up()
left(45)
forward(300)
left(90)
forward(70)
down()
forward(250)

#väike lipuke
color("red")
begin_fill()
right(130)
forward(40)
right(100)
forward(40)
end_fill()


#lipumast
up()
left(110)
forward(5)
down()

#parem puri
color("#3ebdc2")
begin_fill()
forward(250)
right(135)
forward(225)
end_fill()

#mast
up()
forward(5)
right(106)
forward(10)
left(60)
down()
forward(5)

#vasak puri
color("#51c4a9")
begin_fill()
forward(200)
right(130)
forward(180)
end_fill()

#ankur
up()
right(110)
forward(250)
down()
pencolor("#8a5f04")
width(6)
i = 0
while i < 15:
    forward(10)
    up()
    forward(5)
    down()
    i += 1
    
forward(50)
right(135)
forward(25)
right(180)
forward(25)
left(90)
forward(25)



exitonclick()
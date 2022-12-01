from turtle import *
r=20

up()
left(180)
forward(15*r)
left(90)
forward(10*r)
left(90)
down()

#joonistab paadi
forward(30*r)
right(120)
forward(10*r)
right(60)
forward(20*r)
right(60)
forward(10*r)

#liigub akende asukohta
up()
right(120)
forward(3*r)
right(90)
forward(4*r)
left(90)
down()

#joonistab akna
i=1
up()
while i<6:
    forward(4*r)
    down()
    circle(r)
    up()
    i+=1

#liigub masti asukohta
up()    
left(180)
forward(8*r+r/5)
right(90)
forward(4*r)

#joonistab masti
down()
forward(30*r)
right(90)
forward(2*r/5)
right(90)
forward(30*r)

#liigub lipu asukohta
up()
right(180)
forward(29*r)

#joonistab lipu
down()
right(105)
forward(3*r)
right(150)
forward(3*r)
left(75)
forward(r)

#joonistab purje
left(30)
forward(25*r)
right(120)
forward(20*r+2*r/5)
right(120)
forward(15*r)
up()

exitonclick()
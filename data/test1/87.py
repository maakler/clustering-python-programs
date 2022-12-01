import turtle
pen = turtle.Pen()
pen.speed(0)

pen.up()
pen.pensize(20)
pen.setpos(-500, 500)
pen.down()
#taevas
for i in range(20):
    pen.color(0.95 , 0.4 + i*0.01, 0)
    pen.forward(1000)
    pen.sety(500 - i*20)
    pen.right(180)
#päike
pen.up()
pen.setpos(0,130)
pen.color(1,1,0)
pen.down()
for i in range(300):
    pen.forward(i/3)
    pen.left(96)
    pen.color(0.5 + i/600, 0.5 + i/600, 0)
pen.up()

pen.setpos(-500, 120)
pen.down()

#meri
for i in range(20):
    pen.color(0.25, 0.7 - i*0.01, 0.7)
    pen.forward(1000)
    if(i != 19):
        pen.sety(100 - i*20)
        pen.right(180)
#laev
pen.up()
pen.setpos(-450, 40)
pen.color(0.4, 0.3, 0)
pen.pensize(10)
pen.down()
pen.setheading(300)
pen.forward(200)
pen.left(60)
pen.forward(400)
pen.left(60)
pen.forward(200)
pen.up()
pen.setpos(-450,40)
pen.setheading(0)
for i in range(19):
    pen.down()
    pen.color(0.4 + i*0.01, 0.3 + i* 0.01, 0)
    pen.forward(600 - i * 10)
    pen.up()
    pen.sety(40 - i*10)
    pen.right(180)
#purjekas
pen.setpos(-160, 40)
pen.color(0, 0, 0)
pen.down()
pen.setheading(90)
pen.forward(400)
pen.color(1, 1, 1)
pen.setheading(0)
for i in range(40):
    pen.down()
    pen.forward(i * 10)
    pen.up()
    pen.setpos(-160 - i * 10, 440 - i * 10)
#logo
pen.setpos(-260, 200)

pen.down()
for i in range(350):
    pen.pensize(3 + i/35)
    pen.forward(i/2)
    pen.left(111)
    pen.color(i/350, 0 , 0)
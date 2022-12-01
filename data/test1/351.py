import turtle

tc = turtle.Screen()
t = turtle.Turtle()

t.left(180)
t.forward(200)
t.left(90)
t.forward(30)

i = 0
while i < 90:
    i = i + 1
    t.left(1)
    t.forward(1.5)

t.forward(100)

while i < 180:
    i = i + 1
    t.left(1)
    t.forward(2)
    
t.left(90)
t.forward(160)

t.right(90)
t.forward(150)
t.left(90)
t.forward(10)
t.left(22.5)
t.forward(80)
t.left(135)
t.forward(80)
t.right(67.5)
t.forward(88.77065)
t.right(180)
t.forward(150)

turtle.done()
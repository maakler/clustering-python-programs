from turtle import Turtle, Screen
import math
import random as r

s = Screen()
t = Turtle()

s.bgcolor("#022F8E")

def body():
    t.speed(8)
    t.up()
    t.setposition(-s.window_width()/2.25,0)
    starting_pos = [t.xcor(), t.ycor()]
    t.down()
    t.color("black","#b76f20")
    t.begin_fill()
    t.rt(60)
    for i in range(15):
        t.fd(10)
        t.rt(math.log(0.5,1.2))
    t.setheading(0)
    t.fd(250)
    for i in range(999):
        t.fd(10)
        t.rt(math.log(0.5,1.4))
        if -1 < t.ycor() < 1:
            break
    t.setheading(180)
    t.goto(starting_pos)
    t.end_fill()

def waves():
    t.color("#ADD8E6")
    t.speed(10)
    for i in range(30):
        t.up()
        t.home()
        t.goto(r.randint(-300, 300), r.randint(-300,300))
        t.down()
        t.fd(100)
    
def pole():
    t.color("#654321")
    t.up()
    t.goto(-10,50)
    t.down()
    t.begin_fill()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(20)
    t.end_fill()
    
def sail():
    t.color("black",r.choice(["lightgray", "purple", "red", "limegreen"]))
    t.up()
    t.goto(0,50)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.fd(150)
    t.goto(-10, 275)
    t.goto(-150, 50)
    t.goto(0,50)
    t.end_fill()

waves()
body()
pole()
sail()


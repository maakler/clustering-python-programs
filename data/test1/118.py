from turtle import *
from math import *

hideturtle()
speed(-1)
penup()
goto(-100,0)
pendown()


def paat():
    #põhi
    rt(90)
    fd(40)
    lt(80)
    circle(500,20)
    lt(70-10)
    fd(43)
    lt(110)
    fd(188)
    penup()
    #mast
    begin_fill()
    color("black")
    pendown()
    goto(55,0)
    rt(90)
    fd(155)
    lt(90)
    fd(6)
    lt(90)
    fd(140)
    rt(90)
    fd(130)
    lt(90)
    fd(6)
    lt(90)
    fd(130)
    rt(90)
    fd(9)
    end_fill()
    penup()
    #puri
    goto(49,155)
    pendown()
    rt(130)
    fd(90)
    lt(100)
    fd(70)
    lt(15)
    fd(70)
    lt(10)
    fd(70)


paat()
mainloop()
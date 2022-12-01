from turtle import *


a = 300
kere = "brown"
mast = "brown"
lipp = "cyan"

pencolor(kere)
fillcolor(kere)
pencolor(mast)

up()
pensize(5)
fd(150)
lt(180)
down()

begin_fill()
fd(a)
lt(135)
fd(a/3)
lt(45)
fd(a-((a/3)**2+(a/3)**2)**0.5)
lt(45)
fd(a/3)
lt(135)
end_fill()

fd(a/2)
rt(90)
fd(a/2)

pencolor("black")
fillcolor(lipp)
pensize(3)
begin_fill()
rt(90)
fd(a/3)
rt(90)
fd(a/6)
rt(90)
fd(a/3)
rt(90)
fd(a/6)
end_fill()

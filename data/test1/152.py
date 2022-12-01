from turtle import *
from math import cos, pi, sin

x = 130
print(cos(45))

nurk1 = 45

color("black", "brown")
begin_fill()

forward(x)
left(nurk1)
forward(9 * x/ 10)
left(180 - nurk1)
forward(2*x + 2*(cos(pi/4)*9*x/10))
#forward(425.46)
left(180 - nurk1)
forward(9 * x/10)
left(nurk1)
forward(x)

end_fill()

up()
left(90)
forward(sin(pi/4)*9*x/10)
down()

pensize(20)
forward(1.5*x)
left(90)
pensize(1)

#järgnevalt joonistatav kuju värviga täita
color("black", "blue")
begin_fill()
forward(0.8*x)
left(90)
forward(0.4*x)
left(90)
forward(0.8*x)
end_fill()
#(täitmine lõpetada)

up()
forward(69)
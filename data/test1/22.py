from turtle import *

fillcolor("#DE45BB") #laeva lipp
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

forward(150) #mast ja lipuke
left(90)
forward(350)
fillcolor("#6D1F66")
begin_fill()
left(90)
forward(100)
left(150)
forward(50)
right(120)
forward(50)
left(150)
forward(100)
end_fill()
right(90)
forward(320)

fillcolor("#50202A") #laeva kere
begin_fill()
right(90)
forward(250)
left(140)
forward(200)
left(40)
forward(190)
left(40)
forward(200)
left(140)
forward(250)
end_fill()


exitonclick()
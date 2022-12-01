from turtle import *

col = input("Vali värv, milliseks võiksime sinu purjed teha(gray, red jne...): ")
col2 = input("Vali värv, milliseks võiksime sinu aknad teha(gray, red jne...): ")

forward(50)
left(45)
forward(50)
left(135)
forward(75)
#purjed
fillcolor(col)
    
begin_fill()
right(90)
forward(70)
right(135)
forward(35)
right(90)
forward(35)
left(45)
forward(21)
right(90)

end_fill()
#purjedlopp

#alus lõpetamiseni
fillcolor(col)
    
begin_fill()

forward(10)
right(90)
forward(100)
left(135)
forward(70)
left(90)
forward(71)
end_fill()
right(135)
forward(65)
left(135)
forward(50)
left(45)
forward(50)
end_fill()

#transport esimese aknani
penup()
setx(40)
sety(8)
pendown()

#aken1

fillcolor(col2)
begin_fill()

left(90)
forward(18)
left(90)
forward(18)
left(90)
forward(18)
left(90)
forward(18)

end_fill()

#aknaraam

penup()
backward(9)
pendown()
left(90)
forward(18)
penup()
left(90)
forward(9)
left(90)
forward(9)
left(90)
pendown()
forward(18)

#transport teise aknani

penup()
right(90)
forward(9)
right(90)
forward(50)

#aken2

fillcolor(col2)
begin_fill()

pendown()
left(180)
forward(18)
left(90)
forward(18)
left(90)
forward(18)
left(90)
forward(18)

end_fill()

#aknaraam2

penup()
backward(9)
pendown()
left(90)
forward(18)
penup()
left(90)
forward(9)
left(90)
forward(9)
left(90)
pendown()
forward(18)

exitonclick()
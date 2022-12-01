from turtle import*

s=int(input("Kui suurt laeva soovite (skaalal 1-3)?"))
while s<1 or s>3:
    s=int(input("Sisestage mõistlik nr. (1-3)"))

speed(7)

pencolor("brown")
fillcolor("brown")
begin_fill()
fd (s*50)
right(135)
fd(s*25)
right(45)
fd(s*60)
right(45)
fd(s*25)
right(135)
fd(s*50)
end_fill()

pencolor("black")
pu()
left(90)
fd(s*20)
right(90)
pd()

fd(s*60)
left(115)
fd(s*140)
left(130)
fd(s*140)
left(115)
fd(s*59)
pu()
right(90)
fd(s*20)

pd()
pensize(3)
color("yellow")
bk(s*155)
pu()

left(90)
pencolor("red")
fd(10)

exitonclick()
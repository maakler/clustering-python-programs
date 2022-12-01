from turtle import*

#hull
forward(150)
left(50)
forward(150)
left(130)
forward(230)

#sail
rt(90)
fd(250)
rt(135)
fd(250)
rt(135)
fd(176)
up()
lt(90)
fd(73)
rt(90)
down()

#hull
fd(200)
lt(130)
fd(150)
lt(50)
fd(90)

#paadu stage 1 
up()
lt(90)
fd(80)
lt(90)
fd(130)
rt(90)
down()
color('red')

#paadu p
fd(20)
rt(90)
fd(7)
rt(90)
fd(13)
rt(90)
fd(7)
rt(180)
up()

#paadu aa
a = 0
while a < 2:
    fd(11)
    rt(90)
    fd(7)
    rt(180)
    down()
    
    fd(20)
    rt(90)
    fd(7)
    rt(90)
    fd(20)
    rt(180)
    up()
    fd(7)
    lt(90)
    down()
    fd(7)
    rt(180)
    up()
    a = a + 1

fd(11)
rt(90)
fd(7)
rt(180)
down()

#paadu d
fd(20)
rt(120)
fd(8)
rt(60)
fd(16)
rt(90)
fd(7)
rt(180)
up()

fd(11)
lt(90)
fd(20)
rt(180)
down()

#paadu u
fd(20)
lt(90)
fd(7)
lt(90)
fd(20)
up()

fd(100)


exitonclick()